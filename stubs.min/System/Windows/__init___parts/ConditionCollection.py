class ConditionCollection(Collection[Condition], IList[Condition], ICollection[Condition], IEnumerable[Condition], IEnumerable, IList, ICollection, IReadOnlyList[Condition], IReadOnlyCollection[Condition]):
    """
    Represents a collection of System.Windows.Condition objects.
    
    ConditionCollection()
    """
    def ClearItems(self, *args): #cannot find CLR method
        """ ClearItems(self: ConditionCollection) """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: ConditionCollection, index: int, item: Condition) """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """ RemoveItem(self: ConditionCollection, index: int) """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: ConditionCollection, index: int, item: Condition) """
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

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this trigger is read-only and cannot be changed .

Get: IsSealed(self: ConditionCollection) -> bool

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


