class ThicknessKeyFrameCollection(Freezable, ISealable, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.Windows.Media.Animation.ThicknessKeyFrame objects.
    
    ThicknessKeyFrameCollection()
    """
    def Add(self, keyFrame):
        """
        Add(self: ThicknessKeyFrameCollection, keyFrame: ThicknessKeyFrame) -> int
        
            Adds a System.Windows.Media.Animation.ThicknessKeyFrame to the end of the collection.
        
            keyFrame: The System.Windows.Media.Animation.ThicknessKeyFrame to add to the end of the collection.
            Returns: The index at which the keyFrame was added.
        """
        pass

    def Clear(self):
        """
        Clear(self: ThicknessKeyFrameCollection)
            Removes all System.Windows.Media.Animation.ThicknessKeyFrame objects from the collection.
        """
        pass

    def Clone(self):
        """
        Clone(self: ThicknessKeyFrameCollection) -> ThicknessKeyFrameCollection
        
            Creates a modifiable clone of this System.Windows.Media.Animation.ThicknessKeyFrameCollection, making deep copies of this object's values. When copying dependency properties, this method copies resource 
             references and data bindings (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: ThicknessKeyFrameCollection, sourceFreezable: Freezable)
            Makes this instance a deep copy of the specified System.Windows.Media.Animation.ThicknessKeyFrameCollection. When copying dependency properties, this method copies resource references and data bindings 
             (but they might no longer resolve) but not animations or their current values.
        
        
            sourceFreezable: The System.Windows.Media.Animation.ThicknessKeyFrameCollection to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: ThicknessKeyFrameCollection, sourceFreezable: Freezable)
            Makes this instance a modifiable deep copy of the specified System.Windows.Media.Animation.ThicknessKeyFrameCollection using current property values. Resource references, data bindings, and animations are 
             not copied, but their current values are.
        
        
            sourceFreezable: The System.Windows.Media.Animation.ThicknessKeyFrameCollection to clone.
        """
        pass

    def Contains(self, keyFrame):
        """
        Contains(self: ThicknessKeyFrameCollection, keyFrame: ThicknessKeyFrame) -> bool
        
            Gets a value that indicates whether the collection contains the specified System.Windows.Media.Animation.ThicknessKeyFrame.
        
            keyFrame: The System.Windows.Media.Animation.ThicknessKeyFrame to locate in the collection.
            Returns: true if the collection contains keyFrame; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: ThicknessKeyFrameCollection, array: Array[ThicknessKeyFrame], index: int)
            Copies all of the System.Windows.Media.Animation.ThicknessKeyFrame objects in a collection to a specified array.
        
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
        """
        CreateInstanceCore(self: ThicknessKeyFrameCollection) -> Freezable
        
            Creates a new, frozen instance of System.Windows.Media.Animation.ThicknessKeyFrameCollection.
            Returns: A frozen instance of System.Windows.Media.Animation.ThicknessKeyFrameCollection.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: ThicknessKeyFrameCollection, isChecking: bool) -> bool
        
            Makes this instance of System.Windows.Media.Animation.ThicknessKeyFrameCollection read-only or determines whether it can be made read-only.
        
            isChecking: true to check if this instance can be frozen; false to freeze this instance.
            Returns: If isChecking is true, this method returns true if this instance can be made read-only, or false if it cannot be made read-only. If isChecking is false, this method returns true if this instance is now 
             read-only, or false if it cannot be made read-only, with the side effect of having begun to change the frozen status of this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: ThicknessKeyFrameCollection, sourceFreezable: Freezable)
            Makes this instance a clone of the specified System.Windows.Media.Animation.ThicknessKeyFrameCollection object.
        
            sourceFreezable: The System.Windows.Media.Animation.ThicknessKeyFrameCollection object to clone.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: ThicknessKeyFrameCollection, sourceFreezable: Freezable)
            Makes this instance a modifiable deep copy of the specified System.Windows.Media.Animation.ThicknessKeyFrameCollection using current property values. Resource references, data bindings, and animations are 
             not copied, but their current values are.
        
        
            sourceFreezable: The System.Windows.Media.Animation.ThicknessKeyFrameCollection to clone.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ThicknessKeyFrameCollection) -> IEnumerator
        
            Returns an enumerator that can iterate through the collection.
            Returns: An System.Collections.IEnumerator that can iterate through the collection.
        """
        pass

    def IndexOf(self, keyFrame):
        """
        IndexOf(self: ThicknessKeyFrameCollection, keyFrame: ThicknessKeyFrame) -> int
        
            Searches for the specified System.Windows.Media.Animation.ThicknessKeyFrame and returns the zero-based index of the first occurrence within the entire collection.
        
            keyFrame: The System.Windows.Media.Animation.ThicknessKeyFrame to locate in the collection.
            Returns: The zero-based index of the first occurrence of keyFrame within the entire collection, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, keyFrame):
        """
        Insert(self: ThicknessKeyFrameCollection, index: int, keyFrame: ThicknessKeyFrame)
            Inserts a System.Windows.Media.Animation.ThicknessKeyFrame into a specific location within the collection.
        
            index: The index position at which the System.Windows.Media.Animation.ThicknessKeyFrame is inserted.
            keyFrame: The System.Windows.Media.Animation.ThicknessKeyFrame object to insert in the collection.
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

    def Remove(self, keyFrame):
        """
        Remove(self: ThicknessKeyFrameCollection, keyFrame: ThicknessKeyFrame)
            Removes a System.Windows.Media.Animation.ThicknessKeyFrame object from the collection.
        
            keyFrame: Identifies the System.Windows.Media.Animation.ThicknessKeyFrame to remove from the collection.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ThicknessKeyFrameCollection, index: int)
            Removes the System.Windows.Media.Animation.ThicknessKeyFrame at the specified index position from the collection.
        
            index: Index position of the System.Windows.Media.Animation.ThicknessKeyFrame to be removed.
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

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of key frames contained in the System.Windows.Media.Animation.ThicknessKeyFrameCollection.

Get: Count(self: ThicknessKeyFrameCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if the collection size can ever change.

Get: IsFixedSize(self: ThicknessKeyFrameCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if the collection is read-only.

Get: IsReadOnly(self: ThicknessKeyFrameCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to the collection is synchronized (thread-safe).

Get: IsSynchronized(self: ThicknessKeyFrameCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the collection.

Get: SyncRoot(self: ThicknessKeyFrameCollection) -> object

"""


    Empty = None

