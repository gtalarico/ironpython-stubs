class ExternalResourceReference(object,IDisposable):
 """
 This class identifies an external resource provided by an IExternalResourceServer.

 

 ExternalResourceReference(other: ExternalResourceReference)

 ExternalResourceReference(serverId: Guid,referenceInformation: IDictionary[str,str],version: str,inSessionPath: str)
 """
 @staticmethod
 def CreateLocalResource(doc,resourceType,path,pathType):
  """
  CreateLocalResource(doc: Document,resourceType: ExternalResourceType,path: ModelPath,pathType: PathType) -> ExternalResourceReference

  

   Creates an ExternalResourceReference representing a local file managed

     by 

    Revit's built-in server.

  

  

   doc: The document containing the reference. If the PathType is relative,

     the 

    path will be made relative to the location of this Document. (If

     this 

    Document belongs to a workshared model,

     the reference will be relative to 

    the central model.)

  

   resourceType: The type of the external resource.

   path: A path to the external file. This path must be absolute. If the PathType is

     

    relative,then Revit will relativize the path according to the location

     of 

    the given Document.

  

   pathType: An enum indicating the type of path which the ExternalResourceReference should 

    use.

     The PathType must be PathType.Server if the reference is to a Revit 

    model on

     Revit Server. The PathType must be PathType.Absolute if the 

    reference is local

     but the host model or host's central model are on Revit 

    Server.

  

   Returns: The newly-created ExternalResourceReference.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ExternalResourceReference) """
  pass
 def GetReferenceInformation(self):
  """
  GetReferenceInformation(self: ExternalResourceReference) -> IDictionary[str,str]

  

   Returns a copy of an object containing previously-stored reference or lookup

    

     information about the specific resource provided by the server.

  

   Returns: A copy of a (String,String) map containing previously-stored reference or

     

    lookup information.
  """
  pass
 def GetResourceShortDisplayName(self):
  """
  GetResourceShortDisplayName(self: ExternalResourceReference) -> str

  

   Gets the short display name of the external resource.

   Returns: The short display name of the external resource.
  """
  pass
 def GetResourceVersionStatus(self):
  """
  GetResourceVersionStatus(self: ExternalResourceReference) -> ResourceVersionStatus

  

   Checks whether this ExternalResourceReference corresponds to the current 

    version of the resource.

  

   Returns: An enum indicating whether this reference represents the most recent version

    

     of the resource.
  """
  pass
 def HasValidDisplayPath(self):
  """
  HasValidDisplayPath(self: ExternalResourceReference) -> bool

  

   Checks whether this external Resource has a valid display path.

   Returns: True if the this external Resource has a valid display path. False otherwise.
  """
  pass
 def IsValidReference(self,resourceType):
  """
  IsValidReference(self: ExternalResourceReference,resourceType: ExternalResourceType) -> bool

  

   Checks whether the reference is in a valid format.

  

   resourceType: The type of resource which the ExternalResourceReference should

     correspond 

    to.

  

   Returns: True if this is a valid ExternalResourceReference. False otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalResourceReference,disposing: bool) """
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
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,other: ExternalResourceReference)

  __new__(cls: type,serverId: Guid,referenceInformation: IDictionary[str,str],version: str,inSessionPath: str)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 InSessionPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The path stores the full display path which includes the server name plus the path provided by ExternalResourceServer.The path that Revit will present for user recognizing and browsing to this resource during one session of Revit.This property allows ExternalResourceServers to handle cases where the path to a resource may vary between Revit sessions.

   For example,if this ExternalResourceReference refers to a resource in a folder,

   this property can be used to store the current path of the resource. If the resource is moved to another folder later,

   the ExternalResourceServer could calculate the correct path for the resource from resource identification information

   when it is loaded and store it in this property,

   so that it will work correctly even if the rvt file is opened in a different location.



Get: InSessionPath(self: ExternalResourceReference) -> str



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ExternalResourceReference) -> bool



"""

 ServerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the server that Revit is expecting to provide the external resource.



Get: ServerId(self: ExternalResourceReference) -> Guid



"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The version of the external data that was most recently loaded in Revit.



Get: Version(self: ExternalResourceReference) -> str



"""


