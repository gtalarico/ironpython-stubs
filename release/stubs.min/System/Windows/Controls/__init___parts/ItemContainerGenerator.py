class ItemContainerGenerator(object,IRecyclingItemContainerGenerator,IItemContainerGenerator,IWeakEventListener):
 """ Generates the user interface (UI) on behalf of its host,such as an�System.Windows.Controls.ItemsControl. """
 def ContainerFromIndex(self,index):
  """
  ContainerFromIndex(self: ItemContainerGenerator,index: int) -> DependencyObject

  

   Returns the element corresponding to the item at the given index within the 

    System.Windows.Controls.ItemCollection.

  

  

   index: The index of the desired item.

   Returns: Returns the element corresponding to the item at the given index within the 

    System.Windows.Controls.ItemCollection or returns null if the item is not realized.
  """
  pass
 def ContainerFromItem(self,item):
  """
  ContainerFromItem(self: ItemContainerGenerator,item: object) -> DependencyObject

  

   Returns the System.Windows.UIElement corresponding to the given item.

  

   item: The System.Object item to find the System.Windows.UIElement for.

   Returns: A System.Windows.UIElement that corresponds to the given item. Returns null if the item does not 

    belong to the item collection,or if a System.Windows.UIElement has not been generated for it.
  """
  pass
 def GenerateBatches(self):
  """ GenerateBatches(self: ItemContainerGenerator) -> IDisposable """
  pass
 def IndexFromContainer(self,container,returnLocalIndex=None):
  """
  IndexFromContainer(self: ItemContainerGenerator,container: DependencyObject,returnLocalIndex: bool) -> int

  IndexFromContainer(self: ItemContainerGenerator,container: DependencyObject) -> int

  

   Returns the index to an item that corresponds to the specified,generated 

    System.Windows.UIElement.

  

  

   container: The System.Windows.DependencyObject that corresponds to the item to the index to be returned.

   Returns: An System.Int32 index to an item that corresponds to the specified,generated 

    System.Windows.UIElement or -1 if container is not found.
  """
  pass
 def ItemFromContainer(self,container):
  """
  ItemFromContainer(self: ItemContainerGenerator,container: DependencyObject) -> object

  

   Returns the item that corresponds to the specified,generated System.Windows.UIElement.

  

   container: The System.Windows.DependencyObject that corresponds to the item to be returned.

   Returns: A System.Windows.DependencyObject that is the item which corresponds to the specified,generated 

    System.Windows.UIElement. If the System.Windows.UIElement has not been generated,

    System.Windows.DependencyProperty.UnsetValue is returned.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Items(self: ItemContainerGenerator) -> ReadOnlyCollection[object]



"""

 Status=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The generation status of the System.Windows.Controls.ItemContainerGenerator.



Get: Status(self: ItemContainerGenerator) -> GeneratorStatus



"""


 ItemsChanged=None
 StatusChanged=None

