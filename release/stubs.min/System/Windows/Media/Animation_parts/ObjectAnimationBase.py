class ObjectAnimationBase(AnimationTimeline,ISealable,IAnimatable,IResource):
 """ Abstract class that,when implemented,animates a System.Object value. """
 def AllocateClock(self,*args):
  """
  AllocateClock(self: AnimationTimeline) -> Clock

  

   Creates a System.Windows.Media.Animation.Clock for this 

    System.Windows.Media.Animation.AnimationTimeline.

  

   Returns: A clock for this System.Windows.Media.Animation.AnimationTimeline.
  """
  pass
 def Clone(self):
  """
  Clone(self: ObjectAnimationBase) -> ObjectAnimationBase

  

   Creates a modifiable clone of this System.Windows.Media.Animation.ObjectAnimationBase,making 

    deep copies of this object's values. When copying dependency properties,this method copies 

    resource references and data bindings (but they might no longer resolve) but not animations or 

    their current values.

  

   Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 

    property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """
  CloneCore(self: Freezable,sourceFreezable: Freezable)

   Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base 

    (non-animated) property values.

  

  

   sourceFreezable: The object to clone.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """
  CloneCurrentValueCore(self: Freezable,sourceFreezable: Freezable)

   Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable 

    using current property values.

  

  

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

  

   When implemented in a derived class,creates a new instance of the System.Windows.Freezable 

    derived class.

  

   Returns: The new instance.
  """
  pass
 def FreezeCore(self,*args):
  """
  FreezeCore(self: Timeline,isChecking: bool) -> bool

  

   Makes this System.Windows.Media.Animation.Timeline unmodifiable or determines whether it can be 

    made unmodifiable.

  

  

   isChecking: true to check if this instance can be frozen; false to freeze this instance.

   Returns: If isChecking is true,this method returns true if this instance can be made read-only,or false 

    if it cannot be made read-only. If isChecking is false,this method returns true if this 

    instance is now read-only,or false if it cannot be made read-only,with the side effect of 

    having begun to change the frozen status of this object.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: Timeline,sourceFreezable: Freezable)

   Makes this instance a clone of the specified System.Windows.Media.Animation.Timeline object.

  

   sourceFreezable: The System.Windows.Media.Animation.Timeline instance to clone.
  """
  pass
 def GetCurrentValue(self,defaultOriginValue,defaultDestinationValue,animationClock):
  """
  GetCurrentValue(self: ObjectAnimationBase,defaultOriginValue: object,defaultDestinationValue: object,animationClock: AnimationClock) -> object

  

   Gets the current value of the animation.

  

   defaultOriginValue: The origin value provided to the animation if the animation does not have its own start value.

   defaultDestinationValue: The destination value provided to the animation if the animation does not have its own 

    destination value.

  

   animationClock: The System.Windows.Media.Animation.AnimationClock which can generate the 

    System.Windows.Media.Animation.Clock.CurrentTime or 

    System.Windows.Media.Animation.Clock.CurrentProgress value to be used by the animation to 

    generate its output value.

  

   Returns: The value this animation believes should be the current value for the property.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: Timeline,sourceFreezable: Freezable)

   Makes this instance a frozen clone of the specified System.Windows.Media.Animation.Timeline. 

    Resource references,data bindings,and animations are not copied,but their current values are.

  

  

   sourceFreezable: The System.Windows.Media.Animation.Timeline to copy and freeze.
  """
  pass
 def GetCurrentValueCore(self,*args):
  """
  GetCurrentValueCore(self: ObjectAnimationBase,defaultOriginValue: object,defaultDestinationValue: object,animationClock: AnimationClock) -> object

  

   Calculates a value that represents the current value of the property being animated,as 

    determined by the host animation.

  

  

   defaultOriginValue: The suggested origin value,used if the animation does not have its own explicitly set start 

    value.

  

   defaultDestinationValue: The suggested destination value,used if the animation does not have its own explicitly set end 

    value.

  

   animationClock: An System.Windows.Media.Animation.AnimationClock that generates the 

    System.Windows.Media.Animation.Clock.CurrentTime or 

    System.Windows.Media.Animation.Clock.CurrentProgress used by the host animation.

  

   Returns: The value this animation believes should be the current value for the property.
  """
  pass
 def GetNaturalDuration(self,*args):
  """
  GetNaturalDuration(self: Timeline,clock: Clock) -> Duration

  

   Returns the length of a single iteration of this System.Windows.Media.Animation.Timeline.

  

   clock: The System.Windows.Media.Animation.Clock that was created for this 

    System.Windows.Media.Animation.Timeline.

  

   Returns: The length of a single iteration of this System.Windows.Media.Animation.Timeline,or 

    System.Windows.Duration.Automatic if the natural duration is unknown.
  """
  pass
 def GetNaturalDurationCore(self,*args):
  """
  GetNaturalDurationCore(self: AnimationTimeline,clock: Clock) -> Duration

  

   Returns the length of a single iteration of this 

    System.Windows.Media.Animation.AnimationTimeline.

  

  

   clock: The clock that was created for this System.Windows.Media.Animation.AnimationTimeline.

   Returns: The animation's natural duration. This method always returns a System.Windows.Duration of 1 

    second.
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

   This member supports the Windows Presentation Foundation (WPF) infrastructure and is not 

    intended to be used directly from your code.

  

  

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

    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventAr

    gs) to also invoke any System.Windows.Freezable.Changed handlers in response to a changing 

    dependency property of type System.Windows.Freezable.

  

  

   e: Event data that contains information about which property changed,and its old and new values.
  """
  pass
 def ReadPreamble(self,*args):
  """
  ReadPreamble(self: Freezable)

   Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of 

    System.Windows.Freezable must call this method at the beginning of any API that reads data 

    members that are not dependency properties.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool

  

   Returns a value that indicates whether serialization processes should serialize the value for 

    the provided dependency property.

  

  

   dp: The identifier for the dependency property that should be serialized.

   Returns: true if the dependency property that is supplied should be value-serialized; otherwise,false.
  """
  pass
 def WritePostscript(self,*args):
  """
  WritePostscript(self: Freezable)

   Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes 

    its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable 

    should call this method at the end of any API that modifies class members that are not stored as 

    dependency properties.
  """
  pass
 def WritePreamble(self,*args):
  """
  WritePreamble(self: Freezable)

   Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a 

    valid threading context. System.Windows.Freezable inheritors should call this method at the 

    beginning of any API that writes to data members that are not dependency properties.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 TargetPropertyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of value this animation generates.



Get: TargetPropertyType(self: ObjectAnimationBase) -> Type



"""


