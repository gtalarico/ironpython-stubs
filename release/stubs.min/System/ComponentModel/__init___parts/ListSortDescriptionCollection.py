class ListSortDescriptionCollection(object,IList,ICollection,IEnumerable):
 """
 Represents a collection of System.ComponentModel.ListSortDescription objects.

 

 ListSortDescriptionCollection()

 ListSortDescriptionCollection(sorts: Array[ListSortDescription])
 """
 def Contains(self,value):
  """
  Contains(self: ListSortDescriptionCollection,value: object) -> bool

  

   Determines if the System.ComponentModel.ListSortDescriptionCollection contains a specific value.

  

   value: The System.Object to locate in the collection.

   Returns: true if the System.Object is found in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: ListSortDescriptionCollection,array: Array,index: int)

   Copies the contents of the collection to the specified array,starting at the specified 

    destination array index.

  

  

   array: The destination array for the items copied from the collection.

   index: The index of the destination array at which copying begins.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: ListSortDescriptionCollection,value: object) -> int

  

   Returns the index of the specified item in the collection.

  

   value: The System.Object to locate in the collection.

   Returns: The index of value if found in the list; otherwise,-1.
  """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IList,value: object) -> bool

  

   Determines whether the System.Collections.IList contains a specific value.

  

   value: The object to locate in the System.Collections.IList.

   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
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
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 @staticmethod
 def __new__(self,sorts=None):
  """
  __new__(cls: type)

  __new__(cls: type,sorts: Array[ListSortDescription])
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of items in the collection.



Get: Count(self: ListSortDescriptionCollection) -> int



"""


