class PushButtonData(ButtonData):
 """
 This class contains information necessary to construct a push button in the Ribbon.

 

 PushButtonData(name: str,text: str,assemblyName: str,className: str)
 """
 @staticmethod
 def __new__(self,name,text,assemblyName,className):
  """ __new__(cls: type,name: str,text: str,assemblyName: str,className: str) """
  pass
 AssemblyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The assembly path of the button.



Get: AssemblyName(self: PushButtonData) -> str



Set: AssemblyName(self: PushButtonData)=value

"""

 AvailabilityClassName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The full class name for the class providing the entry point to decide availability of this push button.



Get: AvailabilityClassName(self: PushButtonData) -> str



Set: AvailabilityClassName(self: PushButtonData)=value

"""

 ClassName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The name of the class containing the implementation for the command.



Get: ClassName(self: PushButtonData) -> str



Set: ClassName(self: PushButtonData)=value

"""


