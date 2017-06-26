class Int32Collection(Freezable, ISealable, IFormattable, IList, ICollection, IEnumerable, IList[int], ICollection[int], IEnumerable[int]):
    """
    Represents a collection of System.Int32 values.
    
    Int32Collection()
    Int32Collection(capacity: int)
    Int32Collection(collection: IEnumerable[int])
    """
    def Add(self, value):
        """
        Add(self: Int32Collection, value: int)
            Adds an System.Int32 to the end of the collection.
        
            value: The System.Int32 to add to the end of the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: Int32Collection)
            Removes all System.Int32 values from the collection.
        """
        pass

    def Clone(self):
        """
        Clone(self: Int32Collection) -> Int32Collection
        
            Creates a modifiable clone of this System.Windows.Media.Int32Collection, making deep copies of this object's values. When copying dependency properties, this method copies resource references and data 
             bindings (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: Int32Collection, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: Int32Collection) -> Int32Collection
        
            Creates a modifiable clone of this System.Windows.Media.Int32Collection object, making deep copies of this object's current values. Resource references, data bindings, and animations are not copied, but 
             their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: Int32Collection, source: Freezable) """
        pass

    def Contains(self, value):
        """
        Contains(self: Int32Collection, value: int) -> bool
        
            Gets a value that indicates whether the collection contains the specified System.Int32.
        
            value: The System.Int32 to locate in the collection.
            Returns: true if the System.Int32 is found in the System.Windows.Media.Int32Collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: Int32Collection, array: Array[int], index: int)
            Copies all of the System.Int32 values in a collection to a specified array.
        
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
        """ CreateInstanceCore(self: Int32Collection) -> Freezable """
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
        """ GetAsFrozenCore(self: Int32Collection, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: Int32Collection, source: Freezable) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: Int32Collection) -> Enumerator
        
            Returns an System.Windows.Media.Int32Collection.Enumerator that can iterate through the collection.
            Returns: An System.Windows.Media.Int32Collection.Enumerator that can iterate through the collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: Int32Collection, value: int) -> int
        
            Searches for the specified System.Int32 and returns the zero-based index of the first occurrence within the entire collection.
        
            value: The System.Int32 to locate in the collection.
            Returns: The zero-based index of the first occurrence of value within the entire collection, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: Int32Collection, index: int, value: int)
            Inserts an System.Int32 into a specific location within the collection.
        
            index: The index position at which the System.Int32 is inserted.
            value: The System.Int32 to insert in the collection.
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
        Parse(source: str) -> Int32Collection
        
            Returns an instance of System.Windows.Media.Int32Collection created from a specified string.
        
            source: The string that is converted to an System.Int32.
            Returns: An instance of System.Windows.Media.Int32Collection created from source.
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
        Remove(self: Int32Collection, value: int) -> bool
        
            Removes an System.Int32 from the collection.
        
            value: Identifies the System.Int32 to remove from the collection.
            Returns: true if value was removed from the System.Windows.Media.Int32Collection; otherwise, false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: Int32Collection, index: int)
            Removes the System.Int32 at the specified index position from the collection.
        
            index: Index position of the System.Int32 to be removed.
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
        ToString(self: Int32Collection, provider: IFormatProvider) -> str
        
            Converts the current value of a System.Windows.Media.Int32Collection to a System.String using the specified culture-specific formatting information.
        
            provider: Culture-specific formatting information.
            Returns: A string representation of the System.Windows.Media.Int32Collection.
        ToString(self: Int32Collection) -> str
        
            Converts the current value of a System.Windows.Media.Int32Collection to a System.String.
            Returns: A string representation of the System.Windows.Media.Int32Collection.
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
        __contains__(self: ICollection[int], item: int) -> bool
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
        __new__(cls: type, collection: IEnumerable[int])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of System.Int32 values contained in the System.Windows.Media.Int32Collection.

Get: Count(self: Int32Collection) -> int

"""


    Enumerator = None

