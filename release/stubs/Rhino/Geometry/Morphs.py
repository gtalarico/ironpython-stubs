# encoding: utf-8
# module Rhino.Geometry.Morphs calls itself Morphs
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BendSpaceMorph(SpaceMorph, IDisposable):
    """
    Deforms objects by bending along a spine arc.
    
    BendSpaceMorph(start: Point3d, end: Point3d, point: Point3d, straight: bool, symmetric: bool)
    BendSpaceMorph(start: Point3d, end: Point3d, point: Point3d, angle: float, straight: bool, symmetric: bool)
    """
    def Dispose(self):
        """
        Dispose(self: BendSpaceMorph)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: BendSpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point.
        
            point: A point that will be morphed by this object.
            Returns: Resulting morphed point.
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
    def __new__(self, start, end, point, *__args):
        """
        __new__(cls: type, start: Point3d, end: Point3d, point: Point3d, straight: bool, symmetric: bool)
        __new__(cls: type, start: Point3d, end: Point3d, point: Point3d, angle: float, straight: bool, symmetric: bool)
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the space morph definition is valid, false otherwise.

Get: IsValid(self: BendSpaceMorph) -> bool

"""



class FlowSpaceMorph(SpaceMorph, IDisposable):
    """
    Re-aligns objects from a base curve to a target curve.
    
    FlowSpaceMorph(curve0: Curve, curve1: Curve, preventStretching: bool)
    FlowSpaceMorph(curve0: Curve, curve1: Curve, reverseCurve0: bool, reverseCurve1: bool, preventStretching: bool)
    """
    def Dispose(self):
        """
        Dispose(self: FlowSpaceMorph)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: FlowSpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point.
        
            point: A point that will be morphed by this object.
            Returns: Resulting morphed point.
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
    def __new__(self, curve0, curve1, *__args):
        """
        __new__(cls: type, curve0: Curve, curve1: Curve, preventStretching: bool)
        __new__(cls: type, curve0: Curve, curve1: Curve, reverseCurve0: bool, reverseCurve1: bool, preventStretching: bool)
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the space morph definition is valid, false otherwise.

Get: IsValid(self: FlowSpaceMorph) -> bool

"""



class MaelstromSpaceMorph(SpaceMorph, IDisposable):
    """
    Deforms objects in a spiral as if they were caught in a whirlpool.
    
    MaelstromSpaceMorph(plane: Plane, radius0: float, radius1: float, angle: float)
    """
    def Dispose(self):
        """
        Dispose(self: MaelstromSpaceMorph)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: MaelstromSpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point.
        
            point: A point that will be morphed by this object.
            Returns: Resulting morphed point.
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
    def __new__(self, plane, radius0, radius1, angle):
        """ __new__(cls: type, plane: Plane, radius0: float, radius1: float, angle: float) """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the space morph definition is valid, false otherwise.

Get: IsValid(self: MaelstromSpaceMorph) -> bool

"""



class SplopSpaceMorph(SpaceMorph, IDisposable):
    """
    Rotates, scales, and wraps objects on a surface.
    
    SplopSpaceMorph(plane: Plane, surface: Surface, surfaceParam: Point2d)
    SplopSpaceMorph(plane: Plane, surface: Surface, surfaceParam: Point2d, scale: float)
    SplopSpaceMorph(plane: Plane, surface: Surface, surfaceParam: Point2d, scale: float, angle: float)
    """
    def Dispose(self):
        """
        Dispose(self: SplopSpaceMorph)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: SplopSpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point.
        
            point: A point that will be morphed by this object.
            Returns: Resulting morphed point.
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
    def __new__(self, plane, surface, surfaceParam, scale=None, angle=None):
        """
        __new__(cls: type, plane: Plane, surface: Surface, surfaceParam: Point2d)
        __new__(cls: type, plane: Plane, surface: Surface, surfaceParam: Point2d, scale: float)
        __new__(cls: type, plane: Plane, surface: Surface, surfaceParam: Point2d, scale: float, angle: float)
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the space morph definition is valid, false otherwise.

