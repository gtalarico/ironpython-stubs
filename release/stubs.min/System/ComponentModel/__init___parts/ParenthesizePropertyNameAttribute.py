class ParenthesizePropertyNameAttribute(Attribute,_Attribute):
 """
 Indicates whether the name of the associated property is displayed with parentheses in the Properties window. This class cannot be inherited.

 

 ParenthesizePropertyNameAttribute()

 ParenthesizePropertyNameAttribute(needParenthesis: bool)
 """
 def Equals(self,o):
  """
  Equals(self: ParenthesizePropertyNameAttribute,o: object) -> bool

  

   Compares the specified object to this object and tests for equality.

  

   o: The object to be compared.

   Returns: true if equal; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ParenthesizePropertyNameAttribute) -> int

  

   Gets the hash code for this object.

   Returns: The hash code for the object the attribute belongs to.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: ParenthesizePropertyNameAttribute) -> bool

  

   Gets a value indicating whether the current value of the attribute is the default value for the 

    attribute.

  

   Returns: true if the current value of the attribute is the default value of the attribute; otherwise,

    false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,needParenthesis=None):
  """
  __new__(cls: type)

  __new__(cls: type,needParenthesis: bool)
  """
  pass
 def __ne__(self,*args):
  pass
 NeedParenthesis=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the Properties window displays the name of the property in parentheses in the Properties window.



Get: NeedParenthesis(self: ParenthesizePropertyNameAttribute) -> bool



"""


 Default=None

