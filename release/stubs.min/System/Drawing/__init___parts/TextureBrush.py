class TextureBrush(Brush,ICloneable,IDisposable):
 """
 Each property of the System.Drawing.TextureBrush class is a System.Drawing.Brush object that uses an image to fill the interior of a shape. This class cannot be inherited.

 

 TextureBrush(bitmap: Image)

 TextureBrush(image: Image,wrapMode: WrapMode)

 TextureBrush(image: Image,wrapMode: WrapMode,dstRect: RectangleF)

 TextureBrush(image: Image,wrapMode: WrapMode,dstRect: Rectangle)

 TextureBrush(image: Image,dstRect: RectangleF)

 TextureBrush(image: Image,dstRect: RectangleF,imageAttr: ImageAttributes)

 TextureBrush(image: Image,dstRect: Rectangle)

 TextureBrush(image: Image,dstRect: Rectangle,imageAttr: ImageAttributes)
 """
 def Clone(self):
  """
  Clone(self: TextureBrush) -> object

  

   Creates an exact copy of this System.Drawing.TextureBrush object.

   Returns: The System.Drawing.TextureBrush object this method creates,cast as an System.Object object.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Brush,disposing: bool)

   Releases the unmanaged resources used by the System.Drawing.Brush and optionally releases the 

    managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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
  MultiplyTransform(self: TextureBrush,matrix: Matrix,order: MatrixOrder)

   Multiplies the System.Drawing.Drawing2D.Matrix object that represents the local geometric 

    transformation of this System.Drawing.TextureBrush object by the specified 

    System.Drawing.Drawing2D.Matrix object in the specified order.

  

  

   matrix: The System.Drawing.Drawing2D.Matrix object by which to multiply the geometric transformation.

   order: A System.Drawing.Drawing2D.MatrixOrder enumeration that specifies the order in which to multiply 

    the two matrices.

  

  MultiplyTransform(self: TextureBrush,matrix: Matrix)

   Multiplies the System.Drawing.Drawing2D.Matrix object that represents the local geometric 

    transformation of this System.Drawing.TextureBrush object by the specified 

    System.Drawing.Drawing2D.Matrix object by prepending the specified 

    System.Drawing.Drawing2D.Matrix object.

  

  

   matrix: The System.Drawing.Drawing2D.Matrix object by which to multiply the geometric transformation.
  """
  pass
 def ResetTransform(self):
  """
  ResetTransform(self: TextureBrush)

   Resets the Transform property of this System.Drawing.TextureBrush object to identity.
  """
  pass
 def RotateTransform(self,angle,order=None):
  """
  RotateTransform(self: TextureBrush,angle: Single,order: MatrixOrder)

   Rotates the local geometric transformation of this System.Drawing.TextureBrush object by the 

    specified amount in the specified order.

  

  

   angle: The angle of rotation.

   order: A System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether to append or prepend 

    the rotation matrix.

  

  RotateTransform(self: TextureBrush,angle: Single)

   Rotates the local geometric transformation of this System.Drawing.TextureBrush object by the 

    specified amount. This method prepends the rotation to the transformation.

  

  

   angle: The angle of rotation.
  """
  pass
 def ScaleTransform(self,sx,sy,order=None):
  """
  ScaleTransform(self: TextureBrush,sx: Single,sy: Single,order: MatrixOrder)

   Scales the local geometric transformation of this System.Drawing.TextureBrush object by the 

    specified amounts in the specified order.

  

  

   sx: The amount by which to scale the transformation in the x direction.

   sy: The amount by which to scale the transformation in the y direction.

   order: A System.Drawing.Drawing2D.MatrixOrder enumeration that specifies whether to append or prepend 

    the scaling matrix.

  

  ScaleTransform(self: TextureBrush,sx: Single,sy: Single)

   Scales the local geometric transformation of this System.Drawing.TextureBrush object by the 

    specified amounts. This method prepends the scaling matrix to the transformation.

  

  

   sx: The amount by which to scale the transformation in the x direction.

   sy: The amount by which to scale the transformation in the y direction.
  """
  pass
 def SetNativeBrush(self,*args):
  """
  SetNativeBrush(self: Brush,brush: IntPtr)

   In a derived class,sets a reference to a GDI+ brush object.

  

   brush: A pointer to the GDI+ brush object.
  """
  pass
 def TranslateTransform(self,dx,dy,order=None):
  """
  TranslateTransform(self: TextureBrush,dx: Single,dy: Single,order: MatrixOrder)

   Translates the local geometric transformation of this System.Drawing.TextureBrush object by the 

    specified dimensions in the specified order.

  

  

   dx: The dimension by which to translate the transformation in the x direction.

   dy: The dimension by which to translate the transformation in the y direction.

   order: The order (prepend or append) in which to apply the translation.

  TranslateTransform(self: TextureBrush,dx: Single,dy: Single)

   Translates the local geometric transformation of this System.Drawing.TextureBrush object by the 

    specified dimensions. This method prepends the translation to the transformation.

  

  

   dx: The dimension by which to translate the transformation in the x direction.

   dy: The dimension by which to translate the transformation in the y direction.
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
  __new__(cls: type,bitmap: Image)

  __new__(cls: type,image: Image,wrapMode: WrapMode)

  __new__(cls: type,image: Image,wrapMode: WrapMode,dstRect: RectangleF)

  __new__(cls: type,image: Image,wrapMode: WrapMode,dstRect: Rectangle)

  __new__(cls: type,image: Image,dstRect: RectangleF)

  __new__(cls: type,image: Image,dstRect: RectangleF,imageAttr: ImageAttributes)

  __new__(cls: type,image: Image,dstRect: Rectangle)

  __new__(cls: type,image: Image,dstRect: Rectangle,imageAttr: ImageAttributes)
  """
  pass
 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Image object associated with this System.Drawing.TextureBrush object.



Get: Image(self: TextureBrush) -> Image



"""

 Transform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a copy of the System.Drawing.Drawing2D.Matrix object that defines a local geometric transformation for the image associated with this System.Drawing.TextureBrush object.



Get: Transform(self: TextureBrush) -> Matrix



Set: Transform(self: TextureBrush)=value

"""

 WrapMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Drawing.Drawing2D.WrapMode enumeration that indicates the wrap mode for this System.Drawing.TextureBrush object.



Get: WrapMode(self: TextureBrush) -> WrapMode



Set: WrapMode(self: TextureBrush)=value

"""


