class UCOMIPersistFile:
 """ Use System.Runtime.InteropServices.ComTypes.IPersistFile instead. """
 def GetClassID(self,pClassID):
  """
  GetClassID(self: UCOMIPersistFile) -> Guid

  

   Retrieves the class identifier (CLSID) of an object.
  """
  pass
 def GetCurFile(self,ppszFileName):
  """
  GetCurFile(self: UCOMIPersistFile) -> str

  

   Retrieves either the absolute path to current working file of the object,or if there is no 

    current working file,the default filename prompt of the object.
  """
  pass
 def IsDirty(self):
  """
  IsDirty(self: UCOMIPersistFile) -> int

  

   Checks an object for changes since it was last saved to its current file.

   Returns: S_OK if the file has changed since it was last saved; S_FALSE if the file has not changed since 

    it was last saved.
  """
  pass
 def Load(self,pszFileName,dwMode):
  """
  Load(self: UCOMIPersistFile,pszFileName: str,dwMode: int)

   Opens the specified file and initializes an object from the file contents.

  

   pszFileName: A zero-terminated string containing the absolute path of the file to open.

   dwMode: A combination of values from the STGM enumeration to indicate the access mode in which to open 

    pszFileName.
  """
  pass
 def Save(self,pszFileName,fRemember):
  """
  Save(self: UCOMIPersistFile,pszFileName: str,fRemember: bool)

   Saves a copy of the object into the specified file.

  

   pszFileName: A zero-terminated string containing the absolute path of the file to which the object is saved.

   fRemember: Indicates whether pszFileName is to be used as the current working file.
  """
  pass
 def SaveCompleted(self,pszFileName):
  """
  SaveCompleted(self: UCOMIPersistFile,pszFileName: str)

   Notifies the object that it can write to its file.

  

   pszFileName: The absolute path of the file where the object was previously saved.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
