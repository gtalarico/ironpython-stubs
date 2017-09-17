class StylusPoint(object,IEquatable[StylusPoint]):
 """
 Represents a single data point collected from the digitizer and stylus.
 
 StylusPoint(x: float,y: float)
 StylusPoint(x: float,y: float,pressureFactor: Single)
 StylusPoint(x: float,y: float,pressureFactor: Single,stylusPointDescription: StylusPointDescription,additionalValues: Array[int])
 """
 @staticmethod
 def Equals(*__args):
  """
  Equals(self: StylusPoint,value: StylusPoint) -> bool
  
   Returns a Boolean value that indicates whether the specified 
    System.Windows.Input.StylusPoint is equal to the current 
    System.Windows.Input.StylusPoint.
  
  
   value: The System.Windows.Input.StylusPoint to compare to the current 
    System.Windows.Input.StylusPoint.
  
   Returns: true if the System.Windows.Input.StylusPoint objects are equal; otherwise,
    false.
  
  Equals(self: StylusPoint,o: object) -> bool
  
   Returns a value indicating whether the specified object is equal to the 
    System.Windows.Input.StylusPoint.
  
  
   o: The System.Windows.Input.StylusPoint to compare to the current 
    System.Windows.Input.StylusPoint.
  
   Returns: true if the objects are equal; otherwise,false.
  Equals(stylusPoint1: StylusPoint,stylusPoint2: StylusPoint) -> bool
  
   Returns a Boolean value that indicates whether the two specified 
    System.Windows.Input.StylusPoint objects are equal.
  
  
   stylusPoint1: The first System.Windows.Input.StylusPoint to compare.
   stylusPoint2: The second System.Windows.Input.StylusPoint to compare.
   Returns: true if the System.Windows.Input.StylusPoint objects are equal; otherwise,
    false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: StylusPoint) -> int """
  pass
 def GetPropertyValue(self,stylusPointProperty):
  """
  GetPropertyValue(self: StylusPoint,stylusPointProperty: StylusPointProperty) -> int
  
   Returns the value of the specified property.
  
   stylusPointProperty: The System.Windows.Input.StylusPointProperty that specifies which property 
    value to get.
  
   Returns: The value of the specified System.Windows.Input.StylusPointProperty.
  """
  pass
 def HasProperty(self,stylusPointProperty):
  """
  HasProperty(self: StylusPoint,stylusPointProperty: StylusPointProperty) -> bool
  
   Returns whether the current System.Windows.Input.StylusPoint contains the 
    specified property.
  
  
   stylusPointProperty: The System.Windows.Input.StylusPointProperty to check for in the 
    System.Windows.Input.StylusPoint.
  
   Returns: true if the specified System.Windows.Input.StylusPointProperty is in the 
    current System.Windows.Input.StylusPoint; otherwise,false.
  """
  pass
 def SetPropertyValue(self,stylusPointProperty,value):
  """
  SetPropertyValue(self: StylusPoint,stylusPointProperty: StylusPointProperty,value: int)
   Sets the specified property to the specified value.
  
   stylusPointProperty: The System.Windows.Input.StylusPointProperty that specifies which property 
    value to set.
  
   value: The value of the property.
  """
  pass
 def ToPoint(self):
  """
  ToPoint(self: StylusPoint) -> Point
  
   Converts a System.Windows.Input.StylusPoint to a System.Windows.Point.
   Returns: A System.Windows.Point structure.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,x,y,pressureFactor=None,stylusPointDescription=None,additionalValues=None):
  """
  __new__[StylusPoint]() -> StylusPoint
  
  __new__(cls: type,x: float,y: float)
  __new__(cls: type,x: float,y: float,pressureFactor: Single)
  __new__(cls: type,x: float,y: float,pressureFactor: Single,stylusPointDescription: StylusPointDescription,additionalValues: Array[int])
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Input.StylusPointDescription that specifies the properties stored in the System.Windows.Input.StylusPoint.

Get: Description(self: StylusPoint) -> StylusPointDescription

"""

 PressureFactor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value between 0 and 1 that reflects the amount of pressure the stylus applies to the digitizer's surface when the System.Windows.Input.StylusPoint is created.

Get: PressureFactor(self: StylusPoint) -> Single

Set: PressureFactor(self: StylusPoint)=value
"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value for the x-coordinate of the System.Windows.Input.StylusPoint.

Get: X(self: StylusPoint) -> float

Set: X(self: StylusPoint)=value
"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate of the System.Windows.Input.StylusPoint.

Get: Y(self: StylusPoint) -> float

Set: Y(self: StylusPoint)=value
"""


 MaxXY=81164736.283464298
 MinXY=-81164736.321259603

