class AttachedPropertyBrowsableForTypeAttribute(AttachedPropertyBrowsableAttribute,_Attribute):
 """
 Specifies that an attached property is browsable only for elements that derive from a specified type.
 
 AttachedPropertyBrowsableForTypeAttribute(targetType: Type)
 """
 def Equals(self,obj):
  """
  Equals(self: AttachedPropertyBrowsableForTypeAttribute,obj: object) -> bool
  
   Determines whether the current 
    System.Windows.AttachedPropertyBrowsableForTypeAttribute�.NET Framework 
    attribute is equal to a specified object.
  
  
   obj: The System.Windows.AttachedPropertyBrowsableForTypeAttribute to compare to the 
    current System.Windows.AttachedPropertyBrowsableForTypeAttribute.
  
   Returns: true if the specified System.Windows.AttachedPropertyBrowsableForTypeAttribute 
    is equal to the current 
    System.Windows.AttachedPropertyBrowsableForTypeAttribute; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: AttachedPropertyBrowsableForTypeAttribute) -> int
  
   Returns the hash code for this 
    System.Windows.AttachedPropertyBrowsableForTypeAttribute�.NET Framework 
    attribute.
  
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
 def __new__(self,targetType):
  """ __new__(cls: type,targetType: Type) """
  pass
 def __ne__(self,*args):
  pass
 TargetType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the base type that scopes the use of the attached property where this�.NET Framework attribute�applies.

Get: TargetType(self: AttachedPropertyBrowsableForTypeAttribute) -> Type

"""

 TypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a unique type identifier for this System.Windows.AttachedPropertyBrowsableForTypeAttribute�.NET Framework attribute.

Get: TypeId(self: AttachedPropertyBrowsableForTypeAttribute) -> object

"""


