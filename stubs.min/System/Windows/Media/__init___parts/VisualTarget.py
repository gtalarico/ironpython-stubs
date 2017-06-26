class VisualTarget(CompositionTarget, IDisposable, ICompositionTarget):
    """
    Provides functionality for connecting one visual tree to another visual tree across thread boundaries.
    
    VisualTarget(hostVisual: HostVisual)
    """
    def Dispose(self):
        """
        Dispose(self: VisualTarget)
            Cleans up the state associated with the System.Windows.Interop.HwndTarget.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, hostVisual):
        """ __new__(cls: type, hostVisual: HostVisual) """
        pass

    TransformFromDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a matrix that can be used to transform coordinates from the rendering destination device to the System.Windows.Media.VisualTarget.

Get: TransformFromDevice(self: VisualTarget) -> Matrix

"""

    TransformToDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a matrix that can be used to transform coordinates from the System.Windows.Media.VisualTarget to the rendering destination device.

Get: TransformToDevice(self: VisualTarget) -> Matrix

"""


