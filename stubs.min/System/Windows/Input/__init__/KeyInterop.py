class KeyInterop(object):
    """ Provides static methods to convert between Win32 Virtual-Keys and the WPF�System.Windows.Input.Key enumeration. """
    @staticmethod
    def KeyFromVirtualKey(virtualKey):
        """
        KeyFromVirtualKey(virtualKey: int) -> Key
        
            Converts a Win32 Virtual-Key into WPF�System.Windows.Input.Key.
        
            virtualKey: The virtual key to convert.
            Returns: The WPF key.
        """
        pass

    @staticmethod
    def VirtualKeyFromKey(key):
        """
        VirtualKeyFromKey(key: Key) -> int
        
            Converts a WPF�System.Windows.Input.Key into a�Win32 Virtual-Key.
        
            key: The WPF to convert.
            Returns: The Win32 Virtual-Key.
        """
        pass

    __all__ = [
        'KeyFromVirtualKey',
        'VirtualKeyFromKey',
    ]

