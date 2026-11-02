"""Security-first starter entry point.

This template intentionally does not connect to an exchange or place orders.
"""

import json
from pathlib import Path


def load_config(path: str = "config.example.json") -> dict:
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    config = load_config()
    print("Binance Wallet Agent — starter template")
    print("Mode:", config.get("mode", "paper"))
    print("Live trading enabled:", config.get("live_trading_enabled", False))
    print("No exchange connection or orders are made by this starter.")
    print("Review README.md and config.example.json before extending the project.")


if __name__ == "__main__":
    main()
