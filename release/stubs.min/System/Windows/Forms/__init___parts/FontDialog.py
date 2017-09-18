class FontDialog(CommonDialog,IComponent,IDisposable):
 """
 Prompts the user to choose a font from among those installed on the local computer.

 

 FontDialog()
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
  HookProc(self: FontDialog,hWnd: IntPtr,msg: int,wparam: IntPtr,lparam: IntPtr) -> IntPtr

  

   Specifies the common dialog box hook procedure that is overridden to add specific functionality 

    to a common dialog box.

  

  

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
 def OnApply(self,*args):
  """
  OnApply(self: FontDialog,e: EventArgs)

   Raises the System.Windows.Forms.FontDialog.Apply event.

  

   e: An System.EventArgs that contains the data.
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
  Reset(self: FontDialog)

   Resets all dialog box options to their default values.
  """
  pass
 def RunDialog(self,*args):
  """
  RunDialog(self: FontDialog,hWndOwner: IntPtr) -> bool

  

   Specifies a file dialog box.

  

   hWndOwner: The window handle of the owner window for the common dialog box.

   Returns: true if the dialog box was successfully run; otherwise,false.
  """
  pass
 def ToString(self):
  """
  ToString(self: FontDialog) -> str

  

   Retrieves a string that includes the name of the current font selected in the dialog box.

   Returns: A string that includes the name of the currently selected font.
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
 AllowScriptChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can change the character set specified in the Script combo box to display a character set other than the one currently displayed.



Get: AllowScriptChange(self: FontDialog) -> bool



Set: AllowScriptChange(self: FontDialog)=value

"""

 AllowSimulations=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box allows graphics device interface (GDI) font simulations.



Get: AllowSimulations(self: FontDialog) -> bool



Set: AllowSimulations(self: FontDialog)=value

"""

 AllowVectorFonts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box allows vector font selections.



Get: AllowVectorFonts(self: FontDialog) -> bool



Set: AllowVectorFonts(self: FontDialog)=value

"""

 AllowVerticalFonts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box displays both vertical and horizontal fonts or only horizontal fonts.



Get: AllowVerticalFonts(self: FontDialog) -> bool



Set: AllowVerticalFonts(self: FontDialog)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 Color=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the selected font color.



Get: Color(self: FontDialog) -> Color



Set: Color(self: FontDialog)=value

"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 FixedPitchOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box allows only the selection of fixed-pitch fonts.



Get: FixedPitchOnly(self: FontDialog) -> bool



Set: FixedPitchOnly(self: FontDialog)=value

"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the selected font.



Get: Font(self: FontDialog) -> Font



Set: Font(self: FontDialog)=value

"""

 FontMustExist=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box specifies an error condition if the user attempts to select a font or style that does not exist.



Get: FontMustExist(self: FontDialog) -> bool



Set: FontMustExist(self: FontDialog)=value

"""

 MaxSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum point size a user can select.



Get: MaxSize(self: FontDialog) -> int



Set: MaxSize(self: FontDialog)=value

"""

 MinSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum point size a user can select.



Get: MinSize(self: FontDialog) -> int



Set: MinSize(self: FontDialog)=value

"""

 Options=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets values to initialize the System.Windows.Forms.FontDialog.



"""

 ScriptsOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box allows selection of fonts for all non-OEM and Symbol character sets,as well as the ANSI character set.



Get: ScriptsOnly(self: FontDialog) -> bool



Set: ScriptsOnly(self: FontDialog)=value

"""

 ShowApply=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box contains an Apply button.



Get: ShowApply(self: FontDialog) -> bool



Set: ShowApply(self: FontDialog)=value

"""

 ShowColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box displays the color choice.



Get: ShowColor(self: FontDialog) -> bool



Set: ShowColor(self: FontDialog)=value

"""

 ShowEffects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box contains controls that allow the user to specify strikethrough,underline,and text color options.



Get: ShowEffects(self: FontDialog) -> bool



Set: ShowEffects(self: FontDialog)=value

"""

 ShowHelp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box displays a Help button.



Get: ShowHelp(self: FontDialog) -> bool



Set: ShowHelp(self: FontDialog)=value

"""


 Apply=None
 EventApply=None

