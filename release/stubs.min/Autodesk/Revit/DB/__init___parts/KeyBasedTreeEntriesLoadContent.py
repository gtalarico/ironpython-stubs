class KeyBasedTreeEntriesLoadContent(ExternalResourceLoadContent,IDisposable):
 """
 This class is used by IExternalResourceServers to return KeyBasedTreeEntries data to Revit when their

    LoadResource method is invoked.
 """
 def AddEntry(self,entry):
  """
  AddEntry(self: KeyBasedTreeEntriesLoadContent,entry: KeyBasedTreeEntry) -> bool

  

   Adds one KeyBasedTreeEntry to this KeyBasedTreeEntriesLoadContent,which is 

    used to build a KeyBasedTreeEntries object by BuildEntries function.

  

  

   entry: The entry to be added.

   Returns: Returns true if an entry is added into the entry data set successfully,

     

    returns false if an entry fails to be added because this entry is invalid or a 

    duplicate

     of one in the entry data set.
  """
  pass
 def BuildEntries(self):
  """
  BuildEntries(self: KeyBasedTreeEntriesLoadContent)

   Builds a KeyBasedTreeEntries object.
  """
  pass
 def CanAddEntry(self,entry):
  """
  CanAddEntry(self: KeyBasedTreeEntriesLoadContent,entry: KeyBasedTreeEntry) -> bool

  

   Verifies if the KeyBasedTreeEntry could be added in this 

    KeyBasedTreeEntriesLoadContent.

  

  

   entry: The KeyBasedTreeEntry object to be checked.

   Returns: True if the KeyBasedTreeEntry could be added in,otherwise false.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ExternalResourceLoadContent,A_0: bool) """
  pass
 def GetEntries(self):
  """
  GetEntries(self: KeyBasedTreeEntriesLoadContent) -> KeyBasedTreeEntries

  

   Gets a copy of KeyBasedTreeEntries object owned by this 

    KeyBasedTreeEntriesLoadContent object.

  

   Returns: A copy of KeyBasedTreeEntries object owned by this 

    KeyBasedTreeEntriesLoadContent object.
  """
  pass
 def GetLoadResults(self):
  """
  GetLoadResults(self: KeyBasedTreeEntriesLoadContent) -> KeyBasedTreeEntriesLoadResults

  

   Returns a copy of the KeyBasedTreeEntriesLoadResults owned by this 

    KeyBasedTreeEntriesLoadContent object.

  

   Returns: A copy of a KeyBasedTreeEntriesLoadResults owned by this 

    KeyBasedTreeEntriesLoadContent object.
  """
  pass
 @staticmethod
 def IsEntriesBuilt(content):
  """
  IsEntriesBuilt(content: KeyBasedTreeEntriesLoadContent) -> bool

  

   Verifies that the KeyBasedTreeEntries object owned by a 

    KeyBasedTreeEntriesLoadContent object is built.

  

  

   content: The KeyBasedTreeEntriesLoadContent object to be checked.

   Returns: True if the KeyBasedTreeEntries object is built already,otherwise false.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExternalResourceLoadContent,disposing: bool) """
  pass
 def Reset(self):
  """
  Reset(self: KeyBasedTreeEntriesLoadContent)

   Clears KeyBasedTreeEntriesLoadContent object,including KeyBasedTreeEntries and 

    KeyBasedTreeEntriesLoadResults,owned by this KeyBasedTreeEntriesLoadContent 

    object.
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
