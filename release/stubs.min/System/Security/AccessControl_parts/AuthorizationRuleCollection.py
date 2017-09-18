class AuthorizationRuleCollection(ReadOnlyCollectionBase,ICollection,IEnumerable):
 """
 Represents a collection of System.Security.AccessControl.AuthorizationRule objects.

 

 AuthorizationRuleCollection()
 """
 def AddRule(self,rule):
  """ AddRule(self: AuthorizationRuleCollection,rule: AuthorizationRule) """
  pass
 def CopyTo(self,rules,index):
  """
  CopyTo(self: AuthorizationRuleCollection,rules: Array[AuthorizationRule],index: int)

   Copies the contents of the collection to an array.

  

   rules: An array to which to copy the contents of the collection.

   index: The zero-based index from which to begin copying.
  """
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
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of elements contained in the System.Collections.ReadOnlyCollectionBase instance.



"""


