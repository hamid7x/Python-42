import os
import sys
from dotenv import load_dotenv


load_dotenv()


def load_config() -> dict:
    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    endpoint = os.getenv("ZION_ENDPOINT")
    config = {
            'mode': mode, 'database': database, 'api_key': api_key,
            'log': log, 'endpoint': endpoint
            }
    return config


def check_config(config: dict) -> None:
    for k, v in config.items():
        if v is None:
            print(f"[MISSING] {k} is not configured")
            sys.exit(1)


def display_config(config: dict) -> None:
    print(f"Mode: {config['mode']}")
    if config['mode'] == 'develoment':
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to remote instance")
    print(f"API Access: {config['api_key']}")
    print(f"Log Level: {config['log']}")
    print(f"Zion Network: {config['endpoint']}")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    config = load_config()
    check_config(config)
    display_config(config)
