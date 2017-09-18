class SolidBrush(Brush,ICloneable,IDisposable,ISystemColorTracker):
 """
 Defines a brush of a single color. Brushes are used to fill graphics shapes,such as rectangles,ellipses,pies,polygons,and paths. This class cannot be inherited.

 

 SolidBrush(color: Color)
 """
 def Clone(self):
  """
  Clone(self: SolidBrush) -> object

  

   Creates an exact copy of this System.Drawing.SolidBrush object.

   Returns: The System.Drawing.SolidBrush object that this method creates.
  """
  pass
 def Dispose(self):
  """ Dispose(self: SolidBrush,disposing: bool) """
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
 def SetNativeBrush(self,*args):
  """
  SetNativeBrush(self: Brush,brush: IntPtr)

   In a derived class,sets a reference to a GDI+ brush object.

  

   brush: A pointer to the GDI+ brush object.
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
 def __new__(self,color):
  """ __new__(cls: type,color: Color) """
  pass
 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color of this System.Drawing.SolidBrush object.



Get: Color(self: SolidBrush) -> Color



Set: Color(self: SolidBrush)=value

"""


