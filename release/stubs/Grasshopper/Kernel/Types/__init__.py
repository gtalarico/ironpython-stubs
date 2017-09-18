# encoding: utf-8
# module Grasshopper.Kernel.Types calls itself Types
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Complex(object):
    """
    Complex(real_component: float)
    Complex(real_component: float, imaginary_component: float)
    """
    def ACos(self):
        """ ACos(self: Complex) -> Complex """
        pass

    def ASin(self):
        """ ASin(self: Complex) -> Complex """
        pass

    def ATan(self):
        """ ATan(self: Complex) -> Complex """
        pass

    def Cos(self):
        """ Cos(self: Complex) -> Complex """
        pass

    def Cosecant(self):
        """ Cosecant(self: Complex) -> Complex """
        pass

    def CoTan(self):
        """ CoTan(self: Complex) -> Complex """
        pass

    def Exponential(self):
        """ Exponential(self: Complex) -> Complex """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Complex) -> int """
        pass

    def Log(self):
        """ Log(self: Complex) -> Complex """
        pass

    def Log10(self):
        """ Log10(self: Complex) -> Complex """
        pass

    def Modulus(self):
        """ Modulus(self: Complex) -> float """
        pass

    def ModulusSquared(self):
        """ ModulusSquared(self: Complex) -> float """
        pass

    def Power(self, exponent):
        """ Power(self: Complex, exponent: Complex) -> Complex """
        pass

    def Root(self, rootexponent):
        """ Root(self: Complex, rootexponent: Complex) -> Complex """
        pass

    def Secant(self):
        """ Secant(self: Complex) -> Complex """
        pass

    def Sin(self):
        """ Sin(self: Complex) -> Complex """
        pass

    def Square(self):
        """ Square(self: Complex) -> Complex """
        pass

    def SquareRoot(self):
        """ SquareRoot(self: Complex) -> Complex """
        pass

    def Tan(self):
        """ Tan(self: Complex) -> Complex """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, real_component, imaginary_component=None):
        """
        __new__(cls: type, real_component: float)
        __new__(cls: type, real_component: float, imaginary_component: float)
        __new__[Complex]() -> Complex
        """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(summand: Complex) -> Complex """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(A: float, B: Complex) -> Complex
        __radd__(A: Complex, B: Complex) -> Complex
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(dividend: float, divisor: Complex) -> Complex
        __rdiv__(dividend: Complex, divisor: Complex) -> Complex
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(A: float, B: Complex) -> Complex
        __rmul__(A: Complex, B: Complex) -> Complex
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(A: float, B: Complex) -> Complex
        __rsub__(A: Complex, B: Complex) -> Complex
        """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    Argument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Argument(self: Complex) -> float

Set: Argument(self: Complex) = value
"""

    Imaginary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Imaginary(self: Complex) -> float

Set: Imaginary(self: Complex) = value
"""

    IsReal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReal(self: Complex) -> bool

"""

    IsRealNonNegative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRealNonNegative(self: Complex) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Complex) -> bool

"""

    IsZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsZero(self: Complex) -> bool

"""

    Real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Real(self: Complex) -> float

Set: Real(self: Complex) = value
"""


    ComplexUnit = None
    Infinity = None
    NaN = None
    NegativeInfinity = None
    Zero = None


class GH_Arc(GH_GeometricGoo[Arc], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_Arc()
    GH_Arc(arc: Arc)
    GH_Arc(other: GH_Arc)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Arc, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Arc, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Arc) -> (bool, T) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Arc, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Arc, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Arc) -> IGH_Goo """
        pass

    def DuplicateArc(self):
        """ DuplicateArc(self: GH_Arc) -> GH_Arc """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Arc) -> IGH_GeometricGoo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Arc) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Arc, xform: Transform) -> BoundingBox """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Arc, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Arc, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Arc) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Arc, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Arc, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, arc: Arc)
        __new__(cls: type, other: GH_Arc)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Arc) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Arc) -> BoundingBox

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Arc) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Arc) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Arc) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Arc) -> str

"""


    m_value = None


class GH_Boolean(GH_Goo[bool], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_Boolean()
    GH_Boolean(bool: bool)
    GH_Boolean(other: GH_Boolean)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Boolean, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Boolean) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Boolean) -> IGH_Goo """
        pass

    def DuplicateBoolean(self):
        """ DuplicateBoolean(self: GH_Boolean) -> GH_Boolean """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Boolean) -> IGH_GooProxy """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_Boolean) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_Boolean) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_Boolean, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_Boolean) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_Boolean, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_Boolean) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_Boolean) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_Boolean) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_Boolean) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_Boolean) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_Boolean) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_Boolean) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_Boolean) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_Boolean, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Boolean) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Boolean, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, bool: bool)
        __new__(cls: type, other: GH_Boolean)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Boolean) -> bool

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_Boolean) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Boolean) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Boolean) -> str

"""


    m_value = None


class GH_Box(GH_GeometricGoo[Box], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_Box()
    GH_Box(box: Box)
    GH_Box(box: BoundingBox)
    GH_Box(id: Guid)
    GH_Box(other: GH_Box)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Box, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def Brep(self):
        """ Brep(self: GH_Box) -> Brep """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Box, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Box) -> (bool, T) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_Box) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Box, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Box, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Box) -> IGH_Goo """
        pass

    def DuplicateBox(self):
        """ DuplicateBox(self: GH_Box) -> GH_Box """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Box) -> IGH_GeometricGoo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Box) -> IGH_GooProxy """
        pass

    def Geometry(self, brp, crv, pt):
        """ Geometry(self: GH_Box, brp: Brep, crv: Curve, pt: Point) -> (bool, Brep, Curve, Point) """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Box, xform: Transform) -> BoundingBox """
        pass

    def LoadGeometry(self, doc=None):
        """ LoadGeometry(self: GH_Box, doc: RhinoDoc) -> bool """
        pass

    def Mesh(self):
        """ Mesh(self: GH_Box) -> Mesh """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Box, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Box, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Box) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Box, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Box, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, box: Box)
        __new__(cls: type, box: BoundingBox)
        __new__(cls: type, id: Guid)
        __new__(cls: type, other: GH_Box)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Box) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Box) -> BoundingBox

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_Box) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Box) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Box) -> str

"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_Box) -> Guid

Set: ReferenceID(self: GH_Box) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Box) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Box) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_Box) -> Box

Set: Value(self: GH_Box) = value
"""


    GH_BoxProxy = None
    m_value = None


class GH_Brep(GH_GeometricGoo[Brep], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData):
    """
    GH_Brep()
    GH_Brep(brep: Brep)
    GH_Brep(id: Guid)
    GH_Brep(other: GH_Brep)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Brep, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    @staticmethod
    def BrepTightBoundingBox(in):
        """ BrepTightBoundingBox(in: Brep) -> BoundingBox """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Brep, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Brep) -> (bool, T) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_Brep) """
        pass

    def DestroyPreviewMeshes(self):
        """ DestroyPreviewMeshes(self: GH_Brep) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Brep, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Brep, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Brep) -> IGH_Goo """
        pass

    def DuplicateBrep(self):
        """ DuplicateBrep(self: GH_Brep) -> GH_Brep """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Brep) -> IGH_GeometricGoo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Brep) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Brep, xform: Transform) -> BoundingBox """
        pass

    def GetPreviewMeshes(self):
        """ GetPreviewMeshes(self: GH_Brep) -> Array[Mesh] """
        pass

    def LoadGeometry(self, doc=None):
        """ LoadGeometry(self: GH_Brep, doc: RhinoDoc) -> bool """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Brep, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Brep, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Brep) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Brep) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Brep, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Brep, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, brep: Brep)
        __new__(cls: type, id: Guid)
        __new__(cls: type, other: GH_Brep)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Brep) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Brep) -> BoundingBox

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_Brep) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Brep) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Brep) -> str

"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_Brep) -> Guid

Set: ReferenceID(self: GH_Brep) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Brep) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Brep) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_Brep) -> Brep

