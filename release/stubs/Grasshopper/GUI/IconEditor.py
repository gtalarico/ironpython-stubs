# encoding: utf-8
# module Grasshopper.GUI.IconEditor calls itself IconEditor
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_IconObject(object, IGH_IconObject, GH_ISerializable):
    # no doc
    def Contains(self, pt):
        """ Contains(self: GH_IconObject, pt: PointF) -> bool """
        pass

    def Grips(self):
        """ Grips(self: GH_IconObject) -> List[IGH_IconObjectGrip] """
        pass

    def Read(self, reader):
        """ Read(self: GH_IconObject, reader: GH_IReader) -> bool """
        pass

    def RenderObject(self, G):
        """ RenderObject(self: GH_IconObject, G: Graphics) """
        pass

    def Resize(self, newSize):
        """ Resize(self: GH_IconObject, newSize: Size) """
        pass

    def Write(self, writer):
        """ Write(self: GH_IconObject, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Image(self: GH_IconObject) -> Bitmap

"""

    ObjectID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectID(self: GH_IconObject) -> Guid

"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pivot(self: GH_IconObject) -> Point

Set: Pivot(self: GH_IconObject) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: GH_IconObject) -> Size

Set: Size(self: GH_IconObject) = value
"""



class GH_IconObject_Rectangle(GH_IconObject, IGH_IconObject, GH_ISerializable):
    """ GH_IconObject_Rectangle() """
    def Contains(self, pt):
        """ Contains(self: GH_IconObject_Rectangle, pt: PointF) -> bool """
        pass

    def Read(self, reader):
        """ Read(self: GH_IconObject_Rectangle, reader: GH_IReader) -> bool """
        pass

    def RenderObject(self, G):
        """ RenderObject(self: GH_IconObject_Rectangle, G: Graphics) """
        pass

    def Write(self, writer):
        """ Write(self: GH_IconObject_Rectangle, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ObjectID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectID(self: GH_IconObject_Rectangle) -> Guid

"""

    Rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rectangle(self: GH_IconObject_Rectangle) -> Rectangle

"""



class IGH_IconObject(GH_ISerializable):
    # no doc
    def Contains(self, pt):
        """ Contains(self: IGH_IconObject, pt: PointF) -> bool """
        pass

    def Grips(self):
        """ Grips(self: IGH_IconObject) -> List[IGH_IconObjectGrip] """
        pass

    def RenderObject(self, G):
        """ RenderObject(self: IGH_IconObject, G: Graphics) """
        pass

    def Resize(self, newSize):
        """ Resize(self: IGH_IconObject, newSize: Size) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Image(self: IGH_IconObject) -> Bitmap

"""

    ObjectID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectID(self: IGH_IconObject) -> Guid

"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pivot(self: IGH_IconObject) -> Point

Set: Pivot(self: IGH_IconObject) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: IGH_IconObject) -> Size

Set: Size(self: IGH_IconObject) = value
"""



class IGH_IconObjectGrip:
    # no doc
    def RenderGrip(self, G):
        """ RenderGrip(self: IGH_IconObjectGrip, G: Graphics) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: IGH_IconObjectGrip) -> int

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: IGH_IconObjectGrip) -> IGH_IconObject

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: IGH_IconObjectGrip) -> PointF

Set: Position(self: IGH_IconObjectGrip) = value
"""

    Selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selected(self: IGH_IconObjectGrip) -> bool

Set: Selected(self: IGH_IconObjectGrip) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tag(self: IGH_IconObjectGrip) -> object

Set: Tag(self: IGH_IconObjectGrip) = value
"""



