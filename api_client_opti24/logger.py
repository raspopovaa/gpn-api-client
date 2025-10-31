import logging
from api_client_opti24.config import LOG_LEVEL, LOGGER_FILE
log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
logging.basicConfig(
    level=log_level,
    filename=LOGGER_FILE,
    filemode="w",
    format="%(asctime)s [%(levelname)s] %(module)s: %(message)s",
)
logger = logging.getLogger(__name__)
