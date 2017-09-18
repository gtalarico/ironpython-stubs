class GridViewColumnCollection(ObservableCollection[GridViewColumn],IList[GridViewColumn],ICollection[GridViewColumn],IEnumerable[GridViewColumn],IEnumerable,IList,ICollection,IReadOnlyList[GridViewColumn],IReadOnlyCollection[GridViewColumn],INotifyCollectionChanged,INotifyPropertyChanged):
 """
 Represents a collection of System.Windows.Controls.GridViewColumn objects.

 

 GridViewColumnCollection()
 """
 def add_PropertyChanged(self,*args):
  """ add_PropertyChanged(self: ObservableCollection[GridViewColumn],value: PropertyChangedEventHandler) """
  pass
 def BlockReentrancy(self,*args):
  """
  BlockReentrancy(self: ObservableCollection[GridViewColumn]) -> IDisposable

  

   Disallows reentrant attempts to change this collection.

   Returns: An System.IDisposable object that can be used to dispose of the object.
  """
  pass
 def CheckReentrancy(self,*args):
  """
  CheckReentrancy(self: ObservableCollection[GridViewColumn])

   Checks for reentrant attempts to change this collection.
  """
  pass
 def ClearItems(self,*args):
  """
  ClearItems(self: GridViewColumnCollection)

   Removes all of the System.Windows.Controls.GridViewColumn objects from the 

    System.Windows.Controls.GridViewColumnCollection.
  """
  pass
 def InsertItem(self,*args):
  """
  InsertItem(self: GridViewColumnCollection,index: int,column: GridViewColumn)

   Adds a System.Windows.Controls.GridViewColumn to the collection at the specified index.

  

   index: The position to place the new System.Windows.Controls.GridViewColumn.

   column: The System.Windows.Controls.GridViewColumn to insert.
  """
  pass
 def MoveItem(self,*args):
  """
  MoveItem(self: GridViewColumnCollection,oldIndex: int,newIndex: int)

   Changes the position of a System.Windows.Controls.GridViewColumn in the collection.

  

   oldIndex: The original position of the System.Windows.Controls.GridViewColumn.

   newIndex: The new position of the System.Windows.Controls.GridViewColumn.
  """
  pass
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: GridViewColumnCollection,e: NotifyCollectionChangedEventArgs)

   Raises the System.Collections.ObjectModel.ObservableCollection event when the 

    System.Windows.Controls.GridViewColumnCollection changes.

  

  

   e: The event arguments.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: ObservableCollection[GridViewColumn],e: PropertyChangedEventArgs)

   Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.

  

   e: Arguments of the event being raised.
  """
  pass
 def RemoveItem(self,*args):
  """
  RemoveItem(self: GridViewColumnCollection,index: int)

   Removes a System.Windows.Controls.GridViewColumn from the 

    System.Windows.Controls.GridViewColumnCollection at the specified index.

  

  

   index: The position of the System.Windows.Controls.GridViewColumn to remove.
  """
  pass
 def remove_PropertyChanged(self,*args):
  """ remove_PropertyChanged(self: ObservableCollection[GridViewColumn],value: PropertyChangedEventHandler) """
  pass
 def SetItem(self,*args):
  """
  SetItem(self: GridViewColumnCollection,index: int,column: GridViewColumn)

   Replaces the System.Windows.Controls.GridViewColumn that is at the specified index with another 

    System.Windows.Controls.GridViewColumn.

  

  

   index: The position at which the new System.Windows.Controls.GridViewColumn replaces the old 

    System.Windows.Controls.GridViewColumn.

  

   column: The System.Windows.Controls.GridViewColumn to place at the specified position.
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
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.



"""


