class KeyBasedTreeEntriesLoadResults(object,IDisposable):
 """
 This class contains the results and status information regarding an attempt to load the KeyBasedTreeEntries from an External Resource.
 
 KeyBasedTreeEntriesLoadResults()
 """
 def Dispose(self):
  """ Dispose(self: KeyBasedTreeEntriesLoadResults) """
  pass
 def GetFailureMessages(self):
  """
  GetFailureMessages(self: KeyBasedTreeEntriesLoadResults) -> IList[FailureMessage]
  
   Get all error or warnings created while attempting to load KeyBasedTreeEntries.
   Returns: A collection of FailureMessage objects,if any errors or warnings were 
    encountered while
     loading and building the KeyBasedTreeEntries.
  """
  pass
 def GetFileReadErrors(self):
  """
  GetFileReadErrors(self: KeyBasedTreeEntriesLoadResults) -> IList[str]
  
   Gets the names of any files which could not be read due to access errors.
   Returns: An array of strings containing the filenames of files which could not be read.
  """
  pass
 def GetFileSyntaxErrors(self):
  """
  GetFileSyntaxErrors(self: KeyBasedTreeEntriesLoadResults) -> IList[str]
  
   Gets all the records in the key-based tree data text file that could not be 
    parsed into KeyBasedTreeEntries.
  
   Returns: An array of strings that are copies of the records in the text file that could 
    not be parsed.
  """
  pass
 def GetKeyBasedTreeEntryErrors(self,type=None):
  """
  GetKeyBasedTreeEntryErrors(self: KeyBasedTreeEntriesLoadResults) -> IList[KeyBasedTreeEntryError]
  
   Gets information about KeyBasedTreeEntry objects that could not be included in 
    the KeyBasedTreeEntries
     object due to errors.
  
   Returns: An array of copies of the KeyBasedTreeEntryErrors contained in this object.
  GetKeyBasedTreeEntryErrors(self: KeyBasedTreeEntriesLoadResults,type: KeyBasedTreeEntryErrorType) -> IList[KeyBasedTreeEntryError]
  
   Gets information about specific KeyBasedTreeEntry objects that could not be 
    included in the KeyBasedTreeEntries
     object due to errors of a particular 
    type.
  
  
   type: The type of KeyBasedTreeEntryError to be returned.
   Returns: An array of copies of the KeyBasedTreeEntryErrors contained in this object 
    matching the type specified.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: KeyBasedTreeEntriesLoadResults,disposing: bool) """
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
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: KeyBasedTreeEntriesLoadResults) -> bool

"""


