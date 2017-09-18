class StylusEventArgs(InputEventArgs):
 """
 Provides data for several of the events that are associated with the System.Windows.Input.Stylus class.
 
 StylusEventArgs(stylus: StylusDevice,timestamp: int)
 """
 def GetPosition(self,relativeTo):
  """
  GetPosition(self: StylusEventArgs,relativeTo: IInputElement) -> Point
  
   Gets the position of the stylus.
  
   relativeTo: The System.Windows.IInputElement that the (x,y) coordinates are mapped to.
   Returns: A System.Windows.Point that represents the position of the stylus,based on the 
    coordinates of relativeTo.
  """
  pass
 def GetStylusPoints(self,relativeTo,subsetToReformatTo=None):
  """
  GetStylusPoints(self: StylusEventArgs,relativeTo: IInputElement,subsetToReformatTo: StylusPointDescription) -> StylusPointCollection
  
   Returns a System.Windows.Input.StylusPointCollection that uses the specified 
    System.Windows.Input.StylusPointDescription and contains 
    System.Windows.Input.StylusPoint objects relating to the specified input 
    element.
  
  
   relativeTo: The System.Windows.IInputElement to which the (x,y) coordinates in the 
    System.Windows.Input.StylusPointCollection are mapped.
  
   subsetToReformatTo: The System.Windows.Input.StylusPointDescription to be used by the 
    System.Windows.Input.StylusPointCollection.
  
   Returns: A System.Windows.Input.StylusPointCollection that contains 
    System.Windows.Input.StylusPoint objects collected during an event.
  
  GetStylusPoints(self: StylusEventArgs,relativeTo: IInputElement) -> StylusPointCollection
  
   Returns a System.Windows.Input.StylusPointCollection that contains 
    System.Windows.Input.StylusPoint objects relative to the specified input 
    element.
  
  
   relativeTo: The System.Windows.IInputElement to which the (x,y) coordinates in the 
    System.Windows.Input.StylusPointCollection are mapped.
  
   Returns: A System.Windows.Input.StylusPointCollection that contains 
    System.Windows.Input.StylusPoint objects collected in the event.
  """
  pass
 @staticmethod
 def __new__(self,stylus,timestamp):
  """ __new__(cls: type,stylus: StylusDevice,timestamp: int) """
  pass
 InAir=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus is in proximity to,but not touching,the digitizer.

Get: InAir(self: StylusEventArgs) -> bool

"""

 Inverted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the stylus in inverted.

Get: Inverted(self: StylusEventArgs) -> bool

"""

 StylusDevice=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.StylusDevice that represents the stylus.

Get: StylusDevice(self: StylusEventArgs) -> StylusDevice

"""


