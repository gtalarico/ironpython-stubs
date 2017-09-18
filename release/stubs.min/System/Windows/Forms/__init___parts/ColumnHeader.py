class ColumnHeader(Component,IComponent,IDisposable,ICloneable):
 """
 Displays a single column header in a System.Windows.Forms.ListView control.

 

 ColumnHeader()

 ColumnHeader(imageIndex: int)

 ColumnHeader(imageKey: str)
 """
 def AutoResize(self,headerAutoResize):
  """
  AutoResize(self: ColumnHeader,headerAutoResize: ColumnHeaderAutoResizeStyle)

   Resizes the width of the column as indicated by the resize style.

  

   headerAutoResize: One of the System.Windows.Forms.ColumnHeaderAutoResizeStyle  values.
  """
  pass
 def Clone(self):
  """
  Clone(self: ColumnHeader) -> object

  

   Creates an identical copy of the current System.Windows.Forms.ColumnHeader that is not attached 

    to any list view control.

  

   Returns: An object representing a copy of this System.Windows.Forms.ColumnHeader object.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ColumnHeader,disposing: bool)

   Disposes of the resources (other than memory) used by the System.Windows.Forms.ColumnHeader.

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
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
  ToString(self: ColumnHeader) -> str

  

   Returns a string representation of this column header.

   Returns: A System.String containing the name of the System.ComponentModel.Component,if any,or null if 

    the System.ComponentModel.Component is unnamed.
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
  __new__(cls: type)

  __new__(cls: type,imageIndex: int)

  __new__(cls: type,imageKey: str)
  """
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DisplayIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the display order of the column relative to the currently displayed columns.



Get: DisplayIndex(self: ColumnHeader) -> int



Set: DisplayIndex(self: ColumnHeader)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 ImageIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the image displayed in the System.Windows.Forms.ColumnHeader.



Get: ImageIndex(self: ColumnHeader) -> int



Set: ImageIndex(self: ColumnHeader)=value

"""

 ImageKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the key of the image displayed in the column.



Get: ImageKey(self: ColumnHeader) -> str



Set: ImageKey(self: ColumnHeader)=value

"""

 ImageList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the image list associated with the System.Windows.Forms.ColumnHeader.



Get: ImageList(self: ColumnHeader) -> ImageList



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location with the System.Windows.Forms.ListView control's System.Windows.Forms.ListView.ColumnHeaderCollection of this column.



Get: Index(self: ColumnHeader) -> int



"""

 ListView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ListView control the System.Windows.Forms.ColumnHeader is located in.



Get: ListView(self: ColumnHeader) -> ListView



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the System.Windows.Forms.ColumnHeader.



Get: Name(self: ColumnHeader) -> str



Set: Name(self: ColumnHeader)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that contains data to associate with the System.Windows.Forms.ColumnHeader.



Get: Tag(self: ColumnHeader) -> object



Set: Tag(self: ColumnHeader)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text displayed in the column header.



Get: Text(self: ColumnHeader) -> str



Set: Text(self: ColumnHeader)=value

"""

 TextAlign=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the horizontal alignment of the text displayed in the System.Windows.Forms.ColumnHeader.



Get: TextAlign(self: ColumnHeader) -> HorizontalAlignment



Set: TextAlign(self: ColumnHeader)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the column.



Get: Width(self: ColumnHeader) -> int



Set: Width(self: ColumnHeader)=value

"""


