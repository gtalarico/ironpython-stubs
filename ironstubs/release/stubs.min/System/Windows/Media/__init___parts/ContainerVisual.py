class ContainerVisual(Visual,IResource):
 """
 Manages a collection of System.Windows.Media.Visual objects.
 
 ContainerVisual()
 """
 def AddVisualChild(self,*args):
  """
  AddVisualChild(self: Visual,child: Visual)
   Defines the parent-child relationship between two visuals.
  
   child: The child visual object to add to parent visual.
  AddVisualChild(self: Window_16$17,child: Window_16$17)AddVisualChild(self: Label_17$18,child: Label_17$18)AddVisualChild(self: TextBox_18$19,child: TextBox_18$19)AddVisualChild(self: Button_19$20,child: Button_19$20)AddVisualChild(self: CheckBox_20$21,child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22,child: ComboBox_21$22)AddVisualChild(self: Separator_22$23,child: Separator_22$23)
  """
  pass
 def GetVisualChild(self,*args):
  """
  GetVisualChild(self: ContainerVisual,index: int) -> Visual
  
   Returns a specified child System.Windows.Media.Visual for the parent 
    System.Windows.Media.ContainerVisual.
  
  
   index: A 32-bit signed integer that represents the index value of the child 
    System.Windows.Media.Visual. The value of index must be between 0 and 
    System.Windows.Media.ContainerVisual.VisualChildrenCount - 1.
  
   Returns: The child System.Windows.Media.Visual.
  """
  pass
 def HitTest(self,*__args):
  """
  HitTest(self: ContainerVisual,filterCallback: HitTestFilterCallback,resultCallback: HitTestResultCallback,hitTestParameters: HitTestParameters)
   Initiates a hit test on the System.Windows.Media.ContainerVisual by using the 
    System.Windows.Media.HitTestFilterCallback and 
    System.Windows.Media.HitTestResultCallback objects.
  
  
   filterCallback: The delegate that allows you to ignore parts of the visual tree that you are 
    not interested in processing in your hit test results.
  
   resultCallback: The delegate that is used to control the return of hit test information.
   hitTestParameters: Defines the set of parameters for a hit test.
  HitTest(self: ContainerVisual,point: Point) -> HitTestResult
  
   Returns the top-most visual object of a hit test by specifying a 
    System.Windows.Point.
  
  
   point: The point value to hit test.
   Returns: The hit test result of the visual returned as a 
    System.Windows.Media.HitTestResult type.
  """
  pass
 def HitTestCore(self,*args):
  """
  HitTestCore(self: Visual,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  
   Determines whether a geometry value is within the bounds of the visual object.
  
   hitTestParameters: A System.Windows.Media.GeometryHitTestParameters object that specifies the 
    System.Windows.Media.Geometry to hit test against.
  
   Returns: A System.Windows.Media.GeometryHitTestResult that represents the result of the 
    hit test.
  
  HitTestCore(self: Visual,hitTestParameters: PointHitTestParameters) -> HitTestResult
  
   Determines whether a point coordinate value is within the bounds of the visual 
    object.
  
  
   hitTestParameters: A System.Windows.Media.PointHitTestParameters object that specifies the 
    System.Windows.Point to hit test against.
  
   Returns: A System.Windows.Media.HitTestResult that represents the 
    System.Windows.Media.Visual that is returned from a hit test.
  
  HitTestCore(self: Window_16$17,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Window_16$17,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Label_17$18,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Label_17$18,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: TextBox_18$19,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: TextBox_18$19,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Button_19$20,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Button_19$20,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: CheckBox_20$21,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: CheckBox_20$21,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: ComboBox_21$22,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: ComboBox_21$22,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  HitTestCore(self: Separator_22$23,hitTestParameters: PointHitTestParameters) -> HitTestResult
  HitTestCore(self: Separator_22$23,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  """
  pass
 def OnDpiChanged(self,*args):
  """ OnDpiChanged(self: Visual,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Window_16$17,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Label_17$18,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Button_19$20,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22,oldDpi: DpiScale,newDpi: DpiScale)OnDpiChanged(self: Separator_22$23,oldDpi: DpiScale,newDpi: DpiScale) """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: DependencyObject,e: DependencyPropertyChangedEventArgs)
   Invoked whenever the effective value of any dependency property on this 
    System.Windows.DependencyObject has been updated. The specific dependency 
    property that changed is reported in the event data.
  
  
   e: Event data that will contain the dependency property identifier of interest,
    the property metadata for the type,and old and new values.
  
  OnPropertyChanged(self: Window_16$17,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22,e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23,e: DependencyPropertyChangedEventArgs)
  """
  pass
 def OnVisualChildrenChanged(self,*args):
  """
  OnVisualChildrenChanged(self: Visual,visualAdded: DependencyObject,visualRemoved: DependencyObject)
   Called when the System.Windows.Media.VisualCollection of the visual object is 
    modified.
  
  
   visualAdded: The System.Windows.Media.Visual that was added to the collection
   visualRemoved: The System.Windows.Media.Visual that was removed from the collection
  OnVisualChildrenChanged(self: Window_16$17,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22,visualAdded: DependencyObject,visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23,visualAdded: DependencyObject,visualRemoved: DependencyObject)
  """
  pass
 def OnVisualParentChanged(self,*args):
  """
  OnVisualParentChanged(self: Visual,oldParent: DependencyObject)
   Called when the parent of the visual object is changed.
  
   oldParent: A value of type System.Windows.DependencyObject that represents the previous 
    parent of the System.Windows.Media.Visual object. If the 
    System.Windows.Media.Visual object did not have a previous parent,the value of 
    the parameter is null.
  
  OnVisualParentChanged(self: Window_16$17,oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18,oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19,oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20,oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21,oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22,oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23,oldParent: DependencyObject)
  """
  pass
 def RemoveVisualChild(self,*args):
  """
  RemoveVisualChild(self: Visual,child: Visual)
   Removes the parent-child relationship between two visuals.
  
   child: The child visual object to remove from the parent visual.
  RemoveVisualChild(self: Window_16$17,child: Window_16$17)RemoveVisualChild(self: Label_17$18,child: Label_17$18)RemoveVisualChild(self: TextBox_18$19,child: TextBox_18$19)RemoveVisualChild(self: Button_19$20,child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21,child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22,child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23,child: Separator_22$23)
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
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 BitmapEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.ContainerVisual.

