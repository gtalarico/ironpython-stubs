class SelectedDatesCollection(ObservableCollection[DateTime],IList[DateTime],ICollection[DateTime],IEnumerable[DateTime],IEnumerable,IList,ICollection,IReadOnlyList[DateTime],IReadOnlyCollection[DateTime],INotifyCollectionChanged,INotifyPropertyChanged):
 """
 Represents a set of selected dates in a System.Windows.Controls.Calendar.

 

 SelectedDatesCollection(owner: Calendar)
 """
 def AddRange(self,start,end):
  """
  AddRange(self: SelectedDatesCollection,start: DateTime,end: DateTime)

   Adds all the dates in the specified range,which includes the first and last dates,to the 

    collection.

  

  

   start: The first date to add to the collection.

   end: The last date to add to the collection.
  """
  pass
 def add_PropertyChanged(self,*args):
  """ add_PropertyChanged(self: ObservableCollection[DateTime],value: PropertyChangedEventHandler) """
  pass
 def BlockReentrancy(self,*args):
  """
  BlockReentrancy(self: ObservableCollection[DateTime]) -> IDisposable

  

   Disallows reentrant attempts to change this collection.

   Returns: An System.IDisposable object that can be used to dispose of the object.
  """
  pass
 def CheckReentrancy(self,*args):
  """
  CheckReentrancy(self: ObservableCollection[DateTime])

   Checks for reentrant attempts to change this collection.
  """
  pass
 def ClearItems(self,*args):
  """ ClearItems(self: SelectedDatesCollection) """
  pass
 def InsertItem(self,*args):
  """ InsertItem(self: SelectedDatesCollection,index: int,item: DateTime) """
  pass
 def MoveItem(self,*args):
  """
  MoveItem(self: ObservableCollection[DateTime],oldIndex: int,newIndex: int)

   Moves the item at the specified index to a new location in the collection.

  

   oldIndex: The zero-based index specifying the location of the item to be moved.

   newIndex: The zero-based index specifying the new location of the item.
  """
  pass
 def OnCollectionChanged(self,*args):
  """
  OnCollectionChanged(self: ObservableCollection[DateTime],e: NotifyCollectionChangedEventArgs)

   Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.

  

   e: Arguments of the event being raised.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: ObservableCollection[DateTime],e: PropertyChangedEventArgs)

   Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.

  

   e: Arguments of the event being raised.
  """
  pass
 def RemoveItem(self,*args):
  """ RemoveItem(self: SelectedDatesCollection,index: int) """
  pass
 def remove_PropertyChanged(self,*args):
  """ remove_PropertyChanged(self: ObservableCollection[DateTime],value: PropertyChangedEventHandler) """
  pass
 def SetItem(self,*args):
  """ SetItem(self: SelectedDatesCollection,index: int,item: DateTime) """
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
 def __new__(self,owner):
  """ __new__(cls: type,owner: Calendar) """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.



"""


