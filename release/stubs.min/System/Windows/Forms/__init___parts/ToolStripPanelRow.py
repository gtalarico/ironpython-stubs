class ToolStripPanelRow(Component,IComponent,IDisposable,IArrangedElement):
 """
 Represents a row of a System.Windows.Forms.ToolStripPanel that can contain controls.

 

 ToolStripPanelRow(parent: ToolStripPanel)
 """
 def CanMove(self,toolStripToDrag):
  """
  CanMove(self: ToolStripPanelRow,toolStripToDrag: ToolStrip) -> bool

  

   Gets or sets a value indicating whether a System.Windows.Forms.ToolStrip can be dragged and 

    dropped into a System.Windows.Forms.ToolStripPanelRow.

  

  

   toolStripToDrag: The System.Windows.Forms.ToolStrip to be dragged and dropped into the 

    System.Windows.Forms.ToolStripPanelRow.

  

   Returns: true if there is enough space in the System.Windows.Forms.ToolStripPanelRow to receive the 

    System.Windows.Forms.ToolStrip; otherwise,false.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: ToolStripPanelRow,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.ToolStripPanelRow and 

    optionally releases the managed resources.

  

  

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
 def OnBoundsChanged(self,*args):
  """
  OnBoundsChanged(self: ToolStripPanelRow,oldBounds: Rectangle,newBounds: Rectangle)

   Occurs when the System.Windows.Forms.ToolStripPanelRow.Bounds property changes.

  

   oldBounds: The original value of the System.Windows.Forms.ToolStripPanelRow.Bounds property.

   newBounds: The new value of the System.Windows.Forms.ToolStripPanelRow.Bounds property.
  """
  pass
 def OnControlAdded(self,*args):
  """
  OnControlAdded(self: ToolStripPanelRow,control: Control,index: int)

   Raises the System.Windows.Forms.Control.ControlAdded event.

  

   control: The control that was added to the System.Windows.Forms.ToolStripPanelRow.

   index: The zero-based index representing the position of the added control.
  """
  pass
 def OnControlRemoved(self,*args):
  """
  OnControlRemoved(self: ToolStripPanelRow,control: Control,index: int)

   Raises the System.Windows.Forms.Control.ControlRemoved event.

  

   control: The control that was removed from the System.Windows.Forms.ToolStripPanelRow.

   index: The zero-based index representing the position of the removed control.
  """
  pass
 def OnLayout(self,*args):
  """
  OnLayout(self: ToolStripPanelRow,e: LayoutEventArgs)

   Raises the System.Windows.Forms.Control.Layout event.

  

   e: A System.Windows.Forms.LayoutEventArgs that contains the event data.
  """
  pass
 def OnOrientationChanged(self,*args):
  """
  OnOrientationChanged(self: ToolStripPanelRow)

   Occurs when the value of the System.Windows.Forms.ToolStripPanelRow.Orientation property changes.
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
 def __new__(self,parent):
  """ __new__(cls: type,parent: ToolStripPanel) """
  pass
 def __str__(self,*args):
  pass
 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size and location of the System.Windows.Forms.ToolStripPanelRow,including its nonclient elements,in pixels,relative to the parent control.



Get: Bounds(self: ToolStripPanelRow) -> Rectangle



"""

 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.



"""

 Controls=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the controls in the System.Windows.Forms.ToolStripPanelRow.



Get: Controls(self: ToolStripPanelRow) -> Array[Control]



"""

 DefaultMargin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the space,in pixels,that is specified by default between controls.



"""

 DefaultPadding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the internal spacing,in pixels,of the contents of a control.



"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.



"""

 DisplayRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the display area of the control.



Get: DisplayRectangle(self: ToolStripPanelRow) -> Rectangle



"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.



"""

 LayoutEngine=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an instance of the control's layout engine.



Get: LayoutEngine(self: ToolStripPanelRow) -> LayoutEngine



"""

 Margin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the space between controls.



Get: Margin(self: ToolStripPanelRow) -> Padding



Set: Margin(self: ToolStripPanelRow)=value

"""

 Orientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the layout direction of the System.Windows.Forms.ToolStripPanelRow relative to its containing System.Windows.Forms.ToolStripPanel.



Get: Orientation(self: ToolStripPanelRow) -> Orientation



"""

 Padding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets padding within the control.



Get: Padding(self: ToolStripPanelRow) -> Padding



Set: Padding(self: ToolStripPanelRow)=value

"""

 ToolStripPanel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ToolStripPanel that contains the System.Windows.Forms.ToolStripPanelRow.



Get: ToolStripPanel(self: ToolStripPanelRow) -> ToolStripPanel



"""


