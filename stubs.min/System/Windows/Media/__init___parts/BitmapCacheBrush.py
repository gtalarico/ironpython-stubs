class BitmapCacheBrush(Brush, ISealable, IAnimatable, IResource, IFormattable, ICyclicBrush):
    """
    Paints an area with cached content.
    
    BitmapCacheBrush()
    BitmapCacheBrush(visual: Visual)
    """
    def Clone(self):
        """
        Clone(self: BitmapCacheBrush) -> BitmapCacheBrush
        
            Creates a modifiable clone of the System.Windows.Media.BitmapCacheBrush, making deep copies of the object's values. When copying the object's dependency properties, this method copies expressions (which 
             might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property is false even if the source's System.Windows.Freezable.IsFrozen property is true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base (non-animated) property values.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: BitmapCacheBrush) -> BitmapCacheBrush
        
            Creates a modifiable clone (deep copy) of the System.Windows.Media.BitmapCacheBrush using its current values.
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property is false even if the source's System.Windows.Freezable.IsFrozen property is true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable using current property values.
        
            sourceFreezable: The System.Windows.Freezable to be cloned.
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
        """ CreateInstanceCore(self: BitmapCacheBrush) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether it can be made unmodifiable.
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this instance should actually freeze itself when this method is called.
            Returns: If isChecking is true, this method returns true if this System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method 
             returns true if the if this System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made unmodifiable, with the side effect of having begun to change the frozen status of 
             this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base (non-animated) property values.
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the object has animated dependency properties, their current animated values are copied.
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
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
        """ OnPropertyChanged(self: BitmapCacheBrush, e: DependencyPropertyChangedEventArgs) """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of System.Windows.Freezable must call this method at the beginning of any API that reads data members that are 
             not dependency properties.
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

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, visual=None):
        """
        __new__(cls: type)
        __new__(cls: type, visual: Visual)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AutoLayoutContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether layout is applied to the contents of this brush.

Get: AutoLayoutContent(self: BitmapCacheBrush) -> bool

Set: AutoLayoutContent(self: BitmapCacheBrush) = value
"""

    BitmapCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.CacheMode that represents cached content.

Get: BitmapCache(self: BitmapCacheBrush) -> BitmapCache

Set: BitmapCache(self: BitmapCacheBrush) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target visual to cache.

Get: Target(self: BitmapCacheBrush) -> Visual

Set: Target(self: BitmapCacheBrush) = value
"""


    AutoLayoutContentProperty = None
    BitmapCacheProperty = None
    TargetProperty = None

