from abc import ABC, abstractmethod
from typing import Any


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


def print_stats(stream: DataStream) -> None:
    print("== DataStream statistics ==")
    stream.print_processors_stats()


def test_single_processor(stream: DataStream,
                          data: list[Any]) -> NumericProcessor:
    processor = NumericProcessor()
    stream.register_processor(processor)
    print(f'Send first batch of data on stream: {data}')
    stream.process_stream(data)
    return processor


def test_all_processor(stream: DataStream,
                       data: list[Any]) -> tuple[TextProcessor, LogProcessor]:
    print("\nRegistering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)
    print("Send the same batch again")
    stream.process_stream(data)
    return text_processor, log_processor


def test_consuming(numeric_proc: NumericProcessor,
                   text_proc: TextProcessor,
                   log_proc: LogProcessor) -> None:
    numeric, text, log = 3, 2, 1
    print("\nConsume some elements from the data processors: "
          f"Numeric {numeric}, Text {text}, Log {log}")
    for _ in range(numeric):
        numeric_proc.output()
    for _ in range(text):
        text_proc.output()
    for _ in range(log):
        log_proc.output()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    data: list[Any] = ['Hello world', [3.14, -1, 2.71],
                       [{'log_level': 'WARNING',
                        'log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                         'log_message': 'User wil isconnected'}],
                       42, ['Hi', 'five']]

    print('Initialize Data Stream...')
    data_stream = DataStream()
    print_stats(data_stream)
    numeric_proc = test_single_processor(data_stream, data)
    print_stats(data_stream)
    text_proc, log_proc = test_all_processor(data_stream, data)
    print_stats(data_stream)
    test_consuming(numeric_proc, text_proc, log_proc)
    print_stats(data_stream)
