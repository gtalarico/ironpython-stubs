class MediaTimeline(Timeline,ISealable,IAnimatable,IResource,IUriContext):
 """
 Provides a System.Windows.Media.Animation.Timeline for media content.
 
 MediaTimeline(source: Uri)
 MediaTimeline()
 MediaTimeline(beginTime: Nullable[TimeSpan])
 MediaTimeline(beginTime: Nullable[TimeSpan],duration: Duration)
 MediaTimeline(beginTime: Nullable[TimeSpan],duration: Duration,repeatBehavior: RepeatBehavior)
 """
 def AllocateClock(self,*args):
  """
  AllocateClock(self: MediaTimeline) -> Clock
  
   Creates a System.Windows.Media.MediaClock for this timeline.
   Returns: A new System.Windows.Media.MediaClock for this timeline.
  """
  pass
 def Clone(self):
  """
  Clone(self: MediaTimeline) -> MediaTimeline
  
   Creates a modifiable clone of this System.Windows.Media.MediaTimeline,making 
    deep copies of this object's values. When copying dependency properties,this 
    method copies resource references and data bindings (but they might no longer 
    resolve) but not animations or their current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """
  CloneCore(self: MediaTimeline,sourceFreezable: Freezable)
   Makes this instance a deep copy of the specified 
    System.Windows.Media.MediaTimeline. When copying dependency properties,this 
    method copies resource references and data bindings (but they might no longer 
    resolve) but not animations or their current values.
  
  
   sourceFreezable: The System.Windows.Media.MediaTimeline to clone.
  """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: MediaTimeline) -> MediaTimeline
  
   Creates a modifiable clone of this System.Windows.Media.MediaTimeline object,
    making deep copies of this object's current values. Resource references,data 
    bindings,and animations are not copied,but their current values are.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """
  CloneCurrentValueCore(self: MediaTimeline,sourceFreezable: Freezable)
   Makes this instance a modifiable deep copy of the specified 
    System.Windows.Media.MediaTimeline using current property values. Resource 
    references,data bindings,and animations are not copied,but their current 
    values are.
  
  
   sourceFreezable: The System.Windows.Media.MediaTimeline to clone.
  """
  pass
 def CreateClock(self,hasControllableRoot=None):
  """
  CreateClock(self: MediaTimeline) -> MediaClock
  
   Creates a new System.Windows.Media.MediaClock associated with the 
    System.Windows.Media.MediaTimeline.
  
   Returns: The new System.Windows.Media.MediaClock.
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
  CreateInstanceCore(self: MediaTimeline) -> Freezable
  
   Creates a new instance of the MediaTimeline.
   Returns: The new instance.
  """
  pass
 def FreezeCore(self,*args):
  """
  FreezeCore(self: MediaTimeline,isChecking: bool) -> bool
  
   Makes this instance of MediaTimeline unmodifiable or determines whether it can 
    be made unmodifiable.
  
  
   isChecking: true to check if the timeline can be frozen; false to freeze the timeline.
   Returns: If isChecking is true,this method returns true if this 
    System.Windows.Media.MediaTimeline can be made unmodifiable,or false if it 
    cannot be made unmodifiable. If isChecking is false,this method returns true 
    if the specified System.Windows.Media.MediaTimeline is now unmodifiable,or 
    false if it cannot be made unmodifiable,with the side effect of having made 
    the actual change in frozen status to this object.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: MediaTimeline,source: Freezable)
   Makes this instance a clone of the specified System.Windows.Media.MediaTimeline 
    object.
  
  
   source: The System.Windows.Media.MediaTimeline object to clone and freeze.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: MediaTimeline,source: Freezable)
   Makes this instance a frozen clone of the specified 
    System.Windows.Media.MediaTimeline. Resource references,data bindings,and 
    animations are not copied,but their current values are.
  
  
   source: The System.Windows.Media.MediaTimeline to copy and freeze.
  """
  pass
 def GetNaturalDuration(self,*args):
  """
  GetNaturalDuration(self: Timeline,clock: Clock) -> Duration
  
   Returns the length of a single iteration of this 
    System.Windows.Media.Animation.Timeline.
  
  
   clock: The System.Windows.Media.Animation.Clock that was created for this 
    System.Windows.Media.Animation.Timeline.
  
   Returns: The length of a single iteration of this 
    System.Windows.Media.Animation.Timeline,or System.Windows.Duration.Automatic 
    if the natural duration is unknown.
  """
  pass
 def GetNaturalDurationCore(self,*args):
  """
  GetNaturalDurationCore(self: MediaTimeline,clock: Clock) -> Duration
  
   Retrieves the System.Windows.Duration from a specified clock.
  
   clock: The System.Windows.Media.Animation.Clock whose natural duration is desired.
   Returns: If clock is a System.Windows.Media.MediaClock,the 
    System.Windows.Media.MediaPlayer.NaturalDuration value of the 
    System.Windows.Media.MediaPlayer associated with clock,or 
    System.Windows.Duration.Automatic if the clock is not a 
    System.Windows.Media.MediaClock.
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
 def ToString(self):
  """
  ToString(self: MediaTimeline) -> str
  
   Returns the string that represents the media source.
   Returns: The string that represents the media source.
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
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,source: Uri)
  __new__(cls: type)
  __new__(cls: type,beginTime: Nullable[TimeSpan])
  __new__(cls: type,beginTime: Nullable[TimeSpan],duration: Duration)
  __new__(cls: type,beginTime: Nullable[TimeSpan],duration: Duration,repeatBehavior: RepeatBehavior)
  """
  pass
 def __str__(self,*args):
  pass
 Source=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the media source associated with the timeline.

Get: Source(self: MediaTimeline) -> Uri

Set: Source(self: MediaTimeline)=value
"""


 SourceProperty=None

