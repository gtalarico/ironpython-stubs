class WorksharingDisplaySettings(Element,IDisposable):
 """
 WorksharingDisplaySettings controls how elements will appear when they are

    displayed in any of the worksharing display modes.
 """
 def CanUserHaveOverrides(self,username):
  """
  CanUserHaveOverrides(self: WorksharingDisplaySettings,username: str) -> bool

  

   Checks whether a single username can have customized graphic overrides.

  

   username: The username to check.

   Returns: False if the username is on the list of removed users,True otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAllUsersWithGraphicOverrides(self):
  """
  GetAllUsersWithGraphicOverrides(self: WorksharingDisplaySettings) -> ICollection[str]

  

   Returns all usernames that have graphic overrides.  This list consists of

     

    all users included in the user table + all users who have explicitly been

     

    assigned overrides.

  

   Returns: All usernames that have been assigned graphic overrides.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetGraphicOverrides(self,*__args):
  """
  GetGraphicOverrides(self: WorksharingDisplaySettings,statusInCentral: ModelUpdatesStatus) -> WorksharingDisplayGraphicSettings

  

   Returns the graphic overrides assigned to a particular model update status.

  

   statusInCentral: The model update status of interest.

   Returns: Returns the graphic overrides assigned to the model update status.

  GetGraphicOverrides(self: WorksharingDisplaySettings,ownershipStatus: CheckoutStatus) -> WorksharingDisplayGraphicSettings

  

   Returns the graphic overrides associated with a particular ownership status.

  

   ownershipStatus: The ownership status of interest.

   Returns: Returns the graphic overrides assigned to a particular ownership status.

  GetGraphicOverrides(self: WorksharingDisplaySettings,worksetId: WorksetId) -> WorksharingDisplayGraphicSettings

  

   Returns the graphic overrides assigned to elements in a particular workset.

  

   worksetId: The workset id of interest.  This must be a user workset.

   Returns: Returns the graphic overrides assigned to the workset.

  GetGraphicOverrides(self: WorksharingDisplaySettings,username: str) -> WorksharingDisplayGraphicSettings

  

   Returns the graphic overrides assigned for elements owned by a particular user.

  

   username: The username of a particular user.

   Returns: The graphic overrides assigned to this user.
  """
  pass
 @staticmethod
 def GetOrCreateWorksharingDisplaySettings(doc):
  """
  GetOrCreateWorksharingDisplaySettings(doc: Document) -> WorksharingDisplaySettings

  

   Returns the worksharing display settings for the document,creating

     new 

    settings for the current user if necessary.

  

  

   doc: The document of interest.

   Returns: The worksharing display settings for the document.
  """
  pass
 def GetRemovedUsers(self):
  """
  GetRemovedUsers(self: WorksharingDisplaySettings) -> ICollection[str]

  

   Returns the set of users who have been explicitly removed from the settings.

   Returns: Users who have been explicitly removed from the list.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RemoveUsers(self,document,usersToRemove,usersActuallyRemoved):
  """ RemoveUsers(self: WorksharingDisplaySettings,document: Document,usersToRemove: ICollection[str]) -> ICollection[str] """
  pass
 def RestoreUsers(self,usersToRestore):
  """ RestoreUsers(self: WorksharingDisplaySettings,usersToRestore: ICollection[str]) -> int """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def SetGraphicOverrides(self,*__args):
  """
  SetGraphicOverrides(self: WorksharingDisplaySettings,status: ModelUpdatesStatus,overrides: WorksharingDisplayGraphicSettings)

   Sets the graphic overrides assigned to elements with a particular status in the 

    central model.

  

  

   status: The status in the central model.

   overrides: The desired graphic overrides for this status.

  SetGraphicOverrides(self: WorksharingDisplaySettings,username: str,overrides: WorksharingDisplayGraphicSettings)

   Sets the graphic overrides assigned to elements owned by a particular user.

     

    The username cannot be on the list of removed usernames.

  

  

   username: The username of the desired user.

   overrides: The desired graphic overrides for this user.

  SetGraphicOverrides(self: WorksharingDisplaySettings,worksetId: WorksetId,overrides: WorksharingDisplayGraphicSettings)

   Sets the graphic overrides assigned to elements in a particular user workset.

  

   worksetId: The workset of interest,which must be a user workset.

   overrides: The desired graphic overrides for this workset.

  SetGraphicOverrides(self: WorksharingDisplaySettings,status: CheckoutStatus,overrides: WorksharingDisplayGraphicSettings)

   Sets the graphic overrides assigned to elements with a particular ownership 

    status.

  

  

   status: The ownership status of interest.

   overrides: The desired graphic overrides for this ownership status.
  """
  pass
 def UserHasGraphicOverrides(self,username):
  """
  UserHasGraphicOverrides(self: WorksharingDisplaySettings,username: str) -> bool

  

   Checks whether there are graphic overrides that would apply to elements

     

    owned by the given user in the "Individual Owners" display mode.

  

  

   username: The username to check

   Returns: True if there are graphic overrides assigned to the username,false otherwise.
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
