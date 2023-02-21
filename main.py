"APP Runner"

from monitor.ui.splash import SplashScreen
from monitor.utilities.utils import DPIAwareness

if __name__ == "__main__":
    system_monitor = SplashScreen()
    DPIAwareness(system_monitor)
    system_monitor.mainloop()