# encoding: utf-8
# module Microsoft.Win32.SafeHandles calls itself SafeHandles
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CriticalHandleMinusOneIsInvalid(CriticalHandle, IDisposable):
    """ Provides a base class for Win32 critical handle implementations in which the value of -1 indicates an invalid handle. """
    def Dispose(self):
        """
        Dispose(self: CriticalHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.CriticalHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """
        ReleaseHandle(self: CriticalHandle) -> bool
        
            When overridden in a derived class, executes the code required to free the handle.
            Returns: true if the handle is released successfully; otherwise, in the event of a catastrophic failure, 
             false. In this case, it generates a releaseHandleFailed MDA Managed Debugging Assistant.
        """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: CriticalHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the handle is invalid.

Get: IsInvalid(self: CriticalHandleMinusOneIsInvalid) -> bool

"""


    handle = None


class CriticalHandleZeroOrMinusOneIsInvalid(CriticalHandle, IDisposable):
    """ Provides a base class for Win32 critical handle implementations in which the value of either 0 or -1 indicates an invalid handle. """
    def Dispose(self):
        """
        Dispose(self: CriticalHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.CriticalHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """
        ReleaseHandle(self: CriticalHandle) -> bool
        
            When overridden in a derived class, executes the code required to free the handle.
            Returns: true if the handle is released successfully; otherwise, in the event of a catastrophic failure, 
             false. In this case, it generates a releaseHandleFailed MDA Managed Debugging Assistant.
        """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: CriticalHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the handle is invalid.

Get: IsInvalid(self: CriticalHandleZeroOrMinusOneIsInvalid) -> bool

"""


    handle = None


class SafeAccessTokenHandle(SafeHandle, IDisposable):
    """ SafeAccessTokenHandle(handle: IntPtr) """
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeAccessTokenHandle) -> bool """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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
    def __new__(self, handle):
        """ __new__(cls: type, handle: IntPtr) """
        pass

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInvalid(self: SafeAccessTokenHandle) -> bool

"""


    handle = None
    InvalidHandle = None


class SafeHandleZeroOrMinusOneIsInvalid(SafeHandle, IDisposable):
    """ Provides a base class for Win32 safe handle implementations in which the value of either 0 or -1 indicates an invalid handle. """
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """
        ReleaseHandle(self: SafeHandle) -> bool
        
            When overridden in a derived class, executes the code required to free the handle.
            Returns: true if the handle is released successfully; otherwise, in the event of a catastrophic failure, 
             false. In this case, it generates a releaseHandleFailed MDA Managed Debugging Assistant.
        """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, ownsHandle: bool) """
        pass

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the handle is invalid.

Get: IsInvalid(self: SafeHandleZeroOrMinusOneIsInvalid) -> bool

"""


    handle = None


class SafeFileHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """
    Represents a wrapper class for a file handle.
    
    SafeFileHandle(preexistingHandle: IntPtr, ownsHandle: bool)
    """
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeFileHandle) -> bool """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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
    def __new__(self, preexistingHandle, ownsHandle):
        """ __new__(cls: type, preexistingHandle: IntPtr, ownsHandle: bool) """
        pass

    handle = None


class SafeHandleMinusOneIsInvalid(SafeHandle, IDisposable):
    """ Provides a base class for Win32 safe handle implementations in which the value of -1 indicates an invalid handle. """
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """
        ReleaseHandle(self: SafeHandle) -> bool
        
            When overridden in a derived class, executes the code required to free the handle.
            Returns: true if the handle is released successfully; otherwise, in the event of a catastrophic failure, 
             false. In this case, it generates a releaseHandleFailed MDA Managed Debugging Assistant.
        """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, ownsHandle: bool) """
        pass

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the handle is invalid.

Get: IsInvalid(self: SafeHandleMinusOneIsInvalid) -> bool

"""


    handle = None


class SafeProcessHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """ SafeProcessHandle(existingHandle: IntPtr, ownsHandle: bool) """
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeProcessHandle) -> bool """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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
    def __new__(self, existingHandle, ownsHandle):
        """ __new__(cls: type, existingHandle: IntPtr, ownsHandle: bool) """
        pass

    handle = None


class SafeRegistryHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """
    Represents a safe handle to the Windows registry.
    
    SafeRegistryHandle(preexistingHandle: IntPtr, ownsHandle: bool)
    """
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeRegistryHandle) -> bool """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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
    def __new__(self, preexistingHandle, ownsHandle):
        """ __new__(cls: type, preexistingHandle: IntPtr, ownsHandle: bool) """
        pass

    handle = None


class SafeWaitHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    """
    Represents a wrapper class for a wait handle.
    
    SafeWaitHandle(existingHandle: IntPtr, ownsHandle: bool)
    """
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeWaitHandle) -> bool """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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
    def __new__(self, existingHandle, ownsHandle):
        """ __new__(cls: type, existingHandle: IntPtr, ownsHandle: bool) """
        pass

    handle = None


class SafeX509ChainHandle(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # no doc
    def Dispose(self):
        """
        Dispose(self: SafeHandle, disposing: bool)
            Releases the unmanaged resources used by the System.Runtime.InteropServices.SafeHandle class 
             specifying whether to perform a normal dispose operation.
        
        
            disposing: true for a normal dispose operation; false to finalize the handle.
        """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeX509ChainHandle) -> bool """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """
        SetHandle(self: SafeHandle, handle: IntPtr)
            Sets the handle to the specified pre-existing handle.
        
            handle: The pre-existing handle to use.
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

    handle = None


