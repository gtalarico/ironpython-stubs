class ICancelAddNew:
 """ Adds transactional capability when adding a new item to a collection. """
 def CancelNew(self,itemIndex):
  """
  CancelNew(self: ICancelAddNew,itemIndex: int)

   Discards a pending new item from the collection.

  

   itemIndex: The index of the item that was previously added to the collection.
  """
  pass
 def EndNew(self,itemIndex):
  """
  EndNew(self: ICancelAddNew,itemIndex: int)

   Commits a pending new item to the collection.

  

   itemIndex: The index of the item that was previously added to the collection.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
