#!/usr/bin/env python3


def main() -> None:
    """
    .envファイルの使用デモ
    """

    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    try:
        import os
        from dotenv import load_dotenv
    except ModuleNotFoundError as e:
        print(f"ModuleNotFoundError: {e}")
        print("You need to install dotenv.")
        print("   python3 -m venv ex2_env")
        print("   source ex2_env/bin/activate")
        print("   pip install python-dotenv")
        return

    # 1.環境変数を.envから読み込む
    if load_dotenv():
        # .後に行うセキュリティチェック用フラグ
        sec3 = True

        mode = os.getenv("MATRIX_MODE")
        db_url = os.getenv("DATABASE_URL")
        api = os.getenv("API_KEY")
        log = os.getenv("LOG_LEVEL")
        z_url = os.getenv("ZION_ENDPOINT")

        envs = (mode, db_url, api, log, z_url)
        if None in envs:
            print("Error: Required environment variables are missing.")
            print("Please check your .env file or run: cp .env.example .env")
            return

        # 2.本番環境であればkeyを伏字にする
        if mode == "production":
            api = "**********"
            db_url = "**********"

        # 3.読み込んだ内容をPut
        print("Configuration loaded:\n"
              f"Mode: {mode}\n"
              f"Database: {db_url}\n"
              f"API Access: {api}\n"
              f"Log Level: {log}\n"
              f"Zion Network: {z_url}")
        print()
    else:
        api = None
        sec3 = False

    # 4.セキュリティチェック
    print("Environment security check:")
    # .check1 APIキーが.envから読み込まれているか
    if api and api != "your_api_key_here":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] hardcoded secrets detected")
    # .check2 実際に.envファイルが存在するか
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not found")
        print("    If you were running it outside the ex2 directory, "
              "please try running it inside the ex2 directory.")
    # .check3 .envが読み込まれたか
    if sec3:
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides unavailable")


if __name__ == "__main__":
    main()
