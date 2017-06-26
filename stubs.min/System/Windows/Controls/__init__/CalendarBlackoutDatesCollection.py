class CalendarBlackoutDatesCollection(ObservableCollection[CalendarDateRange], IList[CalendarDateRange], ICollection[CalendarDateRange], IEnumerable[CalendarDateRange], IEnumerable, IList, ICollection, IReadOnlyList[CalendarDateRange], IReadOnlyCollection[CalendarDateRange], INotifyCollectionChanged, INotifyPropertyChanged):
    """
    Represents a collection of non-selectable dates in a System.Windows.Controls.Calendar.
    
    CalendarBlackoutDatesCollection(owner: Calendar)
    """
    def AddDatesInPast(self):
        """
        AddDatesInPast(self: CalendarBlackoutDatesCollection)
            Adds all dates before System.DateTime.Today to the collection.
        """
        pass

    def add_PropertyChanged(self, *args): #cannot find CLR method
        """ add_PropertyChanged(self: ObservableCollection[CalendarDateRange], value: PropertyChangedEventHandler) """
        pass

    def BlockReentrancy(self, *args): #cannot find CLR method
        """
        BlockReentrancy(self: ObservableCollection[CalendarDateRange]) -> IDisposable
        
            Disallows reentrant attempts to change this collection.
            Returns: An System.IDisposable object that can be used to dispose of the object.
        """
        pass

    def CheckReentrancy(self, *args): #cannot find CLR method
        """
        CheckReentrancy(self: ObservableCollection[CalendarDateRange])
            Checks for reentrant attempts to change this collection.
        """
        pass

    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: CalendarBlackoutDatesCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: CalendarBlackoutDatesCollection, start: DateTime, end: DateTime) -> bool
        
            Returns a value that represents whether this collection contains the specified range of dates.
        
            start: The start of the date range.
            end: The end of the date range.
            Returns: true if all dates in the range are contained in the collection; otherwise, false.
        Contains(self: CalendarBlackoutDatesCollection, date: DateTime) -> bool
        
            Returns a value that represents whether this collection contains the specified date.
        
            date: The date to search for.
            Returns: true if the collection contains the specified date; otherwise, false.
        """
        pass

    def ContainsAny(self, range):
        """
        ContainsAny(self: CalendarBlackoutDatesCollection, range: CalendarDateRange) -> bool
        
            Returns a value that represents whether this collection contains any dates in the specified range of dates.
        
            range: The range of dates to search for.
            Returns: true if any dates in the range are contained in the collection; otherwise, false.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: CalendarBlackoutDatesCollection, index: int, item: CalendarDateRange) """
        pass

    def MoveItem(self, *args): #cannot find CLR method
        """
        MoveItem(self: ObservableCollection[CalendarDateRange], oldIndex: int, newIndex: int)
            Moves the item at the specified index to a new location in the collection.
        
            oldIndex: The zero-based index specifying the location of the item to be moved.
            newIndex: The zero-based index specifying the new location of the item.
        """
        pass

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """
        OnCollectionChanged(self: ObservableCollection[CalendarDateRange], e: NotifyCollectionChangedEventArgs)
            Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.
        
            e: Arguments of the event being raised.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: ObservableCollection[CalendarDateRange], e: PropertyChangedEventArgs)
            Raises the System.Collections.ObjectModel.ObservableCollection event with the provided arguments.
        
            e: Arguments of the event being raised.
        """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: CalendarBlackoutDatesCollection, index: int) """
        pass

    def remove_PropertyChanged(self, *args): #cannot find CLR method
        """ remove_PropertyChanged(self: ObservableCollection[CalendarDateRange], value: PropertyChangedEventHandler) """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: CalendarBlackoutDatesCollection, index: int, item: CalendarDateRange) """
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


