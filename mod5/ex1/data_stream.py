
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    id_list: List[Any] = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    @abstractmethod
    def print_log(self) -> None:
        pass

    def __init__(self, id: str | None) -> None:
        """ commune init of stream """
        print("Initializing", self.__class__.__name__, "...")
        self.last_log: List[Any] = []
        self.all_log: List[Any] = []
        self._count = 0
        if id is None:
            id = "ID_" + self.__class__.__name__.upper() + "_"\
                + str(ft_len(self.__class__.id_list) + 1)
        self.__class__.id_list.append(id)
        print("Stream ID:", self.__class__.id_list[ft_len(
            self.__class__.id_list) - 1])

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data by criteria and return matching name-value pair."""

        if not isinstance(criteria, str):
            print("bad filter patern, need ''priority'' or 'key word'")
            raise TypeError("filter is not str type")

        name: str | None = None
        value: int | None = None
        for elem in data_batch:
            (i1, i2), = elem.items()
            if criteria == i1:
                (name, value), = elem.items()
            if criteria == "priority" and i2 >= 100:
                (name, value), = elem.items()
        return [name, value]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream processing statistics."""
        return {"number of processes that occured": self._count}


class CommonStream(DataStream):
    """ abstract base class """

    id_list: List[Any] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return formatted string."""

        try:
            self.checker(data_batch)
        except Exception as e:
            raise TypeError(f"Invalide data type {e}") from e

        new_str: str = "["
        for elem in data_batch:
            new_str = new_str + " " + str(elem)
        new_str = new_str + " ]"

        self.last_log = data_batch
        self._count += 1
        log = self.filter_data(self.last_log, "priority")
        if log[0] is not None:
            self.all_log.append(log)
        return new_str

    def checker(self, data_batch: List[Any]) -> bool:
        """Validate data batch format."""
        if not isinstance(data_batch, List):
            raise TypeError("''List'' expected", "from " +
                            self.__class__.__name__)
        for elem in data_batch:
            if not isinstance(elem, Dict):
                raise TypeError("List of ''Dict'' expected",
                                "from " + self.__class__.__name__)
            (i1, i2), = elem.items()
            if not isinstance(i1, str):
                raise TypeError(
                    "List of Dict ''str'' : int expected",
                    "from " + self.__class__.__name__)
            if not isinstance(i2, (int, float, complex)):
                raise TypeError(
                    "List of Dict str : ''int'' expected",
                    "from " + self.__class__.__name__)
        return True

    def get_count(self) -> int:
        """Return the number of processed batches."""
        return self._count

    def print_log(self) -> None:
        """Print all priority-filtered logs."""
        print(self.__class__.__name__, end=" Prior data occured: ")
        for elem in self.all_log:
            print(elem, end=" ")
        if len(self.all_log) == 0:
            print("None")
        print("")


class SensorStream(CommonStream):
    """Specialized sensor stream: temperature/humidity/pressure filtering."""

    id_list: List[Any] = []

    def __init__(self, id: str | None = None) -> None:
        """Initialize sensor stream."""
        super().__init__(id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor batch."""

        return str("Processing sensor batch:" +
                   super().process_batch(data_batch))

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data by criteria."""

        if not isinstance(criteria, str):
            raise Exception(
                "bad filter patern, need ''priority'' or 'key word'")

        name: str | None = None
        value: int | None = None
        for elem in data_batch:
            (i1, i2), = elem.items()
            if criteria == i1:
                (name, value), = elem.items()
            if criteria == "priority":
                if i1 == "temp" and i2 >= 30:
                    (name, value), = elem.items()
                elif i1 == "humidity" and i2 >= 100:
                    (name, value), = elem.items()
                elif i1 == "pressure" and i2 >= 1100:
                    (name, value), = elem.items()
        return [name, value]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor stream statistics."""
        last_temp = self.filter_data(self.last_log, "temp")[1]
        return {"number of processes that occured": self._count,
                "last temperature registered": last_temp}


