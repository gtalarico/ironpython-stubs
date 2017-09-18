class StatusBarPanel(Component,IComponent,IDisposable,ISupportInitialize):
 """
 Represents a panel in a System.Windows.Forms.StatusBar control. Although the System.Windows.Forms.StatusStrip control replaces and adds functionality to the System.Windows.Forms.StatusBar control of previous versions,System.Windows.Forms.StatusBar is retained for both backward compatibility and future use if you choose.

 

 StatusBarPanel()
 """
 def BeginInit(self):
  """
  BeginInit(self: StatusBarPanel)

   Begins the initialization of a System.Windows.Forms.StatusBarPanel.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: StatusBarPanel,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.StatusBarPanel and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def EndInit(self):
  """
  EndInit(self: StatusBarPanel)

   Ends the initialization of a System.Windows.Forms.StatusBarPanel.
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
  ToString(self: StatusBarPanel) -> str

  

   Retrieves a string that contains information about the panel.

   Returns: Returns a string that contains the class name for the control and the text it contains.
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
 Alignment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the alignment of text and icons within the status bar panel.



Get: Alignment(self: StatusBarPanel) -> HorizontalAlignment



Set: Alignment(self: StatusBarPanel)=value

"""

 AutoSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the status bar panel is automatically resized.



Get: AutoSize(self: StatusBarPanel) -> StatusBarPanelAutoSize



Set: AutoSize(self: StatusBarPanel)=value

"""

 BorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the border style of the status bar panel.



Get: BorderStyle(self: StatusBarPanel) -> StatusBarPanelBorderStyle



Set: BorderStyle(self: StatusBarPanel)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 Icon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the icon to display within the status bar panel.



Get: Icon(self: StatusBarPanel) -> Icon



Set: Icon(self: StatusBarPanel)=value

"""

 MinWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the minimum allowed width of the status bar panel within the System.Windows.Forms.StatusBar control.



Get: MinWidth(self: StatusBarPanel) -> int



Set: MinWidth(self: StatusBarPanel)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name to apply to the System.Windows.Forms.StatusBarPanel.



Get: Name(self: StatusBarPanel) -> str



Set: Name(self: StatusBarPanel)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.StatusBar control that hosts the status bar panel.



Get: Parent(self: StatusBarPanel) -> StatusBar



"""

 Style=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style of the status bar panel.



Get: Style(self: StatusBarPanel) -> StatusBarPanelStyle



Set: Style(self: StatusBarPanel)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that contains data about the System.Windows.Forms.StatusBarPanel.



Get: Tag(self: StatusBarPanel) -> object



Set: Tag(self: StatusBarPanel)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text of the status bar panel.



Get: Text(self: StatusBarPanel) -> str



Set: Text(self: StatusBarPanel)=value

"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets ToolTip text associated with the status bar panel.



Get: ToolTipText(self: StatusBarPanel) -> str



Set: ToolTipText(self: StatusBarPanel)=value

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the status bar panel within the System.Windows.Forms.StatusBar control.



Get: Width(self: StatusBarPanel) -> int



Set: Width(self: StatusBarPanel)=value

"""


