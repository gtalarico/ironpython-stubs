class LogicalTreeHelper(object):
 """ Provides static helper methods for querying objects in the logical tree. """
 @staticmethod
 def BringIntoView(current):
  """
  BringIntoView(current: DependencyObject)
   Attempts to bring the requested UI element into view and raises the 
    System.Windows.FrameworkElement.RequestBringIntoView event on the target in 
    order to report the results.
  
  
   current: The UI element to bring into view.
  """
  pass
 @staticmethod
 def FindLogicalNode(logicalTreeNode,elementName):
  """
  FindLogicalNode(logicalTreeNode: DependencyObject,elementName: str) -> DependencyObject
  
   Attempts to find and return an object that has the specified name. The search 
    starts from the specified object and continues into subnodes of the logical 
    tree.
  
  
   logicalTreeNode: The object to start searching from. This object must be either a 
    System.Windows.FrameworkElement or a System.Windows.FrameworkContentElement.
  
   elementName: The name of the object to find.
   Returns: The object with the matching name,if one is found; returns null if no matching 
    name was found in the logical tree.
  """
  pass
 @staticmethod
 def GetChildren(current):
  """
  GetChildren(current: FrameworkContentElement) -> IEnumerable
  
   Returns the collection of immediate child objects of the specified 
    System.Windows.FrameworkContentElement by processing the logical tree.
  
  
   current: The object from which to start processing the logical tree.
   Returns: The enumerable collection of immediate child objects starting from current in 
    the logical tree.
  
  GetChildren(current: FrameworkElement) -> IEnumerable
  
   Returns the collection of immediate child objects of the specified 
    System.Windows.FrameworkElement by processing the logical tree.
  
  
   current: The object from which to start processing the logical tree.
   Returns: The enumerable collection of immediate child objects starting from current in 
    the logical tree.
  
  GetChildren(current: DependencyObject) -> IEnumerable
  
   Returns the collection of immediate child objects of the specified object,by 
    processing the logical tree.
  
  
   current: The object from which to start processing the logical tree. This is expected to 
    be either a System.Windows.FrameworkElement or 
    System.Windows.FrameworkContentElement.
  
   Returns: The enumerable collection of immediate child objects from the logical tree of 
    the specified object.
  """
  pass
 @staticmethod
 def GetParent(current):
  """
  GetParent(current: DependencyObject) -> DependencyObject
  
   Returns the parent object of the specified object by processing the logical 
    tree.
  
  
   current: The object to find the parent object for. This is expected to be either a 
    System.Windows.FrameworkElement or a System.Windows.FrameworkContentElement.
  
   Returns: The requested parent object.
  """
  pass
 __all__=[
  'BringIntoView',
  'FindLogicalNode',
  'GetChildren',
  'GetParent',
 ]

