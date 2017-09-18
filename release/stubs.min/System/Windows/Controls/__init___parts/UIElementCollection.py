class UIElementCollection(object,IList,ICollection,IEnumerable):
 """
 Represents an ordered collection of System.Windows.UIElement child elements.

 

 UIElementCollection(visualParent: UIElement,logicalParent: FrameworkElement)
 """
 def Add(self,element):
  """
  Add(self: UIElementCollection,element: UIElement) -> int

  

   Adds the specified element to the System.Windows.Controls.UIElementCollection.

  

   element: The System.Windows.UIElement to add.

   Returns: The index position of the added element.
  """
  pass
 def Clear(self):
  """
  Clear(self: UIElementCollection)

   Removes all elements from a System.Windows.Controls.UIElementCollection.
  """
  pass
 def ClearLogicalParent(self,*args):
  """
  ClearLogicalParent(self: UIElementCollection,element: UIElement)

   Clears the logical parent of an element when the element leaves a 

    System.Windows.Controls.UIElementCollection.

  

  

   element: The System.Windows.UIElement whose logical parent is being cleared.
  """
  pass
 def Contains(self,element):
  """
  Contains(self: UIElementCollection,element: UIElement) -> bool

  

   Determines whether a specified element is in the System.Windows.Controls.UIElementCollection.

  

   element: The element to find.

   Returns: true if the specified System.Windows.UIElement is found in the collection; otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: UIElementCollection,array: Array[UIElement],index: int)

   Copies a System.Windows.UIElement from a System.Windows.Controls.UIElementCollection to an 

    array,starting at a specified index position.

  

  

   array: An array of System.Windows.UIElement objects.

   index: The index position of the element where copying begins.

  CopyTo(self: UIElementCollection,array: Array,index: int)

   Copies a System.Windows.UIElement from a System.Windows.Controls.UIElementCollection to an 

    array,starting at a specified index position.

  

  

   array: An array into which the collection is copied.

   index: The index position of the element where copying begins.
  """
  pass
 def GetEnumerator(self):
  """
  GetEnumerator(self: UIElementCollection) -> IEnumerator

  

   Returns an enumerator that can iterate the System.Windows.Controls.UIElementCollection.

   Returns: An System.Collections.IEnumerator that can list the members of this collection.
  """
  pass
 def IndexOf(self,element):
  """
  IndexOf(self: UIElementCollection,element: UIElement) -> int

  

   Returns the index position of a specified element in a 

    System.Windows.Controls.UIElementCollection.

  

  

   element: The element whose index position is required.

   Returns: The index position of the element.  -1 if the element is not in the collection.
  """
  pass
 def Insert(self,index,element):
  """
  Insert(self: UIElementCollection,index: int,element: UIElement)

   Inserts an element into a System.Windows.Controls.UIElementCollection at the specified index 

    position.

  

  

   index: The index position where you want to insert the element.

   element: The element to insert into the System.Windows.Controls.UIElementCollection.
  """
  pass
 def Remove(self,element):
  """
  Remove(self: UIElementCollection,element: UIElement)

   Removes the specified element from a System.Windows.Controls.UIElementCollection.

  

   element: The element to remove from the collection.
  """
  pass
 def RemoveAt(self,index):
  """
  RemoveAt(self: UIElementCollection,index: int)

   Removes the System.Windows.UIElement at the specified index.

  

   index: The index of the System.Windows.UIElement that you want to remove.
  """
  pass
 def RemoveRange(self,index,count):
  """
  RemoveRange(self: UIElementCollection,index: int,count: int)

   Removes a range of elements from a System.Windows.Controls.UIElementCollection.

  

   index: The index position of the element where removal begins.

   count: The number of elements to remove.
  """
  pass
 def SetLogicalParent(self,*args):
  """
  SetLogicalParent(self: UIElementCollection,element: UIElement)

   Sets the logical parent of an element in a System.Windows.Controls.UIElementCollection.

  

   element: The System.Windows.UIElement whose logical parent is set.
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
 def __new__(self,visualParent,logicalParent):
  """ __new__(cls: type,visualParent: UIElement,logicalParent: FrameworkElement) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Capacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of elements that the System.Windows.Controls.UIElementCollection can contain.



Get: Capacity(self: UIElementCollection) -> int



Set: Capacity(self: UIElementCollection)=value

"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the actual number of elements in the collection.



Get: Count(self: UIElementCollection) -> int



"""

 IsSynchronized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether access to the System.Collections.ICollection interface is synchronized (thread-safe).



Get: IsSynchronized(self: UIElementCollection) -> bool



"""

 SyncRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an object that you can use to synchronize access to the System.Collections.ICollection interface.



Get: SyncRoot(self: UIElementCollection) -> object



"""


