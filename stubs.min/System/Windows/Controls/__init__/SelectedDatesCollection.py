class SelectedDatesCollection(ObservableCollection[DateTime], IList[DateTime], ICollection[DateTime], IEnumerable[DateTime], IEnumerable, IList, ICollection, IReadOnlyList[DateTime], IReadOnlyCollection[DateTime], INotifyCollectionChanged, INotifyPropertyChanged):
    """
    Represents a set of selected dates in a System.Windows.Controls.Calendar.
    
    SelectedDatesCollection(owner: Calendar)
    """
    def AddRange(self, start, end):
        """
        AddRange(self: SelectedDatesCollection, start: DateTime, end: DateTime)
            Adds all the dates in the specified range, which includes the first and last dates, to the collection.
        
            start: The first date to add to the collection.
            end: The last date to add to the collection.
        """
        pass

    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: ObservableCollection[DateTime], value: PropertyChangedEventHandler) """
        pass

    def BlockReentrancy(self, *args): #cannot find CLR method
        """
        BlockReentrancy(self: ObservableCollection[DateTime]) -> IDisposable
        
            Disallows reentrant attempts to change this collection.
            Returns: An System.IDisposable object that can be used to dispose of the object.
        """
        pass

    def CheckReentrancy(self, *args): #cannot find CLR method
        """
        CheckReentrancy(self: ObservableCollection[DateTime])
            Checks for reentrant attempts to change this collection.
        """
        pass

    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: SelectedDatesCollection) """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: SelectedDatesCollection, index: int, item: DateTime) """
        pass

    def MoveItem(self, *args): #cannot find CLR method
        """
        MoveItem(self: ObservableCollection[DateTime], oldIndex: int, newIndex: int)
            Moves the item at the specified index to a new location in the collection.
        
            oldIndex: The zero-based index specifying the location of the item to be moved.
            newIndex: The zero-based index specifying the new location of the item.
        """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: ObservableCollection[DateTime], e: NotifyCollectionChangedEventArgs)
            Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.
        
            e: Arguments of the event being raised.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: ObservableCollection[DateTime], e: PropertyChangedEventArgs)
            Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.
        
            e: Arguments of the event being raised.
        """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: SelectedDatesCollection, index: int) """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: ObservableCollection[DateTime], value: PropertyChangedEventHandler) """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: SelectedDatesCollection, index: int, item: DateTime) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: Calendar) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


