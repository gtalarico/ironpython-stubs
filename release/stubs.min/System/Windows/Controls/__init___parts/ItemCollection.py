class ItemCollection(CollectionView,ICollectionView,IEnumerable,INotifyCollectionChanged,INotifyPropertyChanged,IList,ICollection,IEditableCollectionViewAddNewItem,IEditableCollectionView,ICollectionViewLiveShaping,IItemProperties,IWeakEventListener):
 """ Holds the list of items that constitute the content of an System.Windows.Controls.ItemsControl. """
 def Add(self,newItem):
  """
  Add(self: ItemCollection,newItem: object) -> int

  

   Adds an item to the System.Windows.Controls.ItemCollection.

  

   newItem: The item to add to the collection.

   Returns: The zero-based index at which the object is added or -1 if the item cannot be added.
  """
  pass
 def add_CollectionChanged(self,*args):
  """ add_CollectionChanged(self: CollectionView,value: NotifyCollectionChangedEventHandler) """
  pass
 def add_PropertyChanged(self,*args):
  """ add_PropertyChanged(self: CollectionView,value: PropertyChangedEventHandler) """
  pass
 def Clear(self):
  """
  Clear(self: ItemCollection)

   Clears the collection and releases the references on all items currently in the collection.
  """
  pass
 def ClearChangeLog(self,*args):
  """
  ClearChangeLog(self: CollectionView)

   Clears any pending changes from the change log.
  """
  pass
 def ClearPendingChanges(self,*args):
  """ ClearPendingChanges(self: CollectionView) """
  pass
 def Contains(self,containItem):
  """
  Contains(self: ItemCollection,containItem: object) -> bool

  

   Returns a value that indicates whether the specified item is in this view.

  

   containItem: The object to check.

   Returns: true to indicate that the item belongs to this collection and passes the active filter; 

    otherwise,false.
  """
  pass
 def CopyTo(self,array,index):
  """
  CopyTo(self: ItemCollection,array: Array,index: int)

   Copies the elements of the collection to an array,starting at a particular array index.

  

   array: The destination array to copy to.

   index: The zero-based index in the destination array.
  """
  pass
 def DeferRefresh(self):
  """
  DeferRefresh(self: ItemCollection) -> IDisposable

  

   Enters a defer cycle that you can use to merge changes to the view and delay automatic refresh.

   Returns: An System.IDisposable object that you can use to dispose of the calling object.
  """
  pass
 def GetEnumerator(self,*args):
  """ GetEnumerator(self: ItemCollection) -> IEnumerator """
  pass
 def GetItemAt(self,index):
  """
  GetItemAt(self: ItemCollection,index: int) -> object

  

   Returns the item at the specified zero-based index in this view.

  

   index: The zero-based index at which the item is located.

   Returns: The item at the specified zero-based index in this view.
  """
  pass
 def IndexOf(self,item):
  """
  IndexOf(self: ItemCollection,item: object) -> int

  

   Returns the index in this collection where the specified item is located.

  

   item: The object to look for in the collection.

   Returns: The index of the item in the collection,or -1 if the item does not exist in the collection.
  """
  pass
 def Insert(self,insertIndex,insertItem):
  """
  Insert(self: ItemCollection,insertIndex: int,insertItem: object)

   Inserts an element into the collection at the specified index.

  

   insertIndex: The zero-based index at which to insert the item.

   insertItem: The item to insert.
  """
  pass
 def MoveCurrentTo(self,item):
  """
  MoveCurrentTo(self: ItemCollection,item: object) -> bool

  

   Sets the specified item in the collection as the 

    System.Windows.Controls.ItemCollection.CurrentItem.

  

  

   item: The item to set as the System.Windows.Controls.ItemCollection.CurrentItem.

   Returns: true to indicate that the resulting System.Windows.Controls.ItemCollection.CurrentItem is an 

    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToFirst(self):
  """
  MoveCurrentToFirst(self: ItemCollection) -> bool

  

   Sets the first item in the view as the System.Windows.Controls.ItemCollection.CurrentItem.

   Returns: true to indicate that the resulting System.Windows.Controls.ItemCollection.CurrentItem is an 

    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToLast(self):
  """
  MoveCurrentToLast(self: ItemCollection) -> bool

  

   Sets the last item in the view as the System.Windows.Controls.ItemCollection.CurrentItem.

   Returns: true to indicate that the resulting System.Windows.Controls.ItemCollection.CurrentItem is an 

    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToNext(self):
  """
  MoveCurrentToNext(self: ItemCollection) -> bool

  

   Sets the item after the System.Windows.Controls.ItemCollection.CurrentItem in the view as the 

    System.Windows.Controls.ItemCollection.CurrentItem.

  

   Returns: true to indicate that the resulting System.Windows.Controls.ItemCollection.CurrentItem is an 

    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToPosition(self,position):
  """
  MoveCurrentToPosition(self: ItemCollection,position: int) -> bool

  

   Sets the item at the specified index to be the 

    System.Windows.Controls.ItemCollection.CurrentItem in the view.

  

  

   position: The zero-based index of the item to set as the 

    System.Windows.Controls.ItemCollection.CurrentItem.

  

   Returns: true to indicate that the resulting System.Windows.Controls.ItemCollection.CurrentItem is an 

    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToPrevious(self):
  """
  MoveCurrentToPrevious(self: ItemCollection) -> bool

  

   Sets the item before the System.Windows.Controls.ItemCollection.CurrentItem in the view as the 

    System.Windows.Controls.ItemCollection.CurrentItem.

  

   Returns: true  to indicate that the resulting System.Windows.Controls.ItemCollection.CurrentItem is an 

    item within the view; otherwise,false.
  """
  pass
 def OKToChangeCurrent(self,*args):
  """
  OKToChangeCurrent(self: CollectionView) -> bool

  

   Returns a value that indicates whether the view can change which item is the 

    System.Windows.Data.CollectionView.CurrentItem.

  

   Returns: false if a listener cancels the change; otherwise,true.
  """
  pass
 def OnAllowsCrossThreadChangesChanged(self,*args):
  """ OnAllowsCrossThreadChangesChanged(self: CollectionView) """
  pass
 def OnBeginChangeLogging(self,*args):
  """
  OnBeginChangeLogging(self: CollectionView,args: NotifyCollectionChangedEventArgs)

   Called by the base class to notify the derived class that an 

    System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged event has been posted 

    to the message queue.

  

  

   args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object that is added to the 

    change log.
  """
  pass
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: CollectionView,sender: object,args: NotifyCollectionChangedEventArgs)

   Raises the System.Windows.Data.CollectionView.CollectionChanged event.

  

   sender: The sender of the event.

   args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to pass to the event 

    handler.

  

  OnCollectionChanged(self: CollectionView,args: NotifyCollectionChangedEventArgs)

   Raises the System.Windows.Data.CollectionView.CollectionChanged event.

  

   args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to pass to the event 

    handler.
  """
  pass
 def OnCurrentChanged(self,*args):
  """
  OnCurrentChanged(self: CollectionView)

   Raises the System.Windows.Data.CollectionView.CurrentChanged event.
  """
  pass
 def OnCurrentChanging(self,*args):
  """
  OnCurrentChanging(self: CollectionView,args: CurrentChangingEventArgs)

   Raises the System.Windows.Data.CollectionView.CurrentChanging event with the specified arguments.

  

   args: Information about the event.

  OnCurrentChanging(self: CollectionView)

   Raises a System.Windows.Data.CollectionView.CurrentChanging event that is not cancelable.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: CollectionView,e: PropertyChangedEventArgs)

   Raises the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event using the 

    specified arguments.

  

  

   e: Arguments of the event being raised.
  """
  pass
 def PassesFilter(self,item):
  """
  PassesFilter(self: ItemCollection,item: object) -> bool

  

   Returns a value that indicates whether the specified item belongs to this view.

  

   item: The object to test.

   Returns: true to indicate that the specified item belongs to this view or there is no filter set on this 

    collection view; otherwise,false.
  """
  pass
 def ProcessCollectionChanged(self,*args):
  """
  ProcessCollectionChanged(self: CollectionView,args: NotifyCollectionChangedEventArgs)

   When overridden in a derived class,processes a single change on the UI�thread.

  

   args: The System.Collections.Specialized.NotifyCollectionChangedEventArgs object to process.
  """
  pass
 def ProcessPendingChanges(self,*args):
  """ ProcessPendingChanges(self: CollectionView) """
  pass
 def RefreshOrDefer(self,*args):
  """
  RefreshOrDefer(self: CollectionView)

   Refreshes the view or specifies that the view needs to be refreshed when the defer cycle 

    completes.
  """
  pass
 def RefreshOverride(self,*args):
  """ RefreshOverride(self: ItemCollection) """
  pass
 def Remove(self,removeItem):
  """
  Remove(self: ItemCollection,removeItem: object)

   Removes the specified item reference from the collection or view.

  

   removeItem: The object to remove.
  """
  pass
 def RemoveAt(self,removeIndex):
  """
  RemoveAt(self: ItemCollection,removeIndex: int)

   Removes the item at the specified index of the collection or view.

  

   removeIndex: The zero-based index of the item to remove.
  """
  pass
 def remove_CollectionChanged(self,*args):
  """ remove_CollectionChanged(self: CollectionView,value: NotifyCollectionChangedEventHandler) """
  pass
 def remove_PropertyChanged(self,*args):
  """ remove_PropertyChanged(self: CollectionView,value: PropertyChangedEventHandler) """
  pass
 def SetCurrent(self,*args):
  """
  SetCurrent(self: CollectionView,newItem: object,newPosition: int,count: int)

   Sets the specified item and index as the values of the 

    System.Windows.Data.CollectionView.CurrentItem and 

    System.Windows.Data.CollectionView.CurrentPosition properties. This method can be called from a 

    constructor of a derived class.

  

  

   newItem: The item to set as the System.Windows.Data.CollectionView.CurrentItem.

   newPosition: The value to set as the System.Windows.Data.CollectionView.CurrentPosition property value.

   count: The number of items in the System.Windows.Data.CollectionView.

  SetCurrent(self: CollectionView,newItem: object,newPosition: int)

   Sets the specified item and index as the values of the 

    System.Windows.Data.CollectionView.CurrentItem and 

    System.Windows.Data.CollectionView.CurrentPosition properties.

  

  

   newItem: The item to set as the System.Windows.Data.CollectionView.CurrentItem.

   newPosition: The value to set as the System.Windows.Data.CollectionView.CurrentPosition property value.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __contains__(self,*args):
  """
  __contains__(self: IList,value: object) -> bool

  

   Determines whether the System.Collections.IList contains a specific value.

  

   value: The object to locate in the System.Collections.IList.

   Returns: true if the System.Object is found in the System.Collections.IList; otherwise,false.
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
 def __len__(self,*args):
  """ x.__len__() <==> len(x) """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 AllowsCrossThreadChanges=property(lambda self: object(),lambda self,v: None,lambda self: None)

 CanChangeLiveFiltering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CanChangeLiveFiltering(self: ItemCollection) -> bool



