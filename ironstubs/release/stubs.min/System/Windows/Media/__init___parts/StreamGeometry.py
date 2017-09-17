class StreamGeometry(Geometry,ISealable,IAnimatable,IResource,IFormattable):
 """
 Defines a geometric shape,described using a System.Windows.Media.StreamGeometryContext. This geometry is light-weight alternative to System.Windows.Media.PathGeometry: it does not support data binding,animation,or modification.
 
 StreamGeometry()
 """
 def Clear(self):
  """
  Clear(self: StreamGeometry)
   Removes all geometric information from this System.Windows.Media.StreamGeometry.
  """
  pass
 def Clone(self):
  """
  Clone(self: StreamGeometry) -> StreamGeometry
  
   Creates a modifiable clone of this System.Windows.Media.StreamGeometry,making 
    deep copies of this object's values. When copying dependency properties,this 
    method copies resource references and data bindings (but they might no longer 
    resolve) but not animations or their current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """ CloneCore(self: StreamGeometry,source: Freezable) """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: StreamGeometry) -> StreamGeometry
  
   Creates a modifiable clone of this System.Windows.Media.StreamGeometry object,
    making deep copies of this object's current values. Resource references,data 
    bindings,and animations are not copied,but their current values are.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """ CloneCurrentValueCore(self: StreamGeometry,source: Freezable) """
  pass
 def CreateInstance(self,*args):
  """
  CreateInstance(self: Freezable) -> Freezable
  
   Initializes a new instance of the System.Windows.Freezable class.
   Returns: The new instance.
  """
  pass
 def CreateInstanceCore(self,*args):
  """ CreateInstanceCore(self: StreamGeometry) -> Freezable """
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
  """ GetAsFrozenCore(self: StreamGeometry,source: Freezable) """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """ GetCurrentValueAsFrozenCore(self: StreamGeometry,source: Freezable) """
  pass
 def IsEmpty(self):
  """
  IsEmpty(self: StreamGeometry) -> bool
  
   Determines whether this System.Windows.Media.StreamGeometry describes a 
    geometric shape.
  
   Returns: true if this System.Windows.Media.StreamGeometry describes a geometry shape; 
    otherwise,false.
  """
  pass
 def MayHaveCurves(self):
  """
  MayHaveCurves(self: StreamGeometry) -> bool
  
   Determines whether this System.Windows.Media.StreamGeometry contains a curved 
    segment.
  
   Returns: true if this System.Windows.Media.StreamGeometry object has a curved segment; 
    otherwise,false.
  """
  pass
 def OnChanged(self,*args):
  """ OnChanged(self: StreamGeometry) """
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
 def Open(self):
  """
  Open(self: StreamGeometry) -> StreamGeometryContext
  
   Opens a System.Windows.Media.StreamGeometryContext that can be used to describe 
    this System.Windows.Media.StreamGeometry object's contents.
  
   Returns: A System.Windows.Media.StreamGeometryContext that can be used to describe this 
    System.Windows.Media.StreamGeometry object's contents.
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
 def __str__(self,*args):
  pass
 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Windows.Rect that is exactly large enough to contain this System.Windows.Media.StreamGeometry.

Get: Bounds(self: StreamGeometry) -> Rect

"""

 FillRule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines how the intersecting areas contained in this System.Windows.Media.StreamGeometry are combined.

Get: FillRule(self: StreamGeometry) -> FillRule

Set: FillRule(self: StreamGeometry)=value
"""


 FillRuleProperty=None

