class PaintEventArgs(EventArgs, IDisposable):
    """
    Provides data for the System.Windows.Forms.Control.Paint event.
    
    PaintEventArgs(graphics: Graphics, clipRect: Rectangle)
    """
    def Dispose(self):
        """
        Dispose(self: PaintEventArgs)
            Releases all resources used by the System.Windows.Forms.PaintEventArgs.
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
    def __new__(self, graphics, clipRect):
        """ __new__(cls: type, graphics: Graphics, clipRect: Rectangle) """
        pass

    ClipRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the rectangle in which to paint.

Get: ClipRectangle(self: PaintEventArgs) -> Rectangle

"""

    Graphics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the graphics used to paint.

Get: Graphics(self: PaintEventArgs) -> Graphics

"""


