class ExternalResourceBrowserData(object,IDisposable):
 """
 Represents a collection of external resources and external resource folders to be presented as
    the content of a folder in the file browser in Revit.
 
 ExternalResourceBrowserData(document: Document,serverId: Guid,folderPath: str,matchOptions: ExternalResourceMatchOptions)
 """
 def AddResource(self,resourceName,*__args):
  """
  AddResource(self: ExternalResourceBrowserData,resourceName: str,referenceInformation: IDictionary[str,str])AddResource(self: ExternalResourceBrowserData,resourceName: str)
   Adds an external resource to the folder path by supplying the resource name.
  
   resourceName: The unique short name of external resource.
  AddResource(self: ExternalResourceBrowserData,resourceName: str,version: str,referenceInformation: IDictionary[str,str])AddResource(self: ExternalResourceBrowserData,resourceName: str,version: str)
   Adds an external resource to the folder path by supplying the resource name and 
    version.
  
  
   resourceName: The unique short name of external resource.
   version: The version of external resource.
  """
  pass
 def AddSubFolder(self,folderName):
  """
  AddSubFolder(self: ExternalResourceBrowserData,folderName: str)
   Adds a sub folder to the folder path with the given name.
  
   folderName: The name of the folder.
  """
  pass
 def CallingDocumentHasModelPath(self):
  """
  CallingDocumentHasModelPath(self: ExternalResourceBrowserData) -> bool
  
   Indicates whether the document requesting the external resource browser data 
    has a defined ModelPath.
  
   Returns: True if the document has a defined ModelPath.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ExternalResourceBrowserData) """
  pass
 def GetCallingDocumentModelPath(self):
  """
  GetCallingDocumentModelPath(self: ExternalResourceBrowserData) -> ModelPath
  
   Returns a copy of the ModelPath of the document that is requesting the external 
    resource browser data.
  
   Returns: A copy of the ModelPath of the document that is requesting the external 
    resource browser data.
  """
  pass
 def GetMatchOptions(self):
  """
  GetMatchOptions(self: ExternalResourceBrowserData) -> ExternalResourceMatchOptions
  
   Gets the match options used to filter external resources.
   Returns: The external resource match options.
  """
  pass
 def GetResources(self):
  """
  GetResources(self: ExternalResourceBrowserData) -> IList[ExternalResourceReference]
  
   Gets the external resources under the folder path of the browser data.
   Returns: The external resources under current folder of the browser data.
  """
  pass
 def GetSubFolders(self):
  """
  GetSubFolders(self: ExternalResourceBrowserData) -> IList[str]
  
   Gets the sub folders under the folder path of the browser data.
   Returns: The sub folders under folder path of the browser data.
  """
  pass
 def IsValidFolderName(self,folderName):
  """
  IsValidFolderName(self: ExternalResourceBrowserData,folderName: str) -> bool
  
   Checks whether the folder name is valid.
  
   folderName: The folder name to check.
   Returns: True if the name is a valid folder name,false otherwise.
  """
  pass
 def IsValidResouceName(self,resourceName):
  """
  IsValidResouceName(self: ExternalResourceBrowserData,resourceName: str) -> bool
  
   Checks whether the resource name is valid.
  
   resourceName: The resource name to check.
   Returns: True if the name is a valid resource name,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalResourceBrowserData,disposing: bool) """
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
 def __new__(self,document,serverId,folderPath,matchOptions):
  """ __new__(cls: type,document: Document,serverId: Guid,folderPath: str,matchOptions: ExternalResourceMatchOptions) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 FolderPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current folder path to which the new resources and sub folder belong.

Get: FolderPath(self: ExternalResourceBrowserData) -> str

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExternalResourceBrowserData) -> bool

"""

 ServerId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of IExternalResourceServer which handles the external resource load.

Get: ServerId(self: ExternalResourceBrowserData) -> Guid

"""


