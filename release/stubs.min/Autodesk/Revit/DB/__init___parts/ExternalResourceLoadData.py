class ExternalResourceLoadData(object,IDisposable):
 """
 This class contains the input and output data resulting from invoking an IExternalResourceServer's LoadResource method.After the call to LoadResource,the resulting ExternalResourceLoadData will be passed into

    IExternalResourceServer.HandleLoadResourceResults() so that appropriate UI can be displayed. Server providers can inspect the ExternalResourceLoadData to get an ExternalResourceLoadContent

    object of the subclass appropriate to the external resource. The class also contains a copy of the

    ExternalResourceReference,and information about the context of the load operation.
 """
 def Dispose(self):
  """ Dispose(self: ExternalResourceLoadData) """
  pass
 def GetExternalResourceReference(self):
  """
  GetExternalResourceReference(self: ExternalResourceLoadData) -> ExternalResourceReference

  

   Returns the ExternalResourceReference that identifies which resource should be 

    loaded.
  """
  pass
 def GetLoadContent(self):
  """
  GetLoadContent(self: ExternalResourceLoadData) -> ExternalResourceLoadContent

  

   Returns the ExternalResourceLoadContent resulting from this load operation.

   Returns: A reference to an ExternalResourceLoadContent object.
  """
  pass
 def GetLoadContext(self):
  """
  GetLoadContext(self: ExternalResourceLoadData) -> ExternalResourceLoadContext

  

   Returns an object containing information about the context of the load 

    operation.

  

   Returns: An object containing information about the context of the load operation.
  """
  pass
 def GetLoadRequestId(self):
  """
  GetLoadRequestId(self: ExternalResourceLoadData) -> Guid

  

   Returns the load operation GUID.

   Returns: The load operation GUID.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalResourceLoadData,disposing: bool) """
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
 ErrorsReported=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the IExternalResourceUIServer has reported errors

   for this ExternalResourceLoadData. This value can be set by the

   IExternalResourceUIServer in HandleLoadResourceResults().



Get: ErrorsReported(self: ExternalResourceLoadData) -> bool



Set: ErrorsReported(self: ExternalResourceLoadData)=value

"""

 ExternalResourceType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The ExternalResourceType for which Revit is requesting data from the server.



Get: ExternalResourceType(self: ExternalResourceLoadData) -> ExternalResourceType



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ExternalResourceLoadData) -> bool



"""

 LoadStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The success or failure status of the load attempt.



Get: LoadStatus(self: ExternalResourceLoadData) -> ExternalResourceLoadStatus



"""


