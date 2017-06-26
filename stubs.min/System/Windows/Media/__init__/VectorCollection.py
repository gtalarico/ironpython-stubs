class VectorCollection(Freezable, ISealable, IFormattable, IList, ICollection, IEnumerable, IList[Vector], ICollection[Vector], IEnumerable[Vector]):
    """
    Represents an ordered collection of System.Windows.Vector values.
    
    VectorCollection()
    VectorCollection(capacity: int)
    VectorCollection(collection: IEnumerable[Vector])
    """
    def Add(self, value):
        """
        Add(self: VectorCollection, value: Vector)
            Adds a System.Windows.Vector to the end of the System.Windows.Media.VectorCollection.
        
            value: The System.Windows.Vector to add to the end of the System.Windows.Media.VectorCollection.
        """
        pass

    def Clear(self):
        """
        Clear(self: VectorCollection)
            Removes all items from the System.Windows.Media.VectorCollection.
        """
        pass

    def Clone(self):
        """
        Clone(self: VectorCollection) -> VectorCollection
        
            Creates a modifiable clone of this System.Windows.Media.VectorCollection, making deep copies of this object's values. When copying dependency properties, this method copies resource references and data 
             bindings (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: VectorCollection, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: VectorCollection) -> VectorCollection
        
            Creates a modifiable clone of this System.Windows.Media.VectorCollection object, making deep copies of this object's current values. Resource references, data bindings, and animations are not copied, but 
             their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: VectorCollection, source: Freezable) """
        pass

    def Contains(self, value):
        """
        Contains(self: VectorCollection, value: Vector) -> bool
        
            Determines whether the System.Windows.Media.VectorCollection contains the specified System.Windows.Vector.
        
            value: The System.Windows.Vector to locate in the System.Windows.Media.VectorCollection.
            Returns: true if the System.Windows.Vector is found in the System.Windows.Media.VectorCollection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: VectorCollection, array: Array[Vector], index: int)
            Copies the items of the System.Windows.Media.VectorCollection to an array, starting at the specified array index.
        
            array: The one-dimensional array that is the destination of the items copied from the System.Windows.Media.VectorCollection. The array must have zero-based indexing.
            index: The zero-based index in array at which copying begins.
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
        """ CreateInstanceCore(self: VectorCollection) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made unmodifiable.
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); false to actually freeze the object.
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method returns true if the 
             if the specified System.Windows.Freezable is now unmodifiable, or false if it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: VectorCollection, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: VectorCollection, source: Freezable) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: VectorCollection) -> Enumerator
        
            Returns an enumerator that can iterate through the System.Windows.Media.VectorCollection.
            Returns: An System.Windows.Media.VectorCollection.Enumerator that can be used to iterate through the System.Windows.Media.VectorCollection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: VectorCollection, value: Vector) -> int
        
            Determines the index of the specified item in the System.Windows.Media.VectorCollection.
        
            value: The System.Windows.Vector to locate in the System.Windows.Media.VectorCollection.
            Returns: The index of value if found in the System.Windows.Media.VectorCollection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: VectorCollection, index: int, value: Vector)
            Inserts a System.Windows.Vector into the System.Windows.Media.VectorCollection at the specified index.
        
            index: The zero-based index at which value should be inserted.
            value: The System.Windows.Vector to insert into the System.Windows.Media.VectorCollection.
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

    @staticmethod
    def Parse(source):
        """
        Parse(source: str) -> VectorCollection
        
            Converts a System.String representation of a collection of vectors into an equivalent System.Windows.Media.VectorCollection.
        
            source: The System.String representation of the collection of vectors.
            Returns: Returns the equivalent System.Windows.Media.VectorCollection.
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
        Remove(self: VectorCollection, value: Vector) -> bool
        
            Removes the first occurrence of the specified System.Windows.Vector from the System.Windows.Media.VectorCollection.
        
            value: The System.Windows.Vector to remove from the System.Windows.Media.VectorCollection.
            Returns: true if value was removed from the System.Windows.Media.VectorCollection; otherwise, false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: VectorCollection, index: int)
            Removes the System.Windows.Vector at the specified index.
        
            index: The zero-based index of the System.Windows.Vector to remove.
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

    def ToString(self, provider=None):
        """
        ToString(self: VectorCollection, provider: IFormatProvider) -> str
        
            Creates a System.String representation of this System.Windows.Media.VectorCollection.
        
            provider: Culture-specific formatting information.
            Returns: Returns a System.String containing the System.Windows.Vector.X and System.Windows.Vector.Y values of the System.Windows.Vector structures in this System.Windows.Media.VectorCollection.
        ToString(self: VectorCollection) -> str
        
            Creates a System.String representation of this System.Windows.Media.VectorCollection.
            Returns: Returns a System.String containing the System.Windows.Vector.X and System.Windows.Vector.Y values of the System.Windows.Vector structures in this System.Windows.Media.VectorCollection.
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
        __contains__(self: ICollection[Vector], item: Vector) -> bool
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
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
        __new__(cls: type, collection: IEnumerable[Vector])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items contained in the System.Windows.Media.VectorCollection.

Get: Count(self: VectorCollection) -> int

"""


    Enumerator = None

