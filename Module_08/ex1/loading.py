from importlib import util, metadata, import_module
import sys


API_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=32.8811&longitude=-6.9063"
    "&hourly=temperature_2m"
    "&past_days=7&forecast_days=0"
)


def is_installed(package_name: str) -> bool:
    return util.find_spec(package_name) is not None


def check_dependencies(dependencies: list[dict[str, str]]) -> list[str]:
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


def missing_dependencies() -> None:
    print("\nMissing dependencies detected!")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("Or")
    print("Install with Poetry:")
    print("  poetry install")
    print("\nThen run this program again.")


def fetch_api_data(url: str) -> list[float]:
    requests = import_module('requests')
    response = requests.get(url)
    data = response.json()
    try:
        temps = data['hourly']['temperature_2m']
    except KeyError:
        print("Unexpected API response format.")
        sys.exit(1)
    return temps


def analyse_and_visualize_matrix_data(temps: list[float]) -> None:
    pd = import_module("pandas")
    np = import_module('numpy')
    ptl = import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(temps)} data points...")
    temps = np.array(temps)
    df = pd.DataFrame(temps, columns=["temperature"])

    print("Generating visualization...\n")
    ptl.figure(figsize=(10, 5))
    ptl.title("Matrix Temperature Data")
    ptl.xlabel("Time (hours)")
    ptl.ylabel("Temperature (°C)")
    ptl.plot(df["temperature"], label="Temp")
    ptl.legend()
    ptl.savefig("matrix_analysis.png")
    ptl.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


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
        missing_dependencies()
        sys.exit(1)
    temps = fetch_api_data(API_URL)
    analyse_and_visualize_matrix_data(temps)
