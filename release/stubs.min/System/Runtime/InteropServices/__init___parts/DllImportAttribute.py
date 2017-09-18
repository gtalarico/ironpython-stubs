class DllImportAttribute(Attribute,_Attribute):
 """
 Indicates that the attributed method is exposed by an unmanaged dynamic-link library (DLL) as a static entry point.

 

 DllImportAttribute(dllName: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dllName):
  """ __new__(cls: type,dllName: str) """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the DLL file that contains the entry point.



Get: Value(self: DllImportAttribute) -> str



"""


 BestFitMapping=None
 CallingConvention=None
 CharSet=None
 EntryPoint=None
 ExactSpelling=None
 PreserveSig=None
 SetLastError=None
 ThrowOnUnmappableChar=None

