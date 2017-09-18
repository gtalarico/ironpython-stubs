class ImageList(Component,IComponent,IDisposable):
 """
 Provides methods to manage a collection of System.Drawing.Image objects. This class cannot be inherited.

 

 ImageList()

 ImageList(container: IContainer)
 """
 def Dispose(self):
  """ Dispose(self: ImageList,disposing: bool) """
  pass
 def Draw(self,g,*__args):
  """
  Draw(self: ImageList,g: Graphics,x: int,y: int,width: int,height: int,index: int)

   Draws the image indicated by the given index on the specified System.Drawing.Graphics using the 

    specified location and size.

  

  

   g: The System.Drawing.Graphics to draw on.

   x: The horizontal position at which to draw the image.

   y: The vertical position at which to draw the image.

   width: The width,in pixels,of the destination image.

   height: The height,in pixels,of the destination image.

   index: The index of the image in the System.Windows.Forms.ImageList to draw.

  Draw(self: ImageList,g: Graphics,x: int,y: int,index: int)

   Draws the image indicated by the given index on the specified System.Drawing.Graphics at the 

    specified location.

  

  

   g: The System.Drawing.Graphics to draw on.

   x: The horizontal position at which to draw the image.

   y: The vertical position at which to draw the image.

   index: The index of the image in the System.Windows.Forms.ImageList to draw.

  Draw(self: ImageList,g: Graphics,pt: Point,index: int)

   Draws the image indicated by the specified index on the specified System.Drawing.Graphics at the 

    given location.

  

  

   g: The System.Drawing.Graphics to draw on.

   pt: The location defined by a System.Drawing.Point at which to draw the image.

   index: The index of the image in the System.Windows.Forms.ImageList to draw.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object

  

   Returns an object that represents a service provided by the System.ComponentModel.Component or 

    by its System.ComponentModel.Container.

  

  

   service: A service provided by the System.ComponentModel.Component.

   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 

    null if the System.ComponentModel.Component does not provide the specified service.
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
 def ToString(self):
  """
  ToString(self: ImageList) -> str

  

   Returns a string that represents the current System.Windows.Forms.ImageList.

   Returns: A string that represents the current System.Windows.Forms.ImageList.
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
 def __new__(self,container=None):
  """
  __new__(cls: type)

  __new__(cls: type,container: IContainer)
  """
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 ColorDepth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the color depth of the image list.



Get: ColorDepth(self: ImageList) -> ColorDepth



Set: ColorDepth(self: ImageList)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the handle of the image list object.



Get: Handle(self: ImageList) -> IntPtr



"""

 HandleCreated=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the underlying Win32 handle has been created.



Get: HandleCreated(self: ImageList) -> bool



"""

 Images=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ImageList.ImageCollection for this image list.



Get: Images(self: ImageList) -> ImageCollection



"""

 ImageSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the images in the image list.



Get: ImageSize(self: ImageList) -> Size



Set: ImageSize(self: ImageList)=value

"""

 ImageStream=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ImageListStreamer associated with this image list.



Get: ImageStream(self: ImageList) -> ImageListStreamer



Set: ImageStream(self: ImageList)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that contains additional data about the System.Windows.Forms.ImageList.



Get: Tag(self: ImageList) -> object



Set: Tag(self: ImageList)=value

"""

 TransparentColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color to treat as transparent.



Get: TransparentColor(self: ImageList) -> Color



Set: TransparentColor(self: ImageList)=value

"""


 ImageCollection=None
 RecreateHandle=None

