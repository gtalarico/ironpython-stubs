class ExportLinetypeTable(object,IEnumerable[KeyValuePair[ExportLinetypeKey,ExportLinetypeInfo]],IEnumerable,IDisposable):
 """
 A table supporting a mapping of linetypes in Revit to linetype names that will be set

    in the target export format.

 

 ExportLinetypeTable()
 """
 def Add(self,exportLinetypeKey,exportLinetypeInfo):
  """
  Add(self: ExportLinetypeTable,exportLinetypeKey: ExportLinetypeKey,exportLinetypeInfo: ExportLinetypeInfo)

   Inserts a (key,info) pair into Export line type table.

  

   exportLinetypeKey: The export line type Key to be added.

   exportLinetypeInfo: The export line type info to be added.
  """
  pass
 def Clear(self):
  """
  Clear(self: ExportLinetypeTable)

   Removes all contents stored in Export line type table.
  """
  pass
 def ContainsKey(self,exportLinetypeKey):
  """
  ContainsKey(self: ExportLinetypeTable,exportLinetypeKey: ExportLinetypeKey) -> bool

  

   Checks whether a pattern key exists in the table.

  

   exportLinetypeKey: The export line type key.

   Returns: True if the line type exists in the table.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ExportLinetypeTable) """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ExportLinetypeTable) -> IEnumerator[KeyValuePair[ExportLinetypeKey,ExportLinetypeInfo]]

  

   Returns an enumerator that iterates through a collection.

   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def GetExportLinetypeInfo(self,exportLinetypeKey):
  """
  GetExportLinetypeInfo(self: ExportLinetypeTable,exportLinetypeKey: ExportLinetypeKey) -> ExportLinetypeInfo

  

   Gets a copy of the ExportLinetypeInfo corresponding to the given 

    ExportLinetypeKey.

  

  

   exportLinetypeKey: The export line type Key.

   Returns: Returns the line type info for this key.
  """
  pass
 def GetKeys(self):
  """
  GetKeys(self: ExportLinetypeTable) -> IList[ExportLinetypeKey]

  

   Gets all the keys stored in the map.

   Returns: The keys.
  """
  pass
 def GetLinetypeTableIterator(self):
  """
  GetLinetypeTableIterator(self: ExportLinetypeTable) -> ExportLinetypeTableIterator

  

   Returns a ExportLinetypeTableIterator that iterates through the collection.

   Returns: A ExportLinetypeTableIterator object that can be used to iterate through 

    key-value pairs in the collection.
  """
  pass
 def GetValues(self):
  """
  GetValues(self: ExportLinetypeTable) -> IList[ExportLinetypeInfo]

  

   Returns all the values stored in the map.

   Returns: The info.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExportLinetypeTable,disposing: bool) """
  pass
 def Remove(self,exportLinetypeKey):
  """
  Remove(self: ExportLinetypeTable,exportLinetypeKey: ExportLinetypeKey)

   Removes the pair (key,info) corresponding to the given ExportLinetypeKey.

  

   exportLinetypeKey: The export line type key
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[KeyValuePair[ExportLinetypeKey,ExportLinetypeInfo]](enumerable: IEnumerable[KeyValuePair[ExportLinetypeKey,ExportLinetypeInfo]],value: KeyValuePair[ExportLinetypeKey,ExportLinetypeInfo]) -> bool """
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



Get: Count(self: ExportLinetypeTable) -> int



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ExportLinetypeTable) -> bool



"""


