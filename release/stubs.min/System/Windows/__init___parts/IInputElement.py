class IInputElement:
 """ Establishes the common events and also the event-related properties and methods for basic input processing by Windows Presentation Foundation (WPF) elements. """
 def AddHandler(self,routedEvent,handler):
  """
  AddHandler(self: IInputElement,routedEvent: RoutedEvent,handler: Delegate)
   Adds a routed event handler for a specific routed event to an element.
  
   routedEvent: The identifier for the routed event that is being handled.
   handler: A reference to the handler implementation.
  """
  pass
 def CaptureMouse(self):
  """
  CaptureMouse(self: IInputElement) -> bool
  
   Attempts to force capture of the mouse to this element.
   Returns: true if the mouse is successfully captured; otherwise,false.
  """
  pass
 def CaptureStylus(self):
  """
  CaptureStylus(self: IInputElement) -> bool
  
   Attempts to force capture of the stylus to this element.
   Returns: true if the stylus is successfully captured; otherwise,false.
  """
  pass
 def Focus(self):
  """
  Focus(self: IInputElement) -> bool
  
   Attempts to focus the keyboard on this element.
   Returns: true if keyboard focus is moved to this element or already was on this element; 
    otherwise,false.
  """
  pass
 def RaiseEvent(self,e):
  """
  RaiseEvent(self: IInputElement,e: RoutedEventArgs)
   Raises the routed event that is specified by the 
    System.Windows.RoutedEventArgs.RoutedEvent property within the provided 
    System.Windows.RoutedEventArgs.
  
  
   e: An instance of the System.Windows.RoutedEventArgs class that contains the 
    identifier for the event to raise.
  """
  pass
 def ReleaseMouseCapture(self):
  """
  ReleaseMouseCapture(self: IInputElement)
   Releases the mouse capture,if this element holds the capture.
  """
  pass
 def ReleaseStylusCapture(self):
  """
  ReleaseStylusCapture(self: IInputElement)
   Releases the stylus capture,if this element holds the capture.
  """
  pass
 def RemoveHandler(self,routedEvent,handler):
  """
  RemoveHandler(self: IInputElement,routedEvent: RoutedEvent,handler: Delegate)
   Removes all instances of the specified routed event handler from this element.
  
   routedEvent: Identifier of the routed event for which the handler is attached.
   handler: The specific handler implementation to remove from this element's event handler 
    collection.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Focusable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether focus can be set to this element.

Get: Focusable(self: IInputElement) -> bool

Set: Focusable(self: IInputElement)=value
"""

 IsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this element is enabled in the user interface (UI).

Get: IsEnabled(self: IInputElement) -> bool

"""

 IsKeyboardFocused=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether this element has keyboard focus.

Get: IsKeyboardFocused(self: IInputElement) -> bool

"""

 IsKeyboardFocusWithin=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether keyboard focus is anywhere inside the element bounds,including if keyboard focus is inside the bounds of any visual child elements.

Get: IsKeyboardFocusWithin(self: IInputElement) -> bool

"""

 IsMouseCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the mouse is captured to this element.

Get: IsMouseCaptured(self: IInputElement) -> bool

"""

 IsMouseDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the mouse pointer is over this element in the strictest hit testing sense.

Get: IsMouseDirectlyOver(self: IInputElement) -> bool

"""

 IsMouseOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the mouse pointer is located over this element (including visual children elements that are inside its bounds).

Get: IsMouseOver(self: IInputElement) -> bool

"""

 IsStylusCaptured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus is captured to this element.

Get: IsStylusCaptured(self: IInputElement) -> bool

"""

 IsStylusDirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus is over this element in the strictest hit testing sense.

Get: IsStylusDirectlyOver(self: IInputElement) -> bool

"""

 IsStylusOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus is located over this element (or over visual child elements that are inside its bounds).

Get: IsStylusOver(self: IInputElement) -> bool

"""


 GotKeyboardFocus=None
 GotMouseCapture=None
 GotStylusCapture=None
 KeyDown=None
 KeyUp=None
 LostKeyboardFocus=None
 LostMouseCapture=None
 LostStylusCapture=None
 MouseEnter=None
 MouseLeave=None
 MouseLeftButtonDown=None
 MouseLeftButtonUp=None
 MouseMove=None
 MouseRightButtonDown=None
 MouseRightButtonUp=None
 MouseWheel=None
 PreviewGotKeyboardFocus=None
 PreviewKeyDown=None
 PreviewKeyUp=None
 PreviewLostKeyboardFocus=None
 PreviewMouseLeftButtonDown=None
 PreviewMouseLeftButtonUp=None
 PreviewMouseMove=None
 PreviewMouseRightButtonDown=None
 PreviewMouseRightButtonUp=None
 PreviewMouseWheel=None
 PreviewStylusButtonDown=None
 PreviewStylusButtonUp=None
 PreviewStylusDown=None
 PreviewStylusInAirMove=None
 PreviewStylusInRange=None
 PreviewStylusMove=None
 PreviewStylusOutOfRange=None
 PreviewStylusSystemGesture=None
 PreviewStylusUp=None
 PreviewTextInput=None
 StylusButtonDown=None
 StylusButtonUp=None
 StylusDown=None
 StylusEnter=None
 StylusInAirMove=None
 StylusInRange=None
 StylusLeave=None
 StylusMove=None
 StylusOutOfRange=None
 StylusSystemGesture=None
 StylusUp=None
 TextInput=None

