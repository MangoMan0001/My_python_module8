#!/usr/bin/env python3


def main() -> None:
    """
    ライブラリチェッカー
    """

    print()
    print("LOADING STATUS: Loading programs...")
    print()

    # .依存関係の確認
    try:
        print("Checking dependencies:")
        # 1.Pandasインポート
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) ready")

        # 2.Requestsインポート
        import requests
        print(f"[OK] requests ({requests.__version__}) ready")

        # 3.Matplotlibインポート
        import matplotlib
        print(f"[OK] matplotlib ({matplotlib.__version__}) ready")

    except ImportError:
        print("\nWARNING: Some modules are missing!")
        print("The machines prevent you from running this program.")
        print("Please install dependencies using one of these methods:")
        print("\n1. Using pip (Traditional):")
        print("   python3 -m venv my_env")
        print("   source my_env/bin/activate")
        print("   pip install -r ex1/requirements.txt")
        print("\n2. Using Poetry (Modern):")
        print("   poetry install")
        return
    print()

    import pandas as pd
    import matplotlib.pyplot as plt

    # 4.Requestsを使ってテストサイトに接続
    print("Fetching data...")
    try:
        requests.get('https://httpbin.org/json', timeout=3)
        print("[OK] Requests used successfully.")
    except Exception:
        print("[Skipped] Network error (simulated).")

    # 5.Pandas使用
    print("Analyzing Matrix data...")
    data = {"Name": ["Neo", "Morpheus"], "Power": [100, 80]}
    df = pd.DataFrame(data)
    print(df)
    print()

    # 6.Matplotlib使用
    print("Generating visualization...")
    plt.bar(df["Name"], df["Power"])
    plt.savefig("matrix_analysis.png")
    print()

    print("Analysis complete!\n"
          "Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
