class WorksetTable(object,IDisposable):
 """ A table containing references to all the worksets contained in a document. """
 def Dispose(self):
  """ Dispose(self: WorksetTable) """
  pass
 def GetActiveWorksetId(self):
  """
  GetActiveWorksetId(self: WorksetTable) -> WorksetId
  
   Returns the active workset's WorksetId.
   Returns: WorksetId of the active workset.
  """
  pass
 def GetWorkset(self,*__args):
  """
  GetWorkset(self: WorksetTable,id: WorksetId) -> Workset
  
   Returns the workset from a input WorksetId.
  
   id: Id of a workset.
   Returns: The returned workset. ll if there is no workset in this table with this Id.
  GetWorkset(self: WorksetTable,guid: Guid) -> Workset
  
   Returns the workset from a input Guid.
  
   guid: Guid of the workset.
   Returns: The returned workset. ll if there is no workset in this table with this Id.
  """
  pass
 @staticmethod
 def IsWorksetNameUnique(aDoc,name):
  """
  IsWorksetNameUnique(aDoc: Document,name: str) -> bool
  
   Checks if the given workset name is unique in the document.
  
   aDoc: The document in which the workset is accessed.
   name: The workset name.
   Returns: True if this given workset name is unique in the document,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: WorksetTable,disposing: bool) """
  pass
 @staticmethod
 def RenameWorkset(aDoc,worksetId,name):
  """
  RenameWorkset(aDoc: Document,worksetId: WorksetId,name: str)
   Renames the workset.
  
   aDoc: The document in which the workset is accessed.
   worksetId: The workset Id.
   name: The workset name.
  """
  pass
 def SetActiveWorksetId(self,worksetId):
  """
  SetActiveWorksetId(self: WorksetTable,worksetId: WorksetId)
   Sets the active workset.
  
   worksetId: The workset Id.
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: WorksetTable) -> bool

"""


