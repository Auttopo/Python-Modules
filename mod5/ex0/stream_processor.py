
from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """ basic abstract class """

    def __init__(self, data: Any) -> None:
        """ init with verification of the data parameter """

        print(f"\nInitializing {self.__class__.__name__} ...")
        self._data: Any = data
        self._data_str: str = self.process(data)
        if self._data_str is None:
            print("error occured, data not captured, see previous logs")
        else:
            print(f'output : "{self._data_str}"')

    @abstractmethod
    def process(self, data: Any) -> str:
        """function to determinate in sub class """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """function to determinate in sub class """
        pass

    def format_output(self, result: str) -> str:
        """ format a data to a string """
        try:
            out: str = str(result)
            return out
        except Exception as e:
            print("Invalid data, no output :", e)


class NumericProcessor(DataProcessor):
    """ class to use and verify numeric list"""

    def process(self, data: Any) -> str:
        """ process validation and transformation """

        print(f'Processing data "{data}"')
        try:
            for elem in data:
                self.validate(elem)
            return self.format_output(data)
        except Exception as e:
            print("Numeric array needed, data corrupted :", e)
            return None

    def validate(self, data: Any) -> bool:
        """ check if data is valide to the class expectations """

        print(end="Validation: ")
        try:
            float(data)
            print(data, "is Numeric")
            return True
        except Exception:
            raise ValueError("Invalide data type")

    def format_output(self, result: str) -> str:
        """ format the data to a string like parent """

        return super().format_output(data)


class TextProcessor(DataProcessor):
    """ class to use and verify string"""

    def process(self, data: Any) -> str:
        """ process validation and transformation """

        print(f'Processing data "{data}"')
        try:
            TextProcessor.validate(self, data)
            words: List = data.split(" ")
            out: str = TextProcessor.format_output(self, data)
            print(f"Contain {ft_len(words)} words")
            return out
        except Exception as e:
            print("error. String needed :", e)
            return None

    def validate(self, data: Any) -> bool:
        """ check if data is valide to the class expectations """

        print(end="Validation: ")
        try:
            test: str = str(data)
            if test == data:
                print("is String")
                return True
            raise Exception("Invalid type :", data.__class__.__name__)
        except Exception as e:
            print("KO")
            raise e

    def format_output(self, result: str) -> str:
        """ format the data to a string like parent """

        return super().format_output(data)


class LogProcessor(TextProcessor):
    """ class to use and verify log error string """

    def process(self, data: Any) -> str:
        """ process validation and transformation """

        local: str = super().process(data)
        if local is None:
            print("Str verification not passed")
            return
        print("Str verification passed")
        try:
            self.validate(local)
            return self.format_output(data)
        except Exception as e:
            print("error", e)

    def validate(self, data: Any) -> bool:
        """ check if data is valide to the class expectations """

        print(end="Validation: ")
        try:
            if "ERROR:" == data[:6]:
                print("is Log")
                return True
            raise Exception("Unrecognize log format")
        except Exception as e:
            print("KO")
            raise e

    def format_output(self, result: str) -> str:
        """ format the data to a detailed string """

        data: str = 'warning "' + \
            result[:5] + '" detected, log saved:' + result[5:]
        return data


def ft_len(data: Any) -> int:
    """ simple len return function """
    i: int = 0
    for elem in data:
        i += 1
    return i


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    data: List = [1, 5, 70, -2, "caca", 6]
    np: NumericProcessor = NumericProcessor(data)
    data: str = "voici un texte"
    tp: TextProcessor = TextProcessor(data)
    data: str = "ERROR: connection timed out"
    lp: LogProcessor = LogProcessor(data)
