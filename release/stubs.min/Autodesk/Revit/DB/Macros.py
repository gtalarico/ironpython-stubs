# encoding: utf-8
# module Autodesk.Revit.DB.Macros calls itself Macros
# from RevitAPI,Version=17.0.0.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddInIdAttribute(Attribute,_Attribute):
 """
 The custom AddInId attribute for Macros macros use only.

 

 AddInIdAttribute(addInIdStr: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,addInIdStr):
  """ __new__(cls: type,addInIdStr: str) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """AddInId guid value.



Get: Value(self: AddInIdAttribute) -> ValueType



"""



class ApplicationEntryPoint(Application,IDisposable,IEntryPoint):
 """
 For Revit Macros use only.

 

 ApplicationEntryPoint()
 """
 def Dispose(self):
  """ Dispose(self: Application,A_0: bool) """
  pass
 def FinishInitialization(self,*args):
  """ FinishInitialization(self: ApplicationEntryPoint) """
  pass
 def FinishInitializationEO(self):
  """
  FinishInitializationEO(self: ApplicationEntryPoint)

   For Revit Macros internal use only.
  """
  pass
 def Initialize(self,obj,addinFolder):
  """
  Initialize(self: ApplicationEntryPoint,obj: object,addinFolder: str)

   For Revit Macros internal use only.
  """
  pass
 def OnShutdown(self,*args):
  """ OnShutdown(self: ApplicationEntryPoint) """
  pass
 def OnShutdownEO(self):
  """
  OnShutdownEO(self: ApplicationEntryPoint)

   For Revit Macros internal use only.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Application,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AddinFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The full path to the Revit Macros module.



Get: AddinFolder(self: ApplicationEntryPoint) -> str



"""

 PrimaryCookie=property(lambda self: object(),lambda self,v: None,lambda self: None)



class DocumentEntryPoint(Document,IDisposable,IEntryPoint):
 """
 For Revit Macros use only.

 

 DocumentEntryPoint()
 """
 def Dispose(self):
  """ Dispose(self: Document,A_0: bool) """
  pass
 def FinishInitialization(self,*args):
  """ FinishInitialization(self: DocumentEntryPoint) """
  pass
 def FinishInitializationEO(self):
  """
  FinishInitializationEO(self: DocumentEntryPoint)

   For Revit Macros internal use only.
  """
  pass
 def Initialize(self,obj,addinFolder):
  """
  Initialize(self: DocumentEntryPoint,obj: object,addinFolder: str)

   For Revit Macros internal use only.
  """
  pass
 def OnShutdown(self,*args):
  """ OnShutdown(self: DocumentEntryPoint) """
  pass
 def OnShutdownEO(self):
  """
  OnShutdownEO(self: DocumentEntryPoint)

   For Revit Macros internal use only.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Document,disposing: bool) """
  pass
 def ReleaseUnmanagedResources_(self,*args):
  """ ReleaseUnmanagedResources_(self: Document,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AddinFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The full path to the Revit Macros module.



Get: AddinFolder(self: DocumentEntryPoint) -> str



"""

 PrimaryCookie=property(lambda self: object(),lambda self,v: None,lambda self: None)



class IEntryPoint:
 """ The interface supporting Document and Application level entry point classes for macros. """
 def FinishInitialization(self):
  """ FinishInitialization(self: IEntryPoint) """
  pass
 def Initialize(self,obj,addinFolder):
  """ Initialize(self: IEntryPoint,obj: object,addinFolder: str) """
  pass
 def OnShutdown(self):
  """ OnShutdown(self: IEntryPoint) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AddinFolder=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: AddinFolder(self: IEntryPoint) -> str



"""



class VendorIdAttribute(Attribute,_Attribute):
 """
 The custom VendorId attribute for Macros macros use only.

 

 VendorIdAttribute(vendorIdStr: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,vendorIdStr):
  """ __new__(cls: type,vendorIdStr: str) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """AddInId VendorId value.



Get: Value(self: VendorIdAttribute) -> str



"""



