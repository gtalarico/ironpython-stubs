# encoding: utf-8
# module Grasshopper.Kernel.Types.Transforms calls itself Transforms
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Generic(object, ITransform, GH_ISerializable):
    """
    Generic()
    Generic(transform: Transform)
    """
    def Duplicate(self):
        """ Duplicate(self: Generic) -> ITransform """
        pass

    def Read(self, reader):
        """ Read(self: Generic, reader: GH_IReader) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Generic) -> ITransform """
        pass

    def ToMatrix(self):
        """ ToMatrix(self: Generic) -> Transform """
        pass

    def ToString(self):
        """ ToString(self: Generic) -> str """
        pass

    def Write(self, writer):
        """ Write(self: Generic, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, transform=None):
        """
        __new__(cls: type)
        __new__(cls: type, transform: Transform)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Generic) -> str

"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transform(self: Generic) -> Transform

Set: Transform(self: Generic) = value
"""



class Identity(object, ITransform, GH_ISerializable):
    """ Identity() """
    def Duplicate(self):
        """ Duplicate(self: Identity) -> ITransform """
        pass

    def Read(self, reader):
        """ Read(self: Identity, reader: GH_IReader) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Identity) -> ITransform """
        pass

    def ToMatrix(self):
        """ ToMatrix(self: Identity) -> Transform """
        pass

    def ToString(self):
        """ ToString(self: Identity) -> str """
        pass

    def Write(self, writer):
        """ Write(self: Identity, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Identity) -> str

"""



class ITransform(GH_ISerializable):
    # no doc
    def Duplicate(self):
        """ Duplicate(self: ITransform) -> ITransform """
        pass

    def Reverse(self):
        """ Reverse(self: ITransform) -> ITransform """
        pass

    def ToMatrix(self):
        """ ToMatrix(self: ITransform) -> Transform """
        pass

    def ToString(self):
        """ ToString(self: ITransform) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ITransform) -> str

"""



class Orientation(object, ITransform, GH_ISerializable):
    """
    Orientation()
    Orientation(source: Plane, target: Plane)
    """
    def Duplicate(self):
        """ Duplicate(self: Orientation) -> ITransform """
        pass

    def Read(self, reader):
        """ Read(self: Orientation, reader: GH_IReader) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Orientation) -> ITransform """
        pass

    def ToMatrix(self):
        """ ToMatrix(self: Orientation) -> Transform """
        pass

    def ToString(self):
        """ ToString(self: Orientation) -> str """
        pass

    def Write(self, writer):
        """ Write(self: Orientation, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, source=None, target=None):
        """
        __new__(cls: type)
        __new__(cls: type, source: Plane, target: Plane)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Orientation) -> str

"""

    SourceFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceFrame(self: Orientation) -> Plane

Set: SourceFrame(self: Orientation) = value
"""

    TargetFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetFrame(self: Orientation) -> Plane

Set: TargetFrame(self: Orientation) = value
"""



class Projection(object, ITransform, GH_ISerializable):
    """
    Projection()
    Projection(plane: Plane)
    """
    def Duplicate(self):
        """ Duplicate(self: Projection) -> ITransform """
        pass

    def Read(self, reader):
        """ Read(self: Projection, reader: GH_IReader) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Projection) -> ITransform """
        pass

    def ToMatrix(self):
        """ ToMatrix(self: Projection) -> Transform """
        pass

    def ToString(self):
        """ ToString(self: Projection) -> str """
        pass

    def Write(self, writer):
        """ Write(self: Projection, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, plane=None):
        """
        __new__(cls: type)
        __new__(cls: type, plane: Plane)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Projection) -> str

"""

    ProjectionPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionPlane(self: Projection) -> Plane

Set: ProjectionPlane(self: Projection) = value
"""



class Rotation(object, ITransform, GH_ISerializable):
    """
    Rotation()
    Rotation(center: Point3d, axis: Vector3d, angle: float)
    Rotation(center: Point3d, dir0: Vector3d, dir1: Vector3d)
    """
    def Duplicate(self):
        """ Duplicate(self: Rotation) -> ITransform """
        pass

    def Read(self, reader):
        """ Read(self: Rotation, reader: GH_IReader) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Rotation) -> ITransform """
        pass

    def ToMatrix(self):
        """ ToMatrix(self: Rotation) -> Transform """
        pass

    def ToString(self):
        """ ToString(self: Rotation) -> str """
        pass

    def Write(self, writer):
        """ Write(self: Rotation, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, center=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, center: Point3d, axis: Vector3d, angle: float)
        __new__(cls: type, center: Point3d, dir0: Vector3d, dir1: Vector3d)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Rotation) -> str

"""

    RotationAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationAngle(self: Rotation) -> float

Set: RotationAngle(self: Rotation) = value
"""

    RotationAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationAxis(self: Rotation) -> Vector3d

Set: RotationAxis(self: Rotation) = value
"""

    RotationCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationCenter(self: Rotation) -> Point3d

Set: RotationCenter(self: Rotation) = value
"""



class Scale(object, ITransform, GH_ISerializable):
    """
    Scale()
    Scale(point: Point3d, scale: float)
    Scale(frame: Plane, scale: float)
    Scale(frame: Plane, xscale: float, yscale: float, zscale: float)
    """
    def Duplicate(self):
        """ Duplicate(self: Scale) -> ITransform """
        pass

    def Read(self, reader):
        """ Read(self: Scale, reader: GH_IReader) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Scale) -> ITransform """
        pass

    def ToMatrix(self):
        """ ToMatrix(self: Scale) -> Transform """
        pass

    def ToString(self):
        """ ToString(self: Scale) -> str """
        pass

    def Write(self, writer):
        """ Write(self: Scale, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, point: Point3d, scale: float)
        __new__(cls: type, frame: Plane, scale: float)
        __new__(cls: type, frame: Plane, xscale: float, yscale: float, zscale: float)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Scale) -> str

"""

    ScaleXFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleXFactor(self: Scale) -> float

Set: ScaleXFactor(self: Scale) = value
"""

    ScaleYFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleYFactor(self: Scale) -> float

Set: ScaleYFactor(self: Scale) = value
"""

    ScaleZFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleZFactor(self: Scale) -> float

Set: ScaleZFactor(self: Scale) = value
"""

    ScalingFrame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScalingFrame(self: Scale) -> Plane

Set: ScalingFrame(self: Scale) = value
"""



class Translation(object, ITransform, GH_ISerializable):
    """
    Translation()
    Translation(translation: Vector3d)
    """
    def Duplicate(self):
        """ Duplicate(self: Translation) -> ITransform """
        pass

    def Read(self, reader):
        """ Read(self: Translation, reader: GH_IReader) -> bool """
        pass

    def Reverse(self):
        """ Reverse(self: Translation) -> ITransform """
        pass

    def ToMatrix(self):
        """ ToMatrix(self: Translation) -> Transform """
        pass

    def ToString(self):
        """ ToString(self: Translation) -> str """
        pass

    def Write(self, writer):
        """ Write(self: Translation, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, translation=None):
        """
        __new__(cls: type)
        __new__(cls: type, translation: Vector3d)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Translation) -> str

"""

    TranslationVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TranslationVector(self: Translation) -> Vector3d

Set: TranslationVector(self: Translation) = value
"""



