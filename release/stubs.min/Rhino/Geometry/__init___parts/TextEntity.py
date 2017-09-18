class TextEntity(AnnotationBase,IDisposable,ISerializable):
 """
 Represents text geometry.

    This class refers to the geometric element that is independent from the document.

 

 TextEntity()
 """
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CommonObject,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def Explode(self):
  """
  Explode(self: TextEntity) -> Array[Curve]

  

   Explodes this text entity into an array of curves.

   Returns: An array of curves that forms the outline or content of this text entity.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: CommonObject)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 AnnotativeScalingEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Scale annotation according to detail scale factor in paperspace

   or by 1.0 in paperspace and not in a detail

   Otherwise,dimscale or text scale is used



Get: AnnotativeScalingEnabled(self: TextEntity) -> bool



Set: AnnotativeScalingEnabled(self: TextEntity)=value

"""

 FontIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of font in document font table used by the text.



Get: FontIndex(self: TextEntity) -> int



Set: FontIndex(self: TextEntity)=value

"""

 Justification=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the justification of text in relation to its base point.



Get: Justification(self: TextEntity) -> TextJustification



Set: Justification(self: TextEntity)=value

"""

 MaskColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Color to use for drawing a text mask when it is enabled. If the mask is

   enabled and MaskColor is System.Drawing.Color.Transparent,then the

   viewport's color will be used for the MaskColor



Get: MaskColor(self: TextEntity) -> Color



Set: MaskColor(self: TextEntity)=value

"""

 MaskEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether or not to draw a Text Mask



Get: MaskEnabled(self: TextEntity) -> bool



Set: MaskEnabled(self: TextEntity)=value

"""

 MaskOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """distance around text to display mask



Get: MaskOffset(self: TextEntity) -> float



Set: MaskOffset(self: TextEntity)=value

"""

 MaskUsesViewportColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If true,the viewport's color is used for the mask color. If

   false,the color defined by MaskColor is used



Get: MaskUsesViewportColor(self: TextEntity) -> bool



Set: MaskUsesViewportColor(self: TextEntity)=value

"""


