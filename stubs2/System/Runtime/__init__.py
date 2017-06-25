# encoding: utf-8
# module System.Runtime calls itself Runtime
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class AssemblyTargetedPatchBandAttribute(Attribute, _Attribute):
    """
    Specifies patch band information for targeted patching of the .NET Framework.
    
    AssemblyTargetedPatchBandAttribute(targetedPatchBand: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, targetedPatchBand):
        """ __new__(cls: type, targetedPatchBand: str) """
        pass

    TargetedPatchBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the patch band.

Get: TargetedPatchBand(self: AssemblyTargetedPatchBandAttribute) -> str

"""



class GCLargeObjectHeapCompactionMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum GCLargeObjectHeapCompactionMode, values: CompactOnce (2), Default (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CompactOnce = None
    Default = None
    value__ = None


class GCLatencyMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Adjusts the time that the garbage collector intrudes in your application.
    
    enum GCLatencyMode, values: Batch (0), Interactive (1), LowLatency (2), NoGCRegion (4), SustainedLowLatency (3)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Batch = None
    Interactive = None
    LowLatency = None
    NoGCRegion = None
    SustainedLowLatency = None
    value__ = None


class GCSettings(object):
    """ Specifies the garbage collection settings for the current process. """
    IsServerGC = False
    LargeObjectHeapCompactionMode = None
    LatencyMode = None
    __all__ = []


class MemoryFailPoint(CriticalFinalizerObject, IDisposable):
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

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sizeInMegabytes):
        """ __new__(cls: type, sizeInMegabytes: int) """
        pass


class ProfileOptimization(object):
    # no doc
    @staticmethod
    def SetProfileRoot(directoryPath):
        """ SetProfileRoot(directoryPath: str) """
        pass

    @staticmethod
    def StartProfile(profile):
        """ StartProfile(profile: str) """
        pass

    __all__ = [
        'SetProfileRoot',
        'StartProfile',
    ]


class TargetedPatchingOptOutAttribute(Attribute, _Attribute):
    """
    Indicates that the .NET Framework class library method to which this attribute is applied is unlikely to be affected by servicing releases, and therefore is eligible to be inlined across Native Image Generator (NGen) images.
    
    TargetedPatchingOptOutAttribute(reason: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, reason):
        """ __new__(cls: type, reason: str) """
        pass

    Reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the reason why the method to which this attribute is applied is considered to be eligible for inlining across Native Image Generator (NGen) images.

Get: Reason(self: TargetedPatchingOptOutAttribute) -> str

"""



# variables with complex values

