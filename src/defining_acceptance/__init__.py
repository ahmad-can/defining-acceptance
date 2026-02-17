"""
Utility scripts for Allure reporting.
"""

import subprocess
import sys
from pathlib import Path


def generate_allure_report():
    """Generate Allure HTML report from test results."""
    results_dir = Path("reports/allure-results")
    report_dir = Path("reports/allure-report")

    if not results_dir.exists() or not any(results_dir.iterdir()):
        print("No test results found. Run pytest first:")
        print("   pytest")
        sys.exit(1)

    print(f"Generating Allure report from {results_dir}...")
    try:
        subprocess.run(
            ["allure", "generate", str(results_dir), "-o", str(report_dir)],
            check=True,
        )
        print(f"Report generated at: {report_dir}/index.html")
        print("\nTo view the report, run:")
        print("   allure-serve")
        print(f"   or open: file://{report_dir.absolute()}/index.html")
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate report: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Allure command not found. Install it:")
        print("   npm install -g allure-commandline")
        print("   or: brew install allure  (on macOS)")
        sys.exit(1)


def serve_allure_report():
    """Serve Allure report with built-in web server."""
    results_dir = Path("reports/allure-results")

    if not results_dir.exists() or not any(results_dir.iterdir()):
        print("No test results found. Run pytest first:")
        print("   pytest")
        sys.exit(1)

    print(f"Starting Allure server with results from {results_dir}...")
    print("   Press Ctrl+C to stop")
    try:
        subprocess.run(["allure", "serve", str(results_dir)], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped")
    except FileNotFoundError:
        print("Allure command not found. Install it:")
        print("   npm install -g allure-commandline")
        print("   or: brew install allure  (on macOS)")
        sys.exit(1)


def clean_allure_reports():
    """Clean Allure results and reports directories."""
    import shutil

    results_dir = Path("reports/allure-results")
    report_dir = Path("reports/allure-report")

    cleaned = []

    if results_dir.exists():
        shutil.rmtree(results_dir)
        cleaned.append(str(results_dir))

    if report_dir.exists():
        shutil.rmtree(report_dir)
        cleaned.append(str(report_dir))

    if cleaned:
        print("Cleaned:")
        for path in cleaned:
            print(f"   {path}")
    else:
        print("Nothing to clean. Allure directories don't exist.")


if __name__ == "__main__":
    serve_allure_report()
