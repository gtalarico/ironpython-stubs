class EventDescriptorCollection(object,ICollection,IEnumerable,IList):
 """
 Represents a collection of System.ComponentModel.EventDescriptor objects.

 

 EventDescriptorCollection(events: Array[EventDescriptor])

 EventDescriptorCollection(events: Array[EventDescriptor],readOnly: bool)
 """
 def Add(self,value):
  """
  Add(self: EventDescriptorCollection,value: EventDescriptor) -> int

  

   Adds an System.ComponentModel.EventDescriptor to the end of the collection.

  

   value: An System.ComponentModel.EventDescriptor to add to the collection.

   Returns: The position of the System.ComponentModel.EventDescriptor within the collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: EventDescriptorCollection)

   Removes all objects from the collection.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: EventDescriptorCollection,value: EventDescriptor) -> bool

  

   Returns whether the collection contains the given System.ComponentModel.EventDescriptor.

  

   value: The System.ComponentModel.EventDescriptor to find within the collection.

   Returns: true if the collection contains the value parameter given; otherwise,false.
  """
  pass
 def Find(self,name,ignoreCase):
  """
  Find(self: EventDescriptorCollection,name: str,ignoreCase: bool) -> EventDescriptor

  

   Gets the description of the event with the specified name in the collection.

  

   name: The name of the event to get from the collection.

   ignoreCase: true if you want to ignore the case of the event; otherwise,false.

   Returns: The System.ComponentModel.EventDescriptor with the specified name,or null if the event does not 

    exist.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: EventDescriptorCollection) -> IEnumerator

  

   Gets an enumerator for this System.ComponentModel.EventDescriptorCollection.

   Returns: An enumerator that implements System.Collections.IEnumerator.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: EventDescriptorCollection,value: EventDescriptor) -> int

  

   Returns the index of the given System.ComponentModel.EventDescriptor.

  

   value: The System.ComponentModel.EventDescriptor to find within the collection.

   Returns: The index of the given System.ComponentModel.EventDescriptor within the collection.
  """
  pass
 def Insert(self,index,value):
  """
  Insert(self: EventDescriptorCollection,index: int,value: EventDescriptor)

   Inserts an System.ComponentModel.EventDescriptor to the collection at a specified index.

  

   index: The index within the collection in which to insert the value parameter.

   value: An System.ComponentModel.EventDescriptor to insert into the collection.
  """
  pass
 def InternalSort(self,*args):
  """
  InternalSort(self: EventDescriptorCollection,sorter: IComparer)

   Sorts the members of this System.ComponentModel.EventDescriptorCollection,using the specified 

    System.Collections.IComparer.

  

  

   sorter: A comparer to use to sort the System.ComponentModel.EventDescriptor objects in this collection.

  InternalSort(self: EventDescriptorCollection,names: Array[str])

   Sorts the members of this System.ComponentModel.EventDescriptorCollection. The specified order 

    is applied first,followed by the default sort for this collection,which is usually 

    alphabetical.

  

  

   names: An array of strings describing the order in which to sort the 

    System.ComponentModel.EventDescriptor objects in this collection.
  """
  pass
 def Remove(self,value):
  """
  Remove(self: EventDescriptorCollection,value: EventDescriptor)

   Removes the specified System.ComponentModel.EventDescriptor from the collection.

  

   value: The System.ComponentModel.EventDescriptor to remove from the collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: EventDescriptorCollection,index: int)

   Removes the System.ComponentModel.EventDescriptor at the specified index from the collection.

  

   index: The index of the System.ComponentModel.EventDescriptor to remove.
  """
  pass
 def Sort(self,*__args):
  """
  Sort(self: EventDescriptorCollection,names: Array[str],comparer: IComparer) -> EventDescriptorCollection

  

   Sorts the members of this System.ComponentModel.EventDescriptorCollection,given a specified 

    sort order and an System.Collections.IComparer.

  

  

   names: An array of strings describing the order in which to sort the 

    System.ComponentModel.EventDescriptor objects in the collection.

  

   comparer: An System.Collections.IComparer to use to sort the System.ComponentModel.EventDescriptor objects 

    in this collection.

  

   Returns: The new System.ComponentModel.EventDescriptorCollection.

  Sort(self: EventDescriptorCollection,comparer: IComparer) -> EventDescriptorCollection

  

   Sorts the members of this System.ComponentModel.EventDescriptorCollection,using the specified 

    System.Collections.IComparer.

  

  

   comparer: An System.Collections.IComparer to use to sort the System.ComponentModel.EventDescriptor objects 

    in this collection.

  

   Returns: The new System.ComponentModel.EventDescriptorCollection.

  Sort(self: EventDescriptorCollection) -> EventDescriptorCollection

  

   Sorts the members of this System.ComponentModel.EventDescriptorCollection,using the default 

    sort for this collection,which is usually alphabetical.

  

   Returns: The new System.ComponentModel.EventDescriptorCollection.

  Sort(self: EventDescriptorCollection,names: Array[str]) -> EventDescriptorCollection

  

   Sorts the members of this System.ComponentModel.EventDescriptorCollection,given a specified 

    sort order.

  

  

   names: An array of strings describing the order in which to sort the 

    System.ComponentModel.EventDescriptor objects in the collection.

  

   Returns: The new System.ComponentModel.EventDescriptorCollection.
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
 def __new__(self,events,readOnly=None):
  """
  __new__(cls: type,events: Array[EventDescriptor])

  __new__(cls: type,events: Array[EventDescriptor],readOnly: bool)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of event descriptors in the collection.



Get: Count(self: EventDescriptorCollection) -> int



"""


 Empty=None

