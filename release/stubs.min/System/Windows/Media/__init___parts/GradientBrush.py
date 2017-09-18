class GradientBrush(Brush,ISealable,IAnimatable,IResource,IFormattable):
 """ An abstract class that describes a gradient,composed of gradient stops. Classes that inherit from System.Windows.Media.GradientBrush describe different ways of interpreting gradient stops. """
 def Clone(self):
  """
  Clone(self: GradientBrush) -> GradientBrush
  
   Creates a modifiable clone of this System.Windows.Media.GradientBrush,making 
    deep copies of this object's values. When copying dependency properties,this 
    method copies resource references and data bindings (but they might no longer 
    resolve) but not animations or their current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property is false even if the source's 
    System.Windows.Freezable.IsFrozen property is true.
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
  CloneCurrentValue(self: GradientBrush) -> GradientBrush
  
   Creates a modifiable clone of this System.Windows.Media.GradientBrush object,
    making deep copies of this object's current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property is false even if the source's 
    System.Windows.Freezable.IsFrozen property is true.
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
  """
  CreateInstanceCore(self: Freezable) -> Freezable
  
   When implemented in a derived class,creates a new instance of the 
    System.Windows.Freezable derived class.
  
   Returns: The new instance.
  """
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
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)
  __new__(cls: type,gradientStopCollection: GradientStopCollection)
  """
  pass
 def __str__(self,*args):
  pass
 ColorInterpolationMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Media.ColorInterpolationMode enumeration that specifies how the gradient's colors are interpolated.

Get: ColorInterpolationMode(self: GradientBrush) -> ColorInterpolationMode

Set: ColorInterpolationMode(self: GradientBrush)=value
"""

 GradientStops=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the brush's gradient stops.

Get: GradientStops(self: GradientBrush) -> GradientStopCollection

Set: GradientStops(self: GradientBrush)=value
"""

 MappingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Media.BrushMappingMode enumeration that specifies whether the gradient brush's positioning coordinates are absolute or relative to the output area.

Get: MappingMode(self: GradientBrush) -> BrushMappingMode

Set: MappingMode(self: GradientBrush)=value
"""

 SpreadMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of spread method that specifies how to draw a gradient that starts or ends inside the bounds of the object to be painted.

Get: SpreadMethod(self: GradientBrush) -> GradientSpreadMethod

Set: SpreadMethod(self: GradientBrush)=value
"""


 ColorInterpolationModeProperty=None
 GradientStopsProperty=None
 MappingModeProperty=None
 SpreadMethodProperty=None

