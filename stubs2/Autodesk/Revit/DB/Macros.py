# encoding: utf-8
# module Autodesk.Revit.DB.Macros calls itself Macros
# from RevitAPI, Version=17.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddInIdAttribute(Attribute, _Attribute):
    """
    The custom AddInId attribute for Macros macros use only.
    
    AddInIdAttribute(addInIdStr: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, addInIdStr):
        """ __new__(cls: type, addInIdStr: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """AddInId guid value.

Get: Value(self: AddInIdAttribute) -> ValueType

"""



class ApplicationEntryPoint(Application, IDisposable, IEntryPoint):
    """
    For Revit Macros use only.
    
    ApplicationEntryPoint()
    """
    def Dispose(self):
        """ Dispose(self: Application, A_0: bool) """
        pass

    def FinishInitialization(self, *args): #cannot find CLR method
        """ FinishInitialization(self: ApplicationEntryPoint) """
        pass

    def FinishInitializationEO(self):
        """
        FinishInitializationEO(self: ApplicationEntryPoint)
            For Revit Macros internal use only.
        """
        pass

    def Initialize(self, obj, addinFolder):
        """
        Initialize(self: ApplicationEntryPoint, obj: object, addinFolder: str)
            For Revit Macros internal use only.
        """
        pass

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: ApplicationEntryPoint) """
        pass

    def OnShutdownEO(self):
        """
        OnShutdownEO(self: ApplicationEntryPoint)
            For Revit Macros internal use only.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Application, disposing: bool) """
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

    AddinFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full path to the Revit Macros module.

Get: AddinFolder(self: ApplicationEntryPoint) -> str

"""

    PrimaryCookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class DocumentEntryPoint(Document, IDisposable, IEntryPoint):
    """
    For Revit Macros use only.
    
    DocumentEntryPoint()
    """
    def Dispose(self):
        """ Dispose(self: Document, A_0: bool) """
        pass

    def FinishInitialization(self, *args): #cannot find CLR method
        """ FinishInitialization(self: DocumentEntryPoint) """
        pass

    def FinishInitializationEO(self):
        """
        FinishInitializationEO(self: DocumentEntryPoint)
            For Revit Macros internal use only.
        """
        pass

    def Initialize(self, obj, addinFolder):
        """
        Initialize(self: DocumentEntryPoint, obj: object, addinFolder: str)
            For Revit Macros internal use only.
        """
        pass

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: DocumentEntryPoint) """
        pass

    def OnShutdownEO(self):
        """
        OnShutdownEO(self: DocumentEntryPoint)
            For Revit Macros internal use only.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Document, disposing: bool) """
        pass

    def ReleaseUnmanagedResources_(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources_(self: Document, disposing: bool) """
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

    AddinFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full path to the Revit Macros module.

Get: AddinFolder(self: DocumentEntryPoint) -> str

"""

    PrimaryCookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IEntryPoint:
    """ The interface supporting Document and Application level entry point classes for macros. """
    def FinishInitialization(self):
        """ FinishInitialization(self: IEntryPoint) """
        pass

    def Initialize(self, obj, addinFolder):
        """ Initialize(self: IEntryPoint, obj: object, addinFolder: str) """
        pass

    def OnShutdown(self):
        """ OnShutdown(self: IEntryPoint) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AddinFolder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddinFolder(self: IEntryPoint) -> str

"""



class VendorIdAttribute(Attribute, _Attribute):
    """
    The custom VendorId attribute for Macros macros use only.
    
    VendorIdAttribute(vendorIdStr: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, vendorIdStr):
        """ __new__(cls: type, vendorIdStr: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """AddInId VendorId value.

Get: Value(self: VendorIdAttribute) -> str

"""



