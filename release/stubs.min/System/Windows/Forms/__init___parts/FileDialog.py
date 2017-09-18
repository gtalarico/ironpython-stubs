class FileDialog(CommonDialog,IComponent,IDisposable):
 """ Displays a dialog box from which the user can select a file. """
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
  HookProc(self: FileDialog,hWnd: IntPtr,msg: int,wparam: IntPtr,lparam: IntPtr) -> IntPtr

  

   Defines the common dialog box hook procedure that is overridden to add specific functionality to 

    the file dialog box.

  

  

   hWnd: The handle to the dialog box window.

   msg: The message received by the dialog box.

   wparam: Additional information about the message.

   lparam: Additional information about the message.

   Returns: Returns zero if the default dialog box procedure processes the message; returns a nonzero value 

    if the default dialog box procedure ignores the message.
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
 def OnFileOk(self,*args):
  """
  OnFileOk(self: FileDialog,e: CancelEventArgs)

   Raises the System.Windows.Forms.FileDialog.FileOk event.

  

   e: A System.ComponentModel.CancelEventArgs that contains the event data.
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
  Reset(self: FileDialog)

   Resets all properties to their default values.
  """
  pass
 def RunDialog(self,*args):
  """
  RunDialog(self: FileDialog,hWndOwner: IntPtr) -> bool

  

   Specifies a common dialog box.

  

   hWndOwner: A value that represents the window handle of the owner window for the common dialog box.

   Returns: true if the file could be opened; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: FileDialog) -> str

  

   Provides a string version of this object.

   Returns: A string version of this object.
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
 def __str__(self,*args):
  pass
 AddExtension=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box automatically adds an extension to a file name if the user omits the extension.



Get: AddExtension(self: FileDialog) -> bool



Set: AddExtension(self: FileDialog)=value

"""

 AutoUpgradeEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether this System.Windows.Forms.FileDialog instance should automatically upgrade appearance and behavior when running on Windows Vista.



Get: AutoUpgradeEnabled(self: FileDialog) -> bool



Set: AutoUpgradeEnabled(self: FileDialog)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 CheckFileExists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box displays a warning if the user specifies a file name that does not exist.



Get: CheckFileExists(self: FileDialog) -> bool



Set: CheckFileExists(self: FileDialog)=value

"""

 CheckPathExists=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box displays a warning if the user specifies a path that does not exist.



Get: CheckPathExists(self: FileDialog) -> bool



Set: CheckPathExists(self: FileDialog)=value

"""

 CustomPlaces=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the custom places collection for this System.Windows.Forms.FileDialog instance.



Get: CustomPlaces(self: FileDialog) -> FileDialogCustomPlacesCollection



"""

 DefaultExt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default file name extension.



Get: DefaultExt(self: FileDialog) -> str



Set: DefaultExt(self: FileDialog)=value

"""

 DereferenceLinks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box returns the location of the file referenced by the shortcut or whether it returns the location of the shortcut (.lnk).



Get: DereferenceLinks(self: FileDialog) -> bool



Set: DereferenceLinks(self: FileDialog)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string containing the file name selected in the file dialog box.



Get: FileName(self: FileDialog) -> str



Set: FileName(self: FileDialog)=value

"""

 FileNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the file names of all selected files in the dialog box.



Get: FileNames(self: FileDialog) -> Array[str]



"""

 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current file name filter string,which determines the choices that appear in the "Save as file type" or "Files of type" box in the dialog box.



Get: Filter(self: FileDialog) -> str



Set: Filter(self: FileDialog)=value

"""

 FilterIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the filter currently selected in the file dialog box.



Get: FilterIndex(self: FileDialog) -> int



Set: FilterIndex(self: FileDialog)=value

"""

 InitialDirectory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the initial directory displayed by the file dialog box.



Get: InitialDirectory(self: FileDialog) -> str



Set: InitialDirectory(self: FileDialog)=value

"""

 Instance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Win32 instance handle for the application.



"""

 Options=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets values to initialize the System.Windows.Forms.FileDialog.



"""

 RestoreDirectory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box restores the current directory before closing.



Get: RestoreDirectory(self: FileDialog) -> bool



Set: RestoreDirectory(self: FileDialog)=value

"""

 ShowHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Help button is displayed in the file dialog box.



Get: ShowHelp(self: FileDialog) -> bool



Set: ShowHelp(self: FileDialog)=value

"""

 SupportMultiDottedExtensions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether the dialog box supports displaying and saving files that have multiple file name extensions.



Get: SupportMultiDottedExtensions(self: FileDialog) -> bool



Set: SupportMultiDottedExtensions(self: FileDialog)=value

"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the file dialog box title.



Get: Title(self: FileDialog) -> str



Set: Title(self: FileDialog)=value

"""

 ValidateNames=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box accepts only valid Win32 file names.



Get: ValidateNames(self: FileDialog) -> bool



Set: ValidateNames(self: FileDialog)=value

"""


 EventFileOk=None
 FileOk=None

