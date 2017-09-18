class Pen(MarshalByRefObject,ISystemColorTracker,ICloneable,IDisposable):
 """
 Defines an object used to draw lines and curves. This class cannot be inherited.

 

 Pen(color: Color)

 Pen(color: Color,width: Single)

 Pen(brush: Brush)

 Pen(brush: Brush,width: Single)
 """
 def Clone(self):
  """
  Clone(self: Pen) -> object

  

   Creates an exact copy of this System.Drawing.Pen.

   Returns: An System.Object that can be cast to a System.Drawing.Pen.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Pen)

   Releases all resources used by this System.Drawing.Pen.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def MultiplyTransform(self,matrix,order=None):
  """
  MultiplyTransform(self: Pen,matrix: Matrix,order: MatrixOrder)

   Multiplies the transformation matrix for this System.Drawing.Pen by the specified 

    System.Drawing.Drawing2D.Matrix in the specified order.

  

  

   matrix: The System.Drawing.Drawing2D.Matrix by which to multiply the transformation matrix.

   order: The order in which to perform the multiplication operation.

  MultiplyTransform(self: Pen,matrix: Matrix)

   Multiplies the transformation matrix for this System.Drawing.Pen by the specified 

    System.Drawing.Drawing2D.Matrix.

  

  

   matrix: The System.Drawing.Drawing2D.Matrix object by which to multiply the transformation matrix.
  """
  pass
 def ResetTransform(self):
  """
  ResetTransform(self: Pen)

   Resets the geometric transformation matrix for this System.Drawing.Pen to identity.
  """
  pass
 def RotateTransform(self,angle,order=None):
  """
  RotateTransform(self: Pen,angle: Single,order: MatrixOrder)

   Rotates the local geometric transformation by the specified angle in the specified order.

  

   angle: The angle of rotation.

   order: A System.Drawing.Drawing2D.MatrixOrder that specifies whether to append or prepend the rotation 

    matrix.

  

  RotateTransform(self: Pen,angle: Single)

   Rotates the local geometric transformation by the specified angle. This method prepends the 

    rotation to the transformation.

  

  

   angle: The angle of rotation.
  """
  pass
 def ScaleTransform(self,sx,sy,order=None):
  """
  ScaleTransform(self: Pen,sx: Single,sy: Single,order: MatrixOrder)

   Scales the local geometric transformation by the specified factors in the specified order.

  

   sx: The factor by which to scale the transformation in the x-axis direction.

   sy: The factor by which to scale the transformation in the y-axis direction.

   order: A System.Drawing.Drawing2D.MatrixOrder that specifies whether to append or prepend the scaling 

    matrix.

  

  ScaleTransform(self: Pen,sx: Single,sy: Single)

   Scales the local geometric transformation by the specified factors. This method prepends the 

    scaling matrix to the transformation.

  

  

   sx: The factor by which to scale the transformation in the x-axis direction.

   sy: The factor by which to scale the transformation in the y-axis direction.
  """
  pass
 def SetLineCap(self,startCap,endCap,dashCap):
  """
  SetLineCap(self: Pen,startCap: LineCap,endCap: LineCap,dashCap: DashCap)

   Sets the values that determine the style of cap used to end lines drawn by this 

    System.Drawing.Pen.

  

  

   startCap: A System.Drawing.Drawing2D.LineCap that represents the cap style to use at the beginning of 

    lines drawn with this System.Drawing.Pen.

  

   endCap: A System.Drawing.Drawing2D.LineCap that represents the cap style to use at the end of lines 

    drawn with this System.Drawing.Pen.

  

   dashCap: A System.Drawing.Drawing2D.LineCap that represents the cap style to use at the beginning or end 

    of dashed lines drawn with this System.Drawing.Pen.
  """
  pass
 def TranslateTransform(self,dx,dy,order=None):
  """
  TranslateTransform(self: Pen,dx: Single,dy: Single,order: MatrixOrder)

   Translates the local geometric transformation by the specified dimensions in the specified order.

  

   dx: The value of the translation in x.

   dy: The value of the translation in y.

   order: The order (prepend or append) in which to apply the translation.

  TranslateTransform(self: Pen,dx: Single,dy: Single)

   Translates the local geometric transformation by the specified dimensions. This method prepends 

    the translation to the transformation.

  

  

   dx: The value of the translation in x.

   dy: The value of the translation in y.
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
 def __new__(self,*__args):
  """
  __new__(cls: type,color: Color)

  __new__(cls: type,color: Color,width: Single)

  __new__(cls: type,brush: Brush)

  __new__(cls: type,brush: Brush,width: Single)
  """
  pass
 Alignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the alignment for this System.Drawing.Pen.



