class DllImportAttribute:
 """
 Indicates that the attributed method is exposed by an unmanaged dynamic-link library (DLL) as a static entry point.
 
 DllImportAttribute(dllName: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DllImportAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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

