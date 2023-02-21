"APP Runner"

import sys

from monitor.ui.splash import SplashScreen
from monitor.utils import DPIAwareness
from monitor.logger import logging
from monitor.exception import MonitorException


if __name__ == "__main__":
    try:
        logging.info(f"App started")
        system_monitor = SplashScreen()
        DPIAwareness(system_monitor)
        system_monitor.mainloop()
        logging.info(f"App closed")
    except Exception as e:
        raise MonitorException(e, sys)