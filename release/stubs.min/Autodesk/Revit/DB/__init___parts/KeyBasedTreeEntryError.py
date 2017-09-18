class KeyBasedTreeEntryError(object,IDisposable):
 """ This class contains information about a problem encountered while creating a KeyBasedTreeEntries object. """
 def Dispose(self):
  """ Dispose(self: KeyBasedTreeEntryError) """
  pass
 def GetEntry(self):
  """
  GetEntry(self: KeyBasedTreeEntryError) -> KeyBasedTreeEntry

  

   Gets the entry for which an error occurred while building the 

    KeyBasedTreeEntries object.

  

   Returns: A copy of the KeyBasedTreeEntry.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: KeyBasedTreeEntryError,disposing: bool) """
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
 ErrorType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates which of possible types of problems with loading and/or building

   a KeyBasedTreeEntries that this KeyBasedTreeEntryError represents.



Get: ErrorType(self: KeyBasedTreeEntryError) -> KeyBasedTreeEntryErrorType



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: KeyBasedTreeEntryError) -> bool



"""


