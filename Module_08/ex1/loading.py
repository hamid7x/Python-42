from importlib import util, metadata
import sys

def is_installed(package_name: str) -> bool:
    return util.find_spec(package_name) is not None


def check_dependencies(dependencies: list[dict]) -> list[str]:
    missing = []
    for d in dependencies:
        status = 'OK' if is_installed(d['name']) else 'MISSING'
        if status == 'OK':
            version = metadata.version(d['name'])
            print(f"[{status}] {d['name']} ({version}) - {d['description']}")
        else:
            missing.append(d['name'])
            print(f"[{status}] {d['name']} - Dependency Not Installed")
    return missing


def missing_dependencies(missing: list[str]) -> None:
    print("\nMissing dependencies detected!")
    print(f"Missing: {', '.join(missing)}")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("\nInstall with Poetry:")
    print("  poetry install")
    print("\nThen run this program again.")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    dependencies = [
            {'name': 'pandas', 'description': 'Data manipulation ready'},
            {'name': 'numpy', 'description': 'Numerical computation ready'},
            {'name': 'requests', 'description': 'Network access ready'},
            {'name': 'matplotlib', 'description': 'Visualization ready'}
        ]
    missing = check_dependencies(dependencies)
    if missing:
        missing_dependencies(missing)
        sys.exit(1)
    print("hala hashas")
