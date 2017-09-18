class ExtenderProvidedPropertyAttribute(Attribute,_Attribute):
 """
 Specifies a property that is offered by an extender provider. This class cannot be inherited.

 

 ExtenderProvidedPropertyAttribute()
 """
 def Equals(self,obj):
  """
  Equals(self: ExtenderProvidedPropertyAttribute,obj: object) -> bool

  

   Determines whether the specified System.Object is equal to the current System.Object.

  

   obj: An System.Object to compare with this instance or null.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ExtenderProvidedPropertyAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: ExtenderProvidedPropertyAttribute) -> bool

  

   Provides an indication whether the value of this instance is the default value for the derived 

    class.

  

   Returns: true if this instance is the default attribute for the class; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __ne__(self,*args):
  pass
 ExtenderProperty=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the property that is being provided.



Get: ExtenderProperty(self: ExtenderProvidedPropertyAttribute) -> PropertyDescriptor



"""

 Provider=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the extender provider that is providing the property.



Get: Provider(self: ExtenderProvidedPropertyAttribute) -> IExtenderProvider



"""

 ReceiverType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of object that can receive the property.



Get: ReceiverType(self: ExtenderProvidedPropertyAttribute) -> Type



"""


