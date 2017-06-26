# encoding: utf-8
# module Rhino.Runtime calls itself Runtime
# from Rhino3dmIO, Version=5.1.30000.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AssemblyResolver(object):
    # no doc
    @staticmethod
    def AddSearchFile(file):
        """ AddSearchFile(file: str) """
        pass

    @staticmethod
    def AddSearchFolder(folder):
        """ AddSearchFolder(folder: str) """
        pass

    __all__ = [
        'AddSearchFile',
        'AddSearchFolder',
    ]


class CommonObject(object, IDisposable, ISerializable):
    # no doc
    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject) """
        pass

    def EnsurePrivateCopy(self):
        """ EnsurePrivateCopy(self: CommonObject) """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: CommonObject, info: SerializationInfo, context: StreamingContext) """
        pass

    def IsValidWithLog(self, log):
        """ IsValidWithLog(self: CommonObject) -> (bool, str) """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: CommonObject) """
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    HasUserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasUserData(self: CommonObject) -> bool

"""

    IsDocumentControlled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDocumentControlled(self: CommonObject) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: CommonObject) -> bool

"""

    UserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserData(self: CommonObject) -> UserDataList

"""

    UserDictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserDictionary(self: CommonObject) -> ArchivableDictionary

"""



class DocumentCollectedException(Exception, ISerializable, _Exception):
    """ DocumentCollectedException() """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class HostUtils(object):
    # no doc
    @staticmethod
    def DebugDumpToString(*__args):
        """
        DebugDumpToString(bezierCurve: BezierCurve) -> str
        DebugDumpToString(geometry: GeometryBase) -> str
        """
        pass

    @staticmethod
    def DebugString(*__args):
        """ DebugString(format: str, *args: Array[object])DebugString(msg: str) """
        pass

    @staticmethod
    def ExceptionReport(*__args):
        """ ExceptionReport(source: str, ex: Exception)ExceptionReport(ex: Exception) """
        pass

    @staticmethod
    def GetAssemblySearchPaths():
        """ GetAssemblySearchPaths() -> Array[str] """
        pass

    @staticmethod
    def GetRhinoDotNetAssembly():
        """ GetRhinoDotNetAssembly() -> Assembly """
        pass

    @staticmethod
    def InitializeRhinoCommon():
        """ InitializeRhinoCommon() """
        pass

    @staticmethod
    def InitializeZooClient():
        """ InitializeZooClient() """
        pass

    @staticmethod
    def InPlaceConstCast(geometry, makeNonConst):
        """ InPlaceConstCast(geometry: GeometryBase, makeNonConst: bool) """
        pass

    @staticmethod
    def SetInShutDown():
        """ SetInShutDown() """
        pass

    ExceptionReportDelegate = None
    OnExceptionReport = None
    RunningInMono = False
    RunningInRhino = False
    RunningOnOSX = False
    RunningOnWindows = True
    SendDebugToCommandLine = False
    __all__ = [
        'DebugDumpToString',
        'DebugString',
        'ExceptionReport',
        'ExceptionReportDelegate',
        'GetAssemblySearchPaths',
        'GetRhinoDotNetAssembly',
        'InitializeRhinoCommon',
        'InitializeZooClient',
        'InPlaceConstCast',
        'OnExceptionReport',
        'SetInShutDown',
    ]


class Interop(object):
    # no doc
    @staticmethod
    def CreateFromNativePointer(pGeometry):
        """ CreateFromNativePointer(pGeometry: IntPtr) -> GeometryBase """
        pass

    @staticmethod
    def FromOnBrep(source):
        """ FromOnBrep(source: object) -> Brep """
        pass

    @staticmethod
    def FromOnCurve(source):
        """ FromOnCurve(source: object) -> Curve """
        pass

    @staticmethod
    def FromOnMesh(source):
        """ FromOnMesh(source: object) -> Mesh """
        pass

    @staticmethod
    def FromOnSurface(source):
        """ FromOnSurface(source: object) -> Surface """
        pass

    @staticmethod
    def NativeGeometryConstPointer(geometry):
        """ NativeGeometryConstPointer(geometry: GeometryBase) -> IntPtr """
        pass

    @staticmethod
    def NativeGeometryNonConstPointer(geometry):
        """ NativeGeometryNonConstPointer(geometry: GeometryBase) -> IntPtr """
        pass

    @staticmethod
    def NativeNonConstPointer(viewport):
        """ NativeNonConstPointer(viewport: ViewportInfo) -> IntPtr """
        pass

    @staticmethod
    def ToOnBrep(source):
        """ ToOnBrep(source: Brep) -> object """
        pass

    @staticmethod
    def ToOnCurve(source):
        """ ToOnCurve(source: Curve) -> object """
        pass

    @staticmethod
    def ToOnMesh(source):
        """ ToOnMesh(source: Mesh) -> object """
        pass

    @staticmethod
    def ToOnSurface(source):
        """ ToOnSurface(source: Surface) -> object """
        pass

    @staticmethod
    def ToOnXform(source):
        """ ToOnXform(source: Transform) -> object """
        pass

    @staticmethod
    def TryCopyFromOnArc(source, destination):
        """ TryCopyFromOnArc(source: object) -> (bool, Arc) """
        pass

    @staticmethod
    def TryCopyToOnArc(source, destination):
        """ TryCopyToOnArc(source: Arc, destination: object) -> bool """
        pass

    __all__ = [
        'CreateFromNativePointer',
        'FromOnBrep',
        'FromOnCurve',
        'FromOnMesh',
        'FromOnSurface',
        'NativeGeometryConstPointer',
        'NativeGeometryNonConstPointer',
        'NativeNonConstPointer',
        'ToOnBrep',
        'ToOnCurve',
        'ToOnMesh',
        'ToOnSurface',
        'ToOnXform',
        'TryCopyFromOnArc',
        'TryCopyToOnArc',
    ]


class RdkNotLoadedException(Exception, ISerializable, _Exception):
    """ RdkNotLoadedException() """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


# variables with complex values

