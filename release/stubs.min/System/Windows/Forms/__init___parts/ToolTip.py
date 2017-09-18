class ToolTip(Component,IComponent,IDisposable,IExtenderProvider):
 """
 Represents a small rectangular pop-up window that displays a brief description of a control's purpose when the user rests the pointer on the control.

 

 ToolTip(cont: IContainer)

 ToolTip()
 """
 def CanExtend(self,target):
  """
  CanExtend(self: ToolTip,target: object) -> bool

  

   Returns true if the ToolTip can offer an extender property to the specified target component.

  

   target: The target object to add an extender property to.

   Returns: true if the System.Windows.Forms.ToolTip class can offer one or more extender properties; 

    otherwise,false.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ToolTip,disposing: bool)

   Disposes of the System.Windows.Forms.ToolTip component.

  

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
 def GetToolTip(self,control):
  """
  GetToolTip(self: ToolTip,control: Control) -> str

  

   Retrieves the ToolTip text associated with the specified control.

  

   control: The System.Windows.Forms.Control for which to retrieve the System.Windows.Forms.ToolTip text.

   Returns: A System.String containing the ToolTip text for the specified control.
  """
  pass
 def Hide(self,win):
  """
  Hide(self: ToolTip,win: IWin32Window)

   Hides the specified ToolTip window.

  

   win: The System.Windows.Forms.IWin32Window of the associated window or control that the ToolTip is 

    associated with.
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
 def RemoveAll(self):
  """
  RemoveAll(self: ToolTip)

   Removes all ToolTip text currently associated with the ToolTip component.
  """
  pass
 def SetToolTip(self,control,caption):
  """
  SetToolTip(self: ToolTip,control: Control,caption: str)

   Associates ToolTip text with the specified control.

  

   control: The System.Windows.Forms.Control to associate the ToolTip text with.

   caption: The ToolTip text to display when the pointer is on the control.
  """
  pass
 def Show(self,text,window,*__args):
  """
  Show(self: ToolTip,text: str,window: IWin32Window,point: Point,duration: int)

   Sets the ToolTip text associated with the specified control,and then displays the ToolTip for 

    the specified duration at the specified relative position.

  

  

   text: A System.String containing the new ToolTip text.

   window: The System.Windows.Forms.Control to display the ToolTip for.

   point: A System.Drawing.Point containing the offset,in pixels,relative to the upper-left corner of 

    the associated control window,to display the ToolTip.

  

   duration: An System.Int32 containing the duration,in milliseconds,to display the ToolTip.

  Show(self: ToolTip,text: str,window: IWin32Window,x: int,y: int)

   Sets the ToolTip text associated with the specified control,and then displays the ToolTip 

    modally at the specified relative position.

  

  

   text: A System.String containing the new ToolTip text.

   window: The System.Windows.Forms.Control to display the ToolTip for.

   x: The horizontal offset,in pixels,relative to the upper-left corner of the associated control 

    window,to display the ToolTip.

  

   y: The vertical offset,in pixels,relative to the upper-left corner of the associated control 

    window,to display the ToolTip.

  

  Show(self: ToolTip,text: str,window: IWin32Window,x: int,y: int,duration: int)

   Sets the ToolTip text associated with the specified control,and then displays the ToolTip for 

    the specified duration at the specified relative position.

  

  

   text: A System.String containing the new ToolTip text.

   window: The System.Windows.Forms.Control to display the ToolTip for.

   x: The horizontal offset,in pixels,relative to the upper-left corner of the associated control 

    window,to display the ToolTip.

  

   y: The vertical offset,in pixels,relative to the upper-left corner of the associated control 

    window,to display the ToolTip.

  

   duration: An System.Int32 containing the duration,in milliseconds,to display the ToolTip.

  Show(self: ToolTip,text: str,window: IWin32Window)

   Sets the ToolTip text associated with the specified control,and displays the ToolTip modally.

  

   text: A System.String containing the new ToolTip text.

   window: The System.Windows.Forms.Control to display the ToolTip for.

  Show(self: ToolTip,text: str,window: IWin32Window,duration: int)

   Sets the ToolTip text associated with the specified control,and then displays the ToolTip for 

    the specified duration.

  

  

   text: A System.String containing the new ToolTip text.

   window: The System.Windows.Forms.Control to display the ToolTip for.

   duration: An System.Int32 containing the duration,in milliseconds,to display the ToolTip.

  Show(self: ToolTip,text: str,window: IWin32Window,point: Point)

   Sets the ToolTip text associated with the specified control,and then displays the ToolTip 

    modally at the specified relative position.

  

  

   text: A System.String containing the new ToolTip text.

   window: The System.Windows.Forms.Control to display the ToolTip for.

   point: A System.Drawing.Point containing the offset,in pixels,relative to the upper-left corner of 

    the associated control window,to display the ToolTip.
  """
  pass
 def StopTimer(self,*args):
  """
  StopTimer(self: ToolTip)

   Stops the timer that hides displayed ToolTips.
  """
  pass
 def ToString(self):
  """
  ToString(self: ToolTip) -> str

  

   Returns a string representation for this control.

   Returns: A System.String containing a description of the System.Windows.Forms.ToolTip.
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
 def __new__(self,cont=None):
  """
  __new__(cls: type,cont: IContainer)

  __new__(cls: type)
  """
  pass
 def __str__(self,*args):
  pass
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the ToolTip is currently active.



Get: Active(self: ToolTip) -> bool



Set: Active(self: ToolTip)=value

"""

 AutomaticDelay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the automatic delay for the ToolTip.



