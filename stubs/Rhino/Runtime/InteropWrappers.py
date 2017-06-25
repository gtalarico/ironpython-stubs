# encoding: utf-8
# module Rhino.Runtime.InteropWrappers calls itself InteropWrappers
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MeshPointDataStruct(object):
    # no doc
    m_ci_index = None
    m_ci_type = None
    m_edge_index = None
    m_et = None
    m_face_index = None
    m_Px = None
    m_Py = None
    m_Pz = None
    m_t0 = None
    m_t1 = None
    m_t2 = None
    m_t3 = None
    m_Triangle = None


class SimpleArrayBrepPointer(object, IDisposable):
    """ SimpleArrayBrepPointer() """
    def Add(self, brep, asConst):
        """ Add(self: SimpleArrayBrepPointer, brep: Brep, asConst: bool) """
        pass

    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayBrepPointer) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayBrepPointer) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayBrepPointer) -> IntPtr """
        pass

    def ToNonConstArray(self):
        """ ToNonConstArray(self: SimpleArrayBrepPointer) -> Array[Brep] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayBrepPointer) -> int

"""



class SimpleArrayCurvePointer(object, IDisposable):
    """
    SimpleArrayCurvePointer()
    SimpleArrayCurvePointer(curves: IEnumerable[Curve])
    """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayCurvePointer) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayCurvePointer) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayCurvePointer) -> IntPtr """
        pass

    def ToNonConstArray(self):
        """ ToNonConstArray(self: SimpleArrayCurvePointer) -> Array[Curve] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, curves=None):
        """
        __new__(cls: type)
        __new__(cls: type, curves: IEnumerable[Curve])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SimpleArrayDouble(object, IDisposable):
    """
    SimpleArrayDouble()
    SimpleArrayDouble(items: IEnumerable[float])
    """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayDouble) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayDouble) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayDouble) -> IntPtr """
        pass

    def ToArray(self):
        """ ToArray(self: SimpleArrayDouble) -> Array[float] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, items=None):
        """
        __new__(cls: type)
        __new__(cls: type, items: IEnumerable[float])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayDouble) -> int

"""



class SimpleArrayGeometryPointer(object, IDisposable):
    """
    SimpleArrayGeometryPointer()
    SimpleArrayGeometryPointer(geometry: IEnumerable[GeometryBase])
    SimpleArrayGeometryPointer(geometry: IEnumerable)
    """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayGeometryPointer) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayGeometryPointer) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayGeometryPointer) -> IntPtr """
        pass

    def ToNonConstArray(self):
        """ ToNonConstArray(self: SimpleArrayGeometryPointer) -> Array[GeometryBase] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, geometry=None):
        """
        __new__(cls: type)
        __new__(cls: type, geometry: IEnumerable[GeometryBase])
        __new__(cls: type, geometry: IEnumerable)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class SimpleArrayGuid(object, IDisposable):
    """ SimpleArrayGuid() """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayGuid) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayGuid) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayGuid) -> IntPtr """
        pass

    def ToArray(self):
        """ ToArray(self: SimpleArrayGuid) -> Array[Guid] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayGuid) -> int

"""



class SimpleArrayInt(object, IDisposable):
    """
    SimpleArrayInt()
    SimpleArrayInt(values: IEnumerable[int])
    """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayInt) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayInt) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayInt) -> IntPtr """
        pass

    def ToArray(self):
        """ ToArray(self: SimpleArrayInt) -> Array[int] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, values=None):
        """
        __new__(cls: type)
        __new__(cls: type, values: IEnumerable[int])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayInt) -> int

"""



class SimpleArrayInterval(object, IDisposable):
    """ SimpleArrayInterval() """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayInterval) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayInterval) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayInterval) -> IntPtr """
        pass

    def ToArray(self):
        """ ToArray(self: SimpleArrayInterval) -> Array[Interval] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayInterval) -> int

"""



class SimpleArrayLine(object, IDisposable):
    """ SimpleArrayLine() """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayLine) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayLine) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayLine) -> IntPtr """
        pass

    def ToArray(self):
        """ ToArray(self: SimpleArrayLine) -> Array[Line] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayLine) -> int

"""



class SimpleArrayMeshPointer(object, IDisposable):
    """ SimpleArrayMeshPointer() """
    def Add(self, mesh, asConst):
        """ Add(self: SimpleArrayMeshPointer, mesh: Mesh, asConst: bool) """
        pass

    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayMeshPointer) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayMeshPointer) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayMeshPointer) -> IntPtr """
        pass

    def ToNonConstArray(self):
        """ ToNonConstArray(self: SimpleArrayMeshPointer) -> Array[Mesh] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayMeshPointer) -> int

"""



class SimpleArrayPoint2d(object, IDisposable):
    """ SimpleArrayPoint2d() """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayPoint2d) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayPoint2d) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayPoint2d) -> IntPtr """
        pass

    def ToArray(self):
        """ ToArray(self: SimpleArrayPoint2d) -> Array[Point2d] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayPoint2d) -> int

"""



class SimpleArrayPoint3d(object, IDisposable):
    """ SimpleArrayPoint3d() """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArrayPoint3d) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArrayPoint3d) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArrayPoint3d) -> IntPtr """
        pass

    def ToArray(self):
        """ ToArray(self: SimpleArrayPoint3d) -> Array[Point3d] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SimpleArrayPoint3d) -> int

"""



class SimpleArraySurfacePointer(object, IDisposable):
    """ SimpleArraySurfacePointer() """
    def ConstPointer(self):
        """ ConstPointer(self: SimpleArraySurfacePointer) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: SimpleArraySurfacePointer) """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: SimpleArraySurfacePointer) -> IntPtr """
        pass

    def ToNonConstArray(self):
        """ ToNonConstArray(self: SimpleArraySurfacePointer) -> Array[Surface] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class StringHolder(object, IDisposable):
    """ StringHolder() """
    def ConstPointer(self):
        """ ConstPointer(self: StringHolder) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: StringHolder) """
        pass

    @staticmethod
    def GetString(pStringHolder):
        """ GetString(pStringHolder: IntPtr) -> str """
        pass

    def NonConstPointer(self):
        """ NonConstPointer(self: StringHolder) -> IntPtr """
        pass

    def ToString(self):
        """ ToString(self: StringHolder) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class StringWrapper(object, IDisposable):
    """
    StringWrapper()
    StringWrapper(s: str)
    """
    def Dispose(self):
        """ Dispose(self: StringWrapper) """
        pass

    @staticmethod
    def GetStringFromPointer(pConstON_wString):
        """ GetStringFromPointer(pConstON_wString: IntPtr) -> str """
        pass

    def SetString(self, s):
        """ SetString(self: StringWrapper, s: str) """
        pass

    @staticmethod
    def SetStringOnPointer(pON_wString, s):
        """ SetStringOnPointer(pON_wString: IntPtr, s: str) """
        pass

    def ToString(self):
        """ ToString(self: StringWrapper) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, s=None):
        """
        __new__(cls: type)
        __new__(cls: type, s: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ConstPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstPointer(self: StringWrapper) -> IntPtr

"""

    NonConstPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonConstPointer(self: StringWrapper) -> IntPtr

"""