Get: IsValid(self: SplopSpaceMorph) -> bool

"""



class SporphSpaceMorph(SpaceMorph, IDisposable):
    """
    Deforms an object from a source surface to a target surface.
    
    SporphSpaceMorph(surface0: Surface, surface1: Surface)
    SporphSpaceMorph(surface0: Surface, surface1: Surface, surface0Param: Point2d, surface1Param: Point2d)
    """
    def Dispose(self):
        """
        Dispose(self: SporphSpaceMorph)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: SporphSpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point.
        
            point: A point that will be morphed by this object.
            Returns: Resulting morphed point.
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
    def __new__(self, surface0, surface1, surface0Param=None, surface1Param=None):
        """
        __new__(cls: type, surface0: Surface, surface1: Surface)
        __new__(cls: type, surface0: Surface, surface1: Surface, surface0Param: Point2d, surface1Param: Point2d)
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the space morph definition is valid, false otherwise.

Get: IsValid(self: SporphSpaceMorph) -> bool

"""



class StretchSpaceMorph(SpaceMorph, IDisposable):
    """
    Deforms objects toward or away from a specified axis.
    
    StretchSpaceMorph(start: Point3d, end: Point3d, point: Point3d)
    StretchSpaceMorph(start: Point3d, end: Point3d, length: float)
    """
    def Dispose(self):
        """
        Dispose(self: StretchSpaceMorph)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: StretchSpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point.
        
            point: A point that will be morphed by this object.
            Returns: Resulting morphed point.
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
    def __new__(self, start, end, *__args):
        """
        __new__(cls: type, start: Point3d, end: Point3d, point: Point3d)
        __new__(cls: type, start: Point3d, end: Point3d, length: float)
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the space morph definition is valid, false otherwise.

Get: IsValid(self: StretchSpaceMorph) -> bool

"""



class TaperSpaceMorph(SpaceMorph, IDisposable):
    """
    Deforms objects toward or away from a specified axis.
    
    TaperSpaceMorph(start: Point3d, end: Point3d, startRadius: float, endRadius: float, bFlat: bool, infiniteTaper: bool)
    """
    def Dispose(self):
        """
        Dispose(self: TaperSpaceMorph)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: TaperSpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point.
        
            point: A point that will be morphed by this object.
            Returns: Resulting morphed point.
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
    def __new__(self, start, end, startRadius, endRadius, bFlat, infiniteTaper):
        """ __new__(cls: type, start: Point3d, end: Point3d, startRadius: float, endRadius: float, bFlat: bool, infiniteTaper: bool) """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the space morph definition is valid, false otherwise.

Get: IsValid(self: TaperSpaceMorph) -> bool

"""



class TwistSpaceMorph(SpaceMorph, IDisposable):
    """
    Deforms objects by rotating them around an axis.
    
    TwistSpaceMorph()
    """
    def Dispose(self):
        """
        Dispose(self: TwistSpaceMorph)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def MorphPoint(self, point):
        """
        MorphPoint(self: TwistSpaceMorph, point: Point3d) -> Point3d
        
            Morphs an Euclidean point. This method is abstract.
        
            point: A point that will be morphed by this function.
            Returns: Resulting morphed point.
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

    InfiniteTwist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If true, the deformation is constant throughout the object, even if the axis is shorter than the object. 
            If false, the deformation takes place only the length of the axis.

Get: InfiniteTwist(self: TwistSpaceMorph) -> bool

Set: InfiniteTwist(self: TwistSpaceMorph) = value
"""

    TwistAngleRadians = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Twist angle in radians.

Get: TwistAngleRadians(self: TwistSpaceMorph) -> float

Set: TwistAngleRadians(self: TwistSpaceMorph) = value
"""

    TwistAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Axis to rotate about.

Get: TwistAxis(self: TwistSpaceMorph) -> Line

Set: TwistAxis(self: TwistSpaceMorph) = value
"""



