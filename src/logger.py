import logging
import os
from datetime import datetime
"""
Logger is for the purpose that, any excecution that is probably happens, we should be able to log all those information.
like excecution anything in some files
so that, we will be able to track all the information, errors 
so any customer exception occures, we can log them in to a looger.txt file
"""

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
#os.getcwd gives us the current working directory
os.makedirs(logs_path, exist_ok=True)
# exist_ok=True even if there exists a file, keep on appending the file


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


"""
if __name__ == "__main__":
    logging.info("Logging has started")
"""