Get: BitmapEffect(self: ContainerVisual) -> BitmapEffect

Set: BitmapEffect(self: ContainerVisual)=value
"""

 BitmapEffectInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.ContainerVisual.

Get: BitmapEffectInput(self: ContainerVisual) -> BitmapEffectInput

Set: BitmapEffectInput(self: ContainerVisual)=value
"""

 CacheMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a cached representation of the System.Windows.Media.ContainerVisual.

Get: CacheMode(self: ContainerVisual) -> CacheMode

Set: CacheMode(self: ContainerVisual)=value
"""

 Children=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the child collection of the System.Windows.Media.ContainerVisual.

Get: Children(self: ContainerVisual) -> VisualCollection

"""

 Clip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the clipping region of the System.Windows.Media.ContainerVisual.

Get: Clip(self: ContainerVisual) -> Geometry

Set: Clip(self: ContainerVisual)=value
"""

 ContentBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounding box for the contents of the System.Windows.Media.ContainerVisual.

Get: ContentBounds(self: ContainerVisual) -> Rect

"""

 DescendantBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the union of all the content bounding boxes for all of the descendants of the System.Windows.Media.ContainerVisual,but not including the contents of the System.Windows.Media.ContainerVisual.

Get: DescendantBounds(self: ContainerVisual) -> Rect

"""

 Effect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the bitmap effect to apply to the System.Windows.Media.ContainerVisual.

Get: Effect(self: ContainerVisual) -> Effect

Set: Effect(self: ContainerVisual)=value
"""

 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the offset value of the System.Windows.Media.ContainerVisual from its reference point.

Get: Offset(self: ContainerVisual) -> Vector

Set: Offset(self: ContainerVisual)=value
"""

 Opacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the opacity of the System.Windows.Media.ContainerVisual,based on 0=transparent,1=opaque.

Get: Opacity(self: ContainerVisual) -> float

Set: Opacity(self: ContainerVisual)=value
"""

 OpacityMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a brush that specifies a possible opacity mask for the System.Windows.Media.ContainerVisual.

Get: OpacityMask(self: ContainerVisual) -> Brush

Set: OpacityMask(self: ContainerVisual)=value
"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent System.Windows.Media.Visual for the System.Windows.Media.ContainerVisual.

Get: Parent(self: ContainerVisual) -> DependencyObject

"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the transform that is applied to the System.Windows.Media.ContainerVisual.

Get: Transform(self: ContainerVisual) -> Transform

Set: Transform(self: ContainerVisual)=value
"""

 VisualBitmapEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

 VisualBitmapEffectInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

 VisualBitmapScalingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

 VisualCacheMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

 VisualChildrenCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of children for the System.Windows.Media.ContainerVisual.

"""

 VisualClearTypeHint=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

 VisualClip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

 VisualEdgeMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

 VisualEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

 VisualOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the offset value of the visual object.

"""

 VisualOpacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

 VisualOpacityMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

 VisualParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the visual tree parent of the visual object.

"""

 VisualScrollableAreaClip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

 VisualTextHintingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

 VisualTextRenderingMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

 VisualTransform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

 VisualXSnappingGuidelines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate (vertical) guideline collection.

"""

 VisualYSnappingGuidelines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate (horizontal) guideline collection.

"""

 XSnappingGuidelines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X (horizontal) guideline for the System.Windows.Media.ContainerVisual.

Get: XSnappingGuidelines(self: ContainerVisual) -> DoubleCollection

Set: XSnappingGuidelines(self: ContainerVisual)=value
"""

 YSnappingGuidelines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y (vertical) guideline for the System.Windows.Media.ContainerVisual.

Get: YSnappingGuidelines(self: ContainerVisual) -> DoubleCollection

Set: YSnappingGuidelines(self: ContainerVisual)=value
"""


