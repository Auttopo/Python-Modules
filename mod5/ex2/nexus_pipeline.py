
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable, Generator
from typing import Any, List, Dict, Union, Optional


@runtime_checkable
class ProcessingStage(Protocol):

    ___crypt_key: List[int]

    def process(self, data: Any) -> Any:
        pass

    def get_crypted_key(cls) -> List[int]:
        pass

    def set_crypted_key(cls, key: List[int]) -> None:
        pass


class StreamStage(ProcessingStage, ABC):

    _active_state: int = 0

    @classmethod
    def exec(cls, data: Any) -> Union[str, Any]:
        return cls.process(cls, data)

    @classmethod
    def disable(cls) -> None:
        print(cls.__name__, "| stage stream desactivated")
        cls._active_state = 0

    @classmethod
    def status(cls) -> int:
        return cls._active_state


class InputStage(StreamStage):

    active: int = 0

    def process(self, data: Any) -> Any:
        print(end="VERIFYING STAGE OTORISATION ---")
        if self.status() == 1:
            print(" OK --- START STAGE 1 STREAM")
        else:
            print(" STAGE 1 KO --- STREAM STOPPED")
            return None
        return JSONAdapter.exec(data)

    @classmethod
    def enable(cls) -> None:
        print(cls.__name__, "| stage 1 stream actived | Input validation and parsing")
        cls._active_state = 1


class TransformStage(StreamStage):

    active: int = 0

    def process(self, data: Any) -> Any:
        print(end="VERIFYING STAGE OTORISATION ---")
        if self.status() == 1:
            print(" OK --- START STAGE 2 STREAM")
        else:
            print(" STAGE 2 KO --- STREAM STOPPED")
            return None
        return CSVAdapter.exec(data)

    @classmethod
    def enable(cls) -> None:
        print(cls.__name__,
              "| stage 2 stream actived | Data transformation and enrichment")
        cls._active_state = 1


class OutputStage(StreamStage):

    def process(self, data: Any) -> Any:
        print(end="VERIFYING STAGE OTORISATION ---")
        if self.status() == 1:
            print(" OK --- START STAGE 3 STREAM")
        else:
            print(" STAGE 3 KO --- STREAM STOPPED")
            return None
        return StreamAdapter.exec(data)

    @classmethod
    def enable(cls) -> None:
        print(cls.__name__, "| stage 3 stream actived | Output formatting and delivery")
        cls._active_state = 1


class ProcessingPipeline(ABC):

    @classmethod
    def get_crypted_key(cls) -> List[int]:
        return cls.___crypt_key

    @classmethod
    def set_crypted_key(cls, key: List[int]) -> None:
        cls.___crypt_key = key

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    @classmethod
    def exec(cls, data: Any) -> Union[str, Any]:
        return cls.process(cls, data)

    class NexusManager:

        @staticmethod
        def setup(level: int) -> None:
            print("initializing Nexus Manager...")
            print('Pipeline capacity: "faster than Flash McQueen"\n')
            print("Creating Data Processing Pipeline...\n")

            try:
                if isinstance(level, int) is False or (3 < level or level < 0):
                    raise ValueError(
                        f"Invalide type or range, {level} not in (1 - 3)\n")
                if 3 >= level >= 1:
                    InputStage.enable()
                if 3 >= level >= 2:
                    TransformStage.enable()
                if level == 3:
                    OutputStage.enable()
                print("")
            except Exception as e:
                print(e)

        @staticmethod
        def manage() -> None:
            data = {"bonsoir": 5, "coucou": 1, "value": 1, "unit": "C"}
            try:
                out1 = ducking_quack_quack_exec(InputStage, data)
                out2 = ducking_quack_quack_exec(TransformStage, out1)
                ducking_quack_quack_exec(OutputStage, out2)
            except Exception as e:
                print("error occured :", e)


class JSONAdapter(ProcessingPipeline):

    ___crypt_key: List[int] = []

    def checker(self, data_batch: Dict[Any, Any]) -> bool:
        """Validate data batch format."""
        if not isinstance(data_batch, Dict):
            raise TypeError("''Dict'' expected", "from " +
                            self.__name__)

        checker: int = 0
        for elem1, elem2 in data_batch.items():
            if elem1 == "value":
                if isinstance(elem2, (int, float, complex)):
                    checker += 1
                else:
                    raise TypeError("value is not a number")
            if elem1 == "unit":
                if isinstance(elem2, str):
                    checker += 1
                else:
                    raise TypeError("unit is not a string")
        if checker != 2:
            raise ValueError("not enought data, need minimal value + unit")
        return True

    def process(self, data: Any) -> Union[str, Any]:
        print(self.__name__, "process start ...")
        try:
            print("input", data)
            self.checker(JSONAdapter, data)
        except Exception as e:
            raise (e)
        data.update({"datetime": str(datetime.now())})
        out = ""
        for elem, nbr in data.items():
            out += ", " + str(elem) + " " + str(nbr)
        out = out[2:]
        print("Transform: Enriched with metadata and validation; Success")
        print("Informational Output. data streamed: Input saved and ready to use\n")

        return [out, cryptor.crypt_and_send_key(cryptor.seed_gen(),
                str(self.__name__), CSVAdapter)]


