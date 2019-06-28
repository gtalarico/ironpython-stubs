# encoding: utf-8
# module System.Runtime calls itself Runtime
# from mscorlib,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089,System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AssemblyTargetedPatchBandAttribute:
 """
 Specifies patch band information for targeted patching of the .NET Framework.
 
 AssemblyTargetedPatchBandAttribute(targetedPatchBand: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,targetedPatchBand):
  """ __new__(cls: type,targetedPatchBand: str) """
  pass
 TargetedPatchBand=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the patch band.

Get: TargetedPatchBand(self: AssemblyTargetedPatchBandAttribute) -> str

"""



class GCLargeObjectHeapCompactionMode:
 """ enum GCLargeObjectHeapCompactionMode,values: CompactOnce (2),Default (1) """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 CompactOnce=None
 Default=None
 value__=None


class GCLatencyMode:
 """
 Adjusts the time that the garbage collector intrudes in your application.
 
 enum GCLatencyMode,values: Batch (0),Interactive (1),LowLatency (2),NoGCRegion (4),SustainedLowLatency (3)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Batch=None
 Interactive=None
 LowLatency=None
 NoGCRegion=None
 SustainedLowLatency=None
 value__=None


class GCSettings:
 """ Specifies the garbage collection settings for the current process. """
 IsServerGC=False
 LargeObjectHeapCompactionMode=None
 LatencyMode=None
 __all__=[]


class MemoryFailPoint:
 """
 Checks for sufficient memory resources prior to execution. This class cannot be inherited.
 
 MemoryFailPoint(sizeInMegabytes: int)
 """
 def Dispose(self):
  """
  Dispose(self: MemoryFailPoint)
   Releases all resources used by the System.Runtime.MemoryFailPoint.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,sizeInMegabytes):
  """ __new__(cls: type,sizeInMegabytes: int) """
  pass

class ProfileOptimization:
 # no doc
 @staticmethod
 def SetProfileRoot(directoryPath):
  """ SetProfileRoot(directoryPath: str) """
  pass
 @staticmethod
 def StartProfile(profile):
  """ StartProfile(profile: str) """
  pass
 __all__=[
  'SetProfileRoot',
  'StartProfile',
 ]


class TargetedPatchingOptOutAttribute:
 """
 Indicates that the .NET Framework class library method to which this attribute is applied is unlikely to be affected by servicing releases,and therefore is eligible to be inlined across Native Image Generator (NGen) images.
 
 TargetedPatchingOptOutAttribute(reason: str)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,reason):
  """ __new__(cls: type,reason: str) """
  pass
 Reason=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the reason why the method to which this attribute is applied is considered to be eligible for inlining across Native Image Generator (NGen) images.

Get: Reason(self: TargetedPatchingOptOutAttribute) -> str

"""



# variables with complex values

