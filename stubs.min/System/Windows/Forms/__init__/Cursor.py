class Cursor(object, IDisposable, ISerializable):
    """
    Represents the image used to paint the mouse pointer.
    
    Cursor(handle: IntPtr)
    Cursor(stream: Stream)
    Cursor(fileName: str)
    Cursor(type: Type, resource: str)
    """
    def CopyHandle(self):
        """
        CopyHandle(self: Cursor) -> IntPtr
        
            Copies the handle of this System.Windows.Forms.Cursor.
            Returns: An System.IntPtr that represents the cursor's handle.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Cursor)
            Releases all resources used by the System.Windows.Forms.Cursor.
        """
        pass

    def Draw(self, g, targetRect):
        """
        Draw(self: Cursor, g: Graphics, targetRect: Rectangle)
            Draws the cursor on the specified surface, within the specified bounds.
        
            g: The System.Drawing.Graphics surface on which to draw the System.Windows.Forms.Cursor.
            targetRect: The System.Drawing.Rectangle that represents the bounds of the System.Windows.Forms.Cursor.
        """
        pass

    def DrawStretched(self, g, targetRect):
        """
        DrawStretched(self: Cursor, g: Graphics, targetRect: Rectangle)
            Draws the cursor in a stretched format on the specified surface, within the specified bounds.
        
            g: The System.Drawing.Graphics surface on which to draw the System.Windows.Forms.Cursor.
            targetRect: The System.Drawing.Rectangle that represents the bounds of the System.Windows.Forms.Cursor.
        """
        pass

    def Equals(self, obj):
        """
        Equals(self: Cursor, obj: object) -> bool
        
            Returns a value indicating whether this cursor is equal to the specified System.Windows.Forms.Cursor.
        
            obj: The System.Windows.Forms.Cursor to compare.
            Returns: true if this cursor is equal to the specified System.Windows.Forms.Cursor; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Cursor) -> int
        
            Retrieves the hash code for the current System.Windows.Forms.Cursor.
            Returns: A hash code for the current System.Windows.Forms.Cursor.
        """
        pass

    @staticmethod
    def Hide():
        """
        Hide()
            Hides the cursor.
        """
        pass

    @staticmethod
    def Show():
        """
        Show()
            Displays the cursor.
        """
        pass

    def ToString(self):
        """
        ToString(self: Cursor) -> str
        
            Retrieves a human readable string representing this System.Windows.Forms.Cursor.
            Returns: A System.String that represents this System.Windows.Forms.Cursor.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, handle: IntPtr)
        __new__(cls: type, fileName: str)
        __new__(cls: type, type: Type, resource: str)
        __new__(cls: type, stream: Stream)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the handle of the cursor.

Get: Handle(self: Cursor) -> IntPtr

"""

    HotSpot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the cursor hot spot.

Get: HotSpot(self: Cursor) -> Point

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the cursor object.

Get: Size(self: Cursor) -> Size

"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object that contains data about the System.Windows.Forms.Cursor.

Get: Tag(self: Cursor) -> object

Set: Tag(self: Cursor) = value
"""


    Clip = None
    Current = None
    Position = None

