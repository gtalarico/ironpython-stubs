class ClassificationEntry(KeyBasedTreeEntry,IDisposable):
 """
 Represents an entry in the classification table.
 
 ClassificationEntry(key: str,parentKey: str,description: str,level: int,categoryId: ElementId)
 """
 def Dispose(self):
  """ Dispose(self: KeyBasedTreeEntry,A_0: bool) """
  pass
 def HasBadCategoryId(self):
  """
  HasBadCategoryId(self: ClassificationEntry) -> bool
  
   Checks if the category id is Revit BuiltInCategory id.
   Returns: True if the category id is not Revit BuiltInCategory id.
     False otherwise.
  """
  pass
 def HasBadLevel(self):
  """
  HasBadLevel(self: ClassificationEntry) -> bool
  
   Checks if the level is an integer in range between 1 and 5 inclusive.
   Returns: True if the level is not an integer from 1 to 5 inclusive. False otherwise.
  """
  pass
 def HasInvalidKey(self):
  """
  HasInvalidKey(self: ClassificationEntry) -> bool
  
   Checks if the key matches the level and parent key.
   Returns: True if the key doesn't matach the level and parent key.
     False otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: KeyBasedTreeEntry,disposing: bool) """
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
 def __new__(self,key,parentKey,description,level,categoryId):
  """ __new__(cls: type,key: str,parentKey: str,description: str,level: int,categoryId: ElementId) """
  pass
 CategoryId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the category associated with this entry.

Get: CategoryId(self: ClassificationEntry) -> ElementId

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The description associated with this entry.

Get: Description(self: ClassificationEntry) -> str

"""

 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The entry level in the classification table. The expected range is between 1 and 5 inclusive.

Get: Level(self: ClassificationEntry) -> int

"""


