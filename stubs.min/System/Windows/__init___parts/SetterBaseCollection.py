class SetterBaseCollection(Collection[SetterBase],IList[SetterBase],ICollection[SetterBase],IEnumerable[SetterBase],IEnumerable,IList,ICollection,IReadOnlyList[SetterBase],IReadOnlyCollection[SetterBase]):
 """
 Represents a collection of System.Windows.SetterBase objects.
 
 SetterBaseCollection()
 """
 def ClearItems(self,*args):
  """ ClearItems(self: SetterBaseCollection) """
  pass
 def InsertItem(self,*args):
  """ InsertItem(self: SetterBaseCollection,index: int,item: SetterBase) """
  pass
 def RemoveItem(self,*args):
  """ RemoveItem(self: SetterBaseCollection,index: int) """
  pass
 def SetItem(self,*args):
  """ SetItem(self: SetterBaseCollection,index: int,item: SetterBase) """
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
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 IsSealed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this object is in a read-only state.

Get: IsSealed(self: SetterBaseCollection) -> bool

"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


