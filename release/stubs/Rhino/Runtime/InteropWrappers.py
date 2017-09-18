# encoding: utf-8
# module Rhino.Runtime.InteropWrappers calls itself InteropWrappers
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ClassArrayObjRef(object, IDisposable):
    """
    Represents a wrapper to an unmanaged "array" (list) of CRhinoObjRef instances.
                Wrapper for a C++ ON_ClassArray of CRhinoObjRef
    
    ClassArrayObjRef()
    ClassArrayObjRef(objrefs: IEnumerable[ObjRef])
    """
    def Add(self, objref):
        """
        Add(self: ClassArrayObjRef, objref: ObjRef)
            Adds an ObjRef to the list.
        
            objref: An ObjRef to add.
        """
        pass

    def ConstPointer(self):
        """
        ConstPointer(self: ClassArrayObjRef) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ClassArrayObjRef)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: ClassArrayObjRef) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToNonConstArray(self):
        """
        ToNonConstArray(self: ClassArrayObjRef) -> Array[ObjRef]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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
    def __new__(self, objrefs=None):
        """
        __new__(cls: type)
        __new__(cls: type, objrefs: IEnumerable[ObjRef])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of CRhinoObjRef instances in this array.

Get: Count(self: ClassArrayObjRef) -> int

"""



class ClassArrayOnObjRef(object, IDisposable):
    """
    Represents a wrapper to an unmanaged "array" (list) of ON_ObjRef instances.
                Wrapper for a C++ ON_ClassArray of ON_ObjRef
    
    ClassArrayOnObjRef()
    ClassArrayOnObjRef(objrefs: IEnumerable[ObjRef])
    """
    def Add(self, objref):
        """
        Add(self: ClassArrayOnObjRef, objref: ObjRef)
            Adds an ObjRef to the list.
        
            objref: An ObjRef to add.
        """
        pass

    def ConstPointer(self):
        """
        ConstPointer(self: ClassArrayOnObjRef) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ClassArrayOnObjRef)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: ClassArrayOnObjRef) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToNonConstArray(self):
        """
        ToNonConstArray(self: ClassArrayOnObjRef) -> Array[ObjRef]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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
    def __new__(self, objrefs=None):
        """
        __new__(cls: type)
        __new__(cls: type, objrefs: IEnumerable[ObjRef])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of ObjRef instances in this array.

Get: Count(self: ClassArrayOnObjRef) -> int

"""



class MeshPointDataStruct(object):
    """
    This is only needed when passing values to the Rhino C++ core, ignore
                for .NET plug-ins.
    """
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
    """
    Wrapper for a C++ ON_SimpleArray<ON_Brep*> or ON_SimpleArray<const ON_Brep*>
                If you are not writing C++ code then this class is not for you.
    
    SimpleArrayBrepPointer()
    """
    def Add(self, brep, asConst):
        """
        Add(self: SimpleArrayBrepPointer, brep: Brep, asConst: bool)
            Adds a brep to the list.
        
            brep: A brep to add.
            asConst: Whether this brep should be treated as non-modifiable.
        """
        pass

    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayBrepPointer) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayBrepPointer)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayBrepPointer) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToNonConstArray(self):
        """
        ToNonConstArray(self: SimpleArrayBrepPointer) -> Array[Brep]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of breps in this array.

Get: Count(self: SimpleArrayBrepPointer) -> int

"""



class SimpleArrayCurvePointer(object, IDisposable):
    """
    Wrapper for a C++ ON_SimpleArray of ON_Curve* or const ON_Curve*.  If you are not
                writing C++ code, then you can ignore this class.
    
    SimpleArrayCurvePointer()
    SimpleArrayCurvePointer(curves: IEnumerable[Curve])
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayCurvePointer) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayCurvePointer)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayCurvePointer) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToNonConstArray(self):
        """
        ToNonConstArray(self: SimpleArrayCurvePointer) -> Array[Curve]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
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
    Wrapper for ON_SimpleArray<double>. If you are not writing C++ code,
                then this class is not for you.
    
    SimpleArrayDouble()
    SimpleArrayDouble(items: IEnumerable[float])
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayDouble) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayDouble)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayDouble) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: SimpleArrayDouble) -> Array[float]
        
            Returns the managed counterpart of the unmanaged array.
            Returns: The managed array.
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
    """Gets the amount of elements in this array.

Get: Count(self: SimpleArrayDouble) -> int

"""



