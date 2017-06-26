class AppContext(object):
    # no doc
    @staticmethod
    def SetSwitch(switchName, isEnabled):
        """ SetSwitch(switchName: str, isEnabled: bool) """
        pass

    @staticmethod
    def TryGetSwitch(switchName, isEnabled):
        """ TryGetSwitch(switchName: str) -> (bool, bool) """
        pass

    BaseDirectory = 'C:\\Program Files (x86)\\IronPython-2.7.7\\'
    __all__ = [
        'SetSwitch',
        'TryGetSwitch',
    ]