Get: Alignment(self: Pen) -> PenAlignment



Set: Alignment(self: Pen)=value

"""

 Brush=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Drawing.Brush that determines attributes of this System.Drawing.Pen.



Get: Brush(self: Pen) -> Brush



Set: Brush(self: Pen)=value

"""

 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of this System.Drawing.Pen.



Get: Color(self: Pen) -> Color



Set: Color(self: Pen)=value

"""

 CompoundArray=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an array of values that specifies a compound pen. A compound pen draws a compound line made up of parallel lines and spaces.



Get: CompoundArray(self: Pen) -> Array[Single]



Set: CompoundArray(self: Pen)=value

"""

 CustomEndCap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a custom cap to use at the end of lines drawn with this System.Drawing.Pen.



Get: CustomEndCap(self: Pen) -> CustomLineCap



Set: CustomEndCap(self: Pen)=value

"""

 CustomStartCap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a custom cap to use at the beginning of lines drawn with this System.Drawing.Pen.



Get: CustomStartCap(self: Pen) -> CustomLineCap



Set: CustomStartCap(self: Pen)=value

"""

 DashCap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cap style used at the end of the dashes that make up dashed lines drawn with this System.Drawing.Pen.



Get: DashCap(self: Pen) -> DashCap



Set: DashCap(self: Pen)=value

"""

 DashOffset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the distance from the start of a line to the beginning of a dash pattern.



Get: DashOffset(self: Pen) -> Single



Set: DashOffset(self: Pen)=value

"""

 DashPattern=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an array of custom dashes and spaces.



Get: DashPattern(self: Pen) -> Array[Single]



Set: DashPattern(self: Pen)=value

"""

 DashStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style used for dashed lines drawn with this System.Drawing.Pen.



Get: DashStyle(self: Pen) -> DashStyle



Set: DashStyle(self: Pen)=value

"""

 EndCap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cap style used at the end of lines drawn with this System.Drawing.Pen.



Get: EndCap(self: Pen) -> LineCap



Set: EndCap(self: Pen)=value

"""

 LineJoin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the join style for the ends of two consecutive lines drawn with this System.Drawing.Pen.



Get: LineJoin(self: Pen) -> LineJoin



Set: LineJoin(self: Pen)=value

"""

 MiterLimit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the limit of the thickness of the join on a mitered corner.



Get: MiterLimit(self: Pen) -> Single



Set: MiterLimit(self: Pen)=value

"""

 PenType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the style of lines drawn with this System.Drawing.Pen.



Get: PenType(self: Pen) -> PenType



"""

 StartCap=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cap style used at the beginning of lines drawn with this System.Drawing.Pen.



Get: StartCap(self: Pen) -> LineCap



Set: StartCap(self: Pen)=value

"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a copy of the geometric transformation for this System.Drawing.Pen.



Get: Transform(self: Pen) -> Matrix



Set: Transform(self: Pen)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of this System.Drawing.Pen,in units of the System.Drawing.Graphics object used for drawing.



Get: Width(self: Pen) -> Single



Set: Width(self: Pen)=value

"""


