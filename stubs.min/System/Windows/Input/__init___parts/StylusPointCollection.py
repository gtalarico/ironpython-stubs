class StylusPointCollection(Collection[StylusPoint], IList[StylusPoint], ICollection[StylusPoint], IEnumerable[StylusPoint], IEnumerable, IList, ICollection, IReadOnlyList[StylusPoint], IReadOnlyCollection[StylusPoint]):
    """
    Contains a collection of System.Windows.Input.StylusPoint objects.
    
    StylusPointCollection()
    StylusPointCollection(initialCapacity: int)
    StylusPointCollection(stylusPointDescription: StylusPointDescription)
    StylusPointCollection(stylusPointDescription: StylusPointDescription, initialCapacity: int)
    StylusPointCollection(stylusPoints: IEnumerable[StylusPoint])
    StylusPointCollection(points: IEnumerable[Point])
    """
    def Add(self, *__args):
        """
        Add(self: StylusPointCollection, stylusPoints: StylusPointCollection)
            Adds the specified System.Windows.Input.StylusPointCollection to the current System.Windows.Input.StylusPointCollection.
        
            stylusPoints: The System.Windows.Input.StylusPointCollection to add to the current System.Windows.Input.StylusPointCollection.
        """
        pass

    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: StylusPointCollection)
            Removes all System.Windows.Input.StylusPoint objects from the System.Windows.Input.StylusPointCollection.
        """
        pass

    def Clone(self):
        """
        Clone(self: StylusPointCollection) -> StylusPointCollection
        
            Copies the System.Windows.Input.StylusPointCollection.
            Returns: A new System.Windows.Input.StylusPointCollection that contains copies of the System.Windows.Input.StylusPoint objects in the current System.Windows.Input.StylusPointCollection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """
        InsertItem(self: StylusPointCollection, index: int, stylusPoint: StylusPoint)
            Inserts the specified System.Windows.Input.StylusPoint into the System.Windows.Input.StylusPointCollection at the specified position.
        
            index: The position at which to insert the System.Windows.Input.StylusPoint.
            stylusPoint: The System.Windows.Input.StylusPoint to insert into the System.Windows.Input.StylusPointCollection.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: StylusPointCollection, e: EventArgs)
            Raises the System.Windows.Input.StylusPointCollection.Changed event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def Reformat(self, subsetToReformatTo):
        """
        Reformat(self: StylusPointCollection, subsetToReformatTo: StylusPointDescription) -> StylusPointCollection
        
            Finds the intersection of the specified System.Windows.Input.StylusPointDescription and the System.Windows.Input.StylusPointCollection.Description property.
        
            subsetToReformatTo: A System.Windows.Input.StylusPointDescription to intersect with the System.Windows.Input.StylusPointDescription of the current System.Windows.Input.StylusPointCollection.
            Returns: A System.Windows.Input.StylusPointCollection that has a System.Windows.Input.StylusPointDescription that is a subset of the specified System.Windows.Input.StylusPointDescription and the 
             System.Windows.Input.StylusPointDescription that the current System.Windows.Input.StylusPointCollection uses.
        """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: StylusPointCollection, index: int)
            Removes the System.Windows.Input.StylusPoint at the specified position from the System.Windows.Input.StylusPointCollection.
        
            index: The position at which to remove the System.Windows.Input.StylusPoint.
        """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """
        SetItem(self: StylusPointCollection, index: int, stylusPoint: StylusPoint)
            Sets the specified System.Windows.Input.StylusPoint at the specified position.
        
            index: The position at which to set the System.Windows.Input.StylusPoint.
            stylusPoint: The System.Windows.Input.StylusPoint to set at the specified position.
        """
        pass

    def ToHiMetricArray(self):
        """
        ToHiMetricArray(self: StylusPointCollection) -> Array[int]
        
            Converts the property values of the System.Windows.Input.StylusPoint objects into a 32-bit signed integer array.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, initialCapacity: int)
        __new__(cls: type, stylusPointDescription: StylusPointDescription)
        __new__(cls: type, stylusPointDescription: StylusPointDescription, initialCapacity: int)
        __new__(cls: type, stylusPoints: IEnumerable[StylusPoint])
        __new__(cls: type, points: IEnumerable[Point])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Input.StylusPointDescription that is associated with the System.Windows.Input.StylusPoint objects in the System.Windows.Input.StylusPointCollection.

Get: Description(self: StylusPointCollection) -> StylusPointDescription

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


    Changed = None