Get: AutomaticDelay(self: ToolTip) -> int



Set: AutomaticDelay(self: ToolTip)=value

"""

 AutoPopDelay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the period of time the ToolTip remains visible if the pointer is stationary on a control with specified ToolTip text.



Get: AutoPopDelay(self: ToolTip) -> int



Set: AutoPopDelay(self: ToolTip)=value

"""

 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color for the ToolTip.



Get: BackColor(self: ToolTip) -> Color



Set: BackColor(self: ToolTip)=value

"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 CreateParams=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the creation parameters for the ToolTip window.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color for the ToolTip.



Get: ForeColor(self: ToolTip) -> Color



Set: ForeColor(self: ToolTip)=value

"""

 InitialDelay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time that passes before the ToolTip appears.



Get: InitialDelay(self: ToolTip) -> int



Set: InitialDelay(self: ToolTip)=value

"""

 IsBalloon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the ToolTip should use a balloon window.



Get: IsBalloon(self: ToolTip) -> bool



Set: IsBalloon(self: ToolTip)=value

"""

 OwnerDraw=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the ToolTip is drawn by the operating system or by code that you provide.



Get: OwnerDraw(self: ToolTip) -> bool



Set: OwnerDraw(self: ToolTip)=value

"""

 ReshowDelay=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the length of time that must transpire before subsequent ToolTip windows appear as the pointer moves from one control to another.



Get: ReshowDelay(self: ToolTip) -> int



Set: ReshowDelay(self: ToolTip)=value

"""

 ShowAlways=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a ToolTip window is displayed,even when its parent control is not active.



Get: ShowAlways(self: ToolTip) -> bool



Set: ShowAlways(self: ToolTip)=value

"""

 StripAmpersands=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines how ampersand (&) characters are treated.



Get: StripAmpersands(self: ToolTip) -> bool



Set: StripAmpersands(self: ToolTip)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains programmer-supplied data associated with the System.Windows.Forms.ToolTip.



Get: Tag(self: ToolTip) -> object



Set: Tag(self: ToolTip)=value

"""

 ToolTipIcon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that defines the type of icon to be displayed alongside the ToolTip text.



Get: ToolTipIcon(self: ToolTip) -> ToolTipIcon



Set: ToolTipIcon(self: ToolTip)=value

"""

 ToolTipTitle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a title for the ToolTip window.



Get: ToolTipTitle(self: ToolTip) -> str



Set: ToolTipTitle(self: ToolTip)=value

"""

 UseAnimation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value determining whether an animation effect should be used when displaying the ToolTip.



Get: UseAnimation(self: ToolTip) -> bool



Set: UseAnimation(self: ToolTip)=value

"""

 UseFading=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value determining whether a fade effect should be used when displaying the ToolTip.



Get: UseFading(self: ToolTip) -> bool



Set: UseFading(self: ToolTip)=value

"""


 Draw=None
 Popup=None

