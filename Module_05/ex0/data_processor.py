from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.position: int = 0
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

    def ingest(self, data: int | float | list) -> None:
        if self.validate(data):
            data = data if isinstance(data, list) else [data]
            for d in data:
                self.processedData.append((self.position, str(d)))
                self.position += 1
        else:
            raise ValueError('Got exception: Improper numeric data')


class TextProcessor(DataProcessor):
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
        else:
            raise ValueError('Got exception: Improper text data')


class LogProcessor(DataProcessor):
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
        else:
            raise ValueError('Got exception: Improper log data')


def processing_numeric_data() -> None:
    processor = NumericProcessor()
    data_one = '42'
    print(f"Trying to validate input '{data_one}': "
          f"{processor.validate(data_one)}")
    data_two = 'Hello'
    print(f"Trying to validate input '{data_two}': "
          f"{processor.validate(data_two)}")
    data_three = 'foo'
    print(f"Trying to validate ingestion of string'{data_three}' "
          "without prior validation")
    try:
        processor.ingest(data_three)
    except ValueError as e:
        print(e)
    data_four = [1, 2, 3, 4, 5]
    print(f'Processing data: {data_four}')
    try:
        processor.ingest(data_four)
        print('Extracting 3 values....')
        for _ in range(3):
            position, value = processor.output()
            print(f"Numeric value {position}: {int(value)}")
    except (ValueError, IndexError) as e:
        print(e)


def processing_text_data() -> None:
    processor = TextProcessor()
    data_one = '42'
    print(f"Trying to validate input '{data_one}': "
          f"{processor.validate(data_one)}")
    data_two = ['Hello', 'str', 'World']
    print(f'Processing data: {data_two}')
    try:
        processor.ingest(data_two)
        print('Extracting 1 values...')
        position, value = processor.output()
        print(f"Text value {position}: {value}")
    except (ValueError, IndexError) as e:
        print(e)


def processing_logs_data() -> None:
    processor = LogProcessor()
    data_one = 'Hello'
    print(f"Trying to validate input '{data_one}': "
          f"{processor.validate(data_one)}")
    data_two = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f'Processing data: {data_two}')
    try:
        processor.ingest(data_two)
        print('Extracting 2 values...')
        for _ in range(2):
            position, value = processor.output()
            print(f"Log entry {position}: {value}")
    except (ValueError, IndexError) as e:
        print(e)


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print('Testing Numeric Processor...')
    processing_numeric_data()
    print('\nTesting Text Processor...')
    processing_text_data()
    print('\nTesting Log Processor...')
    processing_logs_data()
