class FreezableCollection(Animatable, ISealable, IAnimatable, IResource, IList, ICollection, IEnumerable, IList[T], ICollection[T], IEnumerable[T], INotifyCollectionChanged, INotifyPropertyChanged):
    """
    FreezableCollection[T]()
    FreezableCollection[T](capacity: int)
    FreezableCollection[T](collection: IEnumerable[T])
    """
    def Add(self, value):
        """
        Add(self: FreezableCollection[T], value: T)
            Adds the specified object to the end of the System.Windows.FreezableCollection.
        
            value: The object to be added to the end of the System.Windows.FreezableCollection. This value cannot be null.
        """
        pass

    def Clear(self):
        """
        Clear(self: FreezableCollection[T])
            Removes all elements from the collection.
        """
        pass

    def Clone(self):
        """
        Clone(self: FreezableCollection[T]) -> FreezableCollection[T]
        
                     value is copied, not its current animated value.
        
            Returns: A modifiable copy of this collection and its contents. The copy's System.Windows.Freezable.IsFrozen value is false.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: FreezableCollection[T], source: Freezable)
            Makes this instance a clone (deep copy) of the specified System.Windows.FreezableCollection using base (non-animated) property values.
        
            source: The System.Windows.FreezableCollection to copy.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: FreezableCollection[T]) -> FreezableCollection[T]
        
            Creates a modifiable copy of this System.Windows.FreezableCollection and its contents, making deep copies of this object's current values. If this object (or the objects it contains) contains animated 
             dependency properties, their current animated values are copied.
        
            Returns: A modifiable clone of the collection and its contents. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: FreezableCollection[T], source: Freezable)
            Makes this instance a modifiable clone (deep copy) of the specified System.Windows.FreezableCollection using current property values.
        
            source: The System.Windows.FreezableCollection to clone.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: FreezableCollection[T], value: T) -> bool
        
            Determines whether this System.Windows.FreezableCollection contains the specified value.
        
            value: The object to locate in this collection. This object may be null.
            Returns: true if value is found in the System.Windows.FreezableCollection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: FreezableCollection[T], array: Array[T], index: int) """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """
        CreateInstanceCore(self: FreezableCollection[T]) -> Freezable
        
            Creates a new instance of the System.Windows.FreezableCollection.
            Returns: The new instance.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: FreezableCollection[T], isChecking: bool) -> bool
        
            Makes this System.Windows.FreezableCollection object unmodifiable or determines whether it can be made unmodifiable.
        
            isChecking: true if the System.Windows.FreezableCollection should simply return whether it can be frozen. false if the System.Windows.FreezableCollection instance should actually freeze itself when this method is 
             called.
        
            Returns: If isChecking is true, this method returns true if this System.Windows.FreezableCollection can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method returns 
             true if the if the specified System.Windows.FreezableCollection is now unmodifiable, or false if it cannot be made unmodifiable, with the side effect of having begun to change the frozen status of this 
             object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: FreezableCollection[T], source: Freezable)
            Makes this instance a frozen clone of the specified System.Windows.FreezableCollection using base (non-animated) property values.
        
            source: The System.Windows.FreezableCollection to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: FreezableCollection[T], source: Freezable)
            Makes this instance a frozen clone of the specified System.Windows.Freezable. If this object has animated dependency properties, their current animated values are copied.
        
            source: The System.Windows.FreezableCollection to copy.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FreezableCollection[T]) -> Enumerator
        
            Returns an enumerator for the entire System.Windows.FreezableCollection.
            Returns: An enumerator for the entire System.Windows.FreezableCollection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: FreezableCollection[T], value: T) -> int
        
            Searches for the specified object and returns the zero-based index of the first occurrence within the entire System.Windows.FreezableCollection.
        
            value: The object to locate in the System.Windows.FreezableCollection.
            Returns: The zero-based index of the first occurrence of value within the entire System.Windows.FreezableCollection, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: FreezableCollection[T], index: int, value: T)
            Inserts the specified object into the System.Windows.FreezableCollection at the specified index.
        
            index: The zero-based index at which value should be inserted.
            value: The object to insert.
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
        Remove(self: FreezableCollection[T], value: T) -> bool
        
            Removes the first occurrence of the specified object from the System.Windows.FreezableCollection.
        
            value: The object to remove.
            Returns: true if an occurrence of value was found in the collection and removed; false if value could not be found in the collection.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: FreezableCollection[T], index: int)
            Removes the object at the specified zero-based index of the System.Windows.FreezableCollection.
        
            index: The zero-based index of the object to remove.
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
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
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
        __new__(cls: type, collection: IEnumerable[T])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements contained by this System.Windows.FreezableCollection.

Get: Count(self: FreezableCollection[T]) -> int

"""


    Enumerator = None

