from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.position: int = 0
        self.total: int = 0
        self.processedData: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.processedData:
            raise IndexError('No data to output')
        return self.processedData.pop(0)


def is_valid_number(s: str) -> bool:
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, list):
            for d in data:
                if not is_valid_number(d):
                    return False
            return True
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, str):
            return is_valid_number(data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            data = data if isinstance(data, list) else [data]
            for d in data:
                self.processedData.append((self.position, str(d)))
                self.position += 1
                self.total += 1
        else:
            raise ValueError('Got exception: Improper numeric data')


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, str) or is_valid_number(d):
                    return False
            return True
        if isinstance(data, str) and not is_valid_number(data):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            data = data if isinstance(data, list) else [data]
            for d in data:
                self.processedData.append((self.position, str(d)))
                self.position += 1
                self.total += 1
        else:
            raise ValueError('Got exception: Improper text data')


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            if 'log_level' not in data or 'log_message' not in data:
                return False
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                if 'log_level' not in d or 'log_message' not in d:
                    return False
                for key, value in d.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            data = data if isinstance(data, list) else [data]
            for d in data:
                log_level = d['log_level']
                log_message = d['log_message']
                log_entry = f'{log_level}: {log_message}'
                self.processedData.append((self.position, log_entry))
                self.position += 1
                self.total += 1
        else:
            raise ValueError('Got exception: Improper log data')


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    handled = True
                    break
            if not handled:
                print("DataStream error - Can't process "
                      f"element in stream: {element}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                print(f"{processor.name}: total {processor.total} "
                      f"items processed, remaining "
                      f"{len(processor.processedData)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            consumed_items: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    consumed_items.append(processor.output())
                except IndexError:
                    break
            if consumed_items:
                plugin.process_output(consumed_items)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [v for _, v in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = ", ".join(f'"{f"item_{pos}"}": "{val}"' for pos, val in data)
        print("JSON Output:")
        print("{" + items + "}")


def print_stats(stream: DataStream) -> None:
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()


def register_processors(stream: DataStream) -> None:
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    numeric_proc = NumericProcessor()
    stream.register_processor(numeric_proc)
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)


def csv_exporting(stream: DataStream) -> None:
    csv_plugin = CSVExportPlugin()
    nb = 3
    print(f"\nSend {nb} processed data from each processor to a CSV plugin")
    stream.output_pipeline(nb, csv_plugin)


def json_exporting(stream: DataStream) -> None:
    json_plugin = JSONExportPlugin()
    nb = 5
    print(f"\nSend {nb} processed data from each processor to a JSON plugin")
    stream.output_pipeline(nb, json_plugin)


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    data_1: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {'log_level': 'INFO', 'log_message': 'User wil isconnected'}
        ],
        42,
        ['Hi', 'five']
    ]
    data_2: list[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print('Initialize Data Stream...')
    data_stream = DataStream()
    print_stats(data_stream)
    print('\nRegistering Processors\n')
    register_processors(data_stream)
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    print(f'Send first batch of data on stream: {data_1}')
    data_stream.process_stream(data_1)
    print_stats(data_stream)
    csv_exporting(data_stream)
    print_stats(data_stream)
    print(f'\nSend another batch of data: {data_2}')
    data_stream.process_stream(data_2)
    print_stats(data_stream)
    json_exporting(data_stream)
    print_stats(data_stream)
