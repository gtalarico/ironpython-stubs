class StylusDevice(InputDevice):
 """ Represents a tablet pen used with a Tablet PC. """
 def Capture(self,element,captureMode=None):
  """
  Capture(self: StylusDevice,element: IInputElement) -> bool
  
   Binds input from the stylus to the specified element.
  
   element: The element to which the stylus is bound.
   Returns: true if the input element is captured successfully; otherwise,false. The 
    default is false.
  
  Capture(self: StylusDevice,element: IInputElement,captureMode: CaptureMode) -> bool
  
   Binds the stylus to the specified element.
  
   captureMode: One of the System.Windows.Input.CaptureMode values.
   Returns: true if the input element is captured successfully; otherwise,false. The 
    default is false.
  """
  pass
 def GetPosition(self,relativeTo):
  """
  GetPosition(self: StylusDevice,relativeTo: IInputElement) -> Point
  
   Gets the position of the stylus.
  
   relativeTo: The System.Windows.IInputElement to which the (x,y) coordinates are mapped.
   Returns: A System.Windows.Point that represents the position of the stylus,in relation 
    to relativeTo.
  """
  pass
 def GetStylusPoints(self,relativeTo,subsetToReformatTo=None):
  """
  GetStylusPoints(self: StylusDevice,relativeTo: IInputElement,subsetToReformatTo: StylusPointDescription) -> StylusPointCollection
  
   Returns a System.Windows.Input.StylusPointCollection that contains 
    System.Windows.Input.StylusPoint objects collected from the stylus. Uses the 
    specified System.Windows.Input.StylusPointDescription.
  
  
   relativeTo: The System.Windows.IInputElement to which the (x y) coordinates in the 
    System.Windows.Input.StylusPointCollection are mapped.
  
   subsetToReformatTo: The System.Windows.Input.StylusPointDescription to be used by the 
    System.Windows.Input.StylusPointCollection.
  
   Returns: A System.Windows.Input.StylusPointCollection that contains 
    System.Windows.Input.StylusPoint objects collected from the stylus.
  
  GetStylusPoints(self: StylusDevice,relativeTo: IInputElement) -> StylusPointCollection
  
   Returns a System.Windows.Input.StylusPointCollection that contains 
    System.Windows.Input.StylusPoint objects collected from the stylus.
  
  
   relativeTo: The System.Windows.IInputElement to which the (x,y) coordinates in the 
    System.Windows.Input.StylusPointCollection are mapped.
  
   Returns: A System.Windows.Input.StylusPointCollection that contains 
    System.Windows.Input.StylusPoint objects that the stylus collected.
  """
  pass
 def Synchronize(self):
  """
  Synchronize(self: StylusDevice)
   Synchronizes the cursor and the user interface.
  """
  pass
 def ToString(self):
  """
  ToString(self: StylusDevice) -> str
  
   Returns the name of the stylus device.
   Returns: The name of the System.Windows.Input.StylusDevice.
  """
  pass
 ActiveSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.PresentationSource that reports current input for the stylus.

Get: ActiveSource(self: StylusDevice) -> PresentationSource

"""

 Captured=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element that captured the stylus.

Get: Captured(self: StylusDevice) -> IInputElement

"""

 DirectlyOver=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.IInputElement that the pointer is positioned over.

Get: DirectlyOver(self: StylusDevice) -> IInputElement

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the identifier for the stylus device.

Get: Id(self: StylusDevice) -> int

"""

 InAir=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the tablet pen is positioned above,yet not in contact with,the digitizer.

Get: InAir(self: StylusDevice) -> bool

"""

 InRange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the tablet pen is in range of the digitizer.

Get: InRange(self: StylusDevice) -> bool

"""

 Inverted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the secondary tip of the stylus is in use.

Get: Inverted(self: StylusDevice) -> bool

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: StylusDevice) -> bool

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the stylus.

Get: Name(self: StylusDevice) -> str

"""

 StylusButtons=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the stylus buttons on the stylus.

Get: StylusButtons(self: StylusDevice) -> StylusButtonCollection

"""

 TabletDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.TabletDevice representing the digitizer associated with the current System.Windows.Input.StylusDevice.

Get: TabletDevice(self: StylusDevice) -> TabletDevice

"""

 Target=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element that receives input.

Get: Target(self: StylusDevice) -> IInputElement

"""


