class AttachedPropertyBrowsableWhenAttributePresentAttribute(AttachedPropertyBrowsableAttribute,_Attribute):
 """
 Specifies that an attached property is only browsable on an element that also has another specific �.NET Framework attribute�applied to its class definition.
 
 AttachedPropertyBrowsableWhenAttributePresentAttribute(attributeType: Type)
 """
 def Equals(self,obj):
  """
  Equals(self: AttachedPropertyBrowsableWhenAttributePresentAttribute,obj: object) -> bool
  
   Determines whether the current 
    System.Windows.AttachedPropertyBrowsableWhenAttributePresentAttribute�.NET 
    Framework attribute is equal to a specified object.
  
  
   obj: The System.Windows.AttachedPropertyBrowsableWhenAttributePresentAttribute to 
    compare to the current 
    System.Windows.AttachedPropertyBrowsableWhenAttributePresentAttribute.
  
   Returns: true if the specified 
    System.Windows.AttachedPropertyBrowsableWhenAttributePresentAttribute is equal 
    to the current 
    System.Windows.AttachedPropertyBrowsableWhenAttributePresentAttribute; 
    otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AttachedPropertyBrowsableWhenAttributePresentAttribute) -> int
  
   Returns the hash code for this 
    System.Windows.AttachedPropertyBrowsableWhenAttributePresentAttribute�.NET 
    Framework attribute.
  
   Returns: An unsigned 32-bit integer value.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,attributeType):
  """ __new__(cls: type,attributeType: Type) """
  pass
 def __ne__(self,*args):
  pass
 AttributeType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the �.NET Framework attribute�that must also be applied on a class.

Get: AttributeType(self: AttachedPropertyBrowsableWhenAttributePresentAttribute) -> Type

"""


