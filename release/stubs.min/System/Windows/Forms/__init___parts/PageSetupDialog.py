class PageSetupDialog(CommonDialog,IComponent,IDisposable):
 """
 Enables users to change page-related print settings,including margins and paper orientation. This class cannot be inherited.

 

 PageSetupDialog()
 """
 def Dispose(self):
  """
  Dispose(self: Component,disposing: bool)

   Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 

    releases the managed resources.

  

  

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
 def HookProc(self,*args):
  """
  HookProc(self: CommonDialog,hWnd: IntPtr,msg: int,wparam: IntPtr,lparam: IntPtr) -> IntPtr

  

   Defines the common dialog box hook procedure that is overridden to add specific functionality to 

    a common dialog box.

  

  

   hWnd: The handle to the dialog box window.

   msg: The message being received.

   wparam: Additional information about the message.

   lparam: Additional information about the message.

   Returns: A zero value if the default dialog box procedure processes the message; a nonzero value if the 

    default dialog box procedure ignores the message.
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

  

   Defines the owner window procedure that is overridden to add specific functionality to a common 

    dialog box.

  

  

   hWnd: The window handle of the message to send.

   msg: The Win32 message to send.

   wparam: The wparam to send with the message.

   lparam: The lparam to send with the message.

   Returns: The result of the message processing,which is dependent on the message sent.
  """
  pass
 def Reset(self):
  """
  Reset(self: PageSetupDialog)

   Resets all options to their default values.
  """
  pass
 def RunDialog(self,*args):
  """ RunDialog(self: PageSetupDialog,hwndOwner: IntPtr) -> bool """
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
 def __str__(self,*args):
  pass
 AllowMargins=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the margins section of the dialog box is enabled.



Get: AllowMargins(self: PageSetupDialog) -> bool



Set: AllowMargins(self: PageSetupDialog)=value

"""

 AllowOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the orientation section of the dialog box (landscape versus portrait) is enabled.



Get: AllowOrientation(self: PageSetupDialog) -> bool



Set: AllowOrientation(self: PageSetupDialog)=value

"""

 AllowPaper=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the paper section of the dialog box (paper size and paper source) is enabled.



Get: AllowPaper(self: PageSetupDialog) -> bool



Set: AllowPaper(self: PageSetupDialog)=value

"""

 AllowPrinter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Printer button is enabled.



Get: AllowPrinter(self: PageSetupDialog) -> bool



Set: AllowPrinter(self: PageSetupDialog)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the System.Drawing.Printing.PrintDocument to get page settings from.



Get: Document(self: PageSetupDialog) -> PrintDocument



Set: Document(self: PageSetupDialog)=value

"""

 EnableMetric=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the margin settings,when displayed in millimeters,should be automatically converted to and from hundredths of an inch.



Get: EnableMetric(self: PageSetupDialog) -> bool



Set: EnableMetric(self: PageSetupDialog)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 MinMargins=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the minimum margins,in hundredths of an inch,the user is allowed to select.



Get: MinMargins(self: PageSetupDialog) -> Margins



Set: MinMargins(self: PageSetupDialog)=value

"""

 PageSettings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the page settings to modify.



Get: PageSettings(self: PageSetupDialog) -> PageSettings



Set: PageSettings(self: PageSetupDialog)=value

"""

 PrinterSettings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the printer settings that are modified when the user clicks the Printer button in the dialog.



Get: PrinterSettings(self: PageSetupDialog) -> PrinterSettings



Set: PrinterSettings(self: PageSetupDialog)=value

"""

 ShowHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Help button is visible.



Get: ShowHelp(self: PageSetupDialog) -> bool



Set: ShowHelp(self: PageSetupDialog)=value

"""

 ShowNetwork=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Network button is visible.



Get: ShowNetwork(self: PageSetupDialog) -> bool



Set: ShowNetwork(self: PageSetupDialog)=value

"""


