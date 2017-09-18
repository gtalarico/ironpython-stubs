class IBindingListView(IBindingList,IList,ICollection,IEnumerable):
 """ Extends the System.ComponentModel.IBindingList interface by providing advanced sorting and filtering capabilities. """
 def ApplySort(self,sorts):
  """
  ApplySort(self: IBindingListView,sorts: ListSortDescriptionCollection)

   Sorts the data source based on the given System.ComponentModel.ListSortDescriptionCollection.

  

   sorts: The System.ComponentModel.ListSortDescriptionCollection containing the sorts to apply to the 

    data source.
  """
  pass
 def RemoveFilter(self):
  """
  RemoveFilter(self: IBindingListView)

   Removes the current filter applied to the data source.
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
 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the filter to be used to exclude items from the collection of items returned by the data source



Get: Filter(self: IBindingListView) -> str



Set: Filter(self: IBindingListView)=value

"""

 SortDescriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of sort descriptions currently applied to the data source.



Get: SortDescriptions(self: IBindingListView) -> ListSortDescriptionCollection



"""

 SupportsAdvancedSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the data source supports advanced sorting.



Get: SupportsAdvancedSorting(self: IBindingListView) -> bool



"""

 SupportsFiltering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the data source supports filtering.



Get: SupportsFiltering(self: IBindingListView) -> bool



"""


