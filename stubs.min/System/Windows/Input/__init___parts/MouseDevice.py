class MouseDevice(InputDevice):
 """ Represents a mouse device. """
 def Capture(self,element,captureMode=None):
  """
  Capture(self: MouseDevice,element: IInputElement,captureMode: CaptureMode) -> bool
  
   Captures mouse input to the specified element using the specified 
    System.Windows.Input.CaptureMode.
  
  
   element: The element to capture the mouse..
   captureMode: The capture policy to use.
   Returns: true if the element was able to capture the mouse; otherwise,false.
  Capture(self: MouseDevice,element: IInputElement) -> bool
  
   Captures mouse events to the specified element.
  
   element: The element to capture the mouse.
   Returns: true if the element was able to capture the mouse; otherwise,false.
  """
  pass
 def GetButtonState(self,*args):
  """
  GetButtonState(self: MouseDevice,mouseButton: MouseButton) -> MouseButtonState
  
   Gets the state of the specified mouse button.
  
   mouseButton: The button which is being queried.
   Returns: The state of the button.
  """
  pass
 def GetClientPosition(self,*args):
  """
  GetClientPosition(self: MouseDevice,presentationSource: PresentationSource) -> Point
  
   Calculates the position of the mouse pointer,in client coordinates,in the 
    specified System.Windows.PresentationSource.
  
  
   presentationSource: The source in which to obtain the mouse position.
   Returns: The position of the mouse pointer,in client coordinates,in the specified 
    System.Windows.PresentationSource.
  
  GetClientPosition(self: MouseDevice) -> Point
  
   Calculates the position of the mouse pointer,in client coordinates.
   Returns: The position of the mouse pointer,in client coordinates.
  """
  pass
 def GetPosition(self,relativeTo):
  """
  GetPosition(self: MouseDevice,relativeTo: IInputElement) -> Point
  
   Gets the position of the mouse relative to a specified element.
  
   relativeTo: The frame of reference in which to calculate the position of the mouse.
   Returns: The position of the mouse relative to the parameter relativeTo.
  """
  pass
 def GetScreenPosition(self,*args):
  """
  GetScreenPosition(self: MouseDevice) -> Point
  
   Calculates the screen position of the mouse pointer.
   Returns: The position of the mouse pointer.
  """
  pass
 def SetCursor(self,cursor):
  """
  SetCursor(self: MouseDevice,cursor: Cursor) -> bool
  
   Sets the mouse pointer to the specified System.Windows.Input.Cursor
  
   cursor: The cursor to set the mouse pointer to.
   Returns: true if the mouse cursor is set; otherwise,false.
  """
  pass
 def Synchronize(self):
  """
  Synchronize(self: MouseDevice)
   Forces the mouse to resynchronize.
  """
  pass
 def UpdateCursor(self):
  """
  UpdateCursor(self: MouseDevice)
   Forces the mouse cursor to update.
  """
  pass
 ActiveSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.PresentationSource that is reporting input for this device.

Get: ActiveSource(self: MouseDevice) -> PresentationSource

"""

 Captured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.IInputElement that is captured by the mouse.

Get: Captured(self: MouseDevice) -> IInputElement

"""

 DirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element that the mouse pointer is directly over.

Get: DirectlyOver(self: MouseDevice) -> IInputElement

"""

 LeftButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the left mouse button of this mouse device.

Get: LeftButton(self: MouseDevice) -> MouseButtonState

"""

 MiddleButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The state of the middle button of this mouse device.

Get: MiddleButton(self: MouseDevice) -> MouseButtonState

"""

 OverrideCursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the cursor for the entire application.

Get: OverrideCursor(self: MouseDevice) -> Cursor

Set: OverrideCursor(self: MouseDevice)=value
"""

 RightButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the right button of this mouse device.

Get: RightButton(self: MouseDevice) -> MouseButtonState

"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.IInputElement that the input from this mouse device is sent to.

Get: Target(self: MouseDevice) -> IInputElement

"""

 XButton1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the first extended button on this mouse device.

Get: XButton1(self: MouseDevice) -> MouseButtonState

"""

 XButton2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the second extended button of this mouse device.

Get: XButton2(self: MouseDevice) -> MouseButtonState

"""


