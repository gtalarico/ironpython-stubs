class PrintDialog(CommonDialog,IComponent,IDisposable):
 """
 Lets users select a printer and choose which sections of the document to print from a Windows Forms application.

 

 PrintDialog()
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
  Reset(self: PrintDialog)

   Resets all options,the last selected printer,and the page settings to their default values.
  """
  pass
 def RunDialog(self,*args):
  """ RunDialog(self: PrintDialog,hwndOwner: IntPtr) -> bool """
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
 AllowCurrentPage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Current Page option button is displayed.



Get: AllowCurrentPage(self: PrintDialog) -> bool



Set: AllowCurrentPage(self: PrintDialog)=value

"""

 AllowPrintToFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Print to file check box is enabled.



Get: AllowPrintToFile(self: PrintDialog) -> bool



Set: AllowPrintToFile(self: PrintDialog)=value

"""

 AllowSelection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Selection option button is enabled.



Get: AllowSelection(self: PrintDialog) -> bool



Set: AllowSelection(self: PrintDialog)=value

"""

 AllowSomePages=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Pages option button is enabled.



Get: AllowSomePages(self: PrintDialog) -> bool



Set: AllowSomePages(self: PrintDialog)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the System.Drawing.Printing.PrintDocument used to obtain System.Drawing.Printing.PrinterSettings.



Get: Document(self: PrintDialog) -> PrintDocument



Set: Document(self: PrintDialog)=value

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 PrinterSettings=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the printer settings the dialog box modifies.



Get: PrinterSettings(self: PrintDialog) -> PrinterSettings



Set: PrinterSettings(self: PrintDialog)=value

"""

 PrintToFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Print to file check box is selected.



Get: PrintToFile(self: PrintDialog) -> bool



Set: PrintToFile(self: PrintDialog)=value

"""

 ShowHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Help button is displayed.



Get: ShowHelp(self: PrintDialog) -> bool



Set: ShowHelp(self: PrintDialog)=value

"""

 ShowNetwork=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Network button is displayed.



Get: ShowNetwork(self: PrintDialog) -> bool



Set: ShowNetwork(self: PrintDialog)=value

"""

 UseEXDialog=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog should be shown in the Windows XP style for systems running Windows XP Home Edition,Windows XP Professional,Windows Server 2003�or later.



Get: UseEXDialog(self: PrintDialog) -> bool



Set: UseEXDialog(self: PrintDialog)=value

"""


