class ErrorProvider(Component,IComponent,IDisposable,IExtenderProvider,ISupportInitialize):
 """
 Provides a user interface for indicating that a control on a form has an error associated with it.

 

 ErrorProvider()

 ErrorProvider(parentControl: ContainerControl)

 ErrorProvider(container: IContainer)
 """
 def BindToDataAndErrors(self,newDataSource,newDataMember):
  """
  BindToDataAndErrors(self: ErrorProvider,newDataSource: object,newDataMember: str)

   Provides a method to set both the System.Windows.Forms.ErrorProvider.DataSource and 

    System.Windows.Forms.ErrorProvider.DataMember at run time.

  

  

   newDataSource: A data set based on the System.Collections.IList interface to be monitored for errors. 

    Typically,this is a System.Data.DataSet to be monitored for errors.

  

   newDataMember: A collection within the newDataSource to monitor for errors. Typically,this will be a 

    System.Data.DataTable.
  """
  pass
 def CanExtend(self,extendee):
  """
  CanExtend(self: ErrorProvider,extendee: object) -> bool

  

   Gets a value indicating whether a control can be extended.

  

   extendee: The control to be extended.

   Returns: true if the control can be extended; otherwise,false.This property will be true if the object 

    is a System.Windows.Forms.Control and is not a System.Windows.Forms.Form or 

    System.Windows.Forms.ToolBar.
  """
  pass
 def Clear(self):
  """
  Clear(self: ErrorProvider)

   Clears all settings associated with this component.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ErrorProvider,disposing: bool)

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def GetError(self,control):
  """
  GetError(self: ErrorProvider,control: Control) -> str

  

   Returns the current error description string for the specified control.

  

   control: The item to get the error description string for.

   Returns: The error description string for the specified control.
  """
  pass
 def GetIconAlignment(self,control):
  """
  GetIconAlignment(self: ErrorProvider,control: Control) -> ErrorIconAlignment

  

   Gets a value indicating where the error icon should be placed in relation to the control.

  

   control: The control to get the icon location for.

   Returns: One of the System.Windows.Forms.ErrorIconAlignment values. The default icon alignment is 

    System.Windows.Forms.ErrorIconAlignment.MiddleRight.
  """
  pass
 def GetIconPadding(self,control):
  """
  GetIconPadding(self: ErrorProvider,control: Control) -> int

  

   Returns the amount of extra space to leave next to the error icon.

  

   control: The control to get the padding for.

   Returns: The number of pixels to leave between the icon and the control.
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
 def OnRightToLeftChanged(self,*args):
  """
  OnRightToLeftChanged(self: ErrorProvider,e: EventArgs)

   Raises the System.Windows.Forms.ErrorProvider.RightToLeftChanged event.

  

   e: A System.EventArgs that contains the event data.
  """
  pass
 def SetError(self,control,value):
  """
  SetError(self: ErrorProvider,control: Control,value: str)

   Sets the error description string for the specified control.

  

   control: The control to set the error description string for.

   value: The error description string,or null or System.String.Empty to remove the error.
  """
  pass
 def SetIconAlignment(self,control,value):
  """
  SetIconAlignment(self: ErrorProvider,control: Control,value: ErrorIconAlignment)

   Sets the location where the error icon should be placed in relation to the control.

  

   control: The control to set the icon location for.

   value: One of the System.Windows.Forms.ErrorIconAlignment values.
  """
  pass
 def SetIconPadding(self,control,padding):
  """
  SetIconPadding(self: ErrorProvider,control: Control,padding: int)

   Sets the amount of extra space to leave between the specified control and the error icon.

  

   control: The control to set the padding for.

   padding: The number of pixels to add between the icon and the control.
  """
  pass
 def UpdateBinding(self):
  """
  UpdateBinding(self: ErrorProvider)

   Provides a method to update the bindings of the System.Windows.Forms.ErrorProvider.DataSource,

    System.Windows.Forms.ErrorProvider.DataMember,and the error text.
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

  __new__(cls: type,parentControl: ContainerControl)

  __new__(cls: type,container: IContainer)
  """
  pass
 def __str__(self,*args):
  pass
 BlinkRate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the rate at which the error icon flashes.



Get: BlinkRate(self: ErrorProvider) -> int



Set: BlinkRate(self: ErrorProvider)=value

"""

 BlinkStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating when the error icon flashes.



Get: BlinkStyle(self: ErrorProvider) -> ErrorBlinkStyle



Set: BlinkStyle(self: ErrorProvider)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 ContainerControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the parent control for this System.Windows.Forms.ErrorProvider.



Get: ContainerControl(self: ErrorProvider) -> ContainerControl



Set: ContainerControl(self: ErrorProvider)=value

"""

 DataMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the list within a data source to monitor.



Get: DataMember(self: ErrorProvider) -> str



Set: DataMember(self: ErrorProvider)=value

"""

 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data source that the System.Windows.Forms.ErrorProvider monitors.



Get: DataSource(self: ErrorProvider) -> object



Set: DataSource(self: ErrorProvider)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Icon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Drawing.Icon that is displayed next to a control when an error description string has been set for the control.



Get: Icon(self: ErrorProvider) -> Icon



Set: Icon(self: ErrorProvider)=value

"""

 RightToLeft=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the component is used in a locale that supports right-to-left fonts.



Get: RightToLeft(self: ErrorProvider) -> bool



Set: RightToLeft(self: ErrorProvider)=value

"""

 Site=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Set: Site(self: ErrorProvider)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that contains data about the component.



Get: Tag(self: ErrorProvider) -> object



Set: Tag(self: ErrorProvider)=value

"""


 RightToLeftChanged=None

