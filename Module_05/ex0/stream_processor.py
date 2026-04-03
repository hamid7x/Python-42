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
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid data"
        if isinstance(data, (int, float)):
            data = [data]
        try:
            total = sum(data)
            result = (f'Processed {len(data)} numeric values, '
                      f'sum={total}, avg={(total / len(data)):.1f}')
            return result
        except Exception as e:
            return (f'Error: {e}')

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if (isinstance(data, list)
            and len(data) > 0 and
                all(isinstance(n, (int, float)) for n in data)):
            return True
        return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid Data"
        try:
            total_chars = len(data)
            total_words = len(data.split())
            result = f"Processed {total_chars} characters, {total_words} words"
            return result
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or not data:
            return False
        return True


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid data"
        log = data.split(':', 1)
        level = log[0]
        message = log[1]
        status = 'ALERT' if level == 'ERROR' else 'INFO'
        return f"[{status}] {level}: {message}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if ':' not in data:
            return False
        return True


def demo_individual() -> None:
    print('Initializing Numeric Processor...')
    processor = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    result = processor.process(data)
    print(f'Processing data: {data}')
    valid_data = processor.validate(data)
    if valid_data:
        print('Validation: Numeric data verified')
    else:
        print('Validation: Numeric data not verified')
    print(processor.format_output(result))

    print('\nInitializing Text Processor...')
    processor = TextProcessor()
    data = "Hello Nexus World"
    result = processor.process(data)
    print(f'Processing data: "{data}"')
    valid_data = processor.validate(data)
    if valid_data:
        print('Validation: Text data verified')
    else:
        print('Validation: Text data not verified')
    print(processor.format_output(result))

    print('\nInitializing Log Processor...')
    processor = LogProcessor()
    data = "INFO level detected: System ready"
    result = processor.process(data)
    print(f'Processing data: {data}')
    valid_data = processor.validate(data)
    if valid_data:
        print('Validation: Log entry verified')
    else:
        print('Validation: Log entry not verified')
    print(processor.format_output(result))


def demo_polymorphic() -> None:
    print('Processing multiple data types through same interface...')
    data = [[1, 2, 3], 'Hello Nexus', 'INFO level detected: System ready']
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    for i, processor in enumerate(processors):
        result = processor.process(data[i])
        print(f"Result {i + 1}: {result}")


if __name__ == "__main__":
    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n')
    demo_individual()

    print('\n=== Polymorphic Processing Demo ===\n')
    demo_polymorphic()
    print('\nFoundation systems online. Nexus ready for advanced streams.')
