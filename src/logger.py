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
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)



logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)



"""
checking if the logger is working or not
if __name__ == "__main__":
    logging.info("Logging has started")
"""



"""
Description

Importing Required Modules:

import logging
import os
from datetime import datetime

logging: Provides a flexible framework for emitting log messages from Python programs.
os: Provides a way of using operating system-dependent functionality, such as reading or writing to the file system.
datetime: Supplies classes for manipulating dates and times.


Creating a Log File Name:

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
datetime.now(): Gets the current date and time.
strftime('%m_%d_%Y_%H_%M_%S'): Formats the current date and time as a string in the format MM_DD_YYYY_HH_MM_SS.
The formatted string is used to create a log file name with a .log extension.


Defining the Directory for Logs:

logs_dir = os.path.join(os.getcwd(), "logs")
os.getcwd(): Returns the current working directory.
os.path.join(): Joins the current working directory and a directory named logs to create a full path for the log directory.


Creating the Logs Directory:
os.makedirs(logs_dir, exist_ok=True)
os.makedirs(): Creates the directory specified by logs_dir. The exist_ok=True parameter 
ensures that no error is raised if the directory already exists.




Setting the Log File Path:
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)
This line joins the logs_dir path with the log file name to create the full path to the log file.


Configuring Logging:
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
filename=LOG_FILE_PATH: Specifies the file where logs will be written.
format: Specifies the format of the log messages. The format includes:
%(asctime)s: The time when the log message was created.
%(lineno)d: The line number in the source code where the logging call was made.
%(name)s: The name of the logger used.
%(levelname)s: The log level of the message (e.g., INFO, DEBUG, ERROR).
%(message)s: The log message.
level=logging.INFO: Sets the logging level to INFO, meaning that all messages at this level and higher 
(WARNING, ERROR, CRITICAL) will be logged.


How the Corrected Code Works

When the script is run, it first generates a unique log file name based on the current date and time.
It then constructs the full path to a directory named logs inside the current working directory.
If the logs directory does not exist, it is created.
The log file path is then constructed by combining the logs directory path with the log file name.
The logging is configured to write log messages to the specified log file, using the defined format and log level.
This setup ensures that each run of the script generates a uniquely named log file, which is placed inside a logs directory, keeping the logging organized and preventing file overwrites.
"""