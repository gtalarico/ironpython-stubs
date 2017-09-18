class HostVisual(ContainerVisual,IResource):
 """
 Represents a System.Windows.Media.Visual object that can be connected anywhere to a parent visual tree.
 
 HostVisual()
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
 def HitTestCore(self,*args):
  """
  HitTestCore(self: HostVisual,hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
  
   Implements 
    System.Windows.Media.HostVisual.HitTestCore(System.Windows.Media.GeometryHitTest
    Parameters) to supply base hit testing behavior (returning 
    System.Windows.Media.GeometryHitTestParameters).
  
  
   hitTestParameters: A value of type System.Windows.Media.GeometryHitTestParameters.
   Returns: Returns a value of type System.Windows.Media.GeometryHitTestResult. The 
    System.Windows.Media.GeometryHitTestResult.VisualHit property contains the 
    visual that was hit.
  
  HitTestCore(self: HostVisual,hitTestParameters: PointHitTestParameters) -> HitTestResult
  
   Implements 
    System.Windows.Media.HostVisual.HitTestCore(System.Windows.Media.PointHitTestPar
    ameters) to supply base hit testing behavior (returning 
    System.Windows.Media.PointHitTestParameters).
  
  
   hitTestParameters: A value of type System.Windows.Media.PointHitTestParameters.
   Returns: Returns a value of type System.Windows.Media.HitTestResult. The 
    System.Windows.Media.HitTestResult.VisualHit property contains the visual 
    object that was hit.
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


