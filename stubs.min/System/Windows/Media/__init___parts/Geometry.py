class Geometry(Animatable,ISealable,IAnimatable,IResource,IFormattable):
 """ Classes that derive from this abstract base class define geometric shapes. System.Windows.Media.Geometry objects can be used for clipping,hit-testing,and rendering 2-D graphic data. """
 def Clone(self):
  """
  Clone(self: Geometry) -> Geometry
  
   Creates a modifiable clone of the System.Windows.Media.Geometry,making deep 
    copies of the object's values. When copying dependency properties,this method 
    copies resource references and data bindings (but they might no longer resolve) 
    but not animations or their current values.
  
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
  CloneCurrentValue(self: Geometry) -> Geometry
  
   Creates a modifiable clone of the System.Windows.Media.Geometry object,making 
    deep copies of the object's current values. Resource references,data bindings,
    and animations are not copied,but their current values are.
  
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
 @staticmethod
 def Combine(geometry1,geometry2,mode,transform,tolerance=None,type=None):
  """
  Combine(geometry1: Geometry,geometry2: Geometry,mode: GeometryCombineMode,transform: Transform) -> PathGeometry
  
   Combines the two geometries using the specified 
    System.Windows.Media.GeometryCombineMode and applies the specified transform to 
    the resulting geometry.
  
  
   geometry1: The first geometry to combine.
   geometry2: The second geometry to combine.
   mode: One of the enumeration values that specifies how the geometries are combined.
   transform: A transformation to apply to the combined geometry,or null.
   Returns: The combined geometry.
  Combine(geometry1: Geometry,geometry2: Geometry,mode: GeometryCombineMode,transform: Transform,tolerance: float,type: ToleranceType) -> PathGeometry
  
   Combines the two geometries using the specified 
    System.Windows.Media.GeometryCombineMode and tolerance factor,and applies the 
    specified transform to the resulting geometry.
  
  
   geometry1: The first geometry to combine.
   geometry2: The second geometry to combine.
   mode: One of the enumeration values that specifies how the geometries are combined.
   transform: A transformation to apply to the combined geometry,or null.
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometries. Smaller values produce more accurate results 
    but cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: The combined geometry.
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
 def FillContains(self,*__args):
  """
  FillContains(self: Geometry,geometry: Geometry,tolerance: float,type: ToleranceType) -> bool
  
   Indicates whether the current geometry contains the specified 
    System.Windows.Media.Geometry,given the specified margin of error.
  
  
   geometry: The geometry to test for containment.
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometries. Smaller values produce more accurate results 
    but cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: true if the current geometry contains geometry,given the specified margin of 
    error; otherwise,false.
  
  FillContains(self: Geometry,geometry: Geometry) -> bool
  
   Indicates whether the current geometry completely contains the specified 
    System.Windows.Media.Geometry.
  
  
   geometry: The geometry to test for containment.
   Returns: true if the current geometry completely contains geometry; otherwise,false.
  FillContains(self: Geometry,hitPoint: Point,tolerance: float,type: ToleranceType) -> bool
  
   Indicates whether the geometry contains the specified System.Windows.Point,
    given the specified margin of error.
  
  
   hitPoint: The point to test for containment.
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometry. Smaller values produce more accurate results but 
    cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: true if the geometry contains hitPoint,given the specified margin of error; 
    otherwise,false.
  
  FillContains(self: Geometry,hitPoint: Point) -> bool
  
   Indicates whether the geometry contains the specified System.Windows.Point.
  
   hitPoint: The point to test for containment.
   Returns: true if the geometry contains hitPoint; otherwise,false.
  """
  pass
 def FillContainsWithDetail(self,geometry,tolerance=None,type=None):
  """
  FillContainsWithDetail(self: Geometry,geometry: Geometry) -> IntersectionDetail
  
   Returns a value that describes the intersection between the current geometry 
    and the specified geometry.
  
  
   geometry: The geometry to test for containment.
   Returns: One of the enumeration values.
  FillContainsWithDetail(self: Geometry,geometry: Geometry,tolerance: float,type: ToleranceType) -> IntersectionDetail
  
   Returns a value that describes the intersection between the current geometry 
    and the specified geometry,given the specified margin of error.
  
  
   geometry: The geometry to test for containment.
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometries. Smaller values produce more accurate results 
    but cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: One of the enumeration values.
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
 def GetArea(self,tolerance=None,type=None):
  """
  GetArea(self: Geometry) -> float
  
   Gets the area of the filled region of the System.Windows.Media.Geometry object.
   Returns: The area of the filled region of the geometry.
  GetArea(self: Geometry,tolerance: float,type: ToleranceType) -> float
  
   Gets the area,within the specified tolerance,of the filled region of the 
    System.Windows.Media.Geometry object.
  
  
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometry. Smaller values produce more accurate results but 
    cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: The area of the filled region of the geometry.
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
 def GetFlattenedPathGeometry(self,tolerance=None,type=None):
  """
  GetFlattenedPathGeometry(self: Geometry) -> PathGeometry
  
   Gets a System.Windows.Media.PathGeometry that is a polygonal approximation of 
    the System.Windows.Media.Geometry object.
  
   Returns: The polygonal approximation of the System.Windows.Media.Geometry.
  GetFlattenedPathGeometry(self: Geometry,tolerance: float,type: ToleranceType) -> PathGeometry
  
   Gets a System.Windows.Media.PathGeometry,within the specified tolerance,that 
    is a polygonal approximation of the System.Windows.Media.Geometry object.
  
  
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometry. Smaller values produce more accurate results but 
    cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: The polygonal approximation of the System.Windows.Media.Geometry.
  """
  pass
 def GetOutlinedPathGeometry(self,tolerance=None,type=None):
  """
  GetOutlinedPathGeometry(self: Geometry) -> PathGeometry
  
   Gets a System.Windows.Media.PathGeometry that is a simplified outline of the 
    filled region of the System.Windows.Media.Geometry.
  
   Returns: A simplified outline of the filled region of the System.Windows.Media.Geometry.
  GetOutlinedPathGeometry(self: Geometry,tolerance: float,type: ToleranceType) -> PathGeometry
  
   Gets a System.Windows.Media.PathGeometry,within the specified tolerance,that 
    is a simplified outline of the filled region of the 
    System.Windows.Media.Geometry.
  
  
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometry. Smaller values produce more accurate results but 
    cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: A simplified outline of the filled region of the System.Windows.Media.Geometry.
  """
  pass
 def GetRenderBounds(self,pen,tolerance=None,type=None):
  """
  GetRenderBounds(self: Geometry,pen: Pen) -> Rect
  
   Returns an axis-aligned rectangle that is exactly large enough to contain the 
    geometry after it has been outlined with the specified 
    System.Windows.Media.Pen.
  
  
   pen: An object that describes the area of the geometry's stroke.
   Returns: An axis aligned rectangle that is exactly large enough to contain the outlined 
    geometry.
  
  GetRenderBounds(self: Geometry,pen: Pen,tolerance: float,type: ToleranceType) -> Rect
  
   Returns an axis-aligned rectangle that is exactly large enough to contain the 
    geometry after it has been outlined with the specified 
    System.Windows.Media.Pen,given the specified tolerance factor.
  
  
   pen: An object that describes the area of the geometry's stroke.
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometry. Smaller values produce more accurate results but 
    cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: An axis aligned rectangle that is exactly large enough to contain the outlined 
    geometry.
  """
  pass
 def GetWidenedPathGeometry(self,pen,tolerance=None,type=None):
  """
  GetWidenedPathGeometry(self: Geometry,pen: Pen) -> PathGeometry
  
   Gets a System.Windows.Media.PathGeometry that is the shape defined by the 
    stroke on the System.Windows.Media.Geometry produced by the specified 
    System.Windows.Media.Pen.
  
  
   pen: An object that describes the area of the geometry's stroke.
   Returns: The outlined geometry.
  GetWidenedPathGeometry(self: Geometry,pen: Pen,tolerance: float,type: ToleranceType) -> PathGeometry
  
   Gets a System.Windows.Media.PathGeometry that is the shape defined by the 
    stroke on the System.Windows.Media.Geometry produced by the specified 
    System.Windows.Media.Pen,given the specified tolerance factor.
  
  
   pen: The object used to define the area of the geometry's stroke.
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometry. Smaller values produce more accurate results but 
    cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: The geometry,widened by pen.
  """
  pass
 def IsEmpty(self):
  """
  IsEmpty(self: Geometry) -> bool
  
   Determines whether the object is empty.
   Returns: true if the geometry is empty; otherwise,false.
  """
  pass
 def MayHaveCurves(self):
  """
  MayHaveCurves(self: Geometry) -> bool
  
   Determines whether the object might have curved segments.
   Returns: true if the geometry object might have curved segments; otherwise,false.
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
 @staticmethod
 def Parse(source):
  """
  Parse(source: str) -> Geometry
  
   Creates a new System.Windows.Media.Geometry instance from the specified string 
    using the current culture.
  
  
   source: A string that describes the geometry to be created.
   Returns: A new System.Windows.Media.Geometry instance created from the specified string.
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
 def ShouldSerializeTransform(self):
  """
  ShouldSerializeTransform(self: Geometry) -> bool
  
   Gets a value that indicates whether the value of the 
    System.Windows.Media.Geometry.Transform property should be serialized.
  
   Returns: true if the value of the geometry's System.Windows.Media.Geometry.Transform 
    property should be serialized; otherwise,false.
  """
  pass
 def StrokeContains(self,pen,hitPoint,tolerance=None,type=None):
  """
  StrokeContains(self: Geometry,pen: Pen,hitPoint: Point) -> bool
  
   Determines whether the specified System.Windows.Point is contained in the 
    stroke produced by applying the specified System.Windows.Media.Pen to the 
    geometry.
  
  
   pen: An object that determines the area of the geometry's stroke.
   hitPoint: The point to test for containment.
   Returns: true if hitPoint is contained in the stroke produced by applying the specified 
    System.Windows.Media.Pen to the geometry; otherwise,false.
  
  StrokeContains(self: Geometry,pen: Pen,hitPoint: Point,tolerance: float,type: ToleranceType) -> bool
  
   Determines whether the specified System.Windows.Point is contained in the 
    stroke produced by applying the specified System.Windows.Media.Pen to the 
    geometry,given the specified margin of error.
  
  
   pen: An object that defines the stroke of a geometry.
   hitPoint: The point to test for containment.
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometry. Smaller values produce more accurate results but 
    cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: true if the stroke created by applying the specified System.Windows.Media.Pen 
    to the geometry contains the specified point,given the specified tolerance 
    factor; otherwise,false.
  """
  pass
 def StrokeContainsWithDetail(self,pen,geometry,tolerance=None,type=None):
  """
  StrokeContainsWithDetail(self: Geometry,pen: Pen,geometry: Geometry) -> IntersectionDetail
  
   Returns a value that describes the intersection between the specified 
    System.Windows.Media.Geometry and the stroke created by applying the specified 
    System.Windows.Media.Pen to the current geometry.
  
  
   pen: An object that determines the area of the current geometry's stroke.
   geometry: The geometry to test for containment.
   Returns: One of the enumeration values.
  StrokeContainsWithDetail(self: Geometry,pen: Pen,geometry: Geometry,tolerance: float,type: ToleranceType) -> IntersectionDetail
  
   Gets a value that describes the intersection between the specified 
    System.Windows.Media.Geometry and the stroke created by applying the specified 
    System.Windows.Media.Pen to the current geometry,given the specified margin of 
    error.
  
  
   pen: An object that determines the area of the current geometry's stroke.
   geometry: The geometry to test for containment.
   tolerance: The maximum bounds on the distance between points in the polygonal 
    approximation of the geometries. Smaller values produce more accurate results 
    but cause slower execution. If tolerance is less than .000001,.000001 is used 
    instead.
  
   type: One of the System.Windows.Media.ToleranceType values that specifies whether the 
    tolerance factor is an absolute value or relative to the area of the geometry.
  
   Returns: One of the enumeration values.
  """
  pass
 def ToString(self,provider=None):
  """
  ToString(self: Geometry,provider: IFormatProvider) -> str
  
   Creates a string representation of the object using the specified 
    culture-specific formatting information.
  
  
   provider: Culture-specific formatting information,or null to use the current culture.
   Returns: A string representation of the object.
  ToString(self: Geometry) -> str
  
   Creates a string representation of the object based on the current culture.
   Returns: A string representation of the object.
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
 """Gets a System.Windows.Rect that specifies the axis-aligned bounding box of the System.Windows.Media.Geometry.

Get: Bounds(self: Geometry) -> Rect

"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Transform object applied to a System.Windows.Media.Geometry.

Get: Transform(self: Geometry) -> Transform

Set: Transform(self: Geometry)=value
"""


 Empty=None
 StandardFlatteningTolerance=0.25
 TransformProperty=None

