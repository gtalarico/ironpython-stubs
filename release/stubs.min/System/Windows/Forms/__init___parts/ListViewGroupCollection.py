class ListViewGroupCollection(object,IList,ICollection,IEnumerable):
 """ Represents the collection of groups within a System.Windows.Forms.ListView control. """
 def Add(self,*__args):
  """
  Add(self: ListViewGroupCollection,key: str,headerText: str) -> ListViewGroup

  

   Adds a new System.Windows.Forms.ListViewGroup to the collection using the specified values to 

    initialize the System.Windows.Forms.ListViewGroup.Name and 

    System.Windows.Forms.ListViewGroup.Header properties

  

  

   key: The initial value of the System.Windows.Forms.ListViewGroup.Name property for the new group.

   headerText: The initial value of the System.Windows.Forms.ListViewGroup.Header property for the new group.

   Returns: The new System.Windows.Forms.ListViewGroup.

  Add(self: ListViewGroupCollection,group: ListViewGroup) -> int

  

   Adds the specified System.Windows.Forms.ListViewGroup to the collection.

  

   group: The System.Windows.Forms.ListViewGroup to add to the collection.

   Returns: The index of the group within the collection,or -1 if the group is already present in the 

    collection.
  """
  pass
 def AddRange(self,groups):
  """
  AddRange(self: ListViewGroupCollection,groups: ListViewGroupCollection)

   Adds the groups in an existing System.Windows.Forms.ListViewGroupCollection to the collection.

  

   groups: A System.Windows.Forms.ListViewGroupCollection containing the groups to add to the collection.

  AddRange(self: ListViewGroupCollection,groups: Array[ListViewGroup])

   Adds an array of groups to the collection.

  

   groups: An array of type System.Windows.Forms.ListViewGroup that specifies the groups to add to the 

    collection.
  """
  pass
 def Clear(self):
  """
  Clear(self: ListViewGroupCollection)

   Removes all groups from the collection.
  """
  pass
 def Contains(self,value):
  """
  Contains(self: ListViewGroupCollection,value: ListViewGroup) -> bool

  

   Determines whether the specified group is located in the collection.

  

   value: The System.Windows.Forms.ListViewGroup to locate in the collection.

   Returns: true if the group is in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: ListViewGroupCollection,array: Array,index: int)

   Copies the groups in the collection to a compatible one-dimensional System.Array,starting at 

    the specified index of the target array.

  

  

   array: The System.Array to which the groups are copied.

   index: The first index within the array to which the groups are copied.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: ListViewGroupCollection) -> IEnumerator

  

   Returns an enumerator used to iterate through the collection.

   Returns: An System.Collections.IEnumerator that represents the collection.
  """
  pass
 def IndexOf(self,value):
  """
  IndexOf(self: ListViewGroupCollection,value: ListViewGroup) -> int

  

   Returns the index of the specified System.Windows.Forms.ListViewGroup within the collection.

  

   value: The System.Windows.Forms.ListViewGroup to locate in the collection.

   Returns: The zero-based index of the group within the collection,or -1 if the group is not in the 

    collection.
  """
  pass
 def Insert(self,index,group):
  """
  Insert(self: ListViewGroupCollection,index: int,group: ListViewGroup)

   Inserts the specified System.Windows.Forms.ListViewGroup into the collection at the specified 

    index.

  

  

   index: The index within the collection at which to insert the group.

   group: The System.Windows.Forms.ListViewGroup to insert into the collection.
  """
  pass
 def Remove(self,group):
  """
  Remove(self: ListViewGroupCollection,group: ListViewGroup)

   Removes the specified System.Windows.Forms.ListViewGroup from the collection.

  

   group: The System.Windows.Forms.ListViewGroup to remove from the collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: ListViewGroupCollection,index: int)

   Removes the System.Windows.Forms.ListViewGroup at the specified index within the collection.

  

   index: The index within the collection of the System.Windows.Forms.ListViewGroup to remove.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]=x.__setitem__(i,y) <==> x[i]= """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of groups in the collection.



Get: Count(self: ListViewGroupCollection) -> int



"""


