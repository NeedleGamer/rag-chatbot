"""
scripts/diagnose_my_setup.py

Run this script to dump project + environment info for debugging.
"""

import os, sys, pathlib, platform, subprocess
from importlib.metadata import version, PackageNotFoundError

def safe_version(pkg: str):
    try:
        return version(pkg)
    except PackageNotFoundError:
        return "not installed"

def main():
    root = pathlib.Path(__file__).resolve().parents[1]
    print("="*60)
    print("PROJECT DIAGNOSTICS")
    print("="*60)

    print("\n[System]")
    print("Platform:", platform.platform())
    print("Python exe:", sys.executable)
    print("Python version:", sys.version)
    print("Working dir:", os.getcwd())
    print("Project root (detected):", root)

    print("\n[sys.path first 10]")
    for p in sys.path[:10]:
        print(" ", p)

    print("\n[Environment variables of interest]")
    for key in ["HF_HOME", "GROQ_API_KEY", "CHROMA_DIR", "DATA_DIR", "PYTHONPATH"]:
        print(f" {key} =", os.getenv(key))

    print("\n[Directory structure under project root]")
    for path in sorted(root.glob("*")):
        print(" ", path.name, "->", "dir" if path.is_dir() else "file")

    print("\n[Key packages]")
    for pkg in [
        "langchain", "chromadb", "streamlit",
        "sentence-transformers", "pydantic", "pydantic-settings",
        "python-dotenv", "groq"
    ]:
        print(f" {pkg:20} {safe_version(pkg)}")

    print("\n[Git status]")
    try:
        result = subprocess.run(
            ["git", "status", "-s"],
            cwd=root,
            text=True,
            capture_output=True
        )
        print(result.stdout.strip() or "(clean)")
    except Exception as e:
        print(" git not available:", e)

    print("\n[Config import test]")
    try:
        sys.path.insert(0, str(root))  # ensure project root in path
        from src.config.settings import settings, settings_to_dict
        print(" settings import: OK")
        print(" settings snapshot (without secrets):")
        print(settings_to_dict(settings))
    except Exception as e:
        print(" settings import FAILED:", repr(e))

    print("\nDone.")

if __name__ == "__main__":
    main()
