import json
import os


# Load the map once globally (lazy load)
_exchange_data = None
_alias_map = {}


def load_exchange_map():
    global _exchange_data, _alias_map

    if _exchange_data is not None:
        return

    file_path = os.path.join(os.path.dirname(__file__), "exchange_map.json")
    with open(file_path, "r", encoding="utf-8") as f:
        _exchange_data = json.load(f)

    # Build alias reverse lookup
    for mic, meta in _exchange_data.items():
        _alias_map[mic.upper()] = mic  # MIC is always valid
        for alias in meta.get("alias", []):
            _alias_map[alias.upper()] = mic


def get_exchange_metadata(code: str) -> dict:
    """
    Return metadata dictionary for given MIC code or alias.
    Raises ValueError if not found.
    """
    load_exchange_map()

    key = code.strip().upper()
    if key not in _alias_map:
        raise ValueError(f"Exchange code or alias '{code}' not found.")

    mic = _alias_map[key]
    return _exchange_data[mic]