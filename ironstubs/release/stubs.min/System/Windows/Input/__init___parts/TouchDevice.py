class TouchDevice(InputDevice,IManipulator):
 """ Represents a single touch input produced by a finger on a touchscreen. """
 def Activate(self,*args):
  """
  Activate(self: TouchDevice)
   Adds the System.Windows.Input.TouchDevice to the input messaging system.
  """
  pass
 def Capture(self,element,captureMode=None):
  """
  Capture(self: TouchDevice,element: IInputElement,captureMode: CaptureMode) -> bool
  
   Captures a touch to the specified element by using the specified 
    System.Windows.Input.CaptureMode.
  
  
   element: The element that captures the touch.
   captureMode: The capture policy to use.
   Returns: true if the element was able to capture the touch; otherwise,false.
  Capture(self: TouchDevice,element: IInputElement) -> bool
  
   Captures a touch to the specified element by using the 
    System.Windows.Input.CaptureMode.Element capture mode.
  
  
   element: The element that captures the touch input.
   Returns: true if the element was able to capture the touch; otherwise,false.
  """
  pass
 def Deactivate(self,*args):
  """
  Deactivate(self: TouchDevice)
   Removes the System.Windows.Input.TouchDevice from the input messaging system.
  """
  pass
 def GetIntermediateTouchPoints(self,relativeTo):
  """
  GetIntermediateTouchPoints(self: TouchDevice,relativeTo: IInputElement) -> TouchPointCollection
  
   When overridden in a derived class,returns all touch points that are collected 
    between the most recent and previous touch events.
  
  
   relativeTo: The element that defines the coordinate space.
   Returns: All touch points that were collected between the most recent and previous touch 
    events.
  """
  pass
 def GetTouchPoint(self,relativeTo):
  """
  GetTouchPoint(self: TouchDevice,relativeTo: IInputElement) -> TouchPoint
  
   Returns the current position of the touch device relative to the specified 
    element.
  
  
   relativeTo: The element that defines the coordinate space.
   Returns: The current position of the touch device relative to the specified element.
  """
  pass
 def OnCapture(self,*args):
  """
  OnCapture(self: TouchDevice,element: IInputElement,captureMode: CaptureMode)
   Called when a touch is captured to an element.
  
   element: The element that captures the touch input.
   captureMode: The capture policy.
  """
  pass
 def OnManipulationEnded(self,*args):
  """
  OnManipulationEnded(self: TouchDevice,cancel: bool)
   Called when a manipulation has ended.
  
   cancel: true to cancel the action; otherwise,false.
  """
  pass
 def OnManipulationStarted(self,*args):
  """
  OnManipulationStarted(self: TouchDevice)
   Called when a manipulation is started.
  """
  pass
 def ReportDown(self,*args):
  """
  ReportDown(self: TouchDevice) -> bool
  
   Reports that a touch is pressed on an element.
   Returns: true if the System.Windows.UIElement.TouchDown event was handled; otherwise,
    false.
  """
  pass
 def ReportMove(self,*args):
  """
  ReportMove(self: TouchDevice) -> bool
  
   Reports that a touch is moving across an element.
   Returns: true if the System.Windows.UIElement.TouchMove event was handled; otherwise,
    false.
  """
  pass
 def ReportUp(self,*args):
  """
  ReportUp(self: TouchDevice) -> bool
  
   Reports that a touch was lifted from an element.
   Returns: true if the System.Windows.UIElement.TouchUp event was handled; otherwise,
    false.
  """
  pass
 def SetActiveSource(self,*args):
  """
  SetActiveSource(self: TouchDevice,activeSource: PresentationSource)
   Sets the System.Windows.PresentationSource that is reporting input for this 
    device.
  
  
   activeSource: The source that reports input for this device.
  """
  pass
 def Synchronize(self):
  """
  Synchronize(self: TouchDevice)
   Forces the System.Windows.Input.TouchDevice to synchronize the user interface 
    with underlying touch points.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,deviceId: int) """
  pass
 ActiveSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.PresentationSource that is reporting input for this device.

Get: ActiveSource(self: TouchDevice) -> PresentationSource

"""

 Captured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element that captured the System.Windows.Input.TouchDevice.

Get: Captured(self: TouchDevice) -> IInputElement

"""

 CaptureMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the capture policy of the System.Windows.Input.TouchDevice.

Get: CaptureMode(self: TouchDevice) -> CaptureMode

"""

 DirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element that the touch contact point is directly over.

Get: DirectlyOver(self: TouchDevice) -> IInputElement

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unique identifier of the System.Windows.Input.TouchDevice,as provided by the operating system.

Get: Id(self: TouchDevice) -> int

"""

 IsActive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the device is active.

Get: IsActive(self: TouchDevice) -> bool

"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element that receives input from the System.Windows.Input.TouchDevice.

Get: Target(self: TouchDevice) -> IInputElement

"""


 Activated=None
 Deactivated=None
 Updated=None

