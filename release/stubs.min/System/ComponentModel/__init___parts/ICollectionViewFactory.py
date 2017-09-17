class ICollectionViewFactory:
 """ An interface that enables implementing collections to create a view to their data. Normally,user code does not call methods on this interface. """
 def CreateView(self):
  """
  CreateView(self: ICollectionViewFactory) -> ICollectionView
  
   Creates a new view on the collection that implements this interface. Typically,
    user code does not call this method.
  
   Returns: The newly created view.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
