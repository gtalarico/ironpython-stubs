class RevitLinkType(ElementType,IDisposable):
 """
 This class represents another Revit Document ("link") brought into
    the current one ("host").
 """
 @staticmethod
 def Create(document,*__args):
  """
  Create(document: Document,path: ModelPath,options: RevitLinkOptions) -> RevitLinkLoadResult
  
   Creates a new Revit link type and loads the linked document.
  
   document: The document in which to create the Revit link.
   path: The path of the link to load. This may be a server path.
     This must be a 
    full path.
  
   options: An options class for loading Revit links.
   Returns: An object containing the results of creating and loading
     the Revit link 
    type. It contains the ElementId of the new link.
  
  Create(document: Document,resourceReference: ExternalResourceReference,options: RevitLinkOptions) -> RevitLinkLoadResult
  
   Creates a new Revit link type from an external resource reference and loads the
    
     linked document.
  
  
   document: The document in which to create the Revit link.
   resourceReference: An external resource reference describing the source of the linked Revit 
    document.
  
   options: An options class for loading Revit links.  The path type information will be 
    ignored.
  
   Returns: An object containing the results of creating and loading
     the Revit link 
    type. It contains the ElementId of the new link.
  """
  pass
 @staticmethod
 def CreateFromIFC(document,ifcFilePath,revitLinkedFilePath,recreateLink,options):
  """
  CreateFromIFC(document: Document,ifcFilePath: str,revitLinkedFilePath: str,recreateLink: bool,options: RevitLinkOptions) -> RevitLinkLoadResult
  
   Creates a new Revit link type from an existing Revit file created via import by 
    reference
     of an asscoiated IFC file.
  
  
   document: The document in which to create the Revit link.
   ifcFilePath: The path of the associated IFC file. This must be a full path.
   revitLinkedFilePath: The path of the existing Revit file that contains elements created via an 
    import by reference operation.
     This must be a full path.
  
   recreateLink: If true,the existing Revit file created via an import by reference operation
   
      will be updated based on the information in the IFC file.  If false,the 
    existing Revit file will be used as-is.
  
   options: An options class for loading Revit links.
   Returns: An object containing the results of creating and loading
     the Revit link 
    type. It contains the ElementId of the new link.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetChildIds(self):
  """
  GetChildIds(self: RevitLinkType) -> ICollection[ElementId]
  
   Gets the ids of the immediate children of this link.
   Returns: The element ids of all links which are linked directly into this one
     
    (immediate children)
  """
  pass
 def GetConversionData(self):
  """
  GetConversionData(self: RevitLinkType) -> LinkConversionData
  
   Returns the optional data that is necessary to generate the Revit file for this 
    link.
  
   Returns: The RvtLinkConversionData containing the necessary information.
  """
  pass
 def GetParentId(self):
  """
  GetParentId(self: RevitLinkType) -> ElementId
  
   Gets the id of this link's immediate parent.
   Returns: The id of the immediate parent of this link,or invalidElementId if
     this 
    link is a top-level link.
  """
  pass
 def GetRootId(self):
  """
  GetRootId(self: RevitLinkType) -> ElementId
  
   Gets the id of the top-level link which this link is linked into.
   Returns: The id of the top-level link which this link is ultimately linked under,
     or 
    invalidElementId if this link is a top-level link.
  """
  pass
 @staticmethod
 def GetTopLevelLink(document,*__args):
  """
  GetTopLevelLink(document: Document,path: ModelPath) -> ElementId
  
   Returns the ElementId of the (top-level) linked model with the given path.
  
   document: The document to look for the linked model in.
   path: A path indicating which linked model to return.
   Returns: The id of the link with the given path,or InvalidElementId if
     there is no 
    top-level link at that path.
  
  GetTopLevelLink(document: Document,reference: ExternalResourceReference) -> ElementId
  
   Returns the ElementId of the (top-level) linked model with the given
     
    ExternalResourceReference.
  
  
   document: The document to look for the linked model in.
   reference: An ExternalResourceReference indicating which linked model to return.
   Returns: The id of the link with the given ExternalResourceReference,
     or 
    InvalidElementId if
     there is no top-level link at that location.
  """
  pass
 def HasSaveablePositions(self):
  """
  HasSaveablePositions(self: RevitLinkType) -> bool
  
   Determines whether the link has changes to shared positioning that could
     be 
    saved.
  
   Returns: True if the link has shared positioning changes which can be saved.
     False 
    if there are no changes to shared coordinates,or if the changes
     cannot be 
    saved.
  """
  pass
 def IsFromLocalPath(self):
  """
  IsFromLocalPath(self: RevitLinkType) -> bool
  
   Checks whether the Revit link uses a local path,such as a hard drive.
   Returns: Returns true if the Revit link is from a local drive.
  """
  pass
 def IsFromRevitServer(self):
  """
  IsFromRevitServer(self: RevitLinkType) -> bool
  
   Checks whether the Revit link is located on Revit Server.
   Returns: Returns true if the Revit link is located on Revit Server.
  """
  pass
 @staticmethod
 def IsLoaded(document,typeId):
  """
  IsLoaded(document: Document,typeId: ElementId) -> bool
  
   Checks whether the link with this id is loaded.
  
   document: A document. Revit will see if typeId corresponds to a loaded link in this 
    document.
  
   typeId: An element id. Revit will check if typeId corresponds to a loaded link in the 
    given document.
  
   Returns: True if typeId corresponds to a loaded RevitLinkType. False otherwise.
  """
  pass
 def IsNotLoadedIntoMultipleOpenDocuments(self):
  """
  IsNotLoadedIntoMultipleOpenDocuments(self: RevitLinkType) -> bool
  
   Checks whether the link is loaded into more than one open document
     in this 
    session of Revit. If the link is loaded into multiple open
     documents,
    reload will be disabled.
  
   Returns: True if the link is loaded into at most one open document. False if the link
    
     is loaded into more than one open document.
  """
  pass
 def Load(self):
  """
  Load(self: RevitLinkType) -> RevitLinkLoadResult
  
   Loads or reloads the Revit link from its
     currently-stored location. If the 
    link is an
     external resource,Revit will contact the
     
    IExternalResourceServer to get the latest version
     of the link.
  
   Returns: An object containing the ElementId of the link
     and an enum value indicating 
    any
     errors which occurred while trying to load.
     
    RevitLinkLoadResultType.LinkLoaded indicates
     success.
  """
  pass
 def LoadFrom(self,*__args):
  """
  LoadFrom(self: RevitLinkType,resourceReference: ExternalResourceReference,config: WorksetConfiguration) -> RevitLinkLoadResult
  
   Loads or reloads the Revit link.
     The link will be loaded from the location 
    given in the
     input ExternalResourceReference.
  
  
   resourceReference: An external resource reference describing the source of the linked Revit 
    document.
  
   config: A WorksetConfiguration object indicating which worksets in the
     link to 
    open.If you want to load the same set of worksets the link previously
     had,
    leave this argument as ll.
  
   Returns: An object containing the ElementId of the link
     and an enum value indicating 
    any errors
     which occurred while trying to load.
  
  LoadFrom(self: RevitLinkType,path: ModelPath,config: WorksetConfiguration) -> RevitLinkLoadResult
  
   Loads or reloads the Revit link from disk.
     The link will be loaded from the 
    input path.
  
  
   path: A ModelPath indicating where to load the link from.
     This must be an 
    absolute path.
  
   config: A WorksetConfiguration object indicating which worksets in the
     link to 
    open.If you want to load the same set of worksets the link previously
     had,
    leave this argument as ll.
  
   Returns: An object containing the ElementId of the link
     and an enum value indicating 
    any errors
     which occurred while trying to load.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def Reload(self):
  """
  Reload(self: RevitLinkType) -> RevitLinkLoadResult
  
   Loads or reloads the Revit link from its
     currently-stored location. If the 
    link is an
     external resource,Revit will contact the
     
    IExternalResourceServer to get the latest version
     of the link.
  
   Returns: An object containing the ElementId of the link
     and an enum value indicating 
    any
     errors which occurred while trying to load.
     
    RevitLinkLoadResultType.LinkLoaded indicates
     success.
  """
  pass
 def RevertLocalUnloadStatus(self):
  """
  RevertLocalUnloadStatus(self: RevitLinkType) -> LinkedFileStatus
  
   Restores the workshared load status of a link that has been unloaded only for 
    the current user,
     in a local copy of a workshared model.
  
   Returns: The link's LinkedFileStatus that has resulted from reverting the local unloaded 
    status.
  """
  pass
 def SavePositions(self,callback):
  """
  SavePositions(self: RevitLinkType,callback: ISaveSharedCoordinatesCallback) -> bool
  
   Saves shared coordinates changes back to the linked document.
  
   callback: A callback object to resolve situations when Revit encounters
     modified 
    links.
  
   Returns: True if we saved the link or if there were no changes to save.
     False if the 
    operation failed.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def Unload(self,callback):
  """
  Unload(self: RevitLinkType,callback: ISaveSharedCoordinatesCallback)
   Unloads the Revit link.
  
   callback: A callback indicating what to do if Revit encounters
     links which have 
    changes in shared coordinates.
     If ll,Revit will not save any shared 
    coordinates
     changes to the link before unloading.
  """
  pass
 def UnloadLocally(self,callback):
  """
  UnloadLocally(self: RevitLinkType,callback: ISaveSharedCoordinatesCallbackForUnloadLocally) -> bool
  
   Unloads a Revit link for the current user only.
  
   callback: A callback indicating what to do if Revit encounters
     links which have 
    changes in shared coordinates. The saving options for
     unloading locally  
    only could be: save the link,not save the link.
     If ll,Revit will not save 
    any shared coordinates
     changes to the link before unloading.
  
   Returns: Returns true if the attempt to unload the link locally was successful.
  """
  pass
 def UpdateFromIFC(self,document,ifcFilePath,revitLinkedFilePath,recreateLink):
  """
  UpdateFromIFC(self: RevitLinkType,document: Document,ifcFilePath: str,revitLinkedFilePath: str,recreateLink: bool) -> bool
  
   Updates a Revit link type from an IFC file and loads the linked document.
  
   document: The document that contains Revit link.
   ifcFilePath: The path of the IFC link to load. This must be a full path.
   revitLinkedFilePath: The path of the Revit file to create to hold the IFC information. This must be 
    a full path.
  
   recreateLink: If true,the Revit file will be updated based on the information in the IFC 
    file.  If false,the existing Revit file will be used.
  
   Returns: Returns true if the update succeeded,false otherwise.
  """
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
 AttachmentType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The attachment/overlay status of this link.

Get: AttachmentType(self: RevitLinkType) -> AttachmentType

Set: AttachmentType(self: RevitLinkType)=value
"""

 IsNestedLink=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether this link is a nested or top-level link.

Get: IsNestedLink(self: RevitLinkType) -> bool

"""

 LocallyUnloaded=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Checks whether a Revit link in a local model is unloaded
   only for the current user.

Get: LocallyUnloaded(self: RevitLinkType) -> bool

"""

 PathType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of path the link uses.

Get: PathType(self: RevitLinkType) -> PathType

Set: PathType(self: RevitLinkType)=value
"""


