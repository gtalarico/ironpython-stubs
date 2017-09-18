class Timeline(Animatable,ISealable,IAnimatable,IResource):
 """ Defines a segment of time. """
 def AllocateClock(self,*args):
  """
  AllocateClock(self: Timeline) -> Clock

  

   Creates a System.Windows.Media.Animation.Clock for this System.Windows.Media.Animation.Timeline.

   Returns: A clock for this System.Windows.Media.Animation.Timeline.
  """
  pass
 def Clone(self):
  """
  Clone(self: Timeline) -> Timeline

  

   Creates a modifiable clone of this System.Windows.Media.Animation.Timeline,making deep copies 

    of this object's values.

  

   Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 

    property is false even if the source's System.Windows.Freezable.IsFrozen property is true.
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
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: Timeline) -> Timeline

  

   Creates a modifiable clone of this System.Windows.Media.Animation.Timeline object,making deep 

    copies of this object's current values.

  

   Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 

    property is false even if the source's System.Windows.Freezable.IsFrozen property is true.
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
 def CreateClock(self,hasControllableRoot=None):
  """
  CreateClock(self: Timeline,hasControllableRoot: bool) -> Clock

  

   Creates a new System.Windows.Media.Animation.Clock from this 

    System.Windows.Media.Animation.Timeline and specifies whether the new 

    System.Windows.Media.Animation.Clock is controllable. If this 

    System.Windows.Media.Animation.Timeline has children,a tree of clocks is created with this 

    System.Windows.Media.Animation.Timeline as the root.

  

  

   hasControllableRoot: true if the root System.Windows.Media.Animation.Clock returned should return a 

    System.Windows.Media.Animation.ClockController from its 

    System.Windows.Media.Animation.Clock.Controller property so that the 

    System.Windows.Media.Animation.Clock tree can be interactively controlled; otherwise,false.

  

   Returns: A new System.Windows.Media.Animation.Clock constructed from this 

    System.Windows.Media.Animation.Timeline. If this System.Windows.Media.Animation.Timeline is a 

    System.Windows.Media.Animation.TimelineGroup that contains child timelines,a tree of 

    System.Windows.Media.Animation.Clock objects is created with a controllable 

    System.Windows.Media.Animation.Clock created from this System.Windows.Media.Animation.Timeline 

    as the root.

  

  CreateClock(self: Timeline) -> Clock

  

   Creates a new,controllable System.Windows.Media.Animation.Clock from this 

    System.Windows.Media.Animation.Timeline. If this System.Windows.Media.Animation.Timeline has 

    children,a tree of clocks is created with this System.Windows.Media.Animation.Timeline as the 

    root.

  

   Returns: A new,controllable System.Windows.Media.Animation.Clock constructed from this 

    System.Windows.Media.Animation.Timeline. If this System.Windows.Media.Animation.Timeline is a 

    System.Windows.Media.Animation.TimelineGroup that contains child timelines,a tree of 

    System.Windows.Media.Animation.Clock objects is created with a controllable 

    System.Windows.Media.Animation.Clock created from this System.Windows.Media.Animation.Timeline 

    as the root.
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
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: Timeline,sourceFreezable: Freezable)

   Makes this instance a frozen clone of the specified System.Windows.Media.Animation.Timeline. 

    Resource references,data bindings,and animations are not copied,but their current values are.

  

  

   sourceFreezable: The System.Windows.Media.Animation.Timeline to copy and freeze.
  """
  pass
 @staticmethod
 def GetDesiredFrameRate(timeline):
  """
  GetDesiredFrameRate(timeline: Timeline) -> Nullable[int]

  

   Gets the desired frame rate of the specified System.Windows.Media.Animation.Timeline.

  

   timeline: The timeline from which to retrieve the desired frame rate.

   Returns: The desired frame rate of this timeline. The default value is null.
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
  GetNaturalDurationCore(self: Timeline,clock: Clock) -> Duration

  

   Returns the length of a single iteration of this System.Windows.Media.Animation.Timeline. This 

    method provides the implementation for 

    System.Windows.Media.Animation.Timeline.GetNaturalDuration(System.Windows.Media.Animation.Clock).

  

  

   clock: The System.Windows.Media.Animation.Clock that was created for this 

    System.Windows.Media.Animation.Timeline.

  

   Returns: The length of a single iteration of this System.Windows.Media.Animation.Timeline,or 

    System.Windows.Duration.Automatic if the natural duration is unknown.
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
 @staticmethod
 def SetDesiredFrameRate(timeline,desiredFrameRate):
  """ SetDesiredFrameRate(timeline: Timeline,desiredFrameRate: Nullable[int]) """
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
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type)

  __new__(cls: type,beginTime: Nullable[TimeSpan])

  __new__(cls: type,beginTime: Nullable[TimeSpan],duration: Duration)

  __new__(cls: type,beginTime: Nullable[TimeSpan],duration: Duration,repeatBehavior: RepeatBehavior)
  """
  pass
 AccelerationRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value specifying the percentage of the timeline's System.Windows.Media.Animation.Timeline.Duration spent accelerating the passage of time from zero to its maximum rate.



Get: AccelerationRatio(self: Timeline) -> float



Set: AccelerationRatio(self: Timeline)=value

"""

 AutoReverse=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the timeline plays in reverse after it completes a forward iteration.



Get: AutoReverse(self: Timeline) -> bool



Set: AutoReverse(self: Timeline)=value

"""

 BeginTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time at which this System.Windows.Media.Animation.Timeline should begin.



Get: BeginTime(self: Timeline) -> Nullable[TimeSpan]



Set: BeginTime(self: Timeline)=value

"""

 DecelerationRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value specifying the percentage of the timeline's System.Windows.Media.Animation.Timeline.Duration spent decelerating the passage of time from its maximum rate to zero.



Get: DecelerationRatio(self: Timeline) -> float



Set: DecelerationRatio(self: Timeline)=value

"""

 Duration=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the length of time for which this timeline plays,not counting repetitions.



Get: Duration(self: Timeline) -> Duration



Set: Duration(self: Timeline)=value

"""

 FillBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that specifies how the System.Windows.Media.Animation.Timeline behaves after it reaches the end of its active period.



Get: FillBehavior(self: Timeline) -> FillBehavior



Set: FillBehavior(self: Timeline)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of this System.Windows.Media.Animation.Timeline.



Get: Name(self: Timeline) -> str



Set: Name(self: Timeline)=value

"""

 RepeatBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the repeating behavior of this timeline.



Get: RepeatBehavior(self: Timeline) -> RepeatBehavior



Set: RepeatBehavior(self: Timeline)=value

"""

 SpeedRatio=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rate,relative to its parent,at which time progresses for this System.Windows.Media.Animation.Timeline.



Get: SpeedRatio(self: Timeline) -> float



Set: SpeedRatio(self: Timeline)=value

"""


 AccelerationRatioProperty=None
 AutoReverseProperty=None
 BeginTimeProperty=None
 Completed=None
 CurrentGlobalSpeedInvalidated=None
 CurrentStateInvalidated=None
 CurrentTimeInvalidated=None
 DecelerationRatioProperty=None
 DesiredFrameRateProperty=None
 DurationProperty=None
 FillBehaviorProperty=None
 NameProperty=None
 RemoveRequested=None
 RepeatBehaviorProperty=None
 SpeedRatioProperty=None

