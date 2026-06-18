import logging
import logging
import sys
from pathlib import Path

logs_dir = Path(__file__).resolve().parents[1] / "logs"
logs_dir.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("api_logger")

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    str(logs_dir / "api_test.log")
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Prevent log propagation to the root logger to avoid duplicate messages
logger.propagate = False

console_handler = logging.StreamHandler(
    sys.stdout
)

console_handler.setFormatter(
    formatter
)

logger.addHandler(
    file_handler
)

logger.addHandler(
    console_handler
)