class BindingList(Collection[T],IList[T],ICollection[T],IEnumerable[T],IEnumerable,IList,ICollection,IReadOnlyList[T],IReadOnlyCollection[T],IBindingList,ICancelAddNew,IRaiseItemChangedEvents):
 """
 BindingList[T]()

 BindingList[T](list: IList[T])
 """
 def AddNew(self):
  """
  AddNew(self: BindingList[T]) -> T

  

   Adds a new item to the collection.

   Returns: The item added to the list.
  """
  pass
 def AddNewCore(self,*args):
  """
  AddNewCore(self: BindingList[T]) -> object

  

   Adds a new item to the end of the collection.

   Returns: The item that was added to the collection.
  """
  pass
 def ApplySortCore(self,*args):
  """
  ApplySortCore(self: BindingList[T],prop: PropertyDescriptor,direction: ListSortDirection)

   Sorts the items if overridden in a derived class; otherwise,throws a 

    System.NotSupportedException.

  

  

   prop: A System.ComponentModel.PropertyDescriptor that specifies the property to sort on.

   direction: One of the System.ComponentModel.ListSortDirection  values.
  """
  pass
 def CancelNew(self,itemIndex):
  """
  CancelNew(self: BindingList[T],itemIndex: int)

   Discards a pending new item.

  

   itemIndex: The index of the of the new item to be added
  """
  pass
 def ClearItems(self,*args):
  """
  ClearItems(self: BindingList[T])

   Removes all elements from the collection.
  """
  pass
 def EndNew(self,itemIndex):
  """
  EndNew(self: BindingList[T],itemIndex: int)

   Commits a pending new item to the collection.

  

   itemIndex: The index of the new item to be added.
  """
  pass
 def FindCore(self,*args):
  """
  FindCore(self: BindingList[T],prop: PropertyDescriptor,key: object) -> int

  

   Searches for the index of the item that has the specified property descriptor with the specified 

    value,if searching is implemented in a derived class; otherwise,a 

    System.NotSupportedException.

  

  

   prop: The System.ComponentModel.PropertyDescriptor to search for.

   key: The value of property to match.

   Returns: The zero-based index of the item that matches the property descriptor and contains the specified 

    value.
  """
  pass
 def InsertItem(self,*args):
  """
  InsertItem(self: BindingList[T],index: int,item: T)

   Inserts the specified item in the list at the specified index.

  

   index: The zero-based index where the item is to be inserted.

   item: The item to insert in the list.
  """
  pass
 def OnAddingNew(self,*args):
  """
  OnAddingNew(self: BindingList[T],e: AddingNewEventArgs)

   Raises the System.ComponentModel.BindingList event.

  

   e: An System.ComponentModel.AddingNewEventArgs that contains the event data.
  """
  pass
 def OnListChanged(self,*args):
  """
  OnListChanged(self: BindingList[T],e: ListChangedEventArgs)

   Raises the System.ComponentModel.BindingList event.

  

   e: A System.ComponentModel.ListChangedEventArgs that contains the event data.
  """
  pass
 def RemoveItem(self,*args):
  """
  RemoveItem(self: BindingList[T],index: int)

   Removes the item at the specified index.

  

   index: The zero-based index of the item to remove.
  """
  pass
 def RemoveSortCore(self,*args):
  """
  RemoveSortCore(self: BindingList[T])

   Removes any sort applied with System.ComponentModel.BindingList if sorting is implemented in a 

    derived class; otherwise,raises System.NotSupportedException.
  """
  pass
 def ResetBindings(self):
  """
  ResetBindings(self: BindingList[T])

   Raises a System.ComponentModel.BindingList event of type 

    System.ComponentModel.ListChangedType.Reset.
  """
  pass
 def ResetItem(self,position):
  """
  ResetItem(self: BindingList[T],position: int)

   Raises a System.ComponentModel.BindingList event of type 

    System.ComponentModel.ListChangedType.ItemChanged for the item at the specified position.

  

  

   position: A zero-based index of the item to be reset.
  """
  pass
 def SetItem(self,*args):
  """
  SetItem(self: BindingList[T],index: int,item: T)

   Replaces the item at the specified index with the specified item.

  

   index: The zero-based index of the item to replace.

   item: The new value for the item at the specified index. The value can be null for reference types.
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
 @staticmethod
 def __new__(self,list=None):
  """
  __new__(cls: type)

  __new__(cls: type,list: IList[T])
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 AllowEdit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether items in the list can be edited.



Get: AllowEdit(self: BindingList[T]) -> bool



Set: AllowEdit(self: BindingList[T])=value

"""

 AllowNew=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether you can add items to the list using the System.ComponentModel.BindingList method.



Get: AllowNew(self: BindingList[T]) -> bool



Set: AllowNew(self: BindingList[T])=value

"""

 AllowRemove=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether you can remove items from the collection.



Get: AllowRemove(self: BindingList[T]) -> bool



Set: AllowRemove(self: BindingList[T])=value

"""

 IsSortedCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the list is sorted.



"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.



"""

 RaiseListChangedEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether adding or removing items within the list raises System.ComponentModel.BindingList events.



Get: RaiseListChangedEvents(self: BindingList[T]) -> bool



Set: RaiseListChangedEvents(self: BindingList[T])=value

"""

 SortDirectionCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the direction the list is sorted.



"""

 SortPropertyCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the property descriptor that is used for sorting the list if sorting is implemented in a derived class; otherwise,returns null.



"""

 SupportsChangeNotificationCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether System.ComponentModel.BindingList events are enabled.



"""

 SupportsSearchingCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the list supports searching.



"""

 SupportsSortingCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the list supports sorting.



"""


 AddingNew=None
 ListChanged=None