Set: Value(self: GH_Brep) = value
"""


    GH_BrepProxy = None
    m_value = None


class GH_Circle(GH_GeometricGoo[Circle], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_Circle()
    GH_Circle(circle: Circle)
    GH_Circle(other: GH_Circle)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Circle, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Circle, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Circle) -> (bool, T) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Circle, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Circle, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Circle) -> IGH_Goo """
        pass

    def DuplicateCircle(self):
        """ DuplicateCircle(self: GH_Circle) -> GH_Circle """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Circle) -> IGH_GeometricGoo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Circle) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Circle, xform: Transform) -> BoundingBox """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Circle, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Circle, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Circle) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Circle, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Circle, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, circle: Circle)
        __new__(cls: type, other: GH_Circle)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Circle) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Circle) -> BoundingBox

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Circle) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Circle) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Circle) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Circle) -> str

"""


    GH_CircleProxy = None
    m_value = None


class GH_Colour(GH_Goo[Color], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_Colour()
    GH_Colour(colour: Color)
    GH_Colour(other: GH_Colour)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Colour, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Colour) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Colour) -> IGH_Goo """
        pass

    def DuplicateColour(self):
        """ DuplicateColour(self: GH_Colour) -> GH_Colour """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Colour) -> IGH_GooProxy """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_Colour) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_Colour) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_Colour, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_Colour) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_Colour, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_Colour) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_Colour) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_Colour) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_Colour) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_Colour) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_Colour) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_Colour) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_Colour) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_Colour, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Colour) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Colour, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, colour: Color)
        __new__(cls: type, other: GH_Colour)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Colour) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Colour) -> str

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_Colour) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Colour) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Colour) -> str

"""


    m_value = None


class GH_ComplexNumber(GH_Goo[Complex], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_ComplexNumber()
    GH_ComplexNumber(number: Complex)
    GH_ComplexNumber(other: GH_ComplexNumber)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_ComplexNumber, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_ComplexNumber) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_ComplexNumber) -> IGH_Goo """
        pass

    def DuplicateComplex(self):
        """ DuplicateComplex(self: GH_ComplexNumber) -> GH_ComplexNumber """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_ComplexNumber) -> IGH_GooProxy """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_ComplexNumber) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_ComplexNumber) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_ComplexNumber, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_ComplexNumber) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_ComplexNumber, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_ComplexNumber) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_ComplexNumber) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_ComplexNumber) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_ComplexNumber) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_ComplexNumber) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_ComplexNumber) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_ComplexNumber) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_ComplexNumber) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_ComplexNumber, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_ComplexNumber) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_ComplexNumber, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, number: Complex)
        __new__(cls: type, other: GH_ComplexNumber)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_ComplexNumber) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_ComplexNumber) -> str

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_ComplexNumber) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_ComplexNumber) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_ComplexNumber) -> str

"""


    m_value = None


class GH_Culture(GH_Goo[CultureInfo], IGH_Goo, GH_ISerializable):
    """
    GH_Culture()
    GH_Culture(culture: CultureInfo)
    GH_Culture(other: GH_Culture)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Culture, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Culture) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Culture) -> IGH_Goo """
        pass

    def DuplicateCulture(self):
        """ DuplicateCulture(self: GH_Culture) -> GH_Culture """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Culture) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_Culture, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Culture) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Culture) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Culture, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, culture: CultureInfo)
        __new__(cls: type, other: GH_Culture)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Culture) -> bool

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Culture) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Culture) -> str

"""


    m_value = None


class GH_Curve(GH_GeometricGoo[Curve], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_Curve()
    GH_Curve(curve: Curve)
    GH_Curve(ref_guid: Guid)
    GH_Curve(ref_guid: Guid, ref_edge: int)
    GH_Curve(other: GH_Curve)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Curve, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Curve, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Curve) -> (bool, T) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_Curve) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Curve, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Curve, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Curve) -> IGH_Goo """
        pass

    def DuplicateCurve(self):
        """ DuplicateCurve(self: GH_Curve) -> GH_Curve """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Curve) -> IGH_GeometricGoo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Curve) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Curve, xform: Transform) -> BoundingBox """
        pass

    def LoadGeometry(self, doc=None):
        """ LoadGeometry(self: GH_Curve, doc: RhinoDoc) -> bool """
        pass

    def MakeDeformable(self):
        """ MakeDeformable(self: GH_Curve) -> bool """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Curve, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Curve, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Curve) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Curve) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Curve, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Curve, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, curve: Curve)
        __new__(cls: type, ref_guid: Guid)
        __new__(cls: type, ref_guid: Guid, ref_edge: int)
        __new__(cls: type, other: GH_Curve)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Curve) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Curve) -> BoundingBox

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_Curve) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Curve) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Curve) -> str

"""

    ReferenceEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceEdge(self: GH_Curve) -> int

Set: ReferenceEdge(self: GH_Curve) = value
"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_Curve) -> Guid

Set: ReferenceID(self: GH_Curve) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Curve) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Curve) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_Curve) -> Curve

Set: Value(self: GH_Curve) = value
"""


    GH_CurveProxy = None
    m_value = None


class GH_DifferentialSolver(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_DifferentialSolver, values: Euler (1), None (0), RungeKutta2 (2), RungeKutta3 (3), RungeKutta4 (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Euler = None
    None = None
    RungeKutta2 = None
    RungeKutta3 = None
    RungeKutta4 = None
    value__ = None


class GH_Field(object, IGH_Goo, GH_ISerializable, IGH_PreviewData):
    """
    GH_Field()
    GH_Field(other: GH_Field)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Field, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Field, target: T) -> (bool, T) """
        pass

    def CurvatureAt(self, location):
        """ CurvatureAt(self: GH_Field, location: Point3d) -> float """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Field, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Field, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Field) -> IGH_Goo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Field) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_Field, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Field) -> object """
        pass

    def SolveStep(self, location, factor, method):
        """ SolveStep(self: GH_Field, location: Point3d, factor: float, method: GH_DifferentialSolver) -> Vector3d """
        pass

    def SolveSteps(self, location, accuracy, count, method):
        """ SolveSteps(self: GH_Field, location: Point3d, accuracy: float, count: int, method: GH_DifferentialSolver) -> Point3dList """
        pass

    def TensorAt(self, location):
        """ TensorAt(self: GH_Field, location: Point3d) -> Vector3d """
        pass

    def ToString(self):
        """ ToString(self: GH_Field) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Field, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: GH_Field)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Field) -> BoundingBox

"""

    Elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elements(self: GH_Field) -> List[IGH_FieldElement]

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Field) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Field) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Field) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Field) -> str

"""



class GH_FieldElement(object, IGH_FieldElement, GH_ISerializable, IGH_PreviewData):
    # no doc
    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_FieldElement, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_FieldElement, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_FieldElement) -> IGH_FieldElement """
        pass

    def Force(self, location):
        """ Force(self: GH_FieldElement, location: Point3d) -> Vector3d """
        pass

    def IsCoincident(self, point, tolerance):
        """ IsCoincident(self: GH_FieldElement, point: Point3d, tolerance: float) -> bool """
        pass

    def Read(self, reader):
        """ Read(self: GH_FieldElement, reader: GH_IReader) -> bool """
        pass

    def Write(self, writer):
        """ Write(self: GH_FieldElement, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: GH_FieldElement) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_FieldElement) -> BoundingBox

"""

    ElementGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementGuid(self: GH_FieldElement) -> Guid

"""

    IsLimited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLimited(self: GH_FieldElement) -> bool

Set: IsLimited(self: GH_FieldElement) = value
"""

    Limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Limits(self: GH_FieldElement) -> Box

