
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Protocol, Generator
from typing import Any, List, Dict, Union, Optional


class PipelineException(Exception):
    pass


class Cryptable(Protocol):

    def get_crypted_key(cls) -> List[int]:
        pass

    def set_crypted_key(cls, key: List[int]) -> None:
        pass


class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any:
        pass

    def exec(cls, data: Any) -> Union[str, Any]:
        pass

    def enable(cls) -> None:
        pass


class CommonStage(ProcessingStage):

    _active_state: int = 0

    @classmethod
    def exec(cls, data: Any) -> Union[str, Any]:

        # when used by a children without object
        # the class name need to be gived to the method
        return cls.process(cls, data)  # type: ignore

    @classmethod
    def disable(cls) -> None:
        print(cls.__name__, "| stage stream desactivated")
        cls._active_state = 0

    @classmethod
    def status(cls) -> int:
        return cls._active_state

    def process(self, data: Any) -> Any:

        print(end="VERIFYING STAGE OTORISATION ---")
        if self.status() == 1:
            print(" OK --- START STAGE", data, "STREAM")
            return True
        else:
            print(" STAGE", data, "KO --- STREAM STOPPED\n")
            return False

    def __init__(self) -> None:
        pass


class InputStage(CommonStage):

    _active_state: int = 0

    def process(self, data: Any) -> Dict[str, Any]:

        # when used by a children without object
        # the class name need to be gived to the method
        if not super().process(self, 1):  # type: ignore
            raise PipelineException(
                "try to use unauthorized pipeline, level 1")
        return need_a_dict(JSONAdapter.exec(data))

    @classmethod
    def enable(cls) -> None:
        print(cls.__name__,
              "| stage 1 stream actived | Input validation and parsing")
        cls._active_state = 1


class TransformStage(CommonStage):

    _active_state: int = 0

    def process(self, data: Any) -> Dict[str, Any]:
        # when used by a children without object
        # the class name need to be gived to the method
        if not super().process(self, 2):  # type: ignore
            raise PipelineException(
                "try to use unauthorized pipeline, level 2")
        out = CSVAdapter.exec(data)
        return need_a_dict(out)

    @classmethod
    def enable(cls) -> None:
        print(cls.__name__,
              "| stage 2 stream actived | Data transformation and enrichment")
        cls._active_state = 1


class OutputStage(CommonStage):

    _active_state: int = 0

    def process(self, data: Any) -> str:

        # when used by a children without object
        # the class name need to be gived to the method
        if not super().process(self, 3):  # type: ignore
            raise PipelineException(
                "try to use unauthorized pipeline, level 3")
        out = StreamAdapter.exec(data)
        return out

    @classmethod
    def enable(cls) -> None:
        print(cls.__name__,
              "| stage 3 stream actived | Output formatting and delivery")
        cls._active_state = 1


