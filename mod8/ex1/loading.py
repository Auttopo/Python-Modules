
import sys


def check_import(name: str, v_required: str) -> bool:

    try:
        mod = __import__(name)
        if mod.__version__ != v_required:
            print(
                name,
                ": this program only support prescripted version, current:",
                mod.__version__)
            raise
        print("[OK]", name, v_required)
    except Exception:
        print("[KO]", name, v_required)
        return False
    return True


check = True
if not check_import("pandas", "2.1.0"):
    check = False
if not check_import("numpy", "1.26.4"):
    check = False
if not check_import("matplotlib", "3.7.2"):
    check = False
if not check_import("requests", "2.31.0"):
    check = False

if not check:
    print("\nall imports need to be 'OK' to run the program")
    print("for installation use:")
    print("""
          $> pip install - r requirements.txt
          $ python3 loading.py
          # Should run analysis and create visualization
    """)
    print("""or\n
          $> poetry install
          $ poetry run python loading.py
          # Should run analysis with Poetry environment
          #
          $> poetry run python3 loading.py
          # Should run the program with installed dependencies""")
    print("")
    sys.exit("program stopped")
else:
    import requests  # type: ignore
    import numpy
    import pandas
    import matplotlib.pyplot as plt


def is_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    return False


def create_crypto_data() -> pandas:
    what = requests.get("https://api4.binance.com/api/v3/ticker/24hr")
    what1 = what.json()
    datas = []
    for ln in what1:
        values = [val for val in ln.values()]
        datas.append([float(value) for value in values[1:]])

    mycolumns = [key for key in what1[0].keys()]
    myindex = [ln.get("symbol") for ln in what1]
    new_data = pandas.DataFrame(
        datas, index=myindex, columns=mycolumns[1:])
    return new_data


def matplot_generation(datas: pandas) -> None:

    fig, ax = plt.subplots(figsize=(20, 50), layout='constrained')

    categories = datas.index.tolist()[:10]
    values = datas.iloc[:, 0].tolist()[:10]

    ax.bar(categories, values, width=0.5)

    plt.savefig("matrix_analysis.png")
    plt.show()

    print("\nAnalysis complete!\nResults saved to: matrix_analysis.png")


def main() -> None:

    print("\nREQUESTS 2.31.0 : Getting matrix data .")
    print("\nPANDAS 2.1.0 : Parsing Matrix data ... ")
    datas = create_crypto_data()

    print(datas)
    print(f"\nNUMPY 1.26.4 : Processing {len(datas)} data points...")
    computed_datas = {
        "average price change": numpy.average(datas.iloc[:, 0].tolist()),
        "average price change as a percentage":
        numpy.average(datas.iloc[:, 1].tolist())
    }
    print(computed_datas)

    print("\nMATPLOTLIB 3.7.2 : Generating visualization...")
    matplot_generation(datas)


if __name__ == "__poetry__":
    main()

if __name__ == "__main__":
    if "pypoetry" in sys.executable:
        print("Poetry run used !\n")
    else:
        print("Pip probably used for installations\n")
    main()
