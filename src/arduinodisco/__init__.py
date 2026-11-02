from .arduino_db import BoardDefinition
from .discovery import DiscoveryResult, discover_boards
from .ports import SerialPortInfo

__version__ = "0.1.0"

__all__ = [
    "BoardDefinition",
    "DiscoveryResult",
    "SerialPortInfo",
    "discover_boards",
]