class ProcessingPipeline(ABC):

    stages: List[Any] = []

    @classmethod
    def add_stage(cls, name: str, data: Any) -> None:
        ProcessingPipeline.stages.append([name, "STAGE SUCCESS", data])

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    class NexusManager:

        pipelines: List[str] = []
        exec_time: datetime

        @classmethod
        def add_pipeline(cls, data: Any) -> None:
            if data:
                cls.pipelines.append(data)

        @classmethod
        def show_pipelines(cls) -> None:
            print("\nALL PIPELINES STORED -----------------------------------")
            i = 0
            for item in cls.pipelines:
                i += 1
                print("PIPELINE:", i)
                print(item)
                print("")

        @classmethod
        def error_demonstration(cls) -> None:

            ProcessingPipeline.NexusManager.setup(3)
            print(end="\nERROR DEMONSTRATION: ")
            print("----------------------------------------------------------")
            data = {"bonsoir": 5, "coucou": 1, "level": 1, "unit": "C"}
            try:
                ducking_quack_quack_exec(InputStage(), data)
            except Exception as e:
                if not isinstance(e, PipelineException):
                    print("error occured :", e)

            print(end="ERROR DEMONSTRATION: ")
            print("----------------------------------------------------------")
            data = {"bonsoir": 5, "coucou": 1, "value": 1, "unit": "C"}
            try:
                ducking_quack_quack_exec(
                    TransformStage(), [data, [917, 155, 310]])
            except Exception as e:
                if not isinstance(e, PipelineException):
                    print("error occured :", e)
            print(end="ERROR DEMONSTRATION: ")
            print("----------------------------------------------------------")
            ProcessingPipeline.NexusManager.setup(-5)
            print(end="ERROR DEMONSTRATION: ")
            print("----------------------------------------------------------")
            ProcessingPipeline.NexusManager.setup(0)
            data = {"bonsoir": 5, "coucou": 1, "level": 1, "unit": "C"}
            try:
                ducking_quack_quack_exec(InputStage(), data)
            except Exception as e:
                if not isinstance(e, PipelineException):
                    print("error occured :", e)
            print(end="ERROR DEMONSTRATION END: ")
            print(end="------------------------------------------------------")
            print("----------------------------------------------------------")

        @classmethod
        def monitoring(cls) -> None:
            print("MONITORING DATA --- --- --- ")
            time = str(datetime.now() - cls.exec_time)
            times = time.split(":")
            print("execution time:", times[2], "secondes")
            print("total stream steps:", StreamAdapter.process_nb - 1)
            print("total pipeline steps:", JSONAdapter.process_nb +
                  CSVAdapter.process_nb + StreamAdapter.process_nb - 3)
            print("\nstages logs list:")
            for elem in ProcessingPipeline.stages:
                print(elem)

        @staticmethod
        def setup(level: int) -> None:
            print("initializing Nexus Manager...")
            print('Pipeline capacity: "faster than Flash McQueen"\n')
            print("Creating Data Processing Pipeline...\n")
            ProcessingPipeline.NexusManager.exec_time = datetime.now()
            try:
                if isinstance(level, int) is False or (3 < level or level < 0):
                    raise ValueError(
                        f"Invalide type or range, {level} not in (0 - 3)\n")
                if level == 0:
                    InputStage.disable()
                    TransformStage.disable()
                    OutputStage.disable()
                if level == 1:
                    InputStage.enable()
                    TransformStage.disable()
                    OutputStage.disable()
                elif level == 2:
                    InputStage.enable()
                    TransformStage.enable()
                    OutputStage.disable()
                elif level == 3:
                    InputStage.enable()
                    TransformStage.enable()
                    OutputStage.enable()
                print("")
            except Exception as e:
                print(e)

        @staticmethod
        def process_data(
                first_data: Optional[Dict[str, Any]] = None) -> None | str:

            if first_data is None:
                first_data = {"bonsoir": 5, "coucou": 1,
                              "value": 1, "unit": "C"}
            try:
                out1 = ducking_quack_quack_exec(InputStage(), first_data)
                out2 = ducking_quack_quack_exec(
                    TransformStage(), need_a_list(out1))
                final_output: str = ducking_quack_quack_exec(
                    OutputStage(), need_a_list(out2))
                return final_output
            except Exception as e:
                if not isinstance(e, PipelineException):
                    print("error occured :", e)
            return None


class CommonAdapter(ProcessingPipeline):

    ___crypt_key: List[int] = []

    current_id: str
    process_nb: int

    @classmethod
    def get_crypted_key(cls) -> List[int]:
        return cls.___crypt_key

    @classmethod
    def set_crypted_key(cls, key: List[int]) -> None:
        cls.___crypt_key = key

    @classmethod
    def exec(cls, data: Any) -> Union[str, Any]:
        # when used by a children without object
        # the class name need to be gived to the method
        return cls.process(cls, data)  # type: ignore

    @classmethod
    def set_id(cls, pipeline_id: str) -> None:
        cls.current_id = pipeline_id
        cls.process_nb += 1

    @classmethod
    def get_process_id(cls) -> str:
        return str(cls.process_nb)

    @staticmethod
    def uncrypt(self: Cryptable, valid: str, data: List[int]) -> None:
        try:
            secret_data = Cryptor.uncrypting(self.get_crypted_key(), data)
            if secret_data == valid:
                print("Data OK, send from a valid operator")
            else:
                raise Exception(
                    "Data KO, send from an indalid operator, Process Killed. ")
        except Exception:
            raise Exception(
                "Data KO, send from an indalid operator, Process Killed. ")


class JSONAdapter(CommonAdapter):

    ___crypt_key: List[int] = []
    current_id: str
    process_nb: int = 1

    def __init__(self, pipeline_id: str):
        self.set_id("json_ad" + "_" + pipeline_id)

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
        JSONAdapter(self.get_process_id())

        # self.__name__ exist and can´t Vybe false
        print(self.__name__, "id:", self.current_id,  # type: ignore
              "process start ...")
        try:
            print("input", data)
            # without object
            # methods need direct "self" or "class name" passing
            self.checker(self, data)  # type: ignore
        except Exception as e:
            raise (e)
        data.update({"datetime": str(datetime.now())})
        out = ""
        for elem, nbr in data.items():
            out += "," + str(elem) + " " + str(nbr)
        out = out[1:]
        print("Transform: Enriched with metadata and validation; Success")
        print("Informational Output. data streamed: \
Input saved and ready to use")

        self.add_stage(self.current_id, out)
        # self.__name__ exist and can´t Vybe false
        return [out, Cryptor.crypt_and_send_key(Cryptor.seed_gen(),
                self.__name__, CSVAdapter)]  # type: ignore


