

class CronMonitorException(Exception):

    """
    Generic CronMonitor Exception.
    """

    def __init__(self, message=None, payload=None):
        super(CronMonitorException, self).__init__(message)
        self.payload = payload
