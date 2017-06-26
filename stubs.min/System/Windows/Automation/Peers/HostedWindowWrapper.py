class HostedWindowWrapper(object):
    """
    Exposes System.Windows.Interop.HwndHost types to UI Automation.
    
    HostedWindowWrapper(hwnd: IntPtr)
    """
    @staticmethod # known case of __new__
    def __new__(self, hwnd):
        """ __new__(cls: type, hwnd: IntPtr) """
        pass