class SimpleArrayGeometryPointer(object, IDisposable):
    """
    Wrapper for a C++ ON_SimpleArray<ON_Geometry*>* or ON_SimpleArray<const ON_Geometry*>.
                If you are not writing C++ code, then this class is not for you.
    
    SimpleArrayGeometryPointer()
    SimpleArrayGeometryPointer(geometry: IEnumerable[GeometryBase])
    SimpleArrayGeometryPointer(geometry: IEnumerable)
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayGeometryPointer) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayGeometryPointer)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayGeometryPointer) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToNonConstArray(self):
        """
        ToNonConstArray(self: SimpleArrayGeometryPointer) -> Array[GeometryBase]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
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
    """
    Wrapper for ON_SimpleArray<ON_UUID>. If you are not writing C++ code
                then this class is not for you.
    
    SimpleArrayGuid()
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayGuid) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayGuid)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayGuid) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: SimpleArrayGuid) -> Array[Guid]
        
            Returns the managed counterpart of the unmanaged array.
            Returns: The managed array.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of elements in this array.

Get: Count(self: SimpleArrayGuid) -> int

"""



class SimpleArrayInt(object, IDisposable):
    """
    Wrapper for ON_SimpleArray<int>. If you are not writing C++ code
                then this class is not for you.
    
    SimpleArrayInt()
    SimpleArrayInt(values: IEnumerable[int])
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayInt) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayInt)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayInt) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: SimpleArrayInt) -> Array[int]
        
            Returns the managed counterpart of the unmanaged array.
            Returns: The managed array.
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
    """Gets the amount of elements in this array.

Get: Count(self: SimpleArrayInt) -> int

"""



class SimpleArrayInterval(object, IDisposable):
    """
    Wrapper for ON_SimpleArray<ON_Imterval>. If you are not writing C++ code
                then this class is not for you.
    
    SimpleArrayInterval()
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayInterval) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayInterval)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayInterval) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: SimpleArrayInterval) -> Array[Interval]
        
            Returns the managed counterpart of the unmanaged array.
            Returns: The managed array.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of elements in this array.

Get: Count(self: SimpleArrayInterval) -> int

"""



class SimpleArrayLine(object, IDisposable):
    """
    Wrapper for ON_SimpleArray<ON_Line>. If you are not writing C++ code
                then this class is not for you.
    
    SimpleArrayLine()
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayLine) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayLine)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayLine) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: SimpleArrayLine) -> Array[Line]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of lines in this array.

Get: Count(self: SimpleArrayLine) -> int

"""



class SimpleArrayMeshPointer(object, IDisposable):
    """
    Represents a wrapper to an unmanaged array of mesh pointers.
                Wrapper for a C++ ON_SimpleArray of ON_Mesh* or const ON_Mesh*. If you are not
                writing C++ code then this class is not for you.
    
    SimpleArrayMeshPointer()
    """
    def Add(self, mesh, asConst):
        """
        Add(self: SimpleArrayMeshPointer, mesh: Mesh, asConst: bool)
            Adds a mesh to the list.
        
            mesh: A mesh to add.
            asConst: Whether this mesh should be treated as non-modifiable.
        """
        pass

    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayMeshPointer) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayMeshPointer)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayMeshPointer) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToNonConstArray(self):
        """
        ToNonConstArray(self: SimpleArrayMeshPointer) -> Array[Mesh]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of meshes in this array.

Get: Count(self: SimpleArrayMeshPointer) -> int

"""



class SimpleArrayPoint2d(object, IDisposable):
    """
    ON_SimpleArray<ON_2dPoint> class wrapper.  If you are not writing
                C++ code then this class is not for you.
    
    SimpleArrayPoint2d()
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayPoint2d) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayPoint2d)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayPoint2d) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: SimpleArrayPoint2d) -> Array[Point2d]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of points in this array.

