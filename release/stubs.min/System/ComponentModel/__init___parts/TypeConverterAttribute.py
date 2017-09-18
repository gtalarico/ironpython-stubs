class TypeConverterAttribute(Attribute,_Attribute):
 """
 Specifies what type to use as a converter for the object this attribute is bound to.

 

 TypeConverterAttribute()

 TypeConverterAttribute(type: Type)

 TypeConverterAttribute(typeName: str)
 """
 def Equals(self,obj):
  """
  Equals(self: TypeConverterAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.TypeConverterAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current 

    System.ComponentModel.TypeConverterAttribute; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: TypeConverterAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A hash code for the current System.ComponentModel.TypeConverterAttribute.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,type: Type)

  __new__(cls: type,typeName: str)
  """
  pass
 def __ne__(self,*args):
  pass
 ConverterTypeName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the fully qualified type name of the System.Type to use as a converter for the object this attribute is bound to.



Get: ConverterTypeName(self: TypeConverterAttribute) -> str



"""


 Default=None

