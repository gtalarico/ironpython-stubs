class ProcessModuleCollection(ReadOnlyCollectionBase,ICollection,IEnumerable):
 """
 Provides a strongly typed collection of System.Diagnostics.ProcessModule objects.

 

 ProcessModuleCollection(processModules: Array[ProcessModule])
 """
 def Contains(self,module):
  """
  Contains(self: ProcessModuleCollection,module: ProcessModule) -> bool

  

   Determines whether the specified process module exists in the collection.

  

   module: A System.Diagnostics.ProcessModule instance that indicates the module to find in this collection.

   Returns: true if the module exists in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: ProcessModuleCollection,array: Array[ProcessModule],index: int)

   Copies an array of System.Diagnostics.ProcessModule instances to the collection,at the 

    specified index.

  

  

   array: An array of System.Diagnostics.ProcessModule instances to add to the collection.

   index: The location at which to add the new instances.
  """
  pass
 def IndexOf(self,module):
  """
  IndexOf(self: ProcessModuleCollection,module: ProcessModule) -> int

  

   Provides the location of a specified module within the collection.

  

   module: The System.Diagnostics.ProcessModule whose index is retrieved.

   Returns: The zero-based index that defines the location of the module within the 

    System.Diagnostics.ProcessModuleCollection.
  """
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
 @staticmethod
 def __new__(self,processModules):
  """
  __new__(cls: type)

  __new__(cls: type,processModules: Array[ProcessModule])
  """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.



"""


