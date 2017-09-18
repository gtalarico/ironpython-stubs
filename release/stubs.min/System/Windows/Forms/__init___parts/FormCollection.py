class FormCollection(ReadOnlyCollectionBase,ICollection,IEnumerable):
 """
 Represents a collection of System.Windows.Forms.Form objects.

 

 FormCollection()
 """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.



"""


