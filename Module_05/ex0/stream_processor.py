from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid data"
        try:
            total = sum(data)
            result = (f'{len(data)} numeric values, '
                      f'sum={total}, avg={(total / len(data)):.1f}\n')
            return result
        except Exception as e:
            return (f'Error: {e}')

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            return False
        return all(isinstance(n, (int, float)) for n in data)

    def format_output(self, result: str) -> str:
        return (f'Output: Processed {result}')


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid Data"
        try:
            total_chars = len(data)
            total_words = len(data.split())
            result = f"{total_chars} characters, {total_words} words"
            return result
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or not data:
            return False
        return True

    def format_output(self, result: Any) -> str:
        return (f"Output: Processed {result}")


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return 'Processing data: "ERROR: Connection timeout"'

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return True

    def format_output(self, result: Any) -> str:
        return 'Output: [ALERT] ERROR level detected: Connection timeout\n'


if __name__ == "__main__":
    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n')
    # for processor in [NumericProcessor(), TextProcessor(), LogProcessor()]:
    #     processor.process()
    #     processor.validate()
    #     processor.format_output()
    print('=== Polymorphic Processing Demo ===')
