class Point3DAnimationUsingKeyFrames(Point3DAnimationBase,ISealable,IAnimatable,IResource,IKeyFrameAnimation,IAddChild):
 """
 Animates the value of a System.Windows.Media.Media3D.Point3D property along a set of System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.KeyFrames.

 

 Point3DAnimationUsingKeyFrames()
 """
 def AddChild(self,*args):
  """
  AddChild(self: Point3DAnimationUsingKeyFrames,child: object)

   Adds a child System.Windows.Media.Animation.Point3DKeyFrame to this 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.

  

  

   child: The object to be added as the child of this 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.
  """
  pass
 def AddText(self,*args):
  """
  AddText(self: Point3DAnimationUsingKeyFrames,childText: str)

   Adds a text string as a child of this 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.

  

  

   childText: The text added to the System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.
  """
  pass
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
  Clone(self: Point3DAnimationUsingKeyFrames) -> Point3DAnimationUsingKeyFrames

  

   Creates a modifiable clone of this 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames,making deep copies of this 

    object's values. When copying dependency properties,this method copies resource references and 

    data bindings (but they might no longer resolve) but not animations or their current values.

  

   Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 

    property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """
  CloneCore(self: Point3DAnimationUsingKeyFrames,sourceFreezable: Freezable)

   Makes this instance a deep copy of the specified 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames. When copying dependency 

    properties,this method copies resource references and data bindings (but they might no longer 

    resolve) but not animations or their current values.

  

  

   sourceFreezable: The System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames to clone.
  """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: Point3DAnimationUsingKeyFrames) -> Point3DAnimationUsingKeyFrames

  

   Creates a modifiable clone of this System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames 

    object,making deep copies of this object's current values. Resource references,data bindings,

    and animations are not copied,but their current values are.

  

   Returns: A modifiable clone of the current object. The cloned object's System.Windows.Freezable.IsFrozen 

    property will be false even if the source's System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """
  CloneCurrentValueCore(self: Point3DAnimationUsingKeyFrames,sourceFreezable: Freezable)

   Makes this instance a modifiable deep copy of the specified 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames using current property values. 

    Resource references,data bindings,and animations are not copied,but their current values are.

  

  

   sourceFreezable: The System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames to clone.
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
  CreateInstanceCore(self: Point3DAnimationUsingKeyFrames) -> Freezable

  

   Creates a new instance of System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.

   Returns: A new instance of System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.
  """
  pass
 def FreezeCore(self,*args):
  """
  FreezeCore(self: Point3DAnimationUsingKeyFrames,isChecking: bool) -> bool

  

   Makes this instance of System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames object 

    unmodifiable or determines whether it can be made unmodifiable..

  

  

   isChecking: true to check if this instance can be frozen; false to freeze this instance.

   Returns: If isChecking is true,this method returns true if this instance can be made read-only,or false 

    if it cannot be made read-only. If isChecking is false,this method returns true if this 

    instance is now read-only,or false if it cannot be made read-only,with the side effect of 

    having begun to change the frozen status of this object.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: Point3DAnimationUsingKeyFrames,source: Freezable)

   Makes this instance a clone of the specified 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames object.

  

  

   source: The System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames object to clone.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: Point3DAnimationUsingKeyFrames,source: Freezable)

   Makes this instance a frozen clone of the specified 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames. Resource references,data 

    bindings,and animations are not copied,but their current values are.

  

  

   source: The System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames to copy and freeze.
  """
  pass
 def GetCurrentValueCore(self,*args):
  """
  GetCurrentValueCore(self: Point3DAnimationUsingKeyFrames,defaultOriginValue: Point3D,defaultDestinationValue: Point3D,animationClock: AnimationClock) -> Point3D

  

   Calculates a value that represents the current value of the property being animated,as 

    determined by this instance of System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.

  

  

   defaultOriginValue: The suggested origin value,used if the animation does not have its own explicitly set start 

    value.

  

   defaultDestinationValue: The suggested destination value,used if the animation does not have its own explicitly set end 

    value.

  

   animationClock: An System.Windows.Media.Animation.AnimationClock that generates the 

    System.Windows.Media.Animation.Clock.CurrentTime or 

    System.Windows.Media.Animation.Clock.CurrentProgress used by the host animation.

  

   Returns: The calculated value of the property,as determined by the current instance.
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
  GetNaturalDurationCore(self: Point3DAnimationUsingKeyFrames,clock: Clock) -> Duration

  

   Provide a custom natural System.Windows.Duration when the System.Windows.Duration property is 

    set to System.Windows.Duration.Automatic.

  

  

   clock: The System.Windows.Media.Animation.Clock whose natural duration is desired.

   Returns: If the last key frame of this animation is a System.Windows.Media.Animation.KeyTime,then this 

    value is used as the System.Windows.Media.Animation.Clock.NaturalDuration; otherwise it will be 

    one second.
  """
  pass
 def OnChanged(self,*args):
  """
  OnChanged(self: Point3DAnimationUsingKeyFrames)

   Called when the current System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames object is 

    modified.
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
 def ShouldSerializeKeyFrames(self):
  """
  ShouldSerializeKeyFrames(self: Point3DAnimationUsingKeyFrames) -> bool

  

   Returns true if the value of the 

    System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames.KeyFrames property of this 

    instance of System.Windows.Media.Animation.Point3DAnimationUsingKeyFrames should be 

    value-serialized.

  

   Returns: true if the property value should be serialized; otherwise,false.
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
 IsAdditive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies whether the animation's output value is added to the base value of the property being animated.



Get: IsAdditive(self: Point3DAnimationUsingKeyFrames) -> bool



Set: IsAdditive(self: Point3DAnimationUsingKeyFrames)=value

"""

 IsCumulative=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that specifies whether the animation's value accumulates when it repeats.



Get: IsCumulative(self: Point3DAnimationUsingKeyFrames) -> bool



Set: IsCumulative(self: Point3DAnimationUsingKeyFrames)=value

"""

 KeyFrames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the collection of System.Windows.Media.Animation.Point3DKeyFrame objects that define the animation.



Get: KeyFrames(self: Point3DAnimationUsingKeyFrames) -> Point3DKeyFrameCollection



Set: KeyFrames(self: Point3DAnimationUsingKeyFrames)=value

"""