Set: Limits(self: GH_FieldElement) = value
"""



class GH_GeometricGoo(GH_Goo[T], IGH_Goo, GH_ISerializable, IGH_GeometricGoo):
    # no doc
    def CastFrom(self, source):
        """ CastFrom(self: GH_GeometricGoo[T], source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[Q](self: GH_GeometricGoo[T]) -> (bool, Q) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_GeometricGoo[T]) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_GeometricGoo[T]) -> IGH_Goo """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_GeometricGoo[T]) -> IGH_GeometricGoo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_GeometricGoo[T]) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_GeometricGoo[T], xform: Transform) -> BoundingBox """
        pass

    def LoadGeometry(self, doc=None):
        """
        LoadGeometry(self: GH_GeometricGoo[T], doc: RhinoDoc) -> bool
        LoadGeometry(self: GH_GeometricGoo[T]) -> bool
        """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_GeometricGoo[T], xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_GeometricGoo[T], xform: Transform) -> IGH_GeometricGoo """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, internal_data: T)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_GeometricGoo[T]) -> BoundingBox

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_GeometricGoo[T]) -> bool

"""

    IsReferencedGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferencedGeometry(self: GH_GeometricGoo[T]) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_GeometricGoo[T]) -> bool

"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_GeometricGoo[T]) -> Guid

Set: ReferenceID(self: GH_GeometricGoo[T]) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_GeometricGoo[T]) -> T

Set: Value(self: GH_GeometricGoo[T]) = value
"""


    m_value = None


class GH_GeometricGooWrapper(object, IGH_GeometricGoo, IGH_Goo, GH_ISerializable):
    """
    GH_GeometricGooWrapper()
    GH_GeometricGooWrapper(goo: IGH_GeometricGoo)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_GeometricGooWrapper, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_GeometricGooWrapper, target: T) -> (bool, T) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_GeometricGooWrapper) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_GeometricGooWrapper) -> IGH_Goo """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_GeometricGooWrapper) -> IGH_GeometricGoo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_GeometricGooWrapper) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_GeometricGooWrapper, xform: Transform) -> BoundingBox """
        pass

    def LoadGeometry(self, doc=None):
        """
        LoadGeometry(self: GH_GeometricGooWrapper, doc: RhinoDoc) -> bool
        LoadGeometry(self: GH_GeometricGooWrapper) -> bool
        """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_GeometricGooWrapper, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_GeometricGooWrapper, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_GeometricGooWrapper) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_GeometricGooWrapper) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_GeometricGooWrapper, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_GeometricGooWrapper, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, goo=None):
        """
        __new__(cls: type)
        __new__(cls: type, goo: IGH_GeometricGoo)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_GeometricGooWrapper) -> BoundingBox

"""

    InternalGoo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalGoo(self: GH_GeometricGooWrapper) -> IGH_GeometricGoo

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_GeometricGooWrapper) -> bool

"""

    IsReferencedGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferencedGeometry(self: GH_GeometricGooWrapper) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_GeometricGooWrapper) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_GeometricGooWrapper) -> str

"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_GeometricGooWrapper) -> Guid

Set: ReferenceID(self: GH_GeometricGooWrapper) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_GeometricGooWrapper) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_GeometricGooWrapper) -> str

"""



class GH_GeometryGroup(object, IGH_GeometricGoo, IGH_Goo, GH_ISerializable, IGH_BakeAwareData, IGH_PreviewData):
    """ GH_GeometryGroup() """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_GeometryGroup, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_GeometryGroup, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_GeometryGroup, target: T) -> (bool, T) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_GeometryGroup) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_GeometryGroup, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_GeometryGroup, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_GeometryGroup) -> IGH_Goo """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_GeometryGroup) -> IGH_GeometricGoo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_GeometryGroup) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_GeometryGroup, xform: Transform) -> BoundingBox """
        pass

    def LoadGeometry(self, doc=None):
        """
        LoadGeometry(self: GH_GeometryGroup, doc: RhinoDoc) -> bool
        LoadGeometry(self: GH_GeometryGroup) -> bool
        """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_GeometryGroup, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_GeometryGroup, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_GeometryGroup) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_GeometryGroup) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_GeometryGroup, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_GeometryGroup, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_GeometryGroup) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_GeometryGroup) -> BoundingBox

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_GeometryGroup) -> bool

"""

    IsReferencedGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferencedGeometry(self: GH_GeometryGroup) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_GeometryGroup) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_GeometryGroup) -> str

"""

    Objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Objects(self: GH_GeometryGroup) -> List[IGH_GeometricGoo]

"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_GeometryGroup) -> Guid

Set: ReferenceID(self: GH_GeometryGroup) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_GeometryGroup) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_GeometryGroup) -> str

"""


    GH_GeometryGroupProxy = None


class GH_Goo(object, IGH_Goo, GH_ISerializable):
    # no doc
    def CastFrom(self, source):
        """ CastFrom(self: GH_Goo[T], source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[Q](self: GH_Goo[T], target: Q) -> (bool, Q) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Goo[T]) -> IGH_Goo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Goo[T]) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_Goo[T], reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Goo[T]) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Goo[T]) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Goo[T], writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, internal_data: T)
        __new__(cls: type, other: GH_Goo[T])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Goo[T]) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Goo[T]) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Goo[T]) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Goo[T]) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_Goo[T]) -> T

Set: Value(self: GH_Goo[T]) = value
"""


    m_value = None


class GH_GooProxy(object, IGH_GooProxy):
    # no doc
    def Construct(self):
        """ Construct(self: GH_GooProxy[T]) """
        pass

    def FormatInstance(self):
        """ FormatInstance(self: GH_GooProxy[T]) -> str """
        pass

    def FromString(self, in):
        """ FromString(self: GH_GooProxy[T], in: str) -> bool """
        pass

    def MutateString(self, in):
        """ MutateString(self: GH_GooProxy[T], in: str) -> str """
        pass

    def NumberToString(self, *args): #cannot find CLR method
        """ NumberToString(self: GH_GooProxy[T], number: float) -> str """
        pass

    def StringToNumber(self, *args): #cannot find CLR method
        """ StringToNumber(self: GH_GooProxy[T], text: str) -> float """
        pass

    def ToString(self):
        """ ToString(self: GH_GooProxy[T]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, owner: T) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsParsable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsParsable(self: GH_GooProxy[T]) -> bool

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProxyOwner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProxyOwner(self: GH_GooProxy[T]) -> IGH_Goo

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_GooProxy[T]) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_GooProxy[T]) -> str

"""

    UserString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserString(self: GH_GooProxy[T]) -> str

Set: UserString(self: GH_GooProxy[T]) = value
"""

    Valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valid(self: GH_GooProxy[T]) -> bool

"""



class GH_Guid(GH_Goo[Guid], IGH_Goo, GH_ISerializable):
    """
    GH_Guid()
    GH_Guid(id: Guid)
    GH_Guid(other: GH_Guid)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Guid, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Guid) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Guid) -> IGH_Goo """
        pass

    def DuplicateGuid(self):
        """ DuplicateGuid(self: GH_Guid) -> GH_Guid """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Guid) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_Guid, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Guid) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Guid, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, id: Guid)
        __new__(cls: type, other: GH_Guid)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Guid) -> bool

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Guid) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Guid) -> str

"""


    m_value = None


class GH_Integer(GH_Goo[int], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_Integer()
    GH_Integer(number: int)
    GH_Integer(other: GH_Integer)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Integer, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Integer) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Integer) -> IGH_Goo """
        pass

    def DuplicateInteger(self):
        """ DuplicateInteger(self: GH_Integer) -> GH_Integer """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Integer) -> IGH_GooProxy """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_Integer) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_Integer) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_Integer, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_Integer) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_Integer, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_Integer) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_Integer) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_Integer) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_Integer) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_Integer) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_Integer) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_Integer) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_Integer) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_Integer, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Integer) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Integer, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, number: int)
        __new__(cls: type, other: GH_Integer)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Integer) -> bool

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_Integer) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Integer) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Integer) -> str

"""


    m_value = None


class GH_Interval(GH_Goo[Interval], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_Interval()
    GH_Interval(interval: Interval)
    GH_Interval(other: GH_Interval)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Interval, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Interval) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Interval) -> IGH_Goo """
        pass

    def DuplicateInterval(self):
        """ DuplicateInterval(self: GH_Interval) -> GH_Interval """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Interval) -> IGH_GooProxy """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_Interval) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_Interval) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_Interval, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_Interval) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_Interval, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_Interval) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_Interval) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_Interval) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_Interval) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_Interval) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_Interval) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_Interval) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_Interval) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_Interval, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Interval) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Interval, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, interval: Interval)
        __new__(cls: type, other: GH_Interval)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Interval) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Interval) -> str

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_Interval) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Interval) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Interval) -> str

"""


    m_value = None


