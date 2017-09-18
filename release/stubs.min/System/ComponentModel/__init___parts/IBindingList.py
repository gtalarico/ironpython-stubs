class IBindingList(IList,ICollection,IEnumerable):
 """ Provides the features required to support both complex and simple scenarios when binding to a data source. """
 def AddIndex(self,property):
  """
  AddIndex(self: IBindingList,property: PropertyDescriptor)

   Adds the System.ComponentModel.PropertyDescriptor to the indexes used for searching.

  

   property: The System.ComponentModel.PropertyDescriptor to add to the indexes used for searching.
  """
  pass
 def AddNew(self):
  """
  AddNew(self: IBindingList) -> object

  

   Adds a new item to the list.

   Returns: The item added to the list.
  """
  pass
 def ApplySort(self,property,direction):
  """
  ApplySort(self: IBindingList,property: PropertyDescriptor,direction: ListSortDirection)

   Sorts the list based on a System.ComponentModel.PropertyDescriptor and a 

    System.ComponentModel.ListSortDirection.

  

  

   property: The System.ComponentModel.PropertyDescriptor to sort by.

   direction: One of the System.ComponentModel.ListSortDirection values.
  """
  pass
 def Find(self,property,key):
  """
  Find(self: IBindingList,property: PropertyDescriptor,key: object) -> int

  

   Returns the index of the row that has the given System.ComponentModel.PropertyDescriptor.

  

   property: The System.ComponentModel.PropertyDescriptor to search on.

   key: The value of the property parameter to search for.

   Returns: The index of the row that has the given System.ComponentModel.PropertyDescriptor.
  """
  pass
 def RemoveIndex(self,property):
  """
  RemoveIndex(self: IBindingList,property: PropertyDescriptor)

   Removes the System.ComponentModel.PropertyDescriptor from the indexes used for searching.

  

   property: The System.ComponentModel.PropertyDescriptor to remove from the indexes used for searching.
  """
  pass
 def RemoveSort(self):
  """
  RemoveSort(self: IBindingList)

   Removes any sort applied using 

    System.ComponentModel.IBindingList.ApplySort(System.ComponentModel.PropertyDescriptor,System.Comp

    onentModel.ListSortDirection).
  """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IList,value: object) -> bool

  

   Determines whether the System.Collections.IList contains a specific value.

  

   value: The object to locate in the System.Collections.IList.

   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 AllowEdit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether you can update items in the list.



Get: AllowEdit(self: IBindingList) -> bool



"""

 AllowNew=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether you can add items to the list using System.ComponentModel.IBindingList.AddNew.



Get: AllowNew(self: IBindingList) -> bool



"""

 AllowRemove=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether you can remove items from the list,using System.Collections.IList.Remove(System.Object) or System.Collections.IList.RemoveAt(System.Int32).



Get: AllowRemove(self: IBindingList) -> bool



"""

 IsSorted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the items in the list are sorted.



Get: IsSorted(self: IBindingList) -> bool



"""

 SortDirection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the direction of the sort.



Get: SortDirection(self: IBindingList) -> ListSortDirection



"""

 SortProperty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.ComponentModel.PropertyDescriptor that is being used for sorting.



Get: SortProperty(self: IBindingList) -> PropertyDescriptor



"""

 SupportsChangeNotification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether a System.ComponentModel.IBindingList.ListChanged event is raised when the list changes or an item in the list changes.



Get: SupportsChangeNotification(self: IBindingList) -> bool



"""

 SupportsSearching=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the list supports searching using the System.ComponentModel.IBindingList.Find(System.ComponentModel.PropertyDescriptor,System.Object) method.



Get: SupportsSearching(self: IBindingList) -> bool



"""

 SupportsSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the list supports sorting.



Get: SupportsSorting(self: IBindingList) -> bool



"""


 ListChanged=None

