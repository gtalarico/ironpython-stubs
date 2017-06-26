class ExternalResourceLoadContext(object,IDisposable):
 """
 This class contains data describing the context related
    to an external resource load operation.
 """
 def CallingDocumentHasModelPath(self):
  """
  CallingDocumentHasModelPath(self: ExternalResourceLoadContext) -> bool
  
   Indicates whether the document requesting the external resource has a defined
   
      ModelPath.
  
   Returns: True if the document has a defined ModelPath.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ExternalResourceLoadContext) """
  pass
 def GetCallingDocumentModelPath(self):
  """
  GetCallingDocumentModelPath(self: ExternalResourceLoadContext) -> ModelPath
  
   Returns a copy of the ModelPath of the document that is requesting
     the 
    external resource.
  
   Returns: A copy of the ModelPath of the document that is requesting the external
     
    resource.
  """
  pass
 def GetCurrentlyLoadedReference(self):
  """
  GetCurrentlyLoadedReference(self: ExternalResourceLoadContext) -> ExternalResourceReference
  
   Returns a copy of the ExternalResourceReference currently
     in use by the 
    containing element.
  
   Returns: A copy of the ExternalResourceReference currently in use
     by the containing 
    element.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalResourceLoadContext,disposing: bool) """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExternalResourceLoadContext) -> bool

"""

 LoadOperationType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An enum value indicating whether the resource load was triggered by an
   automatic event (such as file open) or an explicit user action.

Get: LoadOperationType(self: ExternalResourceLoadContext) -> LoadOperationType

"""


