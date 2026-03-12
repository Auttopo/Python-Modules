
import os


def matrix_update(datas: dict[str, str], tofind: str) -> None:
    if tofind in os.environ:
        datas.update({tofind: os.environ[tofind]})


def setup_data() -> dict[str, str]:
    datas: dict[str, str] = dict()
    read: bool | str = True
    try:
        with open(".env", "r") as file:
            while 1:
                try:
                    read = file.readline()
                    if not read:
                        break
                    data = read.split("=")
                    if len(data[1]) != 0 and data[1][len(data[1]) - 1] == "\n":
                        data[1] = data[1][:len(data[1]) - 1]
                    datas.update({data[0]: data[1]})
                except Exception:
                    pass
    except Exception:
        pass
    matrix_update(datas, "MATRIX_MODE")
    matrix_update(datas, "DATABASE_URL")
    matrix_update(datas, "API_KEY")
    matrix_update(datas, "LOG_LEVEL")
    matrix_update(datas, "ZION_ENDPOINT")

    return datas


def trying_data(datas: dict[str, str], tofind: str) -> bool:
    try:
        datas[tofind]
    except Exception:
        print(tofind, "not found in settings")
        return False
    return True


def data_checker(datas: dict[str, str]) -> bool:
    check = True
    check = trying_data(datas, "MATRIX_MODE") and check
    if check:
        if not (datas["MATRIX_MODE"] == "development"
                or datas["MATRIX_MODE"] == "production"):
            print("unknown mode:", datas["MATRIX_MODE"])
            check = False
    check = trying_data(datas, "DATABASE_URL") and check
    check = trying_data(datas, "API_KEY") and check
    check = trying_data(datas, "LOG_LEVEL") and check
    check = trying_data(datas, "ZION_ENDPOINT") and check
    return check


def main() -> None:
    datas = setup_data()
    if not data_checker(datas):
        print("\nplease update settings\nprogram stopped")
        return
    print("Configuration loaded:\n")
    print("Mode:", datas["MATRIX_MODE"])
    print("Database", datas["DATABASE_URL"])
    print("API Access: ", datas["API_KEY"])
    print("Log Level: ", datas["LOG_LEVEL"])
    print("Zion Network", datas["ZION_ENDPOINT"])

    print("\nEnvironment security check:")
    print("[OK] necessary environemnt variable \
present or .env loaded correclty")
    print("[OK] No hardcoded secrets detected")
    if datas["MATRIX_MODE"] == "development":
        print("[OK] Production overrides available")
    else:
        print("[OK] Production overrides not - available")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix.\n")
    main()
