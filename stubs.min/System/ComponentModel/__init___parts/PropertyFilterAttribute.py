class PropertyFilterAttribute(Attribute,_Attribute):
 """
 Specifies which properties should be reported by type descriptors,specifically the System.ComponentModel.TypeDescriptor.GetProperties(System.Object) method.
 
 PropertyFilterAttribute(filter: PropertyFilterOptions)
 """
 def Equals(self,value):
  """
  Equals(self: PropertyFilterAttribute,value: object) -> bool
  
   Returns a value that indicates whether the current 
    System.ComponentModel.PropertyFilterAttribute�.NET Framework attribute is equal 
    to a specified object.
  
  
   value: The object to compare to this System.ComponentModel.PropertyFilterAttribute.
   Returns: true if the specified System.ComponentModel.PropertyFilterAttribute is equal to 
    the current System.ComponentModel.PropertyFilterAttribute; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: PropertyFilterAttribute) -> int
  
   Returns the hash code for the current 
    System.ComponentModel.PropertyFilterAttribute�.NET Framework attribute.
  
   Returns: A signed 32-bit integer value.
  """
  pass
 def Match(self,value):
  """
  Match(self: PropertyFilterAttribute,value: object) -> bool
  
   Returns a value that indicates whether the property filter options of the 
    current System.ComponentModel.PropertyFilterAttribute�.NET Framework attribute 
    match the property filter options of the provided object.
  
  
   value: The object to compare. This object is expected to be a 
    System.ComponentModel.PropertyFilterAttribute.
  
   Returns: true if a match exists; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,filter):
  """ __new__(cls: type,filter: PropertyFilterOptions) """
  pass
 def __ne__(self,*args):
  pass
 Filter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the filter options for this System.ComponentModel.PropertyFilterAttribute�.NET Framework attribute.

Get: Filter(self: PropertyFilterAttribute) -> PropertyFilterOptions

"""


 Default=None

