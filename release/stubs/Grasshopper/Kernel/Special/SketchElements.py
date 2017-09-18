# encoding: utf-8
# module Grasshopper.Kernel.Special.SketchElements calls itself SketchElements
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_SketchBox(object):
    """ GH_SketchBox() """

class GH_SketchCloud(object):
    """ GH_SketchCloud() """

class GH_SketchElement(object, IGH_SketchElement, IGH_InstanceDescription, GH_ISerializable):
    # no doc
    def IsPickPoint(self, *__args):
        """
        IsPickPoint(self: GH_SketchElement, box: RectangleF, bCrossingBox: GH_PickBox) -> bool
        IsPickPoint(self: GH_SketchElement, pt: PointF) -> bool
        """
        pass

    def NewInstanceGuid(self, UUID=None):
        """ NewInstanceGuid(self: GH_SketchElement, UUID: Guid)NewInstanceGuid(self: GH_SketchElement) """
        pass

    def Read(self, reader):
        """ Read(self: GH_SketchElement, reader: GH_IReader) -> bool """
        pass

    def Write(self, writer):
        """ Write(self: GH_SketchElement, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: GH_SketchElement) -> RectangleF

"""

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Category(self: GH_SketchElement) -> str

Set: Category(self: GH_SketchElement) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_SketchElement) -> str

Set: Description(self: GH_SketchElement) = value
"""

    GraphicsPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsPath(self: GH_SketchElement) -> GraphicsPath

"""

    HasCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasCategory(self: GH_SketchElement) -> bool

"""

    HasSubCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasSubCategory(self: GH_SketchElement) -> bool

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: GH_SketchElement) -> Image

"""

    InstanceDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstanceDescription(self: GH_SketchElement) -> str

"""

    InstanceGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstanceGuid(self: GH_SketchElement) -> Guid

"""

    Keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keywords(self: GH_SketchElement) -> IEnumerable[str]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_SketchElement) -> str

Set: Name(self: GH_SketchElement) = value
"""

    NickName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NickName(self: GH_SketchElement) -> str

Set: NickName(self: GH_SketchElement) = value
"""

    SubCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubCategory(self: GH_SketchElement) -> str

Set: SubCategory(self: GH_SketchElement) = value
"""



class GH_SketchEllipse(object):
    """ GH_SketchEllipse() """

class GH_SketchFreehandStroke(object):
    """ GH_SketchFreehandStroke() """

class GH_SketchLine(object):
    """ GH_SketchLine() """

class IGH_SketchElement(IGH_InstanceDescription, GH_ISerializable):
    # no doc
    def IsPickPoint(self, *__args):
        """
        IsPickPoint(self: IGH_SketchElement, box: RectangleF, bCrossingBox: GH_PickBox) -> bool
        IsPickPoint(self: IGH_SketchElement, pt: PointF) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: IGH_SketchElement) -> RectangleF

"""

    GraphicsPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsPath(self: IGH_SketchElement) -> GraphicsPath

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: IGH_SketchElement) -> Image

"""



