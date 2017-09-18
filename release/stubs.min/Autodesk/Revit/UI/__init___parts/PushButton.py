class PushButton(RibbonButton):
 """ The PushButton object represents an button on a RibbonPanel. """
 def setAssemblyName(self,*args):
  """ setAssemblyName(self: PushButton,assemblyName: str) """
  pass
 def setAvailabilityClassName(self,*args):
  """ setAvailabilityClassName(self: PushButton,availabilityClassName: str) """
  pass
 def setClassName(self,*args):
  """ setClassName(self: PushButton,className: str) """
  pass
 AssemblyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assembly path of the button.



Get: AssemblyName(self: PushButton) -> str



Set: AssemblyName(self: PushButton)=value

"""

 AvailabilityClassName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The full class name for the class providing the entry point to decide availability of this push button.



Get: AvailabilityClassName(self: PushButton) -> str



Set: AvailabilityClassName(self: PushButton)=value

"""

 ClassName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the class containing the implementation for the command.



Get: ClassName(self: PushButton) -> str



Set: ClassName(self: PushButton)=value

"""


 m_ItemType=None

