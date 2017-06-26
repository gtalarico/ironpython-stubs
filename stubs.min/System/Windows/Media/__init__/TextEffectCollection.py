class TextEffectCollection(Animatable, ISealable, IAnimatable, IResource, IList, ICollection, IEnumerable, IList[TextEffect], ICollection[TextEffect], IEnumerable[TextEffect]):
    """
    Provides collection support for a collection of System.Windows.Media.TextEffect objects.
    
    TextEffectCollection()
    TextEffectCollection(capacity: int)
    TextEffectCollection(collection: IEnumerable[TextEffect])
    """
    def Add(self, value):
        """
        Add(self: TextEffectCollection, value: TextEffect)
            Adds a System.Windows.Media.TextEffect to the end of the collection.
        
            value: The System.Windows.Media.TextEffect to add to the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: TextEffectCollection)
            Removes all elements from the list.
        """
        pass

    def Clone(self):
        """
        Clone(self: TextEffectCollection) -> TextEffectCollection
        
            Creates a modifiable clone of this System.Windows.Media.TextEffectCollection, making deep copies of this object's values. When copying dependency properties, this method copies resource references and data 
             bindings (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """ CloneCore(self: TextEffectCollection, source: Freezable) """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: TextEffectCollection) -> TextEffectCollection
        
            Creates a modifiable clone of this System.Windows.Media.TextEffectCollection object, making deep copies of this object's current values. Resource references, data bindings, and animations are not copied, 
             but their current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """ CloneCurrentValueCore(self: TextEffectCollection, source: Freezable) """
        pass

    def Contains(self, value):
        """
        Contains(self: TextEffectCollection, value: TextEffect) -> bool
        
            Determines if the specified item is in the collection.
        
            value: The System.Windows.Media.TextEffect to locate in the collection
            Returns: true if the collection contains value; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: TextEffectCollection, array: Array[TextEffect], index: int)
            Copies the entire System.Windows.Media.TextEffectCollection to a one-dimensional array of type System.Windows.Media.TextEffect, starting at the specified index of the target array.
        
            array: The array into which the collection's items are to be copied.
            index: The index of array at which to start copying the contents of the System.Windows.Media.TextEffectCollection.
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
        """ CreateInstanceCore(self: TextEffectCollection) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """ FreezeCore(self: TextEffectCollection, isChecking: bool) -> bool """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """ GetAsFrozenCore(self: TextEffectCollection, source: Freezable) """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """ GetCurrentValueAsFrozenCore(self: TextEffectCollection, source: Freezable) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: TextEffectCollection) -> Enumerator
        
            Returns an enumerator that can iterate through the collection.
            Returns: An System.Collections.IEnumerator that can iterate through the collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: TextEffectCollection, value: TextEffect) -> int
        
            Searches for the specified System.Windows.Media.TextEffect and returns the zero-based index of the first occurrence within the entire collection.
        
            value: The System.Windows.Media.TextEffect to locate in the collection.
            Returns: The zero-based index of the first occurrence of value within the entire collection, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: TextEffectCollection, index: int, value: TextEffect)
            Inserts a System.Windows.Media.TextEffect into a specific location in the collection.
        
            index: The zero-based index at which the value System.Windows.Media.TextEffect be inserted.
            value: The System.Windows.Media.TextEffect to insert into the collection.
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
        Remove(self: TextEffectCollection, value: TextEffect) -> bool
        
            Removes the specified System.Windows.Media.TextEffect object from the collection.
        
            value: The System.Windows.Media.TextEffect to remove from the collection.
            Returns: true if value was removed fro the collection; otherwise, false.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: TextEffectCollection, index: int)
            Removes the System.Windows.Media.TextEffect at the specified index in the collection.
        
            index: The zero-based index of the System.Windows.Media.TextEffect to remove.
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
        __contains__(self: ICollection[TextEffect], item: TextEffect) -> bool
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
        __new__(cls: type, collection: IEnumerable[TextEffect])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: TextEffectCollection) -> int

"""


    Enumerator = None

