class GeometryCollection(Animatable, ISealable, IAnimatable, IResource, IList, ICollection, IEnumerable, IList[Geometry], ICollection[Geometry], IEnumerable[Geometry]):
    """
    Represents a collection of System.Windows.Media.Geometry objects.
    
    GeometryCollection()
    GeometryCollection(capacity: int)
    GeometryCollection(collection: IEnumerable[Geometry])
    """
    def Add(self, value):
        """
        Add(self: GeometryCollection, value: Geometry)
            Adds a System.Windows.Media.Geometry to the end of the collection.
        
            value: The System.Windows.Media.Geometry to add to the end of the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: GeometryCollection)
            Removes all System.Windows.Media.Geometry objects from the collection.
        """
        pass

    def Clone(self):
        """
        Clone(self: GeometryCollection) -> GeometryCollection
        
            Creates a modifiable clone of this System.Windows.Media.GeometryCollection, making deep copies of this object's values. When copying dependency properties, this method copies resource references and data 
             bindings (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: GeometryCollection, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: GeometryCollection) -> GeometryCollection
        
            Creates a modifiable clone of this System.Windows.Media.GeometryCollection object, making deep copies of this object's current values. Resource references, data bindings, and animations are not copied, but 
             their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: GeometryCollection, source: Freezable) """
        pass

    def Contains(self, value):
        """
        Contains(self: GeometryCollection, value: Geometry) -> bool
        
            Returns a value that indicates whether the collection contains the specified System.Windows.Media.Geometry.
        
            value: The System.Windows.Media.Geometry to locate in the collection.
            Returns: true if value is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: GeometryCollection, array: Array[Geometry], index: int)
            Copies all of the System.Windows.Media.Geometry objects in a collection to a specified array.
        
            array: Identifies the array to which content is copied.
            index: Index position in the array to which the contents of the collection are copied.
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
        """ CreateInstanceCore(self: GeometryCollection) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """ FreezeCore(self: GeometryCollection, isChecking: bool) -> bool """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: GeometryCollection, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: GeometryCollection, source: Freezable) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: GeometryCollection) -> Enumerator
        
            Returns an enumerator that can iterate through the collection.
            Returns: An System.Windows.Media.GeometryCollection.Enumerator that can iterate through the collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: GeometryCollection, value: Geometry) -> int
        
            Searches for the specified System.Windows.Media.Geometry and returns the zero-based index of the first occurrence within the entire collection.
        
            value: The System.Windows.Media.Geometry to locate in the collection.
            Returns: The zero-based index of the first occurrence of value within the entire collection, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: GeometryCollection, index: int, value: Geometry)
            Inserts a System.Windows.Media.Geometry into a specific location within the collection.
        
            index: The index position at which the System.Windows.Media.Geometry is inserted.
            value: The System.Windows.Media.Geometry object to insert in the collection.
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
        Remove(self: GeometryCollection, value: Geometry) -> bool
        
            Removes the first occurrence of the specified System.Windows.Media.Geometry  from this System.Windows.Media.GeometryCollection.
        
            value: The System.Windows.Media.Geometry  to remove from this System.Windows.Media.GeometryCollection.
            Returns: true if value was removed from the collection; otherwise, false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: GeometryCollection, index: int)
            Removes the System.Windows.Media.Geometry  at the specified index from this System.Windows.Media.GeometryCollection.
        
            index: The index of the System.Windows.Media.Geometry  to remove.
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
        __contains__(self: ICollection[Geometry], item: Geometry) -> bool
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
        __new__(cls: type, collection: IEnumerable[Geometry])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of geometries contained in the System.Windows.Media.GeometryCollection.

Get: Count(self: GeometryCollection) -> int

"""


    Enumerator = None