class TransactionStream(CommonStream):
    """Specialized transaction stream with buy/sell amount filtering."""

    id_list: List[Any] = []

    def __init__(self, id: str | None = None) -> None:
        """Initialize transaction stream."""
        super().__init__(id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transaction batch."""

        return str("Processing transaction batch:" +
                   super().process_batch(data_batch))

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter transaction data by criteria."""

        if not isinstance(criteria, str):
            raise Exception(
                "bad filter patern, need ''priority'' or 'key word'")
            return

        name: str | None = None
        value: str | None = None
        for elem in data_batch:
            (i1, i2), = elem.items()
            if criteria == i1:
                (name, value), = elem.items()
            if criteria == "priority":
                if i1 == "buy" and i2 >= 500:
                    (name, value), = elem.items()
                elif i1 == "sell" and i2 >= 500:
                    (name, value), = elem.items()
        return [name, value]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction stream statistics."""
        sum_: int = 0
        for elem in self.last_log:
            (name, value), = elem.items()
            sum_ += value
        return {"number of processes that occured": self._count,
                "money sum variation": sum_}


class EventStream(CommonStream):
    """Specialized event stream with error event filtering."""

    id_list: List[Any] = []

    def __init__(self, id: str | None = None) -> None:
        """Initialize event stream."""
        super().__init__(id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event batch."""

        return str("Processing event batch:" +
                   super().process_batch(data_batch))

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter event data by criteria."""

        if not isinstance(criteria, str):
            raise Exception(
                "bad filter patern, need ''priority'' or 'key word'")
            return

        event: str | None = None
        for elem in data_batch:
            if criteria == "priority":
                if elem == "error":
                    event = elem
        return [event]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event stream statistics."""

        errors: int = 0
        for elem in self.last_log:
            if elem == "error":
                errors += 1

        return {"number of processes that occured": self._count,
                "errors occured": errors}

    def checker(self, data_batch: List[Any]) -> bool:
        """Validate event batch format (list of strings)."""
        if not isinstance(data_batch, List):
            raise TypeError("''List'' expected", "from " +
                            self.__class__.__name__)
        for elem in data_batch:
            if not isinstance(elem, str):
                err_msg: str = "List of ''str'' expected"
                raise TypeError(err_msg, "from " +
                                self.__class__.__name__)
        return True


class StreamProcessor():
    """Class to manage and process multiple data streams."""

    @staticmethod
    def processing() -> None:
        """Execute basic stream processing for all stream types."""
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

        try:
            sensor = SensorStream()
            print(sensor.process_batch(
                [{"temp": 1}, {"humidity": 8.53}, {"pressure": 1013}]))
            print("Sensor stats:", sensor.get_stats())

            print("")

            market = TransactionStream()
            print(market.process_batch(
                [{"buy": 10}, {"sell": 50}, {"buy": 79}]))
            print("Transaction stats:", market.get_stats())

            print("")

            events = EventStream("JapanExpoID")
            print(events.process_batch(["login", "error", "logout"]))
            print("Events logs", events.get_stats())

            print("")
        except Exception as e:
            err_msg: str = (
                f"program stopped, ERROR OCCURED : {e} "
                "-----!-----!-----!-----!"
            )
            raise type(e)(err_msg) from e

    @staticmethod
    def processing_priority() -> None:
        """Execute priority-filtered stream processing."""

        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        try:
            sensor = SensorStream()
            sensor.process_batch(
                [{"temp": 1}, {"humidity": 8.53}, {"pressure": 1013}])
            sensor.process_batch(
                [{"temp": 21}, {"humidity": 19}, {"pressure": 1250}])

            market = TransactionStream("MoneyScamerID")
            market.process_batch([{"buy": 42}, {"sell": 24}, {"sell": 10}])
            market.process_batch([{"buy": 10}, {"sell": 601}, {"buy": 79}])
            market.process_batch([{"sell": 10}, {"sell": 49}, {"buy": 24}])
            market.process_batch([{"buy": 512}, {"buy": 70}, {"buy": 1}])

            events = EventStream()
            events.process_batch(["login", "error", "logout"])
            events.process_batch(["login", "logout", "login"])
            events.process_batch(["error", "error", "logout"])

            print("\nBatch 1 Results:")
            print(f"- Sensor data: {sensor.get_count()}")
            print(f"- Transaction data: {market.get_count()}")
            print(f"- Event data: {events.get_count()}")

            print(
                "\nStream filtering active, High-priority data only\
 and demonstrate polymorphism ----- ")
            data_set: List[DataStream] = [sensor, market, events]
            for elem in data_set:
                elem.print_log()

        except Exception as e:
            err_msg: str = (
                f"program stopped, ERROR OCCURED : {e} "
                "-----!-----!-----!-----!"
            )
            raise type(e)(err_msg) from e


def ft_len(data: Any) -> int:
    """Return length of iterable without using len()."""
    i: int = 0
    for elem in data:
        i += 1
    return i


if __name__ == "__main__":
    try:
        StreamProcessor().processing()
        StreamProcessor().processing_priority()
        msg: str = ("All streams processed successfully. "
                    "Nexus throughput optimal.")
        print(f"\n{msg}")
    except Exception as e:
        print(e)
