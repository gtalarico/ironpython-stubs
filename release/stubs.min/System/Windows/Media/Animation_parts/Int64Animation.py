class Int64Animation(Int64AnimationBase,ISealable,IAnimatable,IResource):
 """
 Animates the value of a  System.Int64 property between two target values using linear interpolation over a specified System.Windows.Media.Animation.Timeline.Duration.

 

 Int64Animation()

 Int64Animation(toValue: Int64,duration: Duration)

 Int64Animation(toValue: Int64,duration: Duration,fillBehavior: FillBehavior)

 Int64Animation(fromValue: Int64,toValue: Int64,duration: Duration)

 Int64Animation(fromValue: Int64,toValue: Int64,duration: Duration,fillBehavior: FillBehavior)
 """
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
  Clone(self: Int64Animation) -> Int64Animation

  

   Creates a modifiable clone of this System.Windows.Media.Animation.Int64Animation,making deep 

    copies of this object's values. When copying dependency properties,this method copies resource 

    references and data bindings (but they might no longer resolve) but not animations or their 

    current values.

  

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
  CreateInstanceCore(self: Int64Animation) -> Freezable

  

   Implementation of System.Windows.Freezable.CreateInstanceCore.

   Returns: The new System.Windows.Freezable.
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
  GetCurrentValueCore(self: Int64Animation,defaultOriginValue: Int64,defaultDestinationValue: Int64,animationClock: AnimationClock) -> Int64

  

   Calculates the value this animation believes should be the current value for the property.

  

   defaultOriginValue: This value is the suggested origin value provided to the animation to be used if the animation 

    does not have its own concept of a start value. If this animation is the first in a composition 

    chain this value will be the snapshot value if one is available or the base property value if it 

    is not; otherwise this value will be the value returned by the previous animation in the chain 

    with an animationClock that is not Stopped.

  

   defaultDestinationValue: This value is the suggested destination value provided to the animation to be used if the 

    animation does not have its own concept of an end value. This value will be the base value if 

    the animation is in the first composition layer of animations on a property; otherwise this 

    value will be the output value from the previous composition layer of animations for the 

    property.

  

   animationClock: This is the animationClock which can generate the CurrentTime or CurrentProgress value to be 

    used by the animation to generate its output value.

  

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
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,toValue: Int64,duration: Duration)

  __new__(cls: type,toValue: Int64,duration: Duration,fillBehavior: FillBehavior)

  __new__(cls: type,fromValue: Int64,toValue: Int64,duration: Duration)

  __new__(cls: type,fromValue: Int64,toValue: Int64,duration: Duration,fillBehavior: FillBehavior)
  """
  pass
 By=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the total amount by which the animation changes its starting value.



Get: By(self: Int64Animation) -> Nullable[Int64]



Set: By(self: Int64Animation)=value

"""

 EasingFunction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the easing function applied to this animation.



Get: EasingFunction(self: Int64Animation) -> IEasingFunction



Set: EasingFunction(self: Int64Animation)=value

"""

 From=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the animation's starting value.



Get: From(self: Int64Animation) -> Nullable[Int64]



Set: From(self: Int64Animation)=value

"""

 IsAdditive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the target property's current value should be added to this animation's starting value.



Get: IsAdditive(self: Int64Animation) -> bool



Set: IsAdditive(self: Int64Animation)=value

"""

 IsCumulative=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that specifies whether the animation's value accumulates when it repeats.



Get: IsCumulative(self: Int64Animation) -> bool



Set: IsCumulative(self: Int64Animation)=value

"""

 To=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the animation's ending value.



Get: To(self: Int64Animation) -> Nullable[Int64]



Set: To(self: Int64Animation)=value

"""


 ByProperty=None
 EasingFunctionProperty=None
 FromProperty=None
 ToProperty=None

