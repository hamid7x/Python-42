import os
from dotenv import load_dotenv  # type: ignore


load_dotenv()


def load_config() -> dict:
    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    config = {
            'mode': matrix_mode, 'database': database_url, 'api_key': api_key,
            'log': log_level, 'endpoint': zion_endpoint
            }
    return config


def display_config(config: dict) -> None:
    modes = {'development': 'local', 'production': 'remote'}

    mode_status = config['mode'] if config['mode'] else "Not Configured"
    print(f"Mode: {mode_status}")

    if config['database'] and config['mode'] in modes:
        db_location = modes.get(config['mode'], 'unknown')
        print(f"Database: Connected to {db_location} instance")
    else:
        print("Database: Not Connected")

    api_status = "Authenticated" if config['api_key'] else "Not Authenticated"
    print(f"API Access: {api_status}")

    log_status = config['log'] if config['log'] else "Not Configured"
    print(f"Log Level: {log_status}")

    zion_status = "Online" if config['endpoint'] else "Offline"
    print(f"Zion Network: {zion_status}")


def check_hardcoded_secrets() -> bool:
    with open(__file__, 'r') as f:
        content = f.read()
        keywords = [
                'matrix_mode' + ' = "',
                'matrix_mode' + " = '",
                'api_key' + ' = "',
                'api_key' + " = '",
                'database_url' + ' = "',
                'database_url' + " = '",
                'log_level' + ' = "',
                'log_level' + " = '",
                'zion_endpoint' + ' = "',
                'zion_endpoint' + ' = "',
            ]
        for keyword in keywords:
            if keyword in content.lower():
                return False
        return True


def is_production_override() -> bool:
    return os.environ.get("MATRIX_MODE") == "production"


def security_check() -> None:
    if check_hardcoded_secrets():
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARN] hardcoded secrets found!")

    if not os.path.exists(".env"):
        print("[WARN] .env file not found")
    elif os.path.getsize(".env") == 0:
        print("[WARN] .env file is empty")
    else:
        print("[OK] .env file is configured")

    if is_production_override():
        print("[OK] Production overrides available")
    else:
        print("[OK] Running in development mode")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    config = load_config()
    display_config(config)
    print("\nEnvironment security check:")
    security_check()
    print("\nThe Oracle sees all configurations.")