class CSVAdapter(ProcessingPipeline):

    ___crypt_key: List[int] = []

    def process(self, data: Any) -> Union[str, Any]:

        print(self.__name__, "process start ...")
        print("input", data[0], " paired with crypted data")
        new_data = []
        try:
            secret_data = cryptor.uncrypting(self.get_crypted_key(), data[1])
            if secret_data == "JSONAdapter":
                print("Data OK, send from a valid operator")
                new_data = data[0].split(",")
            else:
                raise Exception(
                    "Data KO, send from an indalid operator, Process Killed. ")
        except Exception as e:
            raise (e)
        print("Transform: Uncrypt , parsed and structured data; Success")
        print(
            "Informational Output. data streamed:", new_data, "\n"
        )
        return [new_data, cryptor.crypt_and_send_key(cryptor.seed_gen(),
                str(self.__name__), StreamAdapter)]


class StreamAdapter(ProcessingPipeline):

    ___crypt_key: List[int] = []
    _stream_status: int = 0

    @classmethod
    def real_time_app(cls, data: List[Any]) -> List[Any]:
        cls._stream_status = 1
        print("----------------------------REAL TIME SENSOR START STREAM\
-------------------------------------------------------------------------------------------------------------------")
        gen = cryptor.random_number(cryptor.seed_gen(), 30)
        log: List[Any] = []
        log.append(data)
        for i in range(next(gen)):
            new_input: Dict = {"data": "temp",
                               "value": next(gen), "unit": "C"}
            out1 = ducking_quack_quack_exec(InputStage, new_input)
            out2 = ducking_quack_quack_exec(TransformStage, out1)
            log.append(ducking_quack_quack_exec(StreamAdapter, out2))

        print("----------------------------REAL TIME SENSOR END STREAM\
-------------------------------------------------------------------------------------------------------------------")
        return log

    @classmethod
    def stats(cls, data) -> None:
        for elem in data:
            print(elem[0])

    def process(self, data: Any) -> Union[str, Any]:

        print(self.__name__, "process start ...")
        print("input", data[0], " paired with crypted data")
        try:
            secret_data = cryptor.uncrypting(self.get_crypted_key(), data[1])
            if secret_data == "CSVAdapter":
                print("Data OK, send from a valid operator")
            else:
                raise Exception(
                    "Data KO, send from an indalid operator, Process Killed. ")
        except Exception as e:
            raise (e)
        if self._stream_status == 1:
            return data

        new_data = self.real_time_app(data)

        print("Transform: Uncrypt the previous data of the stream, and add it to the new generated complex stream")
        print(
            "Informational Output. data streamed: Steam processed normaly, program end",
        )

        self.stats(new_data)
        return new_data


def ducking_quack_quack_exec(operator: ProcessingStage, data: Any) -> Any:
    return operator.exec(data)


class cryptor:

    @staticmethod
    def crypting(seed: str, data: str) -> List[List[int]]:
        gen: Generator = cryptor.random_number(seed, 999999999)
        out: List[int] = []
        key: List[int] = []
        for elem in data:
            n = next(gen)
            out.append(ord(elem) + n)
            key.append(n)
        print("Encryption Success\n")
        return [out, key]

    @staticmethod
    def uncrypting(keys: List[int], data: List[int]) -> str:
        out: str = ""
        i: int = 0
        for elem, key in zip(data, keys):
            out += chr(elem - key)
            i += 1
        print("Decyption try; data recovered:", out)
        return out

    @staticmethod
    def random_number(seed: int, range: int = 10) -> Generator[int, None, None]:
        """create a random number"""

        r = seed
        plage = 4294967296
        multiple_chaos = 1664525
        jump = 1013904223
        for i in iter(int, 1):
            r = (r * multiple_chaos + jump) % plage
            yield r % range

    @staticmethod
    def crypt_and_send_key(seed: str, data: str, dest: ProcessingStage) -> List[int]:
        new_data = cryptor.crypting(seed, data)
        dest.set_crypted_key(new_data[1])
        return new_data[0]

    @staticmethod
    def seed_gen() -> int:
        start = str(datetime.now())
        seed: int = 0
        for elem in start:
            seed = seed * 10 + ord(elem)
        return seed


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    ProcessingPipeline.NexusManager.setup(3)
    ProcessingPipeline.NexusManager.manage()
