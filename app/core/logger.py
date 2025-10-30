import logging
import os

os.makedirs("app/logs", exist_ok=True)

logging.basicConfig(
    filename="app/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
