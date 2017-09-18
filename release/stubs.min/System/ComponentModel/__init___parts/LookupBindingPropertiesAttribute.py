class LookupBindingPropertiesAttribute(Attribute,_Attribute):
 """
 Specifies the properties that support lookup-based binding. This class cannot be inherited.

 

 LookupBindingPropertiesAttribute()

 LookupBindingPropertiesAttribute(dataSource: str,displayMember: str,valueMember: str,lookupMember: str)
 """
 def Equals(self,obj):
  """
  Equals(self: LookupBindingPropertiesAttribute,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to the current 

    System.ComponentModel.LookupBindingPropertiesAttribute instance.

  

  

   obj: The System.Object to compare with the current 

    System.ComponentModel.LookupBindingPropertiesAttribute instance

  

   Returns: true if the object is equal to the current instance; otherwise,false,indicating they are not 

    equal.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: LookupBindingPropertiesAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.LookupBindingPropertiesAttribute.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dataSource=None,displayMember=None,valueMember=None,lookupMember=None):
  """
  __new__(cls: type)

  __new__(cls: type,dataSource: str,displayMember: str,valueMember: str,lookupMember: str)
  """
  pass
 def __ne__(self,*args):
  pass
 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the data source property for the component to which the System.ComponentModel.LookupBindingPropertiesAttribute is bound.



Get: DataSource(self: LookupBindingPropertiesAttribute) -> str



"""

 DisplayMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the display member property for the component to which the System.ComponentModel.LookupBindingPropertiesAttribute is bound.



Get: DisplayMember(self: LookupBindingPropertiesAttribute) -> str



"""

 LookupMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the lookup member for the component to which this attribute is bound.



Get: LookupMember(self: LookupBindingPropertiesAttribute) -> str



"""

 ValueMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the value member property for the component to which the System.ComponentModel.LookupBindingPropertiesAttribute is bound.



Get: ValueMember(self: LookupBindingPropertiesAttribute) -> str



"""


 Default=None

