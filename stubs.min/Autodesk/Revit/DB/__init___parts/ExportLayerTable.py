class ExportLayerTable(object,IEnumerable[KeyValuePair[ExportLayerKey,ExportLayerInfo]],IEnumerable,IDisposable):
 """
 A table supporting a mapping of category and subcategory to layer name and other layer properties that will be set
    in the target export format.
 
 ExportLayerTable()
 """
 def Add(self,exportLayerKey,exportLayerInfo):
  """
  Add(self: ExportLayerTable,exportLayerKey: ExportLayerKey,exportLayerInfo: ExportLayerInfo)
   Inserts a (key,info) pair into Export layer table.
  
   exportLayerKey: The export layer key to be added.
   exportLayerInfo: The export layer info to be added.
  """
  pass
 def Clear(self):
  """
  Clear(self: ExportLayerTable)
   Removes all contents stored in the table.
  """
  pass
 def ContainsKey(self,exportlayerKey):
  """
  ContainsKey(self: ExportLayerTable,exportlayerKey: ExportLayerKey) -> bool
  
   Checks whether a layer key exists in the table.
  
   exportlayerKey: The export layer Key.
   Returns: True if the layer key exists in the table.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ExportLayerTable) """
  pass
 @staticmethod
 def GetAvaliableLayerModifierTypes(document,exportLayerKey):
  """
  GetAvaliableLayerModifierTypes(document: Document,exportLayerKey: ExportLayerKey) -> IList[ModifierType]
  
   Gets all the avaliable layer modifier types for the layer key.
  
   document: A Revit document to retrieve avaliable layer modifier types from.
   exportLayerKey: The export layer key to specify wich category and subCategory will be used to 
    get the layer modifier types.
  
   Returns: The layer modifier types.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ExportLayerTable) -> IEnumerator[KeyValuePair[ExportLayerKey,ExportLayerInfo]]
  
   Returns an enumerator that iterates through a collection.
   Returns: An IEnumerator object that can be used to iterate through the collection.
  """
  pass
 def GetExportLayerInfo(self,exportLayerKey):
  """
  GetExportLayerInfo(self: ExportLayerTable,exportLayerKey: ExportLayerKey) -> ExportLayerInfo
  
   Gets a copy of the layer info associated to the input pattern key.
  
   exportLayerKey: The export layer Key.
   Returns: Return the layerInfo for this key.
  """
  pass
 def GetKeys(self):
  """
  GetKeys(self: ExportLayerTable) -> IList[ExportLayerKey]
  
   Gets all the keys stored in the map.
   Returns: Return the key array.
  """
  pass
 def GetLayerTableIterator(self):
  """
  GetLayerTableIterator(self: ExportLayerTable) -> ExportLayerTableIterator
  
   Returns a LayerTableIterator that iterates through the collection.
   Returns: A LayerTableIterator object that can be used to iterate through key-value pairs 
    in the collection.
  """
  pass
 def GetValues(self):
  """
  GetValues(self: ExportLayerTable) -> IList[ExportLayerInfo]
  
   Returns all the values stored in the map.
   Returns: Return the info array.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ExportLayerTable,disposing: bool) """
  pass
 def Remove(self,exportLayerKey):
  """
  Remove(self: ExportLayerTable,exportLayerKey: ExportLayerKey)
   Removes the pair (key,info) by pattern key.
  
   exportLayerKey: The export pattern key.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """ __contains__[KeyValuePair[ExportLayerKey,ExportLayerInfo]](enumerable: IEnumerable[KeyValuePair[ExportLayerKey,ExportLayerInfo]],value: KeyValuePair[ExportLayerKey,ExportLayerInfo]) -> bool """
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

Get: Count(self: ExportLayerTable) -> int

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportLayerTable) -> bool

"""


