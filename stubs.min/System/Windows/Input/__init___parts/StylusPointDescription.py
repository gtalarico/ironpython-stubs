class StylusPointDescription(object):
 """
 Specifies the properties that are in a System.Windows.Input.StylusPoint.
 
 StylusPointDescription()
 StylusPointDescription(stylusPointPropertyInfos: IEnumerable[StylusPointPropertyInfo])
 """
 @staticmethod
 def AreCompatible(stylusPointDescription1,stylusPointDescription2):
  """
  AreCompatible(stylusPointDescription1: StylusPointDescription,stylusPointDescription2: StylusPointDescription) -> bool
  
   Returns a value that indicates whether the specified 
    System.Windows.Input.StylusPointDescription objects are identical.
  
  
   stylusPointDescription1: The first System.Windows.Input.StylusPointDescription to check.
   stylusPointDescription2: The second System.Windows.Input.StylusPointDescription to check.
   Returns: true if the System.Windows.Input.StylusPointDescription objects are identical; 
    otherwise,false.
  """
  pass
 @staticmethod
 def GetCommonDescription(stylusPointDescription,stylusPointDescriptionPreserveInfo):
  """
  GetCommonDescription(stylusPointDescription: StylusPointDescription,stylusPointDescriptionPreserveInfo: StylusPointDescription) -> StylusPointDescription
  
   Returns the intersection of the specified 
    System.Windows.Input.StylusPointDescription objects.
  
  
   stylusPointDescriptionPreserveInfo: The second System.Windows.Input.StylusPointDescription to intersect.
   Returns: A System.Windows.Input.StylusPointDescription that contains the properties that 
    are present if both of the specified 
    System.Windows.Input.StylusPointDescription objects.
  """
  pass
 def GetPropertyInfo(self,stylusPointProperty):
  """
  GetPropertyInfo(self: StylusPointDescription,stylusPointProperty: StylusPointProperty) -> StylusPointPropertyInfo
  
   Gets the System.Windows.Input.StylusPointPropertyInfo for the specified 
    property.
  
  
   stylusPointProperty: The System.Windows.Input.StylusPointProperty that specifies the property of the 
    desired System.Windows.Input.StylusPointPropertyInfo.
  
   Returns: The System.Windows.Input.StylusPointPropertyInfo for the specified 
    System.Windows.Input.StylusPointProperty.
  """
  pass
 def GetStylusPointProperties(self):
  """
  GetStylusPointProperties(self: StylusPointDescription) -> ReadOnlyCollection[StylusPointPropertyInfo]
  
   Gets all the properties of the System.Windows.Input.StylusPointDescription.
   Returns: A collection that contains all of the 
    System.Windows.Input.StylusPointPropertyInfo objects in the 
    System.Windows.Input.StylusPointDescription.
  """
  pass
 def HasProperty(self,stylusPointProperty):
  """
  HasProperty(self: StylusPointDescription,stylusPointProperty: StylusPointProperty) -> bool
  
   Returns a value that indicates whether the current 
    System.Windows.Input.StylusPointDescription has the specified property.
  
  
   stylusPointProperty: The System.Windows.Input.StylusPointProperty to check for in the 
    System.Windows.Input.StylusPointDescription.
  
   Returns: true if the System.Windows.Input.StylusPointDescription has the specified 
    System.Windows.Input.StylusPointProperty; otherwise,false.
  """
  pass
 def IsSubsetOf(self,stylusPointDescriptionSuperset):
  """
  IsSubsetOf(self: StylusPointDescription,stylusPointDescriptionSuperset: StylusPointDescription) -> bool
  
   Returns a value that indicates whether the current 
    System.Windows.Input.StylusPointDescription is a subset of the specified 
    System.Windows.Input.StylusPointDescription.
  
  
   stylusPointDescriptionSuperset: The System.Windows.Input.StylusPointDescription against which to check whether 
    the current System.Windows.Input.StylusPointDescription is a subset.
  
   Returns: true if the current System.Windows.Input.StylusPointDescription is a subset of 
    the specified System.Windows.Input.StylusPointDescription; otherwise,false.
  """
  pass
 @staticmethod
 def __new__(self,stylusPointPropertyInfos=None):
  """
  __new__(cls: type)
  __new__(cls: type,stylusPointPropertyInfos: IEnumerable[StylusPointPropertyInfo])
  """
  pass
 PropertyCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of properties in the System.Windows.Input.StylusPointDescription.

Get: PropertyCount(self: StylusPointDescription) -> int

"""


