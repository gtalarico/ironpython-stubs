class CombinedGeometry(Geometry,ISealable,IAnimatable,IResource,IFormattable):
 """
 Represents a 2-D geometric shape defined by the combination of two System.Windows.Media.Geometry objects.
 
 CombinedGeometry()
 CombinedGeometry(geometry1: Geometry,geometry2: Geometry)
 CombinedGeometry(geometryCombineMode: GeometryCombineMode,geometry1: Geometry,geometry2: Geometry)
 CombinedGeometry(geometryCombineMode: GeometryCombineMode,geometry1: Geometry,geometry2: Geometry,transform: Transform)
 """
 def Clone(self):
  """
  Clone(self: CombinedGeometry) -> CombinedGeometry
  
   Creates a modifiable clone of this System.Windows.Media.CombinedGeometry,
    making deep copies of this object's values. When copying dependency properties,
    this method copies resource references and data bindings (but they might no 
    longer resolve) but not animations or their current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """
  CloneCore(self: Freezable,sourceFreezable: Freezable)
   Makes the instance a clone (deep copy) of the specified 
    System.Windows.Freezable using base (non-animated) property values.
  
  
   sourceFreezable: The object to clone.
  """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: CombinedGeometry) -> CombinedGeometry
  
   Creates a modifiable clone of this System.Windows.Media.CombinedGeometry 
    object,making deep copies of this object's current values. Resource 
    references,data bindings,and animations are not copied,but their current 
    values are.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """
  CloneCurrentValueCore(self: Freezable,sourceFreezable: Freezable)
   Makes the instance a modifiable clone (deep copy) of the specified 
    System.Windows.Freezable using current property values.
  
  
   sourceFreezable: The System.Windows.Freezable to be cloned.
  """
  pass
 def CreateInstance(self,*args):
  """
  CreateInstance(self: Freezable) -> Freezable
  
   Initializes a new instance of the System.Windows.Freezable class.
   Returns: The new instance.
  """
  pass
 def CreateInstanceCore(self,*args):
  """ CreateInstanceCore(self: CombinedGeometry) -> Freezable """
  pass
 def FreezeCore(self,*args):
  """
  FreezeCore(self: Animatable,isChecking: bool) -> bool
  
   Makes this System.Windows.Media.Animation.Animatable object unmodifiable or 
    determines whether it can be made unmodifiable.
  
  
   isChecking: true if this method should simply determine whether this instance can be 
    frozen. false if this instance should actually freeze itself when this method 
    is called.
  
   Returns: If isChecking is true,this method returns true if this 
    System.Windows.Media.Animation.Animatable can be made unmodifiable,or false if 
    it cannot be made unmodifiable. If isChecking is false,this method returns 
    true if the if this System.Windows.Media.Animation.Animatable is now 
    unmodifiable,or false if it cannot be made unmodifiable,with the side effect 
    of having begun to change the frozen status of this object.
  """
  pass
 def GetArea(self,tolerance=None,type=None):
  """
  GetArea(self: CombinedGeometry,tolerance: float,type: ToleranceType) -> float
  
   Gets the area of the filled region.
  
   tolerance: The computational tolerance of error.
   type: Specifies how the error tolerance will be interpreted.
   Returns: The area of the filled region of this combined geometry.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: Freezable,sourceFreezable: Freezable)
   Makes the instance a frozen clone of the specified System.Windows.Freezable 
    using base (non-animated) property values.
  
  
   sourceFreezable: The instance to copy.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: Freezable,sourceFreezable: Freezable)
   Makes the current instance a frozen clone of the specified 
    System.Windows.Freezable. If the object has animated dependency properties,
    their current animated values are copied.
  
  
   sourceFreezable: The System.Windows.Freezable to copy and freeze.
  """
  pass
 def IsEmpty(self):
  """
  IsEmpty(self: CombinedGeometry) -> bool
  
   Determines whether this System.Windows.Media.CombinedGeometry object is empty.
   Returns: true if this System.Windows.Media.CombinedGeometry is empty; otherwise,false.
  """
  pass
 def MayHaveCurves(self):
  """
  MayHaveCurves(self: CombinedGeometry) -> bool
  
   Determines whether this System.Windows.Media.CombinedGeometry object may have 
    curved segments.
  
   Returns: true if this System.Windows.Media.CombinedGeometry object may have curved 
    segments; otherwise,false.
  """
  pass
 def OnChanged(self,*args):
  """
  OnChanged(self: Freezable)
   Called when the current System.Windows.Freezable object is modified.
  """
  pass
 def OnFreezablePropertyChanged(self,*args):
  """
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject,property: DependencyProperty)
   This member supports the Windows Presentation Foundation (WPF) infrastructure 
    and is not intended to be used directly from your code.
  
  
   oldValue: The previous value of the data member.
   newValue: The current value of the data member.
   property: The property that changed.
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject)
   Ensures that appropriate context pointers are established for a 
    System.Windows.DependencyObjectType data member that has just been set.
  
  
   oldValue: The previous value of the data member.
   newValue: The current value of the data member.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: Freezable,e: DependencyPropertyChangedEventArgs)
   Overrides the System.Windows.DependencyObject implementation of 
    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
    rtyChangedEventArgs) to also invoke any System.Windows.Freezable.Changed 
    handlers in response to a changing dependency property of type 
    System.Windows.Freezable.
  
  
   e: Event data that contains information about which property changed,and its old 
    and new values.
  """
  pass
 def ReadPreamble(self,*args):
  """
  ReadPreamble(self: Freezable)
   Ensures that the System.Windows.Freezable is being accessed from a valid 
    thread. Inheritors of System.Windows.Freezable must call this method at the 
    beginning of any API that reads data members that are not dependency 
    properties.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def WritePostscript(self,*args):
  """
  WritePostscript(self: Freezable)
   Raises the System.Windows.Freezable.Changed event for the 
    System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged 
    method. Classes that derive from System.Windows.Freezable should call this 
    method at the end of any API that modifies class members that are not stored as 
    dependency properties.
  """
  pass
 def WritePreamble(self,*args):
  """
  WritePreamble(self: Freezable)
   Verifies that the System.Windows.Freezable is not frozen and that it is being 
    accessed from a valid threading context. System.Windows.Freezable inheritors 
    should call this method at the beginning of any API that writes to data members 
    that are not dependency properties.
  """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)
  __new__(cls: type,geometry1: Geometry,geometry2: Geometry)
  __new__(cls: type,geometryCombineMode: GeometryCombineMode,geometry1: Geometry,geometry2: Geometry)
  __new__(cls: type,geometryCombineMode: GeometryCombineMode,geometry1: Geometry,geometry2: Geometry,transform: Transform)
  """
  pass
 def __str__(self,*args):
  pass
 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Windows.Rect that specifies the bounding box of this System.Windows.Media.CombinedGeometry object.   Note: This method does not take any pens into account.

Get: Bounds(self: CombinedGeometry) -> Rect

"""

 Geometry1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the first System.Windows.Media.Geometry object of this System.Windows.Media.CombinedGeometry object.

Get: Geometry1(self: CombinedGeometry) -> Geometry

Set: Geometry1(self: CombinedGeometry)=value
"""

 Geometry2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the second System.Windows.Media.Geometry object of this System.Windows.Media.CombinedGeometry object.

Get: Geometry2(self: CombinedGeometry) -> Geometry

Set: Geometry2(self: CombinedGeometry)=value
"""

 GeometryCombineMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the method by which the two geometries (specified by the System.Windows.Media.CombinedGeometry.Geometry1 and System.Windows.Media.CombinedGeometry.Geometry2 properties) are combined.

Get: GeometryCombineMode(self: CombinedGeometry) -> GeometryCombineMode

Set: GeometryCombineMode(self: CombinedGeometry)=value
"""


 Geometry1Property=None
 Geometry2Property=None
 GeometryCombineModeProperty=None

