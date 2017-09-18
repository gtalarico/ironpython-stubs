class ListChangedEventArgs(EventArgs):
 """
 Provides data for the System.ComponentModel.IBindingList.ListChanged event.

 

 ListChangedEventArgs(listChangedType: ListChangedType,newIndex: int)

 ListChangedEventArgs(listChangedType: ListChangedType,newIndex: int,propDesc: PropertyDescriptor)

 ListChangedEventArgs(listChangedType: ListChangedType,propDesc: PropertyDescriptor)

 ListChangedEventArgs(listChangedType: ListChangedType,newIndex: int,oldIndex: int)
 """
 @staticmethod
 def __new__(self,listChangedType,*__args):
  """
  __new__(cls: type,listChangedType: ListChangedType,newIndex: int)

  __new__(cls: type,listChangedType: ListChangedType,newIndex: int,propDesc: PropertyDescriptor)

  __new__(cls: type,listChangedType: ListChangedType,propDesc: PropertyDescriptor)

  __new__(cls: type,listChangedType: ListChangedType,newIndex: int,oldIndex: int)
  """
  pass
 ListChangedType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of change.



Get: ListChangedType(self: ListChangedEventArgs) -> ListChangedType



"""

 NewIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the item affected by the change.



Get: NewIndex(self: ListChangedEventArgs) -> int



"""

 OldIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the old index of an item that has been moved.



Get: OldIndex(self: ListChangedEventArgs) -> int



"""

 PropertyDescriptor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.ComponentModel.PropertyDescriptor that was added,changed,or deleted.



Get: PropertyDescriptor(self: ListChangedEventArgs) -> PropertyDescriptor



"""


