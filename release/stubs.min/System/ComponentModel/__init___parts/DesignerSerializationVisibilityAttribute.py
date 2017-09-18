class DesignerSerializationVisibilityAttribute(Attribute,_Attribute):
 """
 Specifies the type of persistence to use when serializing a property on a component at design time.

 

 DesignerSerializationVisibilityAttribute(visibility: DesignerSerializationVisibility)
 """
 def Equals(self,obj):
  """
  Equals(self: DesignerSerializationVisibilityAttribute,obj: object) -> bool

  

   Indicates whether this instance and a specified object are equal.

  

   obj: Another object to compare to.

   Returns: true if obj is equal to this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DesignerSerializationVisibilityAttribute) -> int

  

   Returns the hash code for this object.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DesignerSerializationVisibilityAttribute) -> bool

  

   Gets a value indicating whether the current value of the attribute is the default value for the 

    attribute.

  

   Returns: true if the attribute is set to the default value; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,visibility):
  """ __new__(cls: type,visibility: DesignerSerializationVisibility) """
  pass
 def __ne__(self,*args):
  pass
 Visibility=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the basic serialization mode a serializer should use when determining whether and how to persist the value of a property.



Get: Visibility(self: DesignerSerializationVisibilityAttribute) -> DesignerSerializationVisibility



"""


 Content=None
 Default=None
 Hidden=None
 Visible=None

