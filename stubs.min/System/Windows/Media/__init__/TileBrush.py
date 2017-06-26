class TileBrush(Brush, ISealable, IAnimatable, IResource, IFormattable):
    """ Describes a way to paint a region by using one or more tiles. """
    def Clone(self):
        """
        Clone(self: TileBrush) -> TileBrush
        
            Creates a modifiable copy of this System.Windows.Media.TileBrush by making deep copies of its values.
            Returns: A modifiable deep copy of the current object. The System.Windows.Freezable.IsFrozen property of the cloned object returns false even if the System.Windows.Freezable.IsFrozen property of the source is true.
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
        CloneCurrentValue(self: TileBrush) -> TileBrush
        
            Creates a modifiable copy of this System.Windows.Media.TileBrush object by making deep copies of its values. This method does not copy resource references, data bindings, or animations, although it does 
             copy their current values.
        
            Returns: A modifiable deep copy of the current object. The System.Windows.Freezable.IsFrozen property of the cloned object is false even if the System.Windows.Freezable.IsFrozen prope-rty of the source is true.
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
        """
        CreateInstanceCore(self: Freezable) -> Freezable
        
            When implemented in a derived class, creates a new instance of the System.Windows.Freezable derived class.
            Returns: The new instance.
        """
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

    def GetContentBounds(self, *args): #cannot find CLR method
        """
        GetContentBounds(self: TileBrush) -> Rect
        
            Obtains the current bounds of the System.Windows.Media.TileBrush content
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

    def __str__(self, *args): #cannot find CLR method
        pass

    AlignmentX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the horizontal alignment of content in the System.Windows.Media.TileBrush base tile.

Get: AlignmentX(self: TileBrush) -> AlignmentX

Set: AlignmentX(self: TileBrush) = value
"""

    AlignmentY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the vertical alignment of content in the System.Windows.Media.TileBrush base tile.

Get: AlignmentY(self: TileBrush) -> AlignmentY

Set: AlignmentY(self: TileBrush) = value
"""

    Stretch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies how the content of this System.Windows.Media.TileBrush stretches to fit its tiles.

Get: Stretch(self: TileBrush) -> Stretch

Set: Stretch(self: TileBrush) = value
"""

    TileMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies how a System.Windows.Media.TileBrush fills the area that you are painting if the base tile is smaller than the output area.

Get: TileMode(self: TileBrush) -> TileMode

Set: TileMode(self: TileBrush) = value
"""

    Viewbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position and dimensions of the content in a System.Windows.Media.TileBrush tile.

Get: Viewbox(self: TileBrush) -> Rect

Set: Viewbox(self: TileBrush) = value
"""

    ViewboxUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that specifies whether the System.Windows.Media.TileBrush.Viewbox value is relative to the bounding box of the System.Windows.Media.TileBrush contents or whether the value is absolute.

Get: ViewboxUnits(self: TileBrush) -> BrushMappingMode

Set: ViewboxUnits(self: TileBrush) = value
"""

    Viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the position and dimensions of the base tile for a System.Windows.Media.TileBrush.

Get: Viewport(self: TileBrush) -> Rect

Set: Viewport(self: TileBrush) = value
"""

    ViewportUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.BrushMappingMode enumeration that specifies whether the value of the System.Windows.Media.TileBrush.Viewport, which indicates the size and position of the System.Windows.Media.TileBrush base tile, is relative to the size of the output area.

Get: ViewportUnits(self: TileBrush) -> BrushMappingMode

Set: ViewportUnits(self: TileBrush) = value
"""


    AlignmentXProperty = None
    AlignmentYProperty = None
    StretchProperty = None
    TileModeProperty = None
    ViewboxProperty = None
    ViewboxUnitsProperty = None
    ViewportProperty = None
    ViewportUnitsProperty = None

