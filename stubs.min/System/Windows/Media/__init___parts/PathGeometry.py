class PathGeometry(Geometry, ISealable, IAnimatable, IResource, IFormattable):
    """
    Represents a complex shape that may be composed of arcs, curves, ellipses, lines, and rectangles.
    
    PathGeometry()
    PathGeometry(figures: IEnumerable[PathFigure])
    PathGeometry(figures: IEnumerable[PathFigure], fillRule: FillRule, transform: Transform)
    """
    def AddGeometry(self, geometry):
        """
        AddGeometry(self: PathGeometry, geometry: Geometry)
            Converts the specified System.Windows.Media.Geometry into a collection of System.Windows.Media.PathFigure objects and adds it to the path.   Note: If the specified System.Windows.Media.Geometry is 
             animated, the conversion from System.Windows.Media.Geometry to System.Windows.Media.PathFigure may result in some loss of information.
        
        
            geometry: The geometry to add to the path.
        """
        pass

    def Clear(self):
        """
        Clear(self: PathGeometry)
            Removes all System.Windows.Media.PathFigure objects from this System.Windows.Media.PathGeometry.
        """
        pass

    def Clone(self):
        """
        Clone(self: PathGeometry) -> PathGeometry
        
            Creates a modifiable clone of this System.Windows.Media.PathGeometry, making deep copies of this object's values. When copying dependency properties, this method copies resource references and data 
             bindings (but they might no longer resolve) but not animations or their current values.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
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
        CloneCurrentValue(self: PathGeometry) -> PathGeometry
        
            Creates a modifiable clone of this System.Windows.Media.PathGeometry object, making deep copies of this object's current values. Resource references, data bindings, and animations are not copied, but their 
             current values are.
        
            Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable using current property values.
        
            sourceFreezable: The System.Windows.Freezable to be cloned.
        """
        pass

    @staticmethod
    def CreateFromGeometry(geometry):
        """
        CreateFromGeometry(geometry: Geometry) -> PathGeometry
        
            Creates a System.Windows.Media.PathGeometry version of the specified System.Windows.Media.Geometry.
        
            geometry: The geometry from which to create a System.Windows.Media.PathGeometry.
            Returns: A System.Windows.Media.PathGeometry created from the current values of the specified System.Windows.Media.Geometry.
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
        """ CreateInstanceCore(self: PathGeometry) -> Freezable """
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

    def GetPointAtFractionLength(self, progress, point, tangent):
        """
        GetPointAtFractionLength(self: PathGeometry, progress: float) -> (Point, Point)
        
            Gets the System.Windows.Point and a tangent vector on this System.Windows.Media.PathGeometry at the specified fraction of its length.
        
            progress: The fraction of the length of this System.Windows.Media.PathGeometry.
        """
        pass

    def IsEmpty(self):
        """
        IsEmpty(self: PathGeometry) -> bool
        
            Determines whether this System.Windows.Media.PathGeometry object is empty.
            Returns: true if this System.Windows.Media.PathGeometry is empty; otherwise, false.
        """
        pass

    def MayHaveCurves(self):
        """
        MayHaveCurves(self: PathGeometry) -> bool
        
            Determines whether this System.Windows.Media.PathGeometry object may have curved segments.
            Returns: true if this System.Windows.Media.PathGeometry object may have curved segments; otherwise, false.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """ OnChanged(self: PathGeometry) """
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

    @staticmethod # known case of __new__
    def __new__(self, figures=None, fillRule=None, transform=None):
        """
        __new__(cls: type)
        __new__(cls: type, figures: IEnumerable[PathFigure])
        __new__(cls: type, figures: IEnumerable[PathFigure], fillRule: FillRule, transform: Transform)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Rect that specifies the bounding box of this System.Windows.Media.PathGeometry object.   Note: This method does not take any pens into account.

Get: Bounds(self: PathGeometry) -> Rect

"""

    Figures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the collection of System.Windows.Media.PathFigure objects that describe the path's contents.

Get: Figures(self: PathGeometry) -> PathFigureCollection

Set: Figures(self: PathGeometry) = value
"""

    FillRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that determines how the intersecting areas contained in this System.Windows.Media.PathGeometry are combined.

Get: FillRule(self: PathGeometry) -> FillRule

Set: FillRule(self: PathGeometry) = value
"""


    FiguresProperty = None
    FillRuleProperty = None

