class SwitchLevelAttribute(Attribute,_Attribute):
 """
 Identifies the level type for a switch.

 

 SwitchLevelAttribute(switchLevelType: Type)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,switchLevelType):
  """ __new__(cls: type,switchLevelType: Type) """
  pass
 SwitchLevelType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type that determines whether a trace should be written.



Get: SwitchLevelType(self: SwitchLevelAttribute) -> Type



Set: SwitchLevelType(self: SwitchLevelAttribute)=value

"""


