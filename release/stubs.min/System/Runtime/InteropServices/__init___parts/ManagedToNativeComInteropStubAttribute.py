class ManagedToNativeComInteropStubAttribute(Attribute,_Attribute):
 """
 Provides support for user customization of interop stubs in managed-to-COM interop scenarios.

 

 ManagedToNativeComInteropStubAttribute(classType: Type,methodName: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,classType,methodName):
  """ __new__(cls: type,classType: Type,methodName: str) """
  pass
 ClassType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the class that contains the required stub method.



Get: ClassType(self: ManagedToNativeComInteropStubAttribute) -> Type



"""

 MethodName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the stub method.



Get: MethodName(self: ManagedToNativeComInteropStubAttribute) -> str



"""