"""

 CanChangeLiveGrouping=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CanChangeLiveGrouping(self: ItemCollection) -> bool



"""

 CanChangeLiveSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: CanChangeLiveSorting(self: ItemCollection) -> bool



"""

 CanFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this collection view supports filtering.



Get: CanFilter(self: ItemCollection) -> bool



"""

 CanGroup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this collection view supports grouping.



Get: CanGroup(self: ItemCollection) -> bool



"""

 CanSort=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this collection view supports sorting.



Get: CanSort(self: ItemCollection) -> bool



"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of records in the collection.



Get: Count(self: ItemCollection) -> int



"""

 CurrentItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current item in the view.



Get: CurrentItem(self: ItemCollection) -> object



"""

 CurrentPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the ordinal position of the current item within the view.



Get: CurrentPosition(self: ItemCollection) -> int



"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a callback used to determine if an item is suitable for inclusion in the view.



Get: Filter(self: ItemCollection) -> Predicate[object]



Set: Filter(self: ItemCollection)=value

"""

 GroupDescriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.ComponentModel.GroupDescription objects that defines how to group the items.



Get: GroupDescriptions(self: ItemCollection) -> ObservableCollection[GroupDescription]



"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the top-level groups that are constructed according to the System.Windows.Controls.ItemCollection.GroupDescriptions.



