class KeySpline(Freezable,ISealable,IFormattable):
 """
 This class is used by a spline key frame to define animation progress.

 

 KeySpline(controlPoint1: Point,controlPoint2: Point)

 KeySpline()

 KeySpline(x1: float,y1: float,x2: float,y2: float)
 """
 def CloneCore(self,*args):
  """
  CloneCore(self: KeySpline,sourceFreezable: Freezable)

   Makes this instance a deep copy of the specified System.Windows.Media.Animation.KeySpline. When 

    copying dependency properties,this method copies resource references and data bindings (but 

    they might no longer resolve) but not animations or their current values.

  

  

   sourceFreezable: The System.Windows.Media.Animation.KeySpline to clone.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """
  CloneCurrentValueCore(self: KeySpline,sourceFreezable: Freezable)

   Makes this instance a modifiable deep copy of the specified 

    System.Windows.Media.Animation.KeySpline using current property values. Resource references,

    data bindings,and animations are not copied,but their current values are.

  

  

   sourceFreezable: The System.Windows.Media.Animation.KeySpline to clone.
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
  CreateInstanceCore(self: KeySpline) -> Freezable

  

   Creates a new instance of System.Windows.Media.Animation.KeySpline.

   Returns: A new instance of System.Windows.Media.Animation.KeySpline.
  """
  pass
 def FreezeCore(self,*args):
  """
  FreezeCore(self: Freezable,isChecking: bool) -> bool

  

   Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made 

    unmodifiable.

  

  

   isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); 

    false to actually freeze the object.

  

   Returns: If isChecking is true,this method returns true if the System.Windows.Freezable can be made 

    unmodifiable,or false if it cannot be made unmodifiable. If isChecking is false,this method 

    returns true if the if the specified System.Windows.Freezable is now unmodifiable,or false if 

    it cannot be made unmodifiable.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: KeySpline,sourceFreezable: Freezable)

   Makes this instance a clone of the specified System.Windows.Media.Animation.KeySpline object.

  

   sourceFreezable: The System.Windows.Media.Animation.KeySpline object to clone.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: KeySpline,sourceFreezable: Freezable)

   Makes this instance a frozen clone of the specified System.Windows.Media.Animation.KeySpline. 

    Resource references,data bindings,and animations are not copied,but their current values are.

  

  

   sourceFreezable: The System.Windows.Media.Animation.KeySpline to copy and freeze.
  """
  pass
 def GetSplineProgress(self,linearProgress):
  """
  GetSplineProgress(self: KeySpline,linearProgress: float) -> float

  

   Calculates spline progress from a supplied linear progress.

  

   linearProgress: The linear progress to evaluate.

   Returns: The calculated spline progress.
  """
  pass
 def OnChanged(self,*args):
  """
  OnChanged(self: KeySpline)

   Called when the current System.Windows.Media.Animation.KeySpline object is modified.
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
 def ToString(self,formatProvider=None):
  """
  ToString(self: KeySpline,formatProvider: IFormatProvider) -> str

  

   Creates a string representation of this System.Windows.Media.Animation.KeySpline based on the 

    supplied System.IFormatProvider.

  

  

   formatProvider: The format provider to use. If provider is null,the current culture is used.

   Returns: A string representation of this instance of System.Windows.Media.Animation.KeySpline.

  ToString(self: KeySpline) -> str

  

   Creates a string representation of this instance of System.Windows.Media.Animation.KeySpline 

    based on the current culture.

  

   Returns: A string representation of this System.Windows.Media.Animation.KeySpline.
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

  __new__(cls: type,x1: float,y1: float,x2: float,y2: float)

  __new__(cls: type,controlPoint1: Point,controlPoint2: Point)
  """
  pass
 def __str__(self,*args):
  pass
 ControlPoint1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The first control point used to define a Bezier curve that describes a System.Windows.Media.Animation.KeySpline.



Get: ControlPoint1(self: KeySpline) -> Point



Set: ControlPoint1(self: KeySpline)=value

"""

 ControlPoint2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The second control point used to define a Bezier curve that describes a System.Windows.Media.Animation.KeySpline.



Get: ControlPoint2(self: KeySpline) -> Point



Set: ControlPoint2(self: KeySpline)=value

"""


