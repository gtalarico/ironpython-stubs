class CollectionChangeEventArgs(EventArgs):
 """
 Provides data for the System.Data.DataColumnCollection.CollectionChanged event.
 
 CollectionChangeEventArgs(action: CollectionChangeAction,element: object)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return CollectionChangeEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,action,element):
  """ __new__(cls: type,action: CollectionChangeAction,element: object) """
  pass
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an action that specifies how the collection changed.

Get: Action(self: CollectionChangeEventArgs) -> CollectionChangeAction

"""

 Element=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the instance of the collection with the change.

Get: Element(self: CollectionChangeEventArgs) -> object

"""


