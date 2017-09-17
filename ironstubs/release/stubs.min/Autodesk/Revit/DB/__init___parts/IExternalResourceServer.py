class IExternalResourceServer(IExternalServer):
 """ The interface used to provide custom implementation to provide access to external resources (such as linked files) from arbitrary locations. """
 def AreSameResources(self,reference1,reference2):
  """ AreSameResources(self: IExternalResourceServer,reference1: IDictionary[str,str],reference2: IDictionary[str,str]) -> bool """
  pass
 def GetIconPath(self):
  """
  GetIconPath(self: IExternalResourceServer) -> str
  
   Implement this method to return the path to an icon file which will be 
    displayed in Revit
     user interfaces associated to this server.
  
   Returns: The image file of the server.
  """
  pass
 def GetInformationLink(self):
  """
  GetInformationLink(self: IExternalResourceServer) -> str
  
   The method that Revit will invoke to obtain a URL address which provides more 
    information about the server.
  
   Returns: The URL providing server information.
  """
  pass
 def GetInSessionPath(self,reference,originalDisplayPath):
  """
  GetInSessionPath(self: IExternalResourceServer,reference: ExternalResourceReference,originalDisplayPath: str) -> str
  
   Implement this method to provide the path that should be used for display and 
    browsing to a given ExternalResourceReference
     during this Revit session.
  
  
   reference: The ExternalResourceReference for which Revit is requesting the in session 
    display path.
  
   originalDisplayPath: The path that was provided for the resource when the resource was originally 
    loaded into the model.
  
   Returns: The display path that should be used for this resource for this session of 
    Revit.
  """
  pass
 def GetResourceVersionStatus(self,reference):
  """
  GetResourceVersionStatus(self: IExternalResourceServer,reference: ExternalResourceReference) -> ResourceVersionStatus
  
   Implement this method to indicate whether the given version of a resource is 
    the most
     current version of the data.
  
  
   reference: The ExternalResourceReference to check.
   Returns: An enum indicating whether the resource is current,out of date,or of unknown 
    status.
  """
  pass
 def GetShortName(self):
  """
  GetShortName(self: IExternalResourceServer) -> str
  
   Implement this method to return the short name of the server.
   Returns: The short name of the server.
  """
  pass
 def GetTypeSpecificServerOperations(self,extensions):
  """
  GetTypeSpecificServerOperations(self: IExternalResourceServer,extensions: ExternalResourceServerExtensions)
   Implement this method to get operations supported by the external server for a 
    particular type of external resource.
  
  
   extensions: The class which owns sub-interface classes,each of which has methods related 
    to a particular type of external resource.
  """
  pass
 def IsResourceWellFormed(self,extRef):
  """
  IsResourceWellFormed(self: IExternalResourceServer,extRef: ExternalResourceReference) -> bool
  
   Implement this method to check whether the given ExternalResourceReference is 
    formatted
     correctly for this server.
  
  
   extRef: The ExternalResourceReference to check.
   Returns: True if the ExternalResourceReference represents a well-formed
     resource. 
    False otherwise.
  """
  pass
 def LoadResource(self,loadRequestId,resourceType,desiredResource,loadContext,loadResults):
  """
  LoadResource(self: IExternalResourceServer,loadRequestId: Guid,resourceType: ExternalResourceType,desiredResource: ExternalResourceReference,loadContext: ExternalResourceLoadContext,loadResults: ExternalResourceLoadContent)
   Implement this method to load the requested resource.
  
   loadRequestId: The id uniquely identifying the load request.
   resourceType: The type of resource requested.
   desiredResource: The specific resource that should be loaded.
   loadContext: A class containing info about the context of the load request.
   loadResults: The data returned by the server as a result of this load operation.
     Revit 
    will ensure that this argument is the appropriate subclass of 
    ExternalResourceLoadContent for the type of data.
  """
  pass
 def SetupBrowserData(self,browseData):
  """
  SetupBrowserData(self: IExternalResourceServer,browseData: ExternalResourceBrowserData)
   Implement this method to setup external resource browser data which will be 
    accessed in Revit external resource browser UI.
  
  
   browseData: The input context to match the external resources and browser results returned 
    by the server.
  """
  pass
 def SupportsExternalResourceType(self,type):
  """
  SupportsExternalResourceType(self: IExternalResourceServer,type: ExternalResourceType) -> bool
  
   Implement this method to indicate whether the server can provide data for a 
    specified type of external resource.
  
  
   type: The ExternalResourceType of interest to the caller.  For example,KeynoteTable 
    - to determine
     if the server provides data for Revit's keynote table.
  
   Returns: True if the server supports the specified type of external resource
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
