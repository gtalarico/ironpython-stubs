class SwitchAttribute(Attribute,_Attribute):
 """
 Identifies a switch used in an assembly,class,or member.

 

 SwitchAttribute(switchName: str,switchType: Type)
 """
 @staticmethod
 def GetAll(assembly):
  """
  GetAll(assembly: Assembly) -> Array[SwitchAttribute]

  

   Returns all switch attributes for the specified assembly.

  

   assembly: The assembly to check for switch attributes.

   Returns: An array that contains all the switch attributes for the assembly.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,switchName,switchType):
  """ __new__(cls: type,switchName: str,switchType: Type) """
  pass
 SwitchDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the description of the switch.



Get: SwitchDescription(self: SwitchAttribute) -> str



Set: SwitchDescription(self: SwitchAttribute)=value

"""

 SwitchName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the display name of the switch.



Get: SwitchName(self: SwitchAttribute) -> str



Set: SwitchName(self: SwitchAttribute)=value

"""

 SwitchType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the type of the switch.



Get: SwitchType(self: SwitchAttribute) -> Type



Set: SwitchType(self: SwitchAttribute)=value

"""


