from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stream_type = "Environmental Data"
        self.total_processed = 0
        self.total_batches = 0
        self.highest_temp_recorded = 0
        self.lowest_temp_recorded = None

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f'Stream ID: {self.stream_id}, Type: {self.stream_type}')
        print(f'Processing sensor batch: {data_batch}')
        self.total_processed += len(data_batch)
        self.total_batches += 1
        temps = []
        
        try:
            for item in data_batch:
                key, temp = item.split(':', 1)
                if key == 'temp':
                    temp = float(temp)
                    temps.append(temp)
                    if self.highest_temp_recorded < temp:
                        self.highest_temp_recorded = temp
                    if (self.lowest_temp_recorded is None
                            or self.lowest_temp_recorded > temp):
                        self.lowest_temp_recorded = temp
            if len(temps) == 0:
                return "No temperature data provided"
            avg_temp = sum(temps) / len(temps)
            return (f"Sensor analysis: "
                    f"{len(data_batch)} readings processed, "
                    f"avg temp: {avg_temp:.1f}°C")
        except ValueError:
            return "Invalid sensor data format"
        except Exception as e:
            return f'Error: {e}'

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        filtred = []
        for item in data_batch:
            try:
                key, val = item.split(':', 1)
                if (criteria == 'critical'
                        and key == 'temp' and float(val) > 50):
                    filtred.append(item)
            except ValueError:
                continue
            except Exception as e:
                print(e)
        return filtred

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "total_batches": self.total_batches,
            "total_processed": self.total_processed,
            "highest_temp_recorded": self.highest_temp_recorded,
            "lowest_temp_recorded": self.lowest_temp_recorded or 0
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f'Stream ID: {self.stream_id}, type: {self.stream_type}')
        data = ''
        for item in data_batch:
            key, val = item
            data += f'{key}:{val}, '
        print(data)
        print(f'Processing transaction batch: {data_batch}')
        total_operation = len(data_batch)
        units = 0
        for item in data_batch:
            try:
                key, unit = item.split(':', 1)
                units += int(unit)
            except ValueError:
                continue
        return (f'Transaction analysis: {total_operation}, '
                f"net flow: +{units} units")


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        pass


if __name__ == "__main__":
    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n')
    print('Initializing Sensor Stream...')
    data = ['temp:22.5', 'humidity:65', 'pressure:1013']
    stream = SensorStream(' SENSOR_001')
    output = stream.process_batch(data)
    print(output)
    print('\nInitializing Transaction Stream...')
    data = [{'buy': 100}, {'sell': 150}, {'buy': 75}]
    stream = TransactionStream(' TRANS_001')
    output = stream.process_batch(data)
    print(output)