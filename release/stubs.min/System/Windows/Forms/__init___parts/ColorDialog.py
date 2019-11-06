class ColorDialog(CommonDialog,IComponent,IDisposable):
 """
 Represents a common dialog box that displays available colors along with controls that enable the user to define custom colors.
 
 ColorDialog()
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return ColorDialog()

 def Dispose(self):
  """
  Dispose(self: Component,disposing: bool)
   Releases the unmanaged resources used by the System.ComponentModel.Component and optionally releases the managed resources.
  
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object
  
   Returns an object that represents a service provided by the System.ComponentModel.Component or by its System.ComponentModel.Container.
  
   service: A service provided by the System.ComponentModel.Component.
   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 def HookProc(self,*args):
  """
  HookProc(self: CommonDialog,hWnd: IntPtr,msg: int,wparam: IntPtr,lparam: IntPtr) -> IntPtr
  
   Defines the common dialog box hook procedure that is overridden to add specific functionality to a common dialog box.
  
   hWnd: The handle to the dialog box window.
   msg: The message being received.
   wparam: Additional information about the message.
   lparam: Additional information about the message.
   Returns: A zero value if the default dialog box procedure processes the message; a nonzero value if the default dialog box procedure ignores the message.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the object to be assigned a new identity when it is marshaled across a remoting boundary. A value of false is usually appropriate. true to copy the current System.MarshalByRefObject object's identity to its clone,which will cause remoting client calls to be routed to the remote server object.
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def OnHelpRequest(self,*args):
  """
  OnHelpRequest(self: CommonDialog,e: EventArgs)
   Raises the System.Windows.Forms.CommonDialog.HelpRequest event.
  
   e: An System.Windows.Forms.HelpEventArgs that provides the event data.
  """
  pass
 def OwnerWndProc(self,*args):
  """
  OwnerWndProc(self: CommonDialog,hWnd: IntPtr,msg: int,wparam: IntPtr,lparam: IntPtr) -> IntPtr
  
   Defines the owner window procedure that is overridden to add specific functionality to a common dialog box.
  
   hWnd: The window handle of the message to send.
   msg: The Win32 message to send.
   wparam: The wparam to send with the message.
   lparam: The lparam to send with the message.
   Returns: The result of the message processing,which is dependent on the message sent.
  """
  pass
 def Reset(self):
  """
  Reset(self: ColorDialog)
   Resets all options to their default values,the last selected color to black,and the custom colors to their default values.
  """
  pass
 def RunDialog(self,*args):
  """
  RunDialog(self: ColorDialog,hwndOwner: IntPtr) -> bool
  
   hwndOwner: A value that represents the window handle of the owner window for the common dialog box.
   Returns: true if the dialog box was successfully run; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: ColorDialog) -> str
  
   Returns a string that represents the System.Windows.Forms.ColorDialog.
   Returns: A System.String that represents the current System.Windows.Forms.ColorDialog.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 AllowFullOpen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can use the dialog box to define custom colors.

Get: AllowFullOpen(self: ColorDialog) -> bool

Set: AllowFullOpen(self: ColorDialog)=value
"""

 AnyColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box displays all available colors in the set of basic colors.

Get: AnyColor(self: ColorDialog) -> bool

Set: AnyColor(self: ColorDialog)=value
"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.

"""

 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color selected by the user.

Get: Color(self: ColorDialog) -> Color

Set: Color(self: ColorDialog)=value
"""

 CustomColors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the set of custom colors shown in the dialog box.

Get: CustomColors(self: ColorDialog) -> Array[int]

Set: CustomColors(self: ColorDialog)=value
"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

 FullOpen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the controls used to create custom colors are visible when the dialog box is opened

Get: FullOpen(self: ColorDialog) -> bool

Set: FullOpen(self: ColorDialog)=value
"""

 Instance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying window instance handle (HINSTANCE).

"""

 Options=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets values to initialize the System.Windows.Forms.ColorDialog.

"""

 ShowHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a Help button appears in the color dialog box.

Get: ShowHelp(self: ColorDialog) -> bool

Set: ShowHelp(self: ColorDialog)=value
"""

 SolidColorOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box will restrict users to selecting solid colors only.

Get: SolidColorOnly(self: ColorDialog) -> bool

Set: SolidColorOnly(self: ColorDialog)=value
"""