class CSVAdapter(CommonAdapter):

    ___crypt_key: List[int] = []
    current_id: str
    process_nb: int = 1

    def __init__(self, pipeline_id: str):
        self.set_id("csv_ad" + "_" + pipeline_id)

    @staticmethod
    def extract(from_: List[Any], to_: List[Any], target: str) -> None:
        for elem in from_:
            if elem[0] == target:
                to_.append(elem)
                from_.remove(elem)

    def sort(self, data: List[Any]) -> List[tuple[str, Any]]:
        out1 = []
        out2: List[tuple[str, Any]] = []
        for elem in data:
            datas = elem.split(" ")
            out1.append((datas[0], datas[1]))
        CSVAdapter.extract(out1, out2, "value")
        CSVAdapter.extract(out1, out2, "unit")
        CSVAdapter.extract(out1, out2, "datetime")
        for elem1, elem2 in out1:
            out2.append((elem1, elem2))
        return out2

    def process(self, data: Any) -> Union[str, Any]:
        CSVAdapter(self.get_process_id())

        # self.__name__ exist and can´t Vybe false
        print(self.__name__,   # type: ignore
              "id:", self.current_id, "process start ...")
        print("input", data[0], " paired with crypted data")

        self.uncrypt(self, "JSONAdapter", data[1])
        new_data: List[str] = data[0].split(",")

        # self atribute not reconize cos used with class
        new_data = self.sort(self, new_data)  # type: ignore
        print("Transform: Uncrypt , parsed and structured data; Success")
        print(
            "Informational Output. data streamed:", new_data
        )
        self.add_stage(self.current_id, new_data)
        # self.__name__ exist and can´t be false
        return [new_data, Cryptor.crypt_and_send_key(Cryptor.seed_gen(),
                str(self.__name__), StreamAdapter)]   # type: ignore


class StreamAdapter(CommonAdapter):

    ___crypt_key: List[int] = []
    _stream_status: int = 0

    current_id: str
    process_nb: int = 1

    def __init__(self, pipeline_id: str):
        self.set_id("stream_ad" + "_" + pipeline_id)

    @classmethod
    def real_time_app(cls, data: List[Any]) -> str:
        cls._stream_status = 1
        print("----------------------------REAL TIME SENSOR START STREAM\
------------------------------------------------------------------------\
-------------------------------------------")
        gen = Cryptor.random_number(Cryptor.seed_gen(), 30)
        log = str(data[0]) + "\n"
        for i in range(next(gen)):
            new_input: Dict[str, Any] = {"data": "temp",
                                         "value": next(gen), "unit": "C"}
            out1 = ducking_quack_quack_exec(InputStage(), new_input)
            out2 = ducking_quack_quack_exec(
                TransformStage(), need_a_list(out1))
            log = log + ducking_quack_quack_exec(
                OutputStage(), need_a_list(out2)) + "\n"

        print("----------------------------REAL TIME SENSOR END STREAM\
----------------------------------------------------------------------\
---------------------------------------------")
        return log

    def process(self, data: Any) -> Union[str, Any]:

        StreamAdapter(self.get_process_id())
        # self.__name__ exist and can´t be false
        print(self.__name__, "id:", self.current_id,  # type: ignore
              "process start ...")
        print("input", data[0], " paired with crypted data")

        self.uncrypt(self, "CSVAdapter", data[1])

        if self._stream_status == 1:
            print("")
            return str(data[0])

        new_data = self.real_time_app(data)
        self._stream_status = 0

        print("Transform: Uncrypt the previous data of the stream\
, and add it to the new generated complex stream")
        print(
            "Informational Output. data streamed and sorted\
: Steam processed normaly, main stream end",
        )
        print("FINALE OUTPUT CREATED .\n")
        self.add_stage(self.current_id, new_data)
        return new_data


def ducking_quack_quack_exec(operator: ProcessingStage, data: Any) -> Any:
    return operator.exec(data)


def need_a_dict(data: Any) -> dict[str, Any]:
    return {"data": data[0], "crypted_name": data[1]}


def need_a_list(data: dict[str, Any]) -> List[Any]:
    return [data.get("data"), data.get("crypted_name")]


class Cryptor:

    @staticmethod
    def crypting(seed: int, data: str) -> List[List[int]]:
        gen: Generator[int, None, None] = Cryptor.random_number(
            seed, 999999999)
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
    def random_number(
            seed: int, range: int = 10) -> Generator[int, None, None]:
        """create a random number"""

        r = seed
        plage = 4294967296
        multiple_chaos = 1664525
        jump = 1013904223
        for i in iter(int, 1):
            r = (r * multiple_chaos + jump) % plage
            yield r % range

    @staticmethod
    def crypt_and_send_key(seed: int, data: str, dest: Cryptable) -> List[int]:
        new_data = Cryptor.crypting(seed, data)
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
    ProcessingPipeline.NexusManager.error_demonstration()
    ProcessingPipeline.NexusManager.setup(3)
    ProcessingPipeline.NexusManager.add_pipeline(
        ProcessingPipeline.NexusManager.process_data())
    ProcessingPipeline.NexusManager.add_pipeline(
        ProcessingPipeline.NexusManager.process_data(
            {"day": "mardi", "logger": "abenabde",
             "value": 8, "unit": "patate"}))
    ProcessingPipeline.NexusManager.monitoring()
    ProcessingPipeline.NexusManager.show_pipelines()
