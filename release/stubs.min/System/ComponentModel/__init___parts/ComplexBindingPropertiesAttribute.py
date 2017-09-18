class ComplexBindingPropertiesAttribute(Attribute,_Attribute):
 """
 Specifies the data source and data member properties for a component that supports complex data binding. This class cannot be inherited.

 

 ComplexBindingPropertiesAttribute()

 ComplexBindingPropertiesAttribute(dataSource: str)

 ComplexBindingPropertiesAttribute(dataSource: str,dataMember: str)
 """
 def Equals(self,obj):
  """
  Equals(self: ComplexBindingPropertiesAttribute,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to the current 

    System.ComponentModel.ComplexBindingPropertiesAttribute instance.

  

  

   obj: The System.Object to compare with the current 

    System.ComponentModel.ComplexBindingPropertiesAttribute instance

  

   Returns: true if the object is equal to the current instance; otherwise,false,indicating they are not 

    equal.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ComplexBindingPropertiesAttribute) -> int

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dataSource=None,dataMember=None):
  """
  __new__(cls: type)

  __new__(cls: type,dataSource: str)

  __new__(cls: type,dataSource: str,dataMember: str)
  """
  pass
 def __ne__(self,*args):
  pass
 DataMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the data member property for the component to which the System.ComponentModel.ComplexBindingPropertiesAttribute is bound.



Get: DataMember(self: ComplexBindingPropertiesAttribute) -> str



"""

 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the data source property for the component to which the System.ComponentModel.ComplexBindingPropertiesAttribute is bound.



Get: DataSource(self: ComplexBindingPropertiesAttribute) -> str



"""


 Default=None

