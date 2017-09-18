class GridItemCollection(object,ICollection,IEnumerable):
 """ Contains a collection of System.Windows.Forms.GridItem objects. """
 def GetEnumerator(self):
  """
  GetEnumerator(self: GridItemCollection) -> IEnumerator

  

   Returns an enumeration of all the grid items in the collection.

   Returns: An System.Collections.IEnumerator for the System.Windows.Forms.GridItemCollection.
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
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of grid items in the collection.



Get: Count(self: GridItemCollection) -> int



"""


 Empty=None

