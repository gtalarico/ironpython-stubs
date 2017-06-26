class ICollectionView(IEnumerable,INotifyCollectionChanged):
 """ Enables collections to have the functionalities of current record management,custom sorting,filtering,and grouping. """
 def Contains(self,item):
  """
  Contains(self: ICollectionView,item: object) -> bool
  
   Returns a value that indicates whether a given item belongs to this collection 
    view.
  
  
   item: The object to check.
   Returns: true if the item belongs to this collection view; otherwise,false.
  """
  pass
 def DeferRefresh(self):
  """
  DeferRefresh(self: ICollectionView) -> IDisposable
  
   Enters a defer cycle that you can use to merge changes to the view and delay 
    automatic refresh.
  
   Returns: An System.IDisposable object that you can use to dispose of the calling object.
  """
  pass
 def MoveCurrentTo(self,item):
  """
  MoveCurrentTo(self: ICollectionView,item: object) -> bool
  
   Sets the specified item to be the 
    System.ComponentModel.ICollectionView.CurrentItem in the view.
  
  
   item: The item to set as the System.ComponentModel.ICollectionView.CurrentItem.
   Returns: true if the resulting System.ComponentModel.ICollectionView.CurrentItem is 
    within the view; otherwise,false.
  """
  pass
 def MoveCurrentToFirst(self):
  """
  MoveCurrentToFirst(self: ICollectionView) -> bool
  
   Sets the first item in the view as the 
    System.ComponentModel.ICollectionView.CurrentItem.
  
   Returns: true if the resulting System.ComponentModel.ICollectionView.CurrentItem is an 
    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToLast(self):
  """
  MoveCurrentToLast(self: ICollectionView) -> bool
  
   Sets the last item in the view as the 
    System.ComponentModel.ICollectionView.CurrentItem.
  
   Returns: true if the resulting System.ComponentModel.ICollectionView.CurrentItem is an 
    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToNext(self):
  """
  MoveCurrentToNext(self: ICollectionView) -> bool
  
   Sets the item after the System.ComponentModel.ICollectionView.CurrentItem in 
    the view as the System.ComponentModel.ICollectionView.CurrentItem.
  
   Returns: true if the resulting System.ComponentModel.ICollectionView.CurrentItem is an 
    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToPosition(self,position):
  """
  MoveCurrentToPosition(self: ICollectionView,position: int) -> bool
  
   Sets the item at the specified index to be the 
    System.ComponentModel.ICollectionView.CurrentItem in the view.
  
  
   position: The index to set the System.ComponentModel.ICollectionView.CurrentItem to.
   Returns: true if the resulting System.ComponentModel.ICollectionView.CurrentItem is an 
    item within the view; otherwise,false.
  """
  pass
 def MoveCurrentToPrevious(self):
  """
  MoveCurrentToPrevious(self: ICollectionView) -> bool
  
   Sets the item before the System.ComponentModel.ICollectionView.CurrentItem in 
    the view as the System.ComponentModel.ICollectionView.CurrentItem.
  
   Returns: true if the resulting System.ComponentModel.ICollectionView.CurrentItem is an 
    item within the view; otherwise,false.
  """
  pass
 def Refresh(self):
  """
  Refresh(self: ICollectionView)
   Recreates the view.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 CanFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this view supports filtering via the System.ComponentModel.ICollectionView.Filter property.

Get: CanFilter(self: ICollectionView) -> bool

"""

 CanGroup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this view supports grouping via the System.ComponentModel.ICollectionView.GroupDescriptions property.

Get: CanGroup(self: ICollectionView) -> bool

"""

 CanSort=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this view supports sorting via the System.ComponentModel.ICollectionView.SortDescriptions property.

Get: CanSort(self: ICollectionView) -> bool

"""

 Culture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cultural info for any operations of the view that may differ by culture,such as sorting.

Get: Culture(self: ICollectionView) -> CultureInfo

Set: Culture(self: ICollectionView)=value
"""

 CurrentItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current item in the view.

Get: CurrentItem(self: ICollectionView) -> object

"""

 CurrentPosition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the ordinal position of the System.ComponentModel.ICollectionView.CurrentItem within the view.

Get: CurrentPosition(self: ICollectionView) -> int

"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a callback used to determine if an item is suitable for inclusion in the view.

Get: Filter(self: ICollectionView) -> Predicate[object]

Set: Filter(self: ICollectionView)=value
"""

 GroupDescriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.ComponentModel.GroupDescription objects that describe how the items in the collection are grouped in the view.

Get: GroupDescriptions(self: ICollectionView) -> ObservableCollection[GroupDescription]

"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the top-level groups.

Get: Groups(self: ICollectionView) -> ReadOnlyObservableCollection[object]

"""

 IsCurrentAfterLast=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.ICollectionView.CurrentItem of the view is beyond the end of the collection.

Get: IsCurrentAfterLast(self: ICollectionView) -> bool

"""

 IsCurrentBeforeFirst=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.ICollectionView.CurrentItem of the view is beyond the beginning of the collection.

Get: IsCurrentBeforeFirst(self: ICollectionView) -> bool

"""

 IsEmpty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns a value that indicates whether the resulting view is empty.

Get: IsEmpty(self: ICollectionView) -> bool

"""

 SortDescriptions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of System.ComponentModel.SortDescription objects that describe how the items in the collection are sorted in the view.

Get: SortDescriptions(self: ICollectionView) -> SortDescriptionCollection

"""

 SourceCollection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the underlying collection.

Get: SourceCollection(self: ICollectionView) -> IEnumerable

"""


 CurrentChanged=None
 CurrentChanging=None

