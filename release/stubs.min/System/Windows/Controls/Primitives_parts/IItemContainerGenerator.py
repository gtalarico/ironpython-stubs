class IItemContainerGenerator:
 """ An interface that is implemented by classes which are responsible for generating user interface (UI) content on behalf of a host. """
 def GenerateNext(self,isNewlyRealized=None):
  """
  GenerateNext(self: IItemContainerGenerator) -> (DependencyObject,bool)

  

   Returns the container element used to display the next item,and whether the container element 

    has been newly generated (realized).

  

   Returns: A System.Windows.DependencyObject that is the container element which is used to display the 

    next item.

  

  GenerateNext(self: IItemContainerGenerator) -> DependencyObject

  

   Returns the container element used to display the next item.

   Returns: A System.Windows.DependencyObject that is the container element which is used to display the 

    next item.
  """
  pass
 def GeneratorPositionFromIndex(self,itemIndex):
  """
  GeneratorPositionFromIndex(self: IItemContainerGenerator,itemIndex: int) -> GeneratorPosition

  

   Returns the System.Windows.Controls.Primitives.GeneratorPosition object that maps to the item at 

    the specified index.

  

  

   itemIndex: The index of desired item.

   Returns: An System.Windows.Controls.Primitives.GeneratorPosition object that maps to the item at the 

    specified index.
  """
  pass
 def GetItemContainerGeneratorForPanel(self,panel):
  """
  GetItemContainerGeneratorForPanel(self: IItemContainerGenerator,panel: Panel) -> ItemContainerGenerator

  

   Returns the System.Windows.Controls.ItemContainerGenerator appropriate for use by the specified 

    panel.

  

  

   panel: The panel for which to return an appropriate System.Windows.Controls.ItemContainerGenerator.

   Returns: An System.Windows.Controls.ItemContainerGenerator appropriate for use by the specified panel.
  """
  pass
 def IndexFromGeneratorPosition(self,position):
  """
  IndexFromGeneratorPosition(self: IItemContainerGenerator,position: GeneratorPosition) -> int

  

   Returns the index that maps to the specified 

    System.Windows.Controls.Primitives.GeneratorPosition.

  

  

   position: The index of desired item.The System.Windows.Controls.Primitives.GeneratorPosition  for the 

    desired index.

  

   Returns: An System.Int32 that is the index which maps to the specified 

    System.Windows.Controls.Primitives.GeneratorPosition.
  """
  pass
 def PrepareItemContainer(self,container):
  """
  PrepareItemContainer(self: IItemContainerGenerator,container: DependencyObject)

   Prepares the specified element as the container for the corresponding item.

  

   container: The container to prepare. Normally,container is the result of the previous call to 

    erload:System.Windows.Controls.Primitives.IItemContainerGenerator.GenerateNext.
  """
  pass
 def Remove(self,position,count):
  """
  Remove(self: IItemContainerGenerator,position: GeneratorPosition,count: int)

   Removes one or more generated (realized) items.

  

   position: The System.Int32 index of the element to remove. position must refer to a previously generated 

    (realized) item,which means its offset must be zero.

  

   count: The System.Int32 number of elements to remove,starting at position.
  """
  pass
 def RemoveAll(self):
  """
  RemoveAll(self: IItemContainerGenerator)

   Removes all generated (realized) items.
  """
  pass
 def StartAt(self,position,direction,allowStartAtRealizedItem=None):
  """
  StartAt(self: IItemContainerGenerator,position: GeneratorPosition,direction: GeneratorDirection,allowStartAtRealizedItem: bool) -> IDisposable

  

   Prepares the generator to generate items,starting at the specified 

    System.Windows.Controls.Primitives.GeneratorPosition,and in the specified 

    System.Windows.Controls.Primitives.GeneratorDirection,and controlling whether or not to start 

    at a generated (realized) item.

  

  

   position: A System.Windows.Controls.Primitives.GeneratorPosition,that specifies the position of the item 

    to start generating items at.

  

   direction: Specifies the position of the item to start generating items at.

   allowStartAtRealizedItem: A System.Boolean that specifies whether to start at a generated (realized) item.

   Returns: An System.IDisposable object that tracks the lifetime of the generation process.

  StartAt(self: IItemContainerGenerator,position: GeneratorPosition,direction: GeneratorDirection) -> IDisposable

  

   Prepares the generator to generate items,starting at the specified 

    System.Windows.Controls.Primitives.GeneratorPosition,and in the specified 

    System.Windows.Controls.Primitives.GeneratorDirection.

  

  

   position: A System.Windows.Controls.Primitives.GeneratorPosition,that specifies the position of the item 

    to start generating items at.

  

   direction: A System.Windows.Controls.Primitives.GeneratorDirection that specifies the direction which to 

    generate items.

  

   Returns: An System.IDisposable object that tracks the lifetime of the generation process.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
