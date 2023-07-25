
import logging
import os

logger = None

def setup_logger(log_file="app.log", log_dir=os.path.join(os.path.abspath(__file__),"../../../logs"), log_level=logging.DEBUG):
    global logger
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)
    logging.basicConfig(filename=log_path, level=log_level, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger(__name__)

def get_logger():
    global logger
    if logger is None:
        setup_logger()
    return logger