class GH_Interval2D(GH_Goo[UVInterval], IGH_Goo, GH_ISerializable):
    """
    GH_Interval2D()
    GH_Interval2D(uv: UVInterval)
    GH_Interval2D(other: GH_Interval2D)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Interval2D, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Interval2D, target: T) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Interval2D) -> IGH_Goo """
        pass

    def DuplicateInterval(self):
        """ DuplicateInterval(self: GH_Interval2D) -> GH_Interval2D """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Interval2D) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_Interval2D, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Interval2D) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Interval2D, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, uv: UVInterval)
        __new__(cls: type, other: GH_Interval2D)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Interval2D) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Interval2D) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Interval2D) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Interval2D) -> str

"""


    GH_Interval2DProxy = None
    m_value = None


class GH_Line(GH_GeometricGoo[Line], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_Line()
    GH_Line(line: Line)
    GH_Line(other: GH_Line)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Line, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Line, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Line) -> (bool, T) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Line, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Line, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Line) -> IGH_Goo """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Line) -> IGH_GeometricGoo """
        pass

    def DuplicateLine(self):
        """ DuplicateLine(self: GH_Line) -> GH_Line """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Line) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Line, xform: Transform) -> BoundingBox """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Line, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Line, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Line) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Line, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Line, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, line: Line)
        __new__(cls: type, other: GH_Line)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Line) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Line) -> BoundingBox

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Line) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Line) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Line) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Line) -> str

"""


    GH_LineProxy = None
    m_value = None


class GH_LineCharge(GH_FieldElement, IGH_FieldElement, GH_ISerializable, IGH_PreviewData):
    """ GH_LineCharge() """
    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_LineCharge, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_LineCharge) -> IGH_FieldElement """
        pass

    def Force(self, location):
        """ Force(self: GH_LineCharge, location: Point3d) -> Vector3d """
        pass

    def IsCoincident(self, point, tolerance):
        """ IsCoincident(self: GH_LineCharge, point: Point3d, tolerance: float) -> bool """
        pass

    def Read(self, reader):
        """ Read(self: GH_LineCharge, reader: GH_IReader) -> bool """
        pass

    def Write(self, writer):
        """ Write(self: GH_LineCharge, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: GH_LineCharge) -> BoundingBox

"""

    Charge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Charge(self: GH_LineCharge) -> float

Set: Charge(self: GH_LineCharge) = value
"""

    ElementGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementGuid(self: GH_LineCharge) -> Guid

"""

    Segment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segment(self: GH_LineCharge) -> Line

Set: Segment(self: GH_LineCharge) = value
"""



class GH_LonLatCoordinate(object, IGH_Goo, GH_ISerializable):
    """
    GH_LonLatCoordinate()
    GH_LonLatCoordinate(longitude: float, latitude: float)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_LonLatCoordinate, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_LonLatCoordinate, target: T) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_LonLatCoordinate) -> IGH_Goo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_LonLatCoordinate) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_LonLatCoordinate, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_LonLatCoordinate) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_LonLatCoordinate) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_LonLatCoordinate, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, longitude=None, latitude=None):
        """
        __new__(cls: type)
        __new__(cls: type, longitude: float, latitude: float)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_LonLatCoordinate) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_LonLatCoordinate) -> str

"""

    Latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Latitude(self: GH_LonLatCoordinate) -> float

Set: Latitude(self: GH_LonLatCoordinate) = value
"""

    Longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Longitude(self: GH_LonLatCoordinate) -> float

Set: Longitude(self: GH_LonLatCoordinate) = value
"""

    SphereUParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SphereUParameter(self: GH_LonLatCoordinate) -> float

"""

    SphereVParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SphereVParameter(self: GH_LonLatCoordinate) -> float

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_LonLatCoordinate) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_LonLatCoordinate) -> str

"""



class GH_Material(GH_Goo[DisplayMaterial], IGH_Goo, GH_ISerializable):
    """
    GH_Material()
    GH_Material(rdk_id: Guid)
    GH_Material(diffuse: Color)
    GH_Material(other: DisplayMaterial)
    GH_Material(other: GH_Material)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Material, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Material, target: T) -> (bool, T) """
        pass

    @staticmethod
    def CreateStandardMaterial(colour):
        """ CreateStandardMaterial(colour: Color) -> DisplayMaterial """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Material) -> IGH_Goo """
        pass

    def DuplicateMaterial(self):
        """ DuplicateMaterial(self: GH_Material) -> GH_Material """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Material) -> IGH_GooProxy """
        pass

    @staticmethod
    def GetModuleHandle(lpModuleName):
        """ GetModuleHandle(lpModuleName: str) -> (IntPtr, str) """
        pass

    @staticmethod
    def RDK_GetMaterial():
        """ RDK_GetMaterial() -> Guid """
        pass

    @staticmethod
    def RDK_GetMaterialSimulation(id, on_material_ptr):
        """ RDK_GetMaterialSimulation(id: Guid, on_material_ptr: IntPtr) -> bool """
        pass

    def Read(self, reader):
        """ Read(self: GH_Material, reader: GH_IReader) -> bool """
        pass

    def RefreshReferenceData(self):
        """ RefreshReferenceData(self: GH_Material) -> RDK_GL_Result """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Material) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Material) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Material, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, rdk_id: Guid)
        __new__(cls: type, diffuse: Color)
        __new__(cls: type, other: DisplayMaterial)
        __new__(cls: type, other: GH_Material)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsReferencedShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferencedShader(self: GH_Material) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Material) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Material) -> str

"""

    RDK_ID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RDK_ID(self: GH_Material) -> Guid

Set: RDK_ID(self: GH_Material) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Material) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Material) -> str

"""


    GH_Material_Proxy = None
    m_rdk_id = None
    m_value = None
    RDK_GL_Result = None


class GH_Matrix(GH_Goo[Matrix], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_Matrix()
    GH_Matrix(matrix: Matrix)
    GH_Matrix(other: GH_Matrix)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Matrix, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Matrix) -> (bool, T) """
        pass

    @staticmethod
    def CloneMatrix(matrix):
        """ CloneMatrix(matrix: Matrix) -> Matrix """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Matrix) -> IGH_Goo """
        pass

    def DuplicateMatrix(self):
        """ DuplicateMatrix(self: GH_Matrix) -> GH_Matrix """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_Matrix) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_Matrix) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_Matrix, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_Matrix) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_Matrix, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_Matrix) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_Matrix) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_Matrix) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_Matrix) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_Matrix) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_Matrix) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_Matrix) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_Matrix) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_Matrix, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Matrix) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Matrix) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Matrix, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, matrix: Matrix)
        __new__(cls: type, other: GH_Matrix)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Matrix) -> bool

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_Matrix) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Matrix) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Matrix) -> str

"""


    m_value = None


class GH_Mesh(GH_GeometricGoo[Mesh], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_Mesh()
    GH_Mesh(mesh: Mesh)
    GH_Mesh(id: Guid)
    GH_Mesh(other: GH_Mesh)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Mesh, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Mesh, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Mesh) -> (bool, T) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_Mesh) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Mesh, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Mesh, args: GH_PreviewWireArgs) """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Mesh) -> IGH_GeometricGoo """
        pass

    def DuplicateMesh(self):
        """ DuplicateMesh(self: GH_Mesh) -> GH_Mesh """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Mesh) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Mesh, xform: Transform) -> BoundingBox """
        pass

    def LoadGeometry(self, doc=None):
        """ LoadGeometry(self: GH_Mesh, doc: RhinoDoc) -> bool """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Mesh, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Mesh, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Mesh) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Mesh) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Mesh, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Mesh, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, mesh: Mesh)
        __new__(cls: type, id: Guid)
        __new__(cls: type, other: GH_Mesh)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Mesh) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Mesh) -> BoundingBox

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_Mesh) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Mesh) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Mesh) -> str

