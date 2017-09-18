class IRecyclingItemContainerGenerator(IItemContainerGenerator):
 """ Extends the System.Windows.Controls.Primitives.IItemContainerGenerator interface to reuse the UI content it generates. Classes that are responsible for generating user interface (UI) content on behalf of a host implement this interface. """
 def Recycle(self,position,count):
  """
  Recycle(self: IRecyclingItemContainerGenerator,position: GeneratorPosition,count: int)

   Disassociates item containers from their data items and saves the containers so they can be 

    reused later for other data items.

  

  

   position: The zero-based index of the first element to reuse. position must refer to a previously 

    generated (realized) item.

  

   count: The number of elements to reuse,starting at position.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
