from abc import ABC, abstractmethod
from typing import Any
from collections import deque


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


def is_valid_number(s: str) -> bool:
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False


class NumericProcessor(DataProcessor):
    def __init__(self):
        self.rank = 0
        self.queue = deque()

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

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            data = data if isinstance(data, list) else [data]
            for d in data:
                self.queue.append((self.rank, str(d)))
                self.rank += 1
        else:
            raise ValueError('Got exception: Improper numeric data')

    def output(self) -> tuple[int, str]:
        if not self.queue.popleft:
            raise IndexError('No data to output')
        return self.queue.popleft()


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(list, str):
            return False
        return True

    def ingest(self, data):
        return super().ingest(data)

    def output(self):
        return super().output()


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(list):
            return False
        return True

    def ingest(self, data):
        pass

    def output(self):
        return super().output()


def nemuric_processor() -> None:
    processor = NumericProcessor()
    data = '42'
    print(f"Trying to validate input '{data}': {processor.validate(data)}")
    data = 'Hello'
    print(f"Trying to validate input '{data}': {processor.validate(data)}")
    data = 'foo'
    print(f"Trying to validate ingestion of string'{data}' "
          "without prior validation")
    try:
        processor.ingest(data)
    except ValueError as e:
        print(e)
    data = [1, 2, 3, 4, 5]
    print(f'Processing data: {data}')
    try:
        processor.ingest(data)
        print('Extracting 3 values....')
        for i in range(7):
            rank, value = processor.output()
            print(f"Numeric value {rank}: {int(value)}")
    except (ValueError, IndexError) as e:
        print(e)


def text_processor() -> None:
    pass


def log_processor() -> None:
    pass


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    print('Testing Numeric Processor...')
    nemuric_processor()
    text_processor()
    log_processor()