"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_Mesh) -> Guid

Set: ReferenceID(self: GH_Mesh) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Mesh) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Mesh) -> str

"""


    GH_MeshProxy = None
    m_value = None


class GH_MeshFace(GH_Goo[MeshFace], IGH_Goo, GH_ISerializable):
    """
    GH_MeshFace()
    GH_MeshFace(nA: int, nB: int, nC: int)
    GH_MeshFace(nA: int, nB: int, nC: int, nD: int)
    GH_MeshFace(other: MeshFace)
    GH_MeshFace(other: GH_MeshFace)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_MeshFace, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_MeshFace, target: T) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_MeshFace) -> IGH_Goo """
        pass

    def DuplicateMeshFace(self):
        """ DuplicateMeshFace(self: GH_MeshFace) -> GH_MeshFace """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_MeshFace) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_MeshFace, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_MeshFace) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_MeshFace, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, nA: int, nB: int, nC: int)
        __new__(cls: type, nA: int, nB: int, nC: int, nD: int)
        __new__(cls: type, other: MeshFace)
        __new__(cls: type, other: GH_MeshFace)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_MeshFace) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_MeshFace) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_MeshFace) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_MeshFace) -> str

"""


    GH_MeshFaceProxy = None
    m_value = None


class GH_MeshingParameters(GH_Goo[MeshingParameters], IGH_Goo, GH_ISerializable):
    """
    GH_MeshingParameters()
    GH_MeshingParameters(other: MeshingParameters)
    """
    def Duplicate(self):
        """ Duplicate(self: GH_MeshingParameters) -> IGH_Goo """
        pass

    def DuplicateMesherSettings(self):
        """ DuplicateMesherSettings(self: GH_MeshingParameters) -> GH_MeshingParameters """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_MeshingParameters) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_MeshingParameters, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_MeshingParameters) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_MeshingParameters, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, other=None):
        """
        __new__(cls: type)
        __new__(cls: type, other: MeshingParameters)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_MeshingParameters) -> bool

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_MeshingParameters) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_MeshingParameters) -> str

"""


    m_value = None
    RhMesherSettings_Proxy = None


class GH_Number(GH_Goo[float], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_Number()
    GH_Number(number: float)
    GH_Number(other: GH_Number)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Number, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Number) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Number) -> IGH_Goo """
        pass

    def DuplicateNumber(self):
        """ DuplicateNumber(self: GH_Number) -> GH_Number """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Number) -> IGH_GooProxy """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_Number) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_Number) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_Number, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_Number) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_Number, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_Number) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_Number) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_Number) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_Number) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_Number) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_Number) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_Number) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_Number) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_Number, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Number) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Number, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, number: float)
        __new__(cls: type, other: GH_Number)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Number) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Number) -> str

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_Number) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Number) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Number) -> str

"""


    m_value = None


class GH_ObjectWrapper(GH_Goo[object], IGH_Goo, GH_ISerializable, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_ObjectWrapper()
    GH_ObjectWrapper(obj: object)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_ObjectWrapper, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_ObjectWrapper, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_ObjectWrapper) -> (bool, T) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_ObjectWrapper, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_ObjectWrapper, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_ObjectWrapper) -> IGH_Goo """
        pass

    def DuplicateObject(self):
        """ DuplicateObject(self: GH_ObjectWrapper) -> GH_ObjectWrapper """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_ObjectWrapper) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_ObjectWrapper, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_ObjectWrapper) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_ObjectWrapper) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj=None):
        """
        __new__(cls: type)
        __new__(cls: type, obj: object)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_ObjectWrapper) -> BoundingBox

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_ObjectWrapper) -> bool

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_ObjectWrapper) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_ObjectWrapper) -> str

"""


    m_value = None


class GH_Plane(GH_GeometricGoo[Plane], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_Plane()
    GH_Plane(plane: Plane)
    GH_Plane(other: GH_Plane)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Plane, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Plane, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Plane) -> (bool, T) """
        pass

    @staticmethod
    def DrawPlane(display, plane, size=None, frequency=None, grid_color=None, x_color=None, y_color=None, back_color=None):
        """ DrawPlane(display: DisplayPipeline, plane: Plane, size: float, frequency: int, grid_color: Color, x_color: Color, y_color: Color)DrawPlane(display: DisplayPipeline, plane: Plane, size: float, frequency: int, grid_color: Color, x_color: Color, y_color: Color, back_color: Color)DrawPlane(display: DisplayPipeline, plane: Plane)DrawPlane(display: DisplayPipeline, plane: Plane, size: float, frequency: int) """
        pass

    @staticmethod
    def DrawPlaneIcon(display, plane, size, edgeColour, fillColour):
        """ DrawPlaneIcon(display: DisplayPipeline, plane: Plane, size: float, edgeColour: Color, fillColour: Color) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Plane, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Plane, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Plane) -> IGH_Goo """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Plane) -> IGH_GeometricGoo """
        pass

    def DuplicatePlane(self):
        """ DuplicatePlane(self: GH_Plane) -> GH_Plane """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Plane) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Plane, xform: Transform) -> BoundingBox """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Plane, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Plane, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Plane) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Plane, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Plane, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, plane: Plane)
        __new__(cls: type, other: GH_Plane)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Plane) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Plane) -> BoundingBox

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Plane) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Plane) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Plane) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Plane) -> str

"""


    GH_PlaneProxy = None
    m_value = None


class GH_Point(object, IGH_GeometricGoo, IGH_Goo, GH_ISerializable, IGH_BakeAwareData, IGH_PreviewData, IGH_QuickCast):
    """
    GH_Point()
    GH_Point(pt: Point3d)
    GH_Point(iOther: GH_Point)
    GH_Point(rh_obj_id: Guid)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Point, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Point, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Point) -> (bool, T) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_Point) """
        pass

    def CreateFromCoordinate(self, pt):
        """ CreateFromCoordinate(self: GH_Point, pt: Point3d) """
        pass

    def CreateFromCurveDistance(self, crv_id, crv, t, bFromStart):
        """ CreateFromCurveDistance(self: GH_Point, crv_id: Guid, crv: Curve, t: float, bFromStart: bool) """
        pass

    def CreateFromCurveRatio(self, crv_id, crv, t):
        """ CreateFromCurveRatio(self: GH_Point, crv_id: Guid, crv: Curve, t: float) """
        pass

    def CreateFromEdgeDistance(self, brp_id, edge, e_index, t, bFromStart):
        """ CreateFromEdgeDistance(self: GH_Point, brp_id: Guid, edge: Curve, e_index: int, t: float, bFromStart: bool) """
        pass

    def CreateFromEdgeRatio(self, brp_id, edge, e_index, t):
        """ CreateFromEdgeRatio(self: GH_Point, brp_id: Guid, edge: Curve, e_index: int, t: float) """
        pass

    def CreateFromPointObject(self, id):
        """ CreateFromPointObject(self: GH_Point, id: Guid) """
        pass

    def CreateFromSurfaceParam(self, brp_id, f_index, srf, u, v):
        """ CreateFromSurfaceParam(self: GH_Point, brp_id: Guid, f_index: int, srf: Surface, u: float, v: float) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Point, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Point, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Point) -> IGH_Goo """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Point) -> IGH_GeometricGoo """
        pass

    def DuplicatePoint(self):
        """ DuplicatePoint(self: GH_Point) -> GH_Point """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Point) -> IGH_GooProxy """
        pass

    def EnsureReferenceData(self):
        """ EnsureReferenceData(self: GH_Point) """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Point, xform: Transform) -> BoundingBox """
        pass

    def LoadGeometry(self, doc=None):
        """
        LoadGeometry(self: GH_Point, doc: RhinoDoc) -> bool
        LoadGeometry(self: GH_Point) -> bool
        """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Point, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_Point) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_Point) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_Point, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_Point) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_Point, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_Point) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_Point) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_Point) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_Point) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_Point) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_Point) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_Point) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_Point) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_Point, reader: GH_IReader) -> bool """
        pass

    def ReferenceCurve(self, ref=None):
        """
        ReferenceCurve(self: GH_Point, ref: RhinoObject) -> Curve
        ReferenceCurve(self: GH_Point) -> Curve
        """
        pass

    def ReferenceIndex(self, new_index=None):
        """ ReferenceIndex(self: GH_Point, new_index: int)ReferenceIndex(self: GH_Point) -> int """
        pass

    def ReferenceParam(self, index, new_param=None):
        """ ReferenceParam(self: GH_Point, index: int, new_param: float)ReferenceParam(self: GH_Point, index: int) -> float """
        pass

    def ReferencesCurve(self):
        """ ReferencesCurve(self: GH_Point) -> bool """
        pass

    def ReferencesEdge(self):
        """ ReferencesEdge(self: GH_Point) -> bool """
        pass

    def ReferenceSurface(self):
        """ ReferenceSurface(self: GH_Point) -> BrepFace """
        pass

    def ReferenceType(self, new_type=None):
        """ ReferenceType(self: GH_Point, new_type: GH_PointRefType)ReferenceType(self: GH_Point) -> GH_PointRefType """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Point) -> object """
        pass

    def SetReferenceParams(self, u, v):
        """ SetReferenceParams(self: GH_Point, u: float, v: float) """
        pass

    def ShowReferenceDialog(self, owner=None):
        """
        ShowReferenceDialog(self: GH_Point, owner: IWin32Window) -> DialogResult
        ShowReferenceDialog(self: GH_Point) -> DialogResult
        """
        pass

    def ToString(self):
        """ ToString(self: GH_Point) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Point, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Point, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, pt: Point3d)
        __new__(cls: type, iOther: GH_Point)
        __new__(cls: type, rh_obj_id: Guid)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Point) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Point) -> BoundingBox

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_Point) -> bool

