class IListSource:
 """ Provides functionality to an object to return a list that can be bound to a data source. """
 def GetList(self):
  """
  GetList(self: IListSource) -> IList

  

   Returns an System.Collections.IList that can be bound to a data source from an object that does 

    not implement an System.Collections.IList itself.

  

   Returns: An System.Collections.IList that can be bound to a data source from the object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ContainsListCollection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the collection is a collection of System.Collections.IList objects.



Get: ContainsListCollection(self: IListSource) -> bool



"""


