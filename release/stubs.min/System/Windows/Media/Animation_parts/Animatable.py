class Animatable(Freezable,ISealable,IAnimatable,IResource):
 """ Abstract class that provides animation support. """
 def ApplyAnimationClock(self,dp,clock,handoffBehavior=None):
  """
  ApplyAnimationClock(self: Animatable,dp: DependencyProperty,clock: AnimationClock,handoffBehavior: HandoffBehavior)

   Applies an System.Windows.Media.Animation.AnimationClock to the specified 

    System.Windows.DependencyProperty. If the property is already animated,the specified 

    System.Windows.Media.Animation.HandoffBehavior is used.

  

  

   dp: The property to animate.

   clock: The clock with which to animate the specified property. If handoffBehavior is 

    System.Windows.Media.Animation.HandoffBehavior.SnapshotAndReplace and clock is null,all 

    animations will be removed from the specified property (but not stopped). If handoffBehavior is 

    System.Windows.Media.Animation.HandoffBehavior.Compose and clock is null,this method has no 

    effect.

  

   handoffBehavior: A value that specifies how the new animation should interact with any current animations already 

    affecting the property value.

  

  ApplyAnimationClock(self: Animatable,dp: DependencyProperty,clock: AnimationClock)

   Applies an System.Windows.Media.Animation.AnimationClock to the specified 

    System.Windows.DependencyProperty. If the property is already animated,the 

    System.Windows.Media.Animation.HandoffBehavior.SnapshotAndReplace handoff behavior is used.

  

  

   dp: The property to animate.

   clock: The clock with which to animate the specified property. If clock is null,all animations will be 

    removed from the specified property (but not stopped).
  """
  pass
 def BeginAnimation(self,dp,animation,handoffBehavior=None):
  """
  BeginAnimation(self: Animatable,dp: DependencyProperty,animation: AnimationTimeline,handoffBehavior: HandoffBehavior)

   Applies an animation to the specified System.Windows.DependencyProperty. The animation is 

    started when the next frame is rendered. If the specified property is already animated,the 

    specified System.Windows.Media.Animation.HandoffBehavior is used.

  

  

   dp: The property to animate.

   animation: The animation used to animate the specified property.If handoffBehavior is 

    System.Windows.Media.Animation.HandoffBehavior.SnapshotAndReplace and the animation's 

    System.Windows.Media.Animation.Timeline.BeginTime is null,any current animations will be 

    removed and the current value of the property will be held. If handoffBehavior is 

    System.Windows.Media.Animation.HandoffBehavior.SnapshotAndReplace and animation is a null 

    reference,all animations will be removed from the property and the property value will revert 

    back to its base value.If handoffBehavior is 

    System.Windows.Media.Animation.HandoffBehavior.Compose,this method will have no effect if the 

    animation or its System.Windows.Media.Animation.Timeline.BeginTime is null.

  

   handoffBehavior: A value that specifies how the new animation should interact with any current animations already 

    affecting the property value.

  

  BeginAnimation(self: Animatable,dp: DependencyProperty,animation: AnimationTimeline)

   Applies an animation to the specified System.Windows.DependencyProperty. The animation is 

    started when the next frame is rendered. If the specified property is already animated,the 

    System.Windows.Media.Animation.HandoffBehavior.SnapshotAndReplace handoff behavior is used.

  

  

   dp: The property to animate.

   animation: The animation used to animate the specified property.If the animation's 

    System.Windows.Media.Animation.Timeline.BeginTime is null,any current animations will be 

    removed and the current value of the property will be held.If animation is null,all animations 

    will be removed from the property and the property value will revert back to its base value.
  """
  pass
 def Clone(self):
  """
  Clone(self: Animatable) -> Animatable

  

   Creates a modifiable clone of this System.Windows.Media.Animation.Animatable,making deep copies 

    of this object's values. When copying this object's dependency properties,this method copies 

    resource references and data bindings (but they might no longer resolve) but not animations or 

    their current values.

  

   Returns: A modifiable clone of this instance. The returned clone is effectively a deep copy of the 

    current object. The clone's System.Windows.Freezable.IsFrozen property is false.
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
  FreezeCore(self: Animatable,isChecking: bool) -> bool

  

   Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether 

    it can be made unmodifiable.

  

  

   isChecking: true if this method should simply determine whether this instance can be frozen. false if this 

    instance should actually freeze itself when this method is called.

  

   Returns: If isChecking is true,this method returns true if this 

    System.Windows.Media.Animation.Animatable can be made unmodifiable,or false if it cannot be 

    made unmodifiable. If isChecking is false,this method returns true if the if this 

    System.Windows.Media.Animation.Animatable is now unmodifiable,or false if it cannot be made 

    unmodifiable,with the side effect of having begun to change the frozen status of this object.
  """
  pass
 def GetAnimationBaseValue(self,dp):
  """
  GetAnimationBaseValue(self: Animatable,dp: DependencyProperty) -> object

  

   Returns the non-animated value of the specified System.Windows.DependencyProperty.

  

   dp: Identifies the property whose base (non-animated) value should be retrieved.

   Returns: The value that would be returned if the specified property were not animated.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: Freezable,sourceFreezable: Freezable)

   Makes the instance a frozen clone of the specified System.Windows.Freezable using base 

    (non-animated) property values.

  

  

   sourceFreezable: The instance to copy.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: Freezable,sourceFreezable: Freezable)

   Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the 

    object has animated dependency properties,their current animated values are copied.

  

  

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
 @staticmethod
 def ShouldSerializeStoredWeakReference(target):
  """
  ShouldSerializeStoredWeakReference(target: DependencyObject) -> bool

  

   Specifies whether a dependency object should be serialized.

  

   target: Represents an object that participates in the dependency property system.

   Returns: true to serialize target; otherwise,false. The default is false.
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
 HasAnimatedProperties=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether one or more System.Windows.Media.Animation.AnimationClock objects is associated with any of this object's dependency properties.



Get: HasAnimatedProperties(self: Animatable) -> bool



"""