Get: Groups(self: ItemCollection) -> ReadOnlyObservableCollection[object]



"""

 IsCurrentAfterLast=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the current item of the view is beyond the end of the collection.



Get: IsCurrentAfterLast(self: ItemCollection) -> bool



"""

 IsCurrentBeforeFirst=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the current item of the view is beyond the beginning of the collection.



Get: IsCurrentBeforeFirst(self: ItemCollection) -> bool



"""

 IsCurrentInSync=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.Windows.Data.CollectionView.CurrentItem is at the System.Windows.Data.CollectionView.CurrentPosition.



"""

 IsDynamic=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the underlying collection provides change notifications.



"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the resulting (filtered) view is empty.



Get: IsEmpty(self: ItemCollection) -> bool



"""

 IsLiveFiltering=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLiveFiltering(self: ItemCollection) -> Nullable[bool]



Set: IsLiveFiltering(self: ItemCollection)=value

"""

 IsLiveGrouping=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLiveGrouping(self: ItemCollection) -> Nullable[bool]



Set: IsLiveGrouping(self: ItemCollection)=value

"""

 IsLiveSorting=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsLiveSorting(self: ItemCollection) -> Nullable[bool]



Set: IsLiveSorting(self: ItemCollection)=value

"""

 LiveFilteringProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LiveFilteringProperties(self: ItemCollection) -> ObservableCollection[str]



"""

 LiveGroupingProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LiveGroupingProperties(self: ItemCollection) -> ObservableCollection[str]



"""

 LiveSortingProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LiveSortingProperties(self: ItemCollection) -> ObservableCollection[str]



"""

 NeedsRefresh=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the collection needs to be refreshed.



Get: NeedsRefresh(self: ItemCollection) -> bool



"""

 SortDescriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.ComponentModel.SortDescription objects that describe how the items in the collection are sorted in the view.



Get: SortDescriptions(self: ItemCollection) -> SortDescriptionCollection



"""

 SourceCollection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unsorted and unfiltered collection that underlies this collection view.



Get: SourceCollection(self: ItemCollection) -> IEnumerable



"""

 UpdatedOutsideDispatcher=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether it has been necessary to update the change log because a System.Windows.Data.CollectionView.CollectionChanged notification has been received on a different thread without first entering the user interface (UI) thread dispatcher.



"""


