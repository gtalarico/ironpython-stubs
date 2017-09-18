# encoding: utf-8
# module Grasshopper.GUI.StringDisplay calls itself StringDisplay
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_SimpleListItem(object, IGH_ListItem):
    """ GH_SimpleListItem() """
    def ComputeSize(self, layoutWidth):
        """ ComputeSize(self: GH_SimpleListItem, layoutWidth: int) -> Size """
        pass

    def RenderItem(self, G, destination):
        """ RenderItem(self: GH_SimpleListItem, G: Graphics, destination: Rectangle) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alignment(self: GH_SimpleListItem) -> StringAlignment

Set: Alignment(self: GH_SimpleListItem) = value
"""

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: GH_SimpleListItem) -> Rectangle

Set: BoundingBox(self: GH_SimpleListItem) = value
"""

    Colour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Colour(self: GH_SimpleListItem) -> Color

Set: Colour(self: GH_SimpleListItem) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: GH_SimpleListItem) -> str

Set: Text(self: GH_SimpleListItem) = value
"""



class GH_FormattedListItem(GH_SimpleListItem, IGH_ListItem):
    """ GH_FormattedListItem() """
    def ComputeSize(self, layoutWidth):
        """ ComputeSize(self: GH_FormattedListItem, layoutWidth: int) -> Size """
        pass

    def RenderItem(self, G, destination):
        """ RenderItem(self: GH_FormattedListItem, G: Graphics, destination: Rectangle) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Font(self: GH_FormattedListItem) -> Font

Set: Font(self: GH_FormattedListItem) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: GH_FormattedListItem) -> int

Set: Type(self: GH_FormattedListItem) = value
"""

    Wrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wrap(self: GH_FormattedListItem) -> bool

Set: Wrap(self: GH_FormattedListItem) = value
"""



class GH_StringList(object, IEnumerable[T], IEnumerable):
    """
    GH_StringList[T]()
    GH_StringList[T](initial_capacity: int)
    """
    def AppendItem(self, item):
        """ AppendItem(self: GH_StringList[T], item: T) """
        pass

    def AppendItems(self, items):
        """ AppendItems(self: GH_StringList[T], items: IEnumerable[T]) """
        pass

    def BuildCache(self, layoutBox):
        """ BuildCache(self: GH_StringList[T], layoutBox: Rectangle) """
        pass

    def ClearItems(self):
        """ ClearItems(self: GH_StringList[T]) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: GH_StringList[T]) -> IEnumerator[T] """
        pass

    def GetEnumerator1(self):
        """ GetEnumerator1(self: GH_StringList[T]) -> IEnumerator """
        pass

    def RenderItems(self, graphics, destination, scrollRatio, delegatePreRenderItem=None, delegatePostRenderItem=None):
        """ RenderItems(self: GH_StringList[T], graphics: Graphics, destination: Rectangle, scrollRatio: float, delegatePreRenderItem: RenderItem, delegatePostRenderItem: RenderItem)RenderItems(self: GH_StringList[T], graphics: Graphics, destination: Rectangle, scrollRatio: float) """
        pass

    def RenderScrollBar(self, G, destination, scrollRatio, *__args):
        """
        RenderScrollBar(self: GH_StringList[T], G: Graphics, destination: Rectangle, scrollRatio: float, scrollColor: Color, scrollRectangle: Rectangle) -> Rectangle
        RenderScrollBar(self: GH_StringList[T], G: Graphics, destination: Rectangle, scrollRatio: float, scrollRectangle: Rectangle) -> Rectangle
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, initial_capacity=None):
        """
        __new__(cls: type)
        __new__(cls: type, initial_capacity: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: GH_StringList[T]) -> Rectangle

"""

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: GH_StringList[T]) -> int

Set: Capacity(self: GH_StringList[T]) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GH_StringList[T]) -> int

"""

    IsCached = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCached(self: GH_StringList[T]) -> bool

"""

    StackAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackAlignment(self: GH_StringList[T]) -> StringAlignment

Set: StackAlignment(self: GH_StringList[T]) = value
"""


    RenderItem = None


class IGH_ListItem:
    # no doc
    def ComputeSize(self, layoutWidth):
        """ ComputeSize(self: IGH_ListItem, layoutWidth: int) -> Size """
        pass

    def RenderItem(self, G, destination):
        """ RenderItem(self: IGH_ListItem, G: Graphics, destination: Rectangle) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: IGH_ListItem) -> Rectangle

Set: BoundingBox(self: IGH_ListItem) = value
"""



