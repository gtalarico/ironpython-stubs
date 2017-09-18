class SettingsBindableAttribute(Attribute,_Attribute):
 """
 Specifies when a component property can be bound to an application setting.

 

 SettingsBindableAttribute(bindable: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: SettingsBindableAttribute,obj: object) -> bool

  

   Determines whether two System.ComponentModel.SettingsBindableAttribute objects are equal.

  

   obj: The value to compare to.

   Returns: true if obj equals the type and value of this instance; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SettingsBindableAttribute) -> int

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
 def __new__(self,bindable):
  """ __new__(cls: type,bindable: bool) """
  pass
 def __ne__(self,*args):
  pass
 Bindable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a property is appropriate to bind settings to.



Get: Bindable(self: SettingsBindableAttribute) -> bool



"""


 No=None
 Yes=None

