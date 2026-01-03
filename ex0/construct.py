#!/usr/bin/env python3
import sys
import os
import site


def main() -> None:
    """
    仮想環境判定関数
    """

    # sys.prefixは現在実行されている環境
    # sys.base_prefixは元々のPythonがインストールされちる環境
    is_venv = (sys.prefix != sys.base_prefix)

    if is_venv:
        inside_matrix()
    else:
        outside_matrix()


def outside_matrix() -> None:
    """
    仮想環境に入っていない場合
    作成方法を示す
    """

    print()
    print("MATRIX STATUS: You're still plugged in")
    print()

    # 1.
    print(f"Current Python: {sys.executable}\n"
          "Virtual Environment: None detected")
    print()

    print("WARNING: You're in the global environment!\n"
          "The machines can see everything you install.")
    print()

    print("To enter the construct, run:\n"
          "python -m venv matrix_env\n"
          "source matrix_env/bin/activate # On Unix\n"
          "matrix_env\n"
          "Scripts\n"
          "activate # On Windows")
    print()

    print("Then run this program again.")


def inside_matrix() -> None:
    """
    仮想環境に入っていた場合
    インストールパスを表示する
    """

    print()
    print("MATRIX STATUS: Welcome to the construct")
    print()

    # 仮想環境の情報を出力
    base_name = os.path.basename(sys.prefix)
    print(f"Current Python: {sys.executable}\n"
          f"Virtual Environment: {base_name}\n"
          f"Environment Path: {sys.prefix}")
    print()

    # インストール先のパスを表示
    ins_path = site.getsitepackages()[0]
    print("SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting\n"
          "the global system.\n"
          f"Package installation path:\n{ins_path}")


if __name__ == "__main__":
    main()
