class PathSegmentCollection(Animatable, ISealable, IAnimatable, IResource, IList, ICollection, IEnumerable, IList[PathSegment], ICollection[PathSegment], IEnumerable[PathSegment]):
    """
    Represents a collection of System.Windows.Media.PathSegment objects that can be individually accessed by index.
    
    PathSegmentCollection()
    PathSegmentCollection(capacity: int)
    PathSegmentCollection(collection: IEnumerable[PathSegment])
    """
    def Add(self, value):
        """
        Add(self: PathSegmentCollection, value: PathSegment)
            Adds a System.Windows.Media.PathSegment to the end of the collection.
        
            value: The segment to add to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: PathSegmentCollection)
            Clears the collection of all segments and resets System.Windows.Media.PathSegmentCollection.Count to zero.
        """
        pass

    def Clone(self):
        """
        Clone(self: PathSegmentCollection) -> PathSegmentCollection
        
            Creates a modifiable clone of this System.Windows.Media.PathSegmentCollection, making deep copies of this object's values. When copying dependency properties, this method copies resource references and 
             data bindings (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: PathSegmentCollection, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: PathSegmentCollection) -> PathSegmentCollection
        
            Creates a modifiable clone of this System.Windows.Media.PathSegmentCollection object, making deep copies of this object's current values. Resource references, data bindings, and animations are not copied, 
             but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: PathSegmentCollection, source: Freezable) """
        pass

    def Contains(self, value):
        """
        Contains(self: PathSegmentCollection, value: PathSegment) -> bool
        
            Returns a System.Boolean that indicates whether the specified System.Windows.Media.PathSegment is contained within the collection.
        
            value: The System.Windows.Media.PathSegment to search for.
            Returns: true if the specified System.Windows.Media.PathSegment is contained within the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: PathSegmentCollection, array: Array[PathSegment], index: int)
            Copies the entire System.Windows.Media.PathSegmentCollection to a one-dimensional System.Windows.Media.PathSegment array, starting at the specified index of the target array.
        
            array: The array into which the collection's items are to be copied.
            index: The index of array at which to start copying the contents of the System.Windows.Media.PathSegmentCollection.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: PathSegmentCollection) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """ FreezeCore(self: PathSegmentCollection, isChecking: bool) -> bool """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: PathSegmentCollection, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: PathSegmentCollection, source: Freezable) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PathSegmentCollection) -> Enumerator
        
            Returns an enumerator that can iterate through the collection.
            Returns: An System.Windows.Media.PathSegmentCollection.Enumerator that can iterate through the collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: PathSegmentCollection, value: PathSegment) -> int
        
            Returns the index of the first occurrence of the specified System.Windows.Media.PathSegment.
        
            value: The item to search for.
            Returns: The index of the specified System.Windows.Media.PathSegment.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: PathSegmentCollection, index: int, value: PathSegment)
            Inserts a System.Windows.Media.PathSegment into this System.Windows.Media.PathSegmentCollection at the specified index.
        
            index: The index at which to insert value, the specified System.Windows.Media.PathSegment.
            value: The item to insert.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a System.Windows.DependencyObjectType data member that has just been set.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventArgs) to also invoke any 
             System.Windows.Freezable.Changed handlers in response to a changing dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of System.Windows.Freezable must call this method at the beginning of any API that reads data members that are 
             not dependency properties.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: PathSegmentCollection, value: PathSegment) -> bool
        
            Removes the first occurrence of the specified System.Windows.Media.PathSegment from this System.Windows.Media.PathSegmentCollection.
        
            value: The item to remove from this collection.
            Returns: true if the specified System.Windows.Media.PathSegment is removed from the collection; otherwise, false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: PathSegmentCollection, index: int)
            Removes the System.Windows.Media.PathSegment at the specified index from this System.Windows.Media.PathSegmentCollection.
        
            index: The index of the item to remove.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable should call 
             this method at the end of any API that modifies class members that are not stored as dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a valid threading context. System.Windows.Freezable inheritors should call this method at the beginning of any 
             API that writes to data members that are not dependency properties.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[PathSegment], item: PathSegment) -> bool
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, capacity: int)
        __new__(cls: type, collection: IEnumerable[PathSegment])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of path segments contained in the System.Windows.Media.PathSegmentCollection.

Get: Count(self: PathSegmentCollection) -> int

"""


    Enumerator = None