"""

    IsReferencedGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferencedGeometry(self: GH_Point) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Point) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Point) -> str

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_Point) -> GH_QuickCastType

"""

    ReferenceData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceData(self: GH_Point) -> GH_PointRefData

Set: ReferenceData(self: GH_Point) = value
"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_Point) -> Guid

Set: ReferenceID(self: GH_Point) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Point) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Point) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_Point) -> Point3d

Set: Value(self: GH_Point) = value
"""


    GH_PointProxy = None


class GH_PointCharge(GH_FieldElement, IGH_FieldElement, GH_ISerializable, IGH_PreviewData):
    """ GH_PointCharge() """
    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_PointCharge, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_PointCharge) -> IGH_FieldElement """
        pass

    def Force(self, location):
        """ Force(self: GH_PointCharge, location: Point3d) -> Vector3d """
        pass

    def IsCoincident(self, point, tolerance):
        """ IsCoincident(self: GH_PointCharge, point: Point3d, tolerance: float) -> bool """
        pass

    def Read(self, reader):
        """ Read(self: GH_PointCharge, reader: GH_IReader) -> bool """
        pass

    def Write(self, writer):
        """ Write(self: GH_PointCharge, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: GH_PointCharge) -> BoundingBox

"""

    Charge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Charge(self: GH_PointCharge) -> float

Set: Charge(self: GH_PointCharge) = value
"""

    Decay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Decay(self: GH_PointCharge) -> float

Set: Decay(self: GH_PointCharge) = value
"""

    ElementGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementGuid(self: GH_PointCharge) -> Guid

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: GH_PointCharge) -> Point3d

Set: Location(self: GH_PointCharge) = value
"""



class GH_PointRefData(object):
    """
    GH_PointRefData()
    GH_PointRefData(iOther: GH_PointRefData)
    """
    def EvCurve(self, c):
        """ EvCurve(self: GH_PointRefData, c: Curve) -> Point3d """
        pass

    def EvCurveParam(self, c):
        """ EvCurveParam(self: GH_PointRefData, c: Curve) -> float """
        pass

    def EvSurface(self, s):
        """ EvSurface(self: GH_PointRefData, s: Surface) -> Point3d """
        pass

    def SetCurveDistFromEndParam(self, *args): #cannot find CLR method
        """ SetCurveDistFromEndParam(self: GH_PointRefData, c: Curve, t: float) -> bool """
        pass

    def SetCurveDistFromStartParam(self, *args): #cannot find CLR method
        """ SetCurveDistFromStartParam(self: GH_PointRefData, c: Curve, t: float) -> bool """
        pass

    def SetCurveParam(self, c, t):
        """ SetCurveParam(self: GH_PointRefData, c: Curve, t: float) -> bool """
        pass

    def SetCurveRatioParam(self, *args): #cannot find CLR method
        """ SetCurveRatioParam(self: GH_PointRefData, c: Curve, t: float) -> bool """
        pass

    def SetSurfaceParam(self, srf, u, v):
        """ SetSurfaceParam(self: GH_PointRefData, srf: Surface, u: float, v: float) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, iOther=None):
        """
        __new__(cls: type)
        __new__(cls: type, iOther: GH_PointRefData)
        """
        pass

    m_RefID = None
    m_RefIndex = None
    m_RefParam = None
    m_RefType = None


class GH_PointRefType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_PointRefType, values: coordinate (1), curve_dist_end (12), curve_dist_start (11), curve_ratio (10), point_object (2), srf_param (20) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    coordinate = None
    curve_dist_end = None
    curve_dist_start = None
    curve_ratio = None
    point_object = None
    srf_param = None
    value__ = None


class GH_PointUtil(object):
    # no doc
    @staticmethod
    def FitPlaneThroughPoints(pts):
        """ FitPlaneThroughPoints(pts: IEnumerable[GH_Point]) -> Plane """
        pass

    @staticmethod
    def ProjectPointsToPlane(pts, plane, include_nulls):
        """ ProjectPointsToPlane(pts: IEnumerable[GH_Point], plane: Plane, include_nulls: bool) -> List[GH_Point] """
        pass

    @staticmethod
    def PullPointsToPlane(pts, plane, include_nulls):
        """ PullPointsToPlane(pts: IEnumerable[GH_Point], plane: Plane, include_nulls: bool) -> List[GH_Point] """
        pass

    @staticmethod
    def RemapPointsToPlane(pts, plane, include_nulls):
        """ RemapPointsToPlane(pts: IEnumerable[GH_Point], plane: Plane, include_nulls: bool) -> List[GH_Point] """
        pass


class GH_QuickCastType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_QuickCastType, values: bool (0), col (4), complex (7), int (1), interval (8), matrix (9), num (2), pt (5), text (3), vec (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    bool = None
    col = None
    complex = None
    int = None
    interval = None
    matrix = None
    num = None
    pt = None
    text = None
    value__ = None
    vec = None


class GH_Rectangle(GH_GeometricGoo[Rectangle3d], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData):
    """
    GH_Rectangle()
    GH_Rectangle(rec: Rectangle3d)
    GH_Rectangle(other: GH_Rectangle)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Rectangle, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Rectangle, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Rectangle) -> (bool, T) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Rectangle, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Rectangle, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Rectangle) -> IGH_Goo """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Rectangle) -> IGH_GeometricGoo """
        pass

    def DuplicateRectangle(self):
        """ DuplicateRectangle(self: GH_Rectangle) -> GH_Rectangle """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Rectangle) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Rectangle, xform: Transform) -> BoundingBox """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Rectangle, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Rectangle, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Rectangle) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Rectangle, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Write(self, writer):
        """ Write(self: GH_Rectangle, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, rec: Rectangle3d)
        __new__(cls: type, other: GH_Rectangle)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Rectangle) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Rectangle) -> BoundingBox

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Rectangle) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Rectangle) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Rectangle) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Rectangle) -> str

"""


    GH_RectangleProxy = None
    m_value = None


