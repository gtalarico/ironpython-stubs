class ExportLineweightTable(object,IEnumerable[KeyValuePair[ExportLineweightKey,ExportLineweightInfo]],IEnumerable,IDisposable):
 """
 A table supporting a mapping of line weights in Revit to line weight names that will be set
    in the target export format.
 
 ExportLineweightTable()
 """
 def Add(self,exportLineweightKey,exportLineweightInfo):
  """
  Add(self: ExportLineweightTable,exportLineweightKey: ExportLineweightKey,exportLineweightInfo: ExportLineweightInfo)
   Inserts a (key,info) pair into Export line weight table.
  
   exportLineweightKey: The export line weight Key to be added.
   exportLineweightInfo: The export line weight info to be added.
  """
  pass
 def Clear(self):
  """
  Clear(self: ExportLineweightTable)
   Removes all contents stored in Export line weight table.
  """
  pass
 def ContainsKey(self,exportLineweightKey):
  """
  ContainsKey(self: ExportLineweightTable,exportLineweightKey: ExportLineweightKey) -> bool
  
   Checks whether a line weight key exists in the table.
  
   exportLineweightKey: The export line weight key.
   Returns: True if the line weight exists in the table.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ExportLineweightTable) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ExportLineweightTable) -> IEnumerator[KeyValuePair[ExportLineweightKey,ExportLineweightInfo]]
  
   Returns an enumerator that iterates through a collection.
   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def GetExportLineweightInfo(self,exportLineweightKey):
  """
  GetExportLineweightInfo(self: ExportLineweightTable,exportLineweightKey: ExportLineweightKey) -> ExportLineweightInfo
  
   Gets a copy of the ExportLineweightInfo corresponding to the given 
    ExportLineweightKey.
  
  
   exportLineweightKey: The export line weight Key.
   Returns: Returns the line weight info for this key.
  """
  pass
 def GetKeys(self):
  """
  GetKeys(self: ExportLineweightTable) -> IList[ExportLineweightKey]
  
   Gets all the keys stored in the map.
   Returns: The keys.
  """
  pass
 def GetLineweightTableIterator(self):
  """
  GetLineweightTableIterator(self: ExportLineweightTable) -> ExportLineweightTableIterator
  
   Returns a ExportLineweightTableIterator that iterates through the collection.
   Returns: A ExportLineweightTableIterator object that can be used to iterate through 
    key-value pairs in the collection.
  """
  pass
 def GetValues(self):
  """
  GetValues(self: ExportLineweightTable) -> IList[ExportLineweightInfo]
  
   Returns all the values stored in the map.
   Returns: The info.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExportLineweightTable,disposing: bool) """
  pass
 def Remove(self,exportLineweightKey):
  """
  Remove(self: ExportLineweightTable,exportLineweightKey: ExportLineweightKey)
   Removes the pair (key,info) corresponding to the given ExportLineweightKey.
  
   exportLineweightKey: The export line weight key
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[KeyValuePair[ExportLineweightKey,ExportLineweightInfo]](enumerable: IEnumerable[KeyValuePair[ExportLineweightKey,ExportLineweightInfo]],value: KeyValuePair[ExportLineweightKey,ExportLineweightInfo]) -> bool """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Count of the items contained in the collection.

Get: Count(self: ExportLineweightTable) -> int

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportLineweightTable) -> bool

"""


