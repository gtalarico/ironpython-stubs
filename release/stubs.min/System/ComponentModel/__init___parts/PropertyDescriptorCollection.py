class PropertyDescriptorCollection(object,ICollection,IEnumerable,IList,IDictionary):
 """
 Represents a collection of System.ComponentModel.PropertyDescriptor objects.

 

 PropertyDescriptorCollection(properties: Array[PropertyDescriptor])

 PropertyDescriptorCollection(properties: Array[PropertyDescriptor],readOnly: bool)
 """
 def Add(self,value):
  """
  Add(self: PropertyDescriptorCollection,value: PropertyDescriptor) -> int

  

   Adds the specified System.ComponentModel.PropertyDescriptor to the collection.

  

   value: The System.ComponentModel.PropertyDescriptor to add to the collection.

   Returns: The index of the System.ComponentModel.PropertyDescriptor that was added to the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: PropertyDescriptorCollection)

   Removes all System.ComponentModel.PropertyDescriptor objects from the collection.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: PropertyDescriptorCollection,value: PropertyDescriptor) -> bool

  

   Returns whether the collection contains the given System.ComponentModel.PropertyDescriptor.

  

   value: The System.ComponentModel.PropertyDescriptor to find in the collection.

   Returns: true if the collection contains the given System.ComponentModel.PropertyDescriptor; otherwise,

    false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: PropertyDescriptorCollection,array: Array,index: int)

   Copies the entire collection to an array,starting at the specified index number.

  

   array: An array of System.ComponentModel.PropertyDescriptor objects to copy elements of the collection 

    to.

  

   index: The index of the array parameter at which copying begins.
  """
  pass
 def Find(self,name,ignoreCase):
  """
  Find(self: PropertyDescriptorCollection,name: str,ignoreCase: bool) -> PropertyDescriptor

  

   Returns the System.ComponentModel.PropertyDescriptor with the specified name,using a Boolean to 

    indicate whether to ignore case.

  

  

   name: The name of the System.ComponentModel.PropertyDescriptor to return from the collection.

   ignoreCase: true if you want to ignore the case of the property name; otherwise,false.

   Returns: A System.ComponentModel.PropertyDescriptor with the specified name,or null if the property does 

    not exist.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: PropertyDescriptorCollection) -> IEnumerator

  

   Returns an enumerator for this class.

   Returns: An enumerator of type System.Collections.IEnumerator.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: PropertyDescriptorCollection,value: PropertyDescriptor) -> int

  

   Returns the index of the given System.ComponentModel.PropertyDescriptor.

  

   value: The System.ComponentModel.PropertyDescriptor to return the index of.

   Returns: The index of the given System.ComponentModel.PropertyDescriptor.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: PropertyDescriptorCollection,index: int,value: PropertyDescriptor)

   Adds the System.ComponentModel.PropertyDescriptor to the collection at the specified index 

    number.

  

  

   index: The index at which to add the value parameter to the collection.

   value: The System.ComponentModel.PropertyDescriptor to add to the collection.
  """
  pass
 def InternalSort(self,*args):
  """
  InternalSort(self: PropertyDescriptorCollection,sorter: IComparer)

   Sorts the members of this collection,using the specified System.Collections.IComparer.

  

   sorter: A comparer to use to sort the System.ComponentModel.PropertyDescriptor objects in this 

    collection.

  

  InternalSort(self: PropertyDescriptorCollection,names: Array[str])

   Sorts the members of this collection. The specified order is applied first,followed by the 

    default sort for this collection,which is usually alphabetical.

  

  

   names: An array of strings describing the order in which to sort the 

    System.ComponentModel.PropertyDescriptor objects in this collection.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: PropertyDescriptorCollection,value: PropertyDescriptor)

   Removes the specified System.ComponentModel.PropertyDescriptor from the collection.

  

   value: The System.ComponentModel.PropertyDescriptor to remove from the collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: PropertyDescriptorCollection,index: int)

   Removes the System.ComponentModel.PropertyDescriptor at the specified index from the collection.

  

   index: The index of the System.ComponentModel.PropertyDescriptor to remove from the collection.
  """
  pass
 def Sort(self,*__args):
  """
  Sort(self: PropertyDescriptorCollection,names: Array[str],comparer: IComparer) -> PropertyDescriptorCollection

  

   Sorts the members of this collection. The specified order is applied first,followed by the sort 

    using the specified System.Collections.IComparer.

  

  

   names: An array of strings describing the order in which to sort the 

    System.ComponentModel.PropertyDescriptor objects in this collection.

  

   comparer: A comparer to use to sort the System.ComponentModel.PropertyDescriptor objects in this 

    collection.

  

   Returns: A new System.ComponentModel.PropertyDescriptorCollection that contains the sorted 

    System.ComponentModel.PropertyDescriptor objects.

  

  Sort(self: PropertyDescriptorCollection,comparer: IComparer) -> PropertyDescriptorCollection

  

   Sorts the members of this collection,using the specified System.Collections.IComparer.

  

   comparer: A comparer to use to sort the System.ComponentModel.PropertyDescriptor objects in this 

    collection.

  

   Returns: A new System.ComponentModel.PropertyDescriptorCollection that contains the sorted 

    System.ComponentModel.PropertyDescriptor objects.

  

  Sort(self: PropertyDescriptorCollection) -> PropertyDescriptorCollection

  

   Sorts the members of this collection,using the default sort for this collection,which is 

    usually alphabetical.

  

   Returns: A new System.ComponentModel.PropertyDescriptorCollection that contains the sorted 

    System.ComponentModel.PropertyDescriptor objects.

  

  Sort(self: PropertyDescriptorCollection,names: Array[str]) -> PropertyDescriptorCollection

  

   Sorts the members of this collection. The specified order is applied first,followed by the 

    default sort for this collection,which is usually alphabetical.

  

  

   names: An array of strings describing the order in which to sort the 

    System.ComponentModel.PropertyDescriptor objects in this collection.

  

   Returns: A new System.ComponentModel.PropertyDescriptorCollection that contains the sorted 

    System.ComponentModel.PropertyDescriptor objects.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
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
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
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
 def __new__(self,properties,readOnly=None):
  """
  __new__(cls: type,properties: Array[PropertyDescriptor])

  __new__(cls: type,properties: Array[PropertyDescriptor],readOnly: bool)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of property descriptors in the collection.



Get: Count(self: PropertyDescriptorCollection) -> int



"""


 Empty=None