class GH_SpinForce(GH_FieldElement, IGH_FieldElement, GH_ISerializable, IGH_PreviewData):
    """ GH_SpinForce() """
    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_SpinForce, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_SpinForce) -> IGH_FieldElement """
        pass

    def Force(self, location):
        """ Force(self: GH_SpinForce, location: Point3d) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_SpinForce, reader: GH_IReader) -> bool """
        pass

    def Write(self, writer):
        """ Write(self: GH_SpinForce, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: GH_SpinForce) -> BoundingBox

"""

    Decay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Decay(self: GH_SpinForce) -> float

Set: Decay(self: GH_SpinForce) = value
"""

    ElementGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementGuid(self: GH_SpinForce) -> Guid

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: GH_SpinForce) -> Plane

Set: Plane(self: GH_SpinForce) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: GH_SpinForce) -> float

Set: Radius(self: GH_SpinForce) = value
"""

    Strength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Strength(self: GH_SpinForce) -> float

Set: Strength(self: GH_SpinForce) = value
"""



class GH_String(GH_Goo[str], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_String()
    GH_String(str: str)
    GH_String(other: GH_String)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_String, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_String) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_String) -> IGH_Goo """
        pass

    def DuplicateString(self):
        """ DuplicateString(self: GH_String) -> GH_String """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_String) -> IGH_GooProxy """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_String) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_String) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_String, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_String) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_String, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_String) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_String) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_String) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_String) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_String) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_String) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_String) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_String) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_String, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_String) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_String, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, str: str)
        __new__(cls: type, other: GH_String)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_String) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_String) -> str

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_String) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_String) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_String) -> str

"""


    m_value = None


class GH_StructurePath(GH_Goo[GH_Path], IGH_Goo, GH_ISerializable):
    """
    GH_StructurePath()
    GH_StructurePath(path: GH_Path)
    GH_StructurePath(other: GH_StructurePath)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_StructurePath, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_StructurePath) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_StructurePath) -> IGH_Goo """
        pass

    def DuplicatePath(self):
        """ DuplicatePath(self: GH_StructurePath) -> GH_StructurePath """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_StructurePath) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_StructurePath, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_StructurePath) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_StructurePath) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_StructurePath, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, path: GH_Path)
        __new__(cls: type, other: GH_StructurePath)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_StructurePath) -> bool

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_StructurePath) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_StructurePath) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_StructurePath) -> GH_Path

Set: Value(self: GH_StructurePath) = value
"""


    m_value = None


class GH_Surface(GH_GeometricGoo[Brep], IGH_Goo, GH_ISerializable, IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData):
    """
    GH_Surface()
    GH_Surface(srf: Surface)
    GH_Surface(brep: Brep)
    GH_Surface(id: Guid)
    GH_Surface(other: GH_Surface)
    """
    def BakeGeometry(self, doc, att, obj_guid):
        """ BakeGeometry(self: GH_Surface, doc: RhinoDoc, att: ObjectAttributes, obj_guid: Guid) -> (bool, Guid) """
        pass

    def CastFrom(self, source):
        """ CastFrom(self: GH_Surface, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Surface) -> (bool, T) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_Surface) """
        pass

    def DestroyPreviewMeshes(self):
        """ DestroyPreviewMeshes(self: GH_Surface) """
        pass

    def DrawViewportMeshes(self, args):
        """ DrawViewportMeshes(self: GH_Surface, args: GH_PreviewMeshArgs) """
        pass

    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_Surface, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Surface) -> IGH_Goo """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: GH_Surface) -> IGH_GeometricGoo """
        pass

    def DuplicateSurface(self):
        """ DuplicateSurface(self: GH_Surface) -> GH_Surface """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Surface) -> IGH_GooProxy """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: GH_Surface, xform: Transform) -> BoundingBox """
        pass

    def GetPreviewMeshes(self):
        """ GetPreviewMeshes(self: GH_Surface) -> Array[Mesh] """
        pass

    def IsPointOnDomain(self, u, v):
        """ IsPointOnDomain(self: GH_Surface, u: float, v: float) -> bool """
        pass

    def IsPointOnFace(self, u, v):
        """ IsPointOnFace(self: GH_Surface, u: float, v: float) -> bool """
        pass

    def LoadGeometry(self, doc=None):
        """ LoadGeometry(self: GH_Surface, doc: RhinoDoc) -> bool """
        pass

    def Morph(self, xmorph):
        """ Morph(self: GH_Surface, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Read(self, reader):
        """ Read(self: GH_Surface, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Surface) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Surface) -> str """
        pass

    def Transform(self, xform):
        """ Transform(self: GH_Surface, xform: Transform) -> IGH_GeometricGoo """
        pass

    def Untrim(self):
        """ Untrim(self: GH_Surface) -> bool """
        pass

    def Write(self, writer):
        """ Write(self: GH_Surface, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, srf: Surface)
        __new__(cls: type, brep: Brep)
        __new__(cls: type, id: Guid)
        __new__(cls: type, other: GH_Surface)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: GH_Surface) -> BoundingBox

"""

    ClippingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingBox(self: GH_Surface) -> BoundingBox

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Face(self: GH_Surface) -> BrepFace

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: GH_Surface) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Surface) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Surface) -> str

"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: GH_Surface) -> Guid

Set: ReferenceID(self: GH_Surface) = value
"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Surface) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Surface) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_Surface) -> Brep

Set: Value(self: GH_Surface) = value
"""


    GH_SurfaceProxy = None
    m_value = None


class GH_Time(GH_Goo[DateTime], IGH_Goo, GH_ISerializable):
    """
    GH_Time()
    GH_Time(time: DateTime)
    GH_Time(other: GH_Time)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Time, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Time) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Time) -> IGH_Goo """
        pass

    def DuplicateDateTime(self):
        """ DuplicateDateTime(self: GH_Time) -> GH_Time """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Time) -> IGH_GooProxy """
        pass

    def Read(self, reader):
        """ Read(self: GH_Time, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Time) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Time, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, time: DateTime)
        __new__(cls: type, other: GH_Time)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Time) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Time) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Time) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Time) -> str

"""


    m_value = None


class GH_Transform(GH_Goo[Transform], IGH_Goo, GH_ISerializable):
    """
    GH_Transform()
    GH_Transform(transform: ITransform)
    GH_Transform(transform: Transform)
    GH_Transform(other: GH_Transform)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Transform, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[Q](self: GH_Transform, target: Q) -> (bool, Q) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_Transform) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Transform) -> IGH_Goo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Transform) -> IGH_GooProxy """
        pass

    def GetInverse(self):
        """ GetInverse(self: GH_Transform) -> GH_Transform """
        pass

    def Read(self, reader):
        """ Read(self: GH_Transform, reader: GH_IReader) -> bool """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: GH_Transform) -> object """
        pass

    def ToString(self):
        """ ToString(self: GH_Transform) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Transform, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, transform: ITransform)
        __new__(cls: type, transform: Transform)
        __new__(cls: type, other: GH_Transform)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CompoundTransforms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompoundTransforms(self: GH_Transform) -> List[ITransform]

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Transform) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: GH_Transform) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Transform) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Transform) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_Transform) -> Transform

Set: Value(self: GH_Transform) = value
"""


    m_value = None


class GH_Vector(GH_Goo[Vector3d], IGH_Goo, GH_ISerializable, IGH_QuickCast):
    """
    GH_Vector()
    GH_Vector(vector: Vector3d)
    GH_Vector(other: GH_Vector)
    """
    def CastFrom(self, source):
        """ CastFrom(self: GH_Vector, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: GH_Vector) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Vector) -> IGH_Goo """
        pass

    def DuplicateVector(self):
        """ DuplicateVector(self: GH_Vector) -> GH_Vector """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: GH_Vector) -> IGH_GooProxy """
        pass

    def QC_Bool(self):
        """ QC_Bool(self: GH_Vector) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: GH_Vector) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: GH_Vector, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: GH_Vector) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: GH_Vector, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: GH_Vector) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: GH_Vector) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: GH_Vector) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: GH_Vector) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: GH_Vector) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: GH_Vector) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: GH_Vector) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: GH_Vector) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_Vector, reader: GH_IReader) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_Vector) -> str """
        pass

    def Write(self, writer):
        """ Write(self: GH_Vector, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, vector: Vector3d)
        __new__(cls: type, other: GH_Vector)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_Vector) -> bool

