class EditorBrowsableAttribute(Attribute,_Attribute):
 """
 Specifies that a property or method is viewable in an editor. This class cannot be inherited.

 

 EditorBrowsableAttribute(state: EditorBrowsableState)

 EditorBrowsableAttribute()
 """
 def Equals(self,obj):
  """
  Equals(self: EditorBrowsableAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.EditorBrowsableAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: EditorBrowsableAttribute) -> int """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,state=None):
  """
  __new__(cls: type,state: EditorBrowsableState)

  __new__(cls: type)
  """
  pass
 def __ne__(self,*args):
  pass
 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the browsable state of the property or method.



Get: State(self: EditorBrowsableAttribute) -> EditorBrowsableState



"""


