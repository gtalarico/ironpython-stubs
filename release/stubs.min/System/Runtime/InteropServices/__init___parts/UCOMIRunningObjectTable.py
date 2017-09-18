class UCOMIRunningObjectTable:
 """ Use System.Runtime.InteropServices.ComTypes.IRunningObjectTable instead. """
 def EnumRunning(self,ppenumMoniker):
  """
  EnumRunning(self: UCOMIRunningObjectTable) -> UCOMIEnumMoniker

  

   Enumerates the objects currently registered as running.
  """
  pass
 def GetObject(self,pmkObjectName,ppunkObject):
  """
  GetObject(self: UCOMIRunningObjectTable,pmkObjectName: UCOMIMoniker) -> object

  

   Returns the registered object if the supplied object name is registered as running.

  

   pmkObjectName: Reference to the moniker to search for in the ROT.
  """
  pass
 def GetTimeOfLastChange(self,pmkObjectName,pfiletime):
  """
  GetTimeOfLastChange(self: UCOMIRunningObjectTable,pmkObjectName: UCOMIMoniker) -> FILETIME

  

   Searches for this moniker in the ROT and reports the recorded time of change,if present.

  

   pmkObjectName: Reference to the moniker to search for in the ROT.
  """
  pass
 def IsRunning(self,pmkObjectName):
  """
  IsRunning(self: UCOMIRunningObjectTable,pmkObjectName: UCOMIMoniker)

   Determines if the specified moniker is currently registered in the Running Object Table.

  

   pmkObjectName: Reference to the moniker to search for in the Running Object Table.
  """
  pass
 def NoteChangeTime(self,dwRegister,pfiletime):
  """
  NoteChangeTime(self: UCOMIRunningObjectTable,dwRegister: int,pfiletime: FILETIME) -> FILETIME

  

   Makes a note of the time that a particular object has changed so IMoniker::GetTimeOfLastChange 

    can report an appropriate change time.

  

  

   dwRegister: The ROT entry of the changed object.

   pfiletime: Reference to the object's last change time.
  """
  pass
 def Register(self,grfFlags,punkObject,pmkObjectName,pdwRegister):
  """
  Register(self: UCOMIRunningObjectTable,grfFlags: int,punkObject: object,pmkObjectName: UCOMIMoniker) -> int

  

   Registers that the supplied object has entered the running state.

  

   grfFlags: Specifies whether the Running Object Table's (ROT) reference to punkObject is weak or strong,

    and controls access to the object through its entry in the ROT.

  

   punkObject: Reference to the object being registered as running.

   pmkObjectName: Reference to the moniker that identifies punkObject.
  """
  pass
 def Revoke(self,dwRegister):
  """
  Revoke(self: UCOMIRunningObjectTable,dwRegister: int)

   Unregisters the specified object from the ROT.

  

   dwRegister: The ROT entry to revoke.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