"""

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: GH_Vector) -> GH_QuickCastType

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: GH_Vector) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: GH_Vector) -> str

"""


    GH_VectorProxy = None
    m_value = None


class GH_VectorForce(GH_FieldElement, IGH_FieldElement, GH_ISerializable, IGH_PreviewData):
    """ GH_VectorForce() """
    def DrawViewportWires(self, args):
        """ DrawViewportWires(self: GH_VectorForce, args: GH_PreviewWireArgs) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_VectorForce) -> IGH_FieldElement """
        pass

    def Force(self, location):
        """ Force(self: GH_VectorForce, location: Point3d) -> Vector3d """
        pass

    def Read(self, reader):
        """ Read(self: GH_VectorForce, reader: GH_IReader) -> bool """
        pass

    def Write(self, writer):
        """ Write(self: GH_VectorForce, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: GH_VectorForce) -> BoundingBox

"""

    Chord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chord(self: GH_VectorForce) -> Line

Set: Chord(self: GH_VectorForce) = value
"""

    ElementGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementGuid(self: GH_VectorForce) -> Guid

"""



class GH_WrapperType(object):
    # no doc
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, data: T)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GH_WrapperType[T]) -> T

Set: Value(self: GH_WrapperType[T]) = value
"""


    m_value = None


class IGH_FieldElement(GH_ISerializable, IGH_PreviewData):
    # no doc
    def Duplicate(self):
        """ Duplicate(self: IGH_FieldElement) -> IGH_FieldElement """
        pass

    def Force(self, location):
        """ Force(self: IGH_FieldElement, location: Point3d) -> Vector3d """
        pass

    def IsCoincident(self, point, tolerance):
        """ IsCoincident(self: IGH_FieldElement, point: Point3d, tolerance: float) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBox(self: IGH_FieldElement) -> BoundingBox

"""

    ElementGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementGuid(self: IGH_FieldElement) -> Guid

"""

    IsLimited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLimited(self: IGH_FieldElement) -> bool

Set: IsLimited(self: IGH_FieldElement) = value
"""

    Limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Limits(self: IGH_FieldElement) -> Box

Set: Limits(self: IGH_FieldElement) = value
"""



class IGH_Goo(GH_ISerializable):
    # no doc
    def CastFrom(self, source):
        """ CastFrom(self: IGH_Goo, source: object) -> bool """
        pass

    def CastTo(self, target):
        """ CastTo[T](self: IGH_Goo) -> (bool, T) """
        pass

    def Duplicate(self):
        """ Duplicate(self: IGH_Goo) -> IGH_Goo """
        pass

    def EmitProxy(self):
        """ EmitProxy(self: IGH_Goo) -> IGH_GooProxy """
        pass

    def ScriptVariable(self):
        """ ScriptVariable(self: IGH_Goo) -> object """
        pass

    def ToString(self):
        """ ToString(self: IGH_Goo) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: IGH_Goo) -> bool

"""

    IsValidWhyNot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidWhyNot(self: IGH_Goo) -> str

"""

    TypeDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDescription(self: IGH_Goo) -> str

"""

    TypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeName(self: IGH_Goo) -> str

"""



class IGH_GeometricGoo(IGH_Goo, GH_ISerializable):
    # no doc
    def ClearCaches(self):
        """ ClearCaches(self: IGH_GeometricGoo) """
        pass

    def DuplicateGeometry(self):
        """ DuplicateGeometry(self: IGH_GeometricGoo) -> IGH_GeometricGoo """
        pass

    def GetBoundingBox(self, xform):
        """ GetBoundingBox(self: IGH_GeometricGoo, xform: Transform) -> BoundingBox """
        pass

    def LoadGeometry(self, doc=None):
        """
        LoadGeometry(self: IGH_GeometricGoo, doc: RhinoDoc) -> bool
        LoadGeometry(self: IGH_GeometricGoo) -> bool
        """
        pass

    def Morph(self, xmorph):
        """ Morph(self: IGH_GeometricGoo, xmorph: SpaceMorph) -> IGH_GeometricGoo """
        pass

    def Transform(self, xform):
        """ Transform(self: IGH_GeometricGoo, xform: Transform) -> IGH_GeometricGoo """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Boundingbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundingbox(self: IGH_GeometricGoo) -> BoundingBox

"""

    IsGeometryLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeometryLoaded(self: IGH_GeometricGoo) -> bool

"""

    IsReferencedGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferencedGeometry(self: IGH_GeometricGoo) -> bool

"""

    ReferenceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceID(self: IGH_GeometricGoo) -> Guid

Set: ReferenceID(self: IGH_GeometricGoo) = value
"""



class IGH_GooProxy:
    # no doc
    def Construct(self):
        """ Construct(self: IGH_GooProxy) """
        pass

    def FormatInstance(self):
        """ FormatInstance(self: IGH_GooProxy) -> str """
        pass

    def FromString(self, in):
        """ FromString(self: IGH_GooProxy, in: str) -> bool """
        pass

    def MutateString(self, in):
        """ MutateString(self: IGH_GooProxy, in: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsParsable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsParsable(self: IGH_GooProxy) -> bool

"""

    ProxyOwner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProxyOwner(self: IGH_GooProxy) -> IGH_Goo

"""

    UserString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserString(self: IGH_GooProxy) -> str

Set: UserString(self: IGH_GooProxy) = value
"""

    Valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Valid(self: IGH_GooProxy) -> bool

"""



class IGH_QuickCast:
    # no doc
    def QC_Bool(self):
        """ QC_Bool(self: IGH_QuickCast) -> bool """
        pass

    def QC_Col(self):
        """ QC_Col(self: IGH_QuickCast) -> Color """
        pass

    def QC_CompareTo(self, other):
        """ QC_CompareTo(self: IGH_QuickCast, other: IGH_QuickCast) -> int """
        pass

    def QC_Complex(self):
        """ QC_Complex(self: IGH_QuickCast) -> Complex """
        pass

    def QC_Distance(self, other):
        """ QC_Distance(self: IGH_QuickCast, other: IGH_QuickCast) -> float """
        pass

    def QC_Hash(self):
        """ QC_Hash(self: IGH_QuickCast) -> int """
        pass

    def QC_Int(self):
        """ QC_Int(self: IGH_QuickCast) -> int """
        pass

    def QC_Interval(self):
        """ QC_Interval(self: IGH_QuickCast) -> Interval """
        pass

    def QC_Matrix(self):
        """ QC_Matrix(self: IGH_QuickCast) -> Matrix """
        pass

    def QC_Num(self):
        """ QC_Num(self: IGH_QuickCast) -> float """
        pass

    def QC_Pt(self):
        """ QC_Pt(self: IGH_QuickCast) -> Point3d """
        pass

    def QC_Text(self):
        """ QC_Text(self: IGH_QuickCast) -> str """
        pass

    def QC_Vec(self):
        """ QC_Vec(self: IGH_QuickCast) -> Vector3d """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    QC_Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QC_Type(self: IGH_QuickCast) -> GH_QuickCastType

"""



class UVInterval(object):
    """ UVInterval(newU: Interval, newV: Interval) """
    @staticmethod # known case of __new__
    def __new__(self, newU, newV):
        """
        __new__(cls: type, newU: Interval, newV: Interval)
        __new__[UVInterval]() -> UVInterval
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: UVInterval) -> bool

"""

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: U(self: UVInterval) -> Interval

Set: U(self: UVInterval) = value
"""

    U0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: U0(self: UVInterval) -> float

Set: U0(self: UVInterval) = value
"""

    U1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: U1(self: UVInterval) -> float

Set: U1(self: UVInterval) = value
"""

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: V(self: UVInterval) -> Interval

Set: V(self: UVInterval) = value
"""

    V0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: V0(self: UVInterval) -> float

Set: V0(self: UVInterval) = value
"""

    V1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: V1(self: UVInterval) -> float

Set: V1(self: UVInterval) = value
"""



# variables with complex values