Get: Count(self: SimpleArrayPoint2d) -> int

"""



class SimpleArrayPoint3d(object, IDisposable):
    """
    ON_SimpleArray<ON_3dPoint>, ON_3dPointArray, ON_PolyLine all have the same size
                This class wraps all of these C++ versions.  If you are not writing C++ code then this
                class is not for you.
    
    SimpleArrayPoint3d()
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArrayPoint3d) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArrayPoint3d)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArrayPoint3d) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToArray(self):
        """
        ToArray(self: SimpleArrayPoint3d) -> Array[Point3d]
        
            Copies the unmanaged array to a managed counterpart.
            Returns: The managed array.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of points in this array.

Get: Count(self: SimpleArrayPoint3d) -> int

"""



class SimpleArraySurfacePointer(object, IDisposable):
    """
    Wrapper for a C++ ON_SimpleArray of ON_Surface* or const ON_Surface*.  If
                you are not writing C++ code then this class is not for you.
    
    SimpleArraySurfacePointer()
    """
    def ConstPointer(self):
        """
        ConstPointer(self: SimpleArraySurfacePointer) -> IntPtr
        
            Gets the const (immutable) pointer of this array.
            Returns: The const pointer.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: SimpleArraySurfacePointer)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: SimpleArraySurfacePointer) -> IntPtr
        
            Gets the non-const pointer (for modification) of this array.
            Returns: The non-const pointer.
        """
        pass

    def ToNonConstArray(self):
        """
        ToNonConstArray(self: SimpleArraySurfacePointer) -> Array[Surface]
        
            Copies the unmanaged array to a managed counterpart.
                    Elements are made non-const.
            Returns: The managed array.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class StringHolder(object, IDisposable):
    """
    This class is used to pass strings back and forth between managed
                and unmanaged code.  This should not be be needed by plug-ins.
    
    StringHolder()
    """
    def ConstPointer(self):
        """
        ConstPointer(self: StringHolder) -> IntPtr
        
            C++ pointer used to access the ON_wString, managed plug-ins should
                    never need this.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: StringHolder)
            IDispose implementation
        """
        pass

    @staticmethod
    def GetString(pStringHolder):
        """
        GetString(pStringHolder: IntPtr) -> str
        
            Get managed string from unmanaged ON_wString pointer.
        """
        pass

    def NonConstPointer(self):
        """
        NonConstPointer(self: StringHolder) -> IntPtr
        
            C++ pointer used to access the ON_wString, managed plug-ins should
                    never need this.
        """
        pass

    def ToString(self):
        """
        ToString(self: StringHolder) -> str
        
            Marshal unmanaged ON_wString to a managed .NET string
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class StringWrapper(object, IDisposable):
    """
    Represents a wrapper to an unmanaged OpenNurbs string.
                Wraps a C++ ON_wString*.
    
    StringWrapper()
    StringWrapper(s: str)
    """
    def Dispose(self):
        """
        Dispose(self: StringWrapper)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    @staticmethod
    def GetStringFromPointer(pConstON_wString):
        """
        GetStringFromPointer(pConstON_wString: IntPtr) -> str
        
            Get string from an ON_wString*
        """
        pass

    def SetString(self, s):
        """
        SetString(self: StringWrapper, s: str)
            Set contents of this string.
        
            s: The new string.
        """
        pass

    @staticmethod
    def SetStringOnPointer(pON_wString, s):
        """
        SetStringOnPointer(pON_wString: IntPtr, s: str)
            Set contents of an ON_wString*
        """
        pass

    def ToString(self):
        """
        ToString(self: StringWrapper) -> str
        
            Returns the string contents of this wrapper.
            Returns: A managed string.
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
    """Gets the const pointer (const ON_wString*).

Get: ConstPointer(self: StringWrapper) -> IntPtr

"""

    NonConstPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the non-const pointer (ON_wString*).

Get: NonConstPointer(self: StringWrapper) -> IntPtr

"""



