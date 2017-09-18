class Marshal(object):
 """ Provides a collection of methods for allocating unmanaged memory,copying unmanaged memory blocks,and converting managed to unmanaged types,as well as other miscellaneous methods used when interacting with unmanaged code. """
 @staticmethod
 def AddRef(pUnk):
  """
  AddRef(pUnk: IntPtr) -> int

  

   Increments the reference count on the specified interface.

  

   pUnk: The interface reference count to increment.

   Returns: The new value of the reference count on the pUnk parameter.
  """
  pass
 @staticmethod
 def AllocCoTaskMem(cb):
  """
  AllocCoTaskMem(cb: int) -> IntPtr

  

   Allocates a block of memory of specified size from the COM task memory allocator.

  

   cb: The size of the block of memory to be allocated.

   Returns: An integer representing the address of the block of memory allocated. This memory must be 

    released with System.Runtime.InteropServices.Marshal.FreeCoTaskMem(System.IntPtr).
  """
  pass
 @staticmethod
 def AllocHGlobal(cb):
  """
  AllocHGlobal(cb: int) -> IntPtr

  

   Allocates memory from the unmanaged memory of the process by using the specified number of bytes.

  

   cb: The required number of bytes in memory.

   Returns: A pointer to the newly allocated memory. This memory must be released using the 

    System.Runtime.InteropServices.Marshal.FreeHGlobal(System.IntPtr) method.

  

  AllocHGlobal(cb: IntPtr) -> IntPtr

  

   Allocates memory from the unmanaged memory of the process by using the pointer to the specified 

    number of bytes.

  

  

   cb: The required number of bytes in memory.

   Returns: A pointer to the newly allocated memory. This memory must be released using the 

    System.Runtime.InteropServices.Marshal.FreeHGlobal(System.IntPtr) method.
  """
  pass
 @staticmethod
 def AreComObjectsAvailableForCleanup():
  """
  AreComObjectsAvailableForCleanup() -> bool

  

   Indicates whether runtime callable wrappers (RCWs) from any context are available for cleanup.

   Returns: true if there are any RCWs available for cleanup; otherwise,false.
  """
  pass
 @staticmethod
 def BindToMoniker(monikerName):
  """
  BindToMoniker(monikerName: str) -> object

  

   Gets an interface pointer identified by the specified moniker.

  

   monikerName: The moniker corresponding to the desired interface pointer.

   Returns: An object containing a reference to the interface pointer identified by the monikerName 

    parameter. A moniker is a name,and in this case,the moniker is defined by an interface.
  """
  pass
 @staticmethod
 def ChangeWrapperHandleStrength(otp,fIsWeak):
  """
  ChangeWrapperHandleStrength(otp: object,fIsWeak: bool)

   Changes the strength of an object's COM Callable Wrapper (CCW) handle.

  

   otp: The object whose CCW holds a reference counted handle. The handle is strong if the reference 

    count on the CCW is greater than zero; otherwise,it is weak.

  

   fIsWeak: true to change the strength of the handle on the otp parameter to weak,regardless of its 

    reference count; false to reset the handle strength on otp to be reference counted.
  """
  pass
 @staticmethod
 def CleanupUnusedObjectsInCurrentContext():
  """
  CleanupUnusedObjectsInCurrentContext()

   Notifies the runtime to clean up all Runtime Callable Wrappers (RCWs) allocated in the current 

    context.
  """
  pass
 @staticmethod
 def Copy(source,*__args):
  """
  Copy(source: IntPtr,destination: Array[Int16],startIndex: int,length: int)

   Copies data from an unmanaged memory pointer to a managed 16-bit signed integer array.

  

   source: The memory pointer to copy from.

   destination: The array to copy to.

   startIndex: The zero-based index in the destination  array where copying should start.

   length: The number of array elements to copy.

  Copy(source: IntPtr,destination: Array[Int64],startIndex: int,length: int)

   Copies data from an unmanaged memory pointer to a managed 64-bit signed integer array.

  

   source: The memory pointer to copy from.

   destination: The array to copy to.

   startIndex: The zero-based index in the destination  array where copying should start.

   length: The number of array elements to copy.

  Copy(source: IntPtr,destination: Array[int],startIndex: int,length: int)

   Copies data from an unmanaged memory pointer to a managed 32-bit signed integer array.

  

   source: The memory pointer to copy from.

   destination: The array to copy to.

   startIndex: The zero-based index in the destination  array where copying should start.

   length: The number of array elements to copy.

  Copy(source: IntPtr,destination: Array[Char],startIndex: int,length: int)

   Copies data from an unmanaged memory pointer to a managed character array.

  

   source: The memory pointer to copy from.

   destination: The array to copy to.

   startIndex: The zero-based index in the destination  array where copying should start.

   length: The number of array elements to copy.

  Copy(source: IntPtr,destination: Array[Byte],startIndex: int,length: int)

   Copies data from an unmanaged memory pointer to a managed 8-bit unsigned integer array.

  

   source: The memory pointer to copy from.

   destination: The array to copy to.

   startIndex: The zero-based index in the destination  array where copying should start.

   length: The number of array elements to copy.

  Copy(source: IntPtr,destination: Array[IntPtr],startIndex: int,length: int)

   Copies data from an unmanaged memory pointer to a managed System.IntPtr array.

  

   source: The memory pointer to copy from.

   destination: The array to copy to.

   startIndex: The zero-based index into the destination array where copying should start.

   length: The number of array elements to copy.

  Copy(source: IntPtr,destination: Array[Single],startIndex: int,length: int)

   Copies data from an unmanaged memory pointer to a managed single-precision floating-point number 

    array.

  

  

   source: The memory pointer to copy from.

   destination: The array to copy to.

   startIndex: The zero-based index in the destination  array where copying should start.

   length: The number of array elements to copy.

  Copy(source: IntPtr,destination: Array[float],startIndex: int,length: int)

   Copies data from an unmanaged memory pointer to a managed double-precision floating-point number 

    array.

  

  

   source: The memory pointer to copy from.

   destination: The array to copy to.

   startIndex: The zero-based index in the destination  array where copying should start.

   length: The number of array elements to copy.

  Copy(source: Array[Int16],startIndex: int,destination: IntPtr,length: int)

   Copies data from a one-dimensional,managed 16-bit signed integer array to an unmanaged memory 

    pointer.

  

  

   source: The one-dimensional array to copy from.

   startIndex: The zero-based index in the source array where copying should start.

   destination: The memory pointer to copy to.

   length: The number of array elements to copy.

  Copy(source: Array[Int64],startIndex: int,destination: IntPtr,length: int)

   Copies data from a one-dimensional,managed 64-bit signed integer array to an unmanaged memory 

    pointer.

  

  

   source: The one-dimensional array to copy from.

   startIndex: The zero-based index in the source array where copying should start.

   destination: The memory pointer to copy to.

   length: The number of array elements to copy.

  Copy(source: Array[int],startIndex: int,destination: IntPtr,length: int)

   Copies data from a one-dimensional,managed 32-bit signed integer array to an unmanaged memory 

    pointer.

  

  

   source: The one-dimensional array to copy from.

   startIndex: The zero-based index in the source array where copying should start.

   destination: The memory pointer to copy to.

   length: The number of array elements to copy.

  Copy(source: Array[Char],startIndex: int,destination: IntPtr,length: int)

   Copies data from a one-dimensional,managed character array to an unmanaged memory pointer.

  

   source: The one-dimensional array to copy from.

   startIndex: The zero-based index in the source array where copying should start.

   destination: The memory pointer to copy to.

   length: The number of array elements to copy.

  Copy(source: Array[Byte],startIndex: int,destination: IntPtr,length: int)

   Copies data from a one-dimensional,managed 8-bit unsigned integer array to an unmanaged memory 

    pointer.

  

  

   source: The one-dimensional array to copy from.

   startIndex: The zero-based index in the source array where copying should start.

   destination: The memory pointer to copy to.

   length: The number of array elements to copy.

  Copy(source: Array[IntPtr],startIndex: int,destination: IntPtr,length: int)

   Copies data from a one-dimensional,managed System.IntPtr array to an unmanaged memory pointer.

  

   source: The one-dimensional array to copy from.

   startIndex: The zero-based index into the source array where copying should start.

   destination: The memory pointer to copy to.

   length: The number of array elements to copy.

  Copy(source: Array[Single],startIndex: int,destination: IntPtr,length: int)

   Copies data from a one-dimensional,managed single-precision floating-point number array to an 

    unmanaged memory pointer.

  

  

   source: The one-dimensional array to copy from.

   startIndex: The zero-based index in the source array where copying should start.

   destination: The memory pointer to copy to.

   length: The number of array elements to copy.

  Copy(source: Array[float],startIndex: int,destination: IntPtr,length: int)

   Copies data from a one-dimensional,managed double-precision floating-point number array to an 

    unmanaged memory pointer.

  

  

   source: The one-dimensional array to copy from.

   startIndex: The zero-based index in the source array where copying should start.

   destination: The memory pointer to copy to.

   length: The number of array elements to copy.
  """
  pass
 @staticmethod
 def CreateAggregatedObject(pOuter,o):
  """
  CreateAggregatedObject[T](pOuter: IntPtr,o: T) -> IntPtr

  CreateAggregatedObject(pOuter: IntPtr,o: object) -> IntPtr

  

   Aggregates a managed object with the specified COM object.

  

   pOuter: The outer IUnknown pointer.

   o: An object to aggregate.

   Returns: The inner IUnknown pointer of the managed object.
  """
  pass
 @staticmethod
 def CreateWrapperOfType(o,t=None):
  """
  CreateWrapperOfType[(T,TWrapper)](o: T) -> TWrapper

  CreateWrapperOfType(o: object,t: Type) -> object

  

   Wraps the specified COM object in an object of the specified type.

  

   o: The object to be wrapped.

   t: The type of wrapper to create.

   Returns: The newly wrapped object that is an instance of the desired type.
  """
  pass
 @staticmethod
 def DestroyStructure(ptr,structuretype=None):
  """
  DestroyStructure[T](ptr: IntPtr)DestroyStructure(ptr: IntPtr,structuretype: Type)

   Frees all substructures that the specified unmanaged memory block points to.

  

   ptr: A pointer to an unmanaged block of memory.

   structuretype: Type of a formatted class. This provides the layout information necessary to delete the buffer 

    in the ptr parameter.
  """
  pass
 @staticmethod
 def FinalReleaseComObject(o):
  """
  FinalReleaseComObject(o: object) -> int

  

   Releases all references to a Runtime Callable Wrapper (RCW) by setting its reference count to 0.

  

   o: The RCW to be released.

   Returns: The new value of the reference count of the RCW associated with the oparameter,which is 0 

    (zero) if the release is successful.
  """
  pass
 @staticmethod
 def FreeBSTR(ptr):
  """
  FreeBSTR(ptr: IntPtr)

   Frees a BSTR using the COM SysFreeString function.

  

   ptr: The address of the BSTR to be freed.
  """
  pass
 @staticmethod
 def FreeCoTaskMem(ptr):
  """
  FreeCoTaskMem(ptr: IntPtr)

   Frees a block of memory allocated by the unmanaged COM task memory allocator.

  

   ptr: The address of the memory to be freed.
  """
  pass
 @staticmethod
 def FreeHGlobal(hglobal):
  """
  FreeHGlobal(hglobal: IntPtr)

   Frees memory previously allocated from the unmanaged memory of the process.

  

   hglobal: The handle returned by the original matching call to 

    System.Runtime.InteropServices.Marshal.AllocHGlobal(System.IntPtr).
  """
  pass
 @staticmethod
 def GenerateGuidForType(type):
  """
  GenerateGuidForType(type: Type) -> Guid

  

   Returns the globally unique identifier (GUID) for the specified type,or generates a GUID using 

    the algorithm used by the Type Library Exporter (Tlbexp.exe).

  

  

   type: The type to generate a GUID for.

   Returns: An identifier for the specified type.
  """
  pass
 @staticmethod
 def GenerateProgIdForType(type):
  """
  GenerateProgIdForType(type: Type) -> str

  

   Returns a programmatic identifier (ProgID) for the specified type.

  

   type: The type to get a ProgID for.

   Returns: The ProgID of the specified type.
  """
  pass
 @staticmethod
 def GetActiveObject(progID):
  """
  GetActiveObject(progID: str) -> object

  

   Obtains a running instance of the specified object from the running object table (ROT).

  

   progID: The programmatic identifier (ProgID) of the object that was requested.

   Returns: The object that was requested; otherwise null. You can cast this object to any COM interface 

    that it supports.
  """
  pass
 @staticmethod
 def GetComInterfaceForObject(o,T=None,mode=None):
  """
  GetComInterfaceForObject(o: object,T: Type,mode: CustomQueryInterfaceMode) -> IntPtr

  

   Returns a pointer to an IUnknown interface that represents the specified interface on the 

    specified object. Custom query interface access is controlled by the specified customization 

    mode.

  

  

   o: The object that provides the interface.

   T: The type of interface that is requested.

   mode: One of the enumeration values that indicates whether to apply an IUnknown::QueryInterface 

    customization that is supplied by an System.Runtime.InteropServices.ICustomQueryInterface.

  

   Returns: The interface pointer that represents the interface for the object.

  GetComInterfaceForObject[(T,TInterface)](o: T) -> IntPtr

  GetComInterfaceForObject(o: object,T: Type) -> IntPtr

  

   Returns a pointer to an IUnknown interface that represents the specified interface on the 

    specified object. Custom query interface access is enabled by default.

  

  

   o: The object that provides the interface.

   T: The type of interface that is requested.

   Returns: The interface pointer that represents the specified interface for the object.
  """
  pass
 @staticmethod
 def GetComInterfaceForObjectInContext(o,t):
  """
  GetComInterfaceForObjectInContext(o: object,t: Type) -> IntPtr

  

   Returns an interface pointer that represents the specified interface for an object,if the 

    caller is in the same context as that object.

  

  

   o: The object that provides the interface.

   t: The type of interface that is requested.

   Returns: The interface pointer specified by t that represents the interface for the specified object,or 

    null if the caller is not in the same context as the object.
  """
  pass
 @staticmethod
 def GetComObjectData(obj,key):
  """
  GetComObjectData(obj: object,key: object) -> object

  

   Retrieves data that is referenced by the specified key from the specified COM object.

  

   obj: The COM object that contains the data that you want.

   key: The key in the internal hash table of obj to retrieve the data from.

   Returns: The data represented by the key parameter in the internal hash table of the obj parameter.
  """
  pass
 @staticmethod
 def GetComSlotForMethodInfo(m):
  """
  GetComSlotForMethodInfo(m: MemberInfo) -> int

  

   Retrieves the virtual function table (v-table or VTBL) slot for a specified 

    System.Reflection.MemberInfo type when that type is exposed to COM.

  

  

   m: An object that represents an interface method.

   Returns: The VTBL slot m identifier when it is exposed to COM.
  """
  pass
 @staticmethod
 def GetDelegateForFunctionPointer(ptr,t=None):
  """
  GetDelegateForFunctionPointer[TDelegate](ptr: IntPtr) -> TDelegate

  GetDelegateForFunctionPointer(ptr: IntPtr,t: Type) -> Delegate

  

   Converts an unmanaged function pointer to a delegate.

  

   ptr: The unmanaged function pointer to be converted.

   t: The type of the delegate to be returned.

   Returns: A delegate instance that can be cast to the appropriate delegate type.
  """
  pass
 @staticmethod
 def GetEndComSlot(t):
  """
  GetEndComSlot(t: Type) -> int

  

   Retrieves the last slot in the virtual function table (v-table or VTBL) of a type when exposed 

    to COM.

  

  

   t: A type that represents an interface or class.

   Returns: The last VTBL slot of the interface when exposed to COM. If the t parameter is a class,the 

    returned VTBL slot is the last slot in the interface that is generated from the class.
  """
  pass
 @staticmethod
 def GetExceptionCode():
  """
  GetExceptionCode() -> int

  

   Retrieves a code that identifies the type of the exception that occurred.

   Returns: The type of the exception.
  """
  pass
 @staticmethod
 def GetExceptionForHR(errorCode,errorInfo=None):
  """
  GetExceptionForHR(errorCode: int,errorInfo: IntPtr) -> Exception

  

   Converts the specified HRESULT error code to a corresponding System.Exception object,with 

    additional error information passed in an IErrorInfo interface for the exception object.

  

  

   errorCode: The HRESULT to be converted.

   errorInfo: A pointer to the IErrorInfo interface that provides more information about the error. You can 

    specify IntPtr(0) to use the current IErrorInfo interface,or IntPtr(-1) to ignore the current 

    IErrorInfo interface and construct the exception just from the error code.

  

   Returns: An object that represents the converted HRESULT and information obtained from errorInfo.

  GetExceptionForHR(errorCode: int) -> Exception

  

   Converts the specified HRESULT error code to a corresponding System.Exception object.

  

   errorCode: The HRESULT to be converted.

   Returns: An object that represents the converted HRESULT.
  """
  pass
 @staticmethod
 def GetExceptionPointers():
  """
  GetExceptionPointers() -> IntPtr

  

   Retrieves a computer-independent description of an exception,and information about the state 

    that existed for the thread when the exception occurred.

  

   Returns: A pointer to an EXCEPTION_POINTERS structure.
  """
  pass
 @staticmethod
 def GetFunctionPointerForDelegate(d):
  """
  GetFunctionPointerForDelegate[TDelegate](d: TDelegate) -> IntPtr

  GetFunctionPointerForDelegate(d: Delegate) -> IntPtr

  

   Converts a delegate into a function pointer that is callable from unmanaged code.

  

   d: The delegate to be passed to unmanaged code.

   Returns: A value that can be passed to unmanaged code,which,in turn,can use it to call the underlying 

    managed delegate.
  """
  pass
 @staticmethod
 def GetHINSTANCE(m):
  """
  GetHINSTANCE(m: Module) -> IntPtr

  

   Returns the instance handle (HINSTANCE) for the specified module.

  

   m: The module whose HINSTANCE is desired.

   Returns: The HINSTANCE for m; or -1 if the module does not have an HINSTANCE.
  """
  pass
 @staticmethod
 def GetHRForException(e):
  """
  GetHRForException(e: Exception) -> int

  

   Converts the specified exception to an HRESULT.

  

   e: The exception to convert to an HRESULT.

   Returns: The HRESULT mapped to the supplied exception.
  """
  pass
 @staticmethod
 def GetHRForLastWin32Error():
  """
  GetHRForLastWin32Error() -> int

  

   Returns the HRESULT corresponding to the last error incurred by Win32 code executed using 

    System.Runtime.InteropServices.Marshal.

  

   Returns: The HRESULT corresponding to the last Win32 error code.
  """
  pass
 @staticmethod
 def GetIDispatchForObject(o):
  """
  GetIDispatchForObject(o: object) -> IntPtr

  

   Returns an IDispatch interface from a managed object.

  

   o: The object whose IDispatch interface is requested.

   Returns: The IDispatch pointer for the o parameter.
  """
  pass
 @staticmethod
 def GetIDispatchForObjectInContext(o):
  """
  GetIDispatchForObjectInContext(o: object) -> IntPtr

  

   Returns an IDispatch interface pointer from a managed object,if the caller is in the same 

    context as that object.

  

  

   o: The object whose IDispatch interface is requested.

   Returns: The IDispatch interface pointer for the specified object,or null if the caller is not in the 

    same context as the specified object.
  """
  pass
 @staticmethod
 def GetITypeInfoForType(t):
  """
  GetITypeInfoForType(t: Type) -> IntPtr

  

   Returns a System.Runtime.InteropServices.ComTypes.ITypeInfo interface from a managed type.

  

   t: The type whose ITypeInfo interface is being requested.

   Returns: A pointer to the ITypeInfo interface for the t parameter.
  """
  pass
 @staticmethod
 def GetIUnknownForObject(o):
  """
  GetIUnknownForObject(o: object) -> IntPtr

  

   Returns an IUnknown interface from a managed object.

  

   o: The object whose IUnknown interface is requested.

   Returns: The IUnknown pointer for the o parameter.
  """
  pass
 @staticmethod
 def GetIUnknownForObjectInContext(o):
  """
  GetIUnknownForObjectInContext(o: object) -> IntPtr

  

   Returns an IUnknown interface from a managed object,if the caller is in the same context as 

    that object.

  

  

   o: The object whose IUnknown interface is requested.

   Returns: The IUnknown pointer for the specified object,or null if the caller is not in the same context 

    as the specified object.
  """
  pass
 @staticmethod
 def GetLastWin32Error():
  """
  GetLastWin32Error() -> int

  

   Returns the error code returned by the last unmanaged function that was called using platform 

    invoke that has the System.Runtime.InteropServices.DllImportAttribute.SetLastError flag set.

  

   Returns: The last error code set by a call to the Win32 SetLastError function.
  """
  pass
 @staticmethod
 def GetManagedThunkForUnmanagedMethodPtr(pfnMethodToWrap,pbSignature,cbSignature):
  """
  GetManagedThunkForUnmanagedMethodPtr(pfnMethodToWrap: IntPtr,pbSignature: IntPtr,cbSignature: int) -> IntPtr

  

   Gets a pointer to a runtime-generated function that marshals a call from managed to unmanaged 

    code.

  

  

   pfnMethodToWrap: A pointer to the method to marshal.

   pbSignature: A pointer to the method signature.

   cbSignature: The number of bytes in pbSignature.

   Returns: A pointer to the function that will marshal a call from the pfnMethodToWrap parameter to 

    unmanaged code.
  """
  pass
 @staticmethod
 def GetMethodInfoForComSlot(t,slot,memberType):
  """
  GetMethodInfoForComSlot(t: Type,slot: int,memberType: ComMemberType) -> (MemberInfo,ComMemberType)

  

   Retrieves a System.Reflection.MemberInfo object for the specified virtual function table 

    (v-table or VTBL) slot.

  

  

   t: The type for which the System.Reflection.MemberInfo is to be retrieved.

   slot: The VTBL slot.

   memberType: On successful return,one of the enumeration values that specifies the type of the member.

   Returns: The object that represents the member at the specified VTBL slot.
  """
  pass
 @staticmethod
 def GetNativeVariantForObject(obj,pDstNativeVariant):
  """
  GetNativeVariantForObject[T](obj: T,pDstNativeVariant: IntPtr)GetNativeVariantForObject(obj: object,pDstNativeVariant: IntPtr)

   Converts an object to a COM VARIANT.

  

   obj: The object for which to get a COM VARIANT.

   pDstNativeVariant: A pointer to receive the VARIANT that corresponds to the obj parameter.
  """
  pass
 @staticmethod
 def GetObjectForIUnknown(pUnk):
  """
  GetObjectForIUnknown(pUnk: IntPtr) -> object

  

   Returns an instance of a type that represents a COM object by a pointer to its IUnknown 

    interface.

  

  

   pUnk: A pointer to the IUnknown interface.

   Returns: An object that represents the specified unmanaged COM object.
  """
  pass
 @staticmethod
 def GetObjectForNativeVariant(pSrcNativeVariant):
  """
  GetObjectForNativeVariant[T](pSrcNativeVariant: IntPtr) -> T

  

   Converts a COM VARIANT to an object.

  

   pSrcNativeVariant: A pointer to a COM VARIANT.

   Returns: An object that corresponds to the pSrcNativeVariant parameter.

  GetObjectForNativeVariant(pSrcNativeVariant: IntPtr) -> object

  

   Converts a COM VARIANT to an object.

  

   pSrcNativeVariant: A pointer to a COM VARIANT.

   Returns: An object that corresponds to the pSrcNativeVariant parameter.
  """
  pass
 @staticmethod
 def GetObjectsForNativeVariants(aSrcNativeVariant,cVars):
  """
  GetObjectsForNativeVariants[T](aSrcNativeVariant: IntPtr,cVars: int) -> Array[T]

  

   Converts an array of COM VARIANTs to an array of objects.

  

   aSrcNativeVariant: A pointer to the first element of an array of COM VARIANTs.

   cVars: The count of COM VARIANTs in aSrcNativeVariant.

   Returns: An object array that corresponds to aSrcNativeVariant.

  GetObjectsForNativeVariants(aSrcNativeVariant: IntPtr,cVars: int) -> Array[object]

  

   Converts an array of COM VARIANTs to an array of objects.

  

   aSrcNativeVariant: A pointer to the first element of an array of COM VARIANTs.

   cVars: The count of COM VARIANTs in aSrcNativeVariant.

   Returns: An object array that corresponds to aSrcNativeVariant.
  """
  pass
 @staticmethod
 def GetStartComSlot(t):
  """
  GetStartComSlot(t: Type) -> int

  

   Gets the first slot in the virtual function table (v-table or VTBL) that contains user-defined 

    methods.

  

  

   t: A type that represents an interface.

   Returns: The first VTBL slot that contains user-defined methods. The first slot is 3 if the interface is 

    based on IUnknown,and 7 if the interface is based on IDispatch.
  """
  pass
 @staticmethod
 def GetThreadFromFiberCookie(cookie):
  """
  GetThreadFromFiberCookie(cookie: int) -> Thread

  

   Converts a fiber cookie into the corresponding System.Threading.Thread instance.

  

   cookie: An integer that represents a fiber cookie.

   Returns: A thread that corresponds to the cookie parameter.
  """
  pass
 @staticmethod
 def GetTypedObjectForIUnknown(pUnk,t):
  """
  GetTypedObjectForIUnknown(pUnk: IntPtr,t: Type) -> object

  

   Returns a managed object of a specified type that represents a COM object.

  

   pUnk: A pointer to the IUnknown interface of the unmanaged object.

   t: The type of the requested managed class.

   Returns: An instance of the class corresponding to the System.Type object that represents the requested 

    unmanaged COM object.
  """
  pass
 @staticmethod
 def GetTypeForITypeInfo(piTypeInfo):
  """
  GetTypeForITypeInfo(piTypeInfo: IntPtr) -> Type

  

   Converts an unmanaged ITypeInfo object into a managed System.Type object.

  

   piTypeInfo: The ITypeInfo interface to marshal.

   Returns: A managed type that represents the unmanaged ITypeInfo object.
  """
  pass
 @staticmethod
 def GetTypeFromCLSID(clsid):
  """ GetTypeFromCLSID(clsid: Guid) -> Type """
  pass
 @staticmethod
 def GetTypeInfoName(*__args):
  """
  GetTypeInfoName(typeInfo: ITypeInfo) -> str

  

   Retrieves the name of the type represented by an ITypeInfo object.

  

   typeInfo: An object that represents an ITypeInfo pointer.

   Returns: The name of the type that the typeInfo parameter points to.

  GetTypeInfoName(pTI: UCOMITypeInfo) -> str

  

   Retrieves the name of the type represented by an ITypeInfo object.

  

   pTI: An object that represents an ITypeInfo pointer.

   Returns: The name of the type that the pTI parameter points to.
  """
  pass
 @staticmethod
 def GetTypeLibGuid(*__args):
  """
  GetTypeLibGuid(typelib: ITypeLib) -> Guid

  

   Retrieves the library identifier (LIBID) of a type library.

  

   typelib: The type library whose LIBID is to be retrieved.

   Returns: The LIBID of the specified type library.

  GetTypeLibGuid(pTLB: UCOMITypeLib) -> Guid

  

   Retrieves the library identifier (LIBID) of a type library.

  

   pTLB: The type library whose LIBID is to be retrieved.

   Returns: The LIBID of the type library that the pTLB parameter points to.
  """
  pass
 @staticmethod
 def GetTypeLibGuidForAssembly(asm):
  """
  GetTypeLibGuidForAssembly(asm: Assembly) -> Guid

  

   Retrieves the library identifier (LIBID) that is assigned to a type library when it was exported 

    from the specified assembly.

  

  

   asm: The assembly from which the type library was exported.

   Returns: The LIBID that is assigned to a type library when it is exported from the specified assembly.
  """
  pass
 @staticmethod
 def GetTypeLibLcid(*__args):
  """
  GetTypeLibLcid(typelib: ITypeLib) -> int

  

   Retrieves the LCID of a type library.

  

   typelib: The type library whose LCID is to be retrieved.

   Returns: The LCID of the type library that the typelib parameter points to.

  GetTypeLibLcid(pTLB: UCOMITypeLib) -> int

  

   Retrieves the LCID of a type library.

  

   pTLB: The type library whose LCID is to be retrieved.

   Returns: The LCID of the type library that the pTLB parameter points to.
  """
  pass
 @staticmethod
 def GetTypeLibName(*__args):
  """
  GetTypeLibName(typelib: ITypeLib) -> str

  

   Retrieves the name of a type library.

  

   typelib: The type library whose name is to be retrieved.

   Returns: The name of the type library that the typelib parameter points to.

  GetTypeLibName(pTLB: UCOMITypeLib) -> str

  

   Retrieves the name of a type library.

  

   pTLB: The type library whose name is to be retrieved.

   Returns: The name of the type library that the pTLB parameter points to.
  """
  pass
 @staticmethod
 def GetTypeLibVersionForAssembly(inputAssembly,majorVersion,minorVersion):
  """
  GetTypeLibVersionForAssembly(inputAssembly: Assembly) -> (int,int)

  

   Retrieves the version number of a type library that will be exported from the specified assembly.

  

   inputAssembly: A managed assembly.
  """
  pass
 @staticmethod
 def GetUniqueObjectForIUnknown(unknown):
  """
  GetUniqueObjectForIUnknown(unknown: IntPtr) -> object

  

   Creates a unique Runtime Callable Wrapper (RCW) object for a given IUnknown interface.

  

   unknown: A managed pointer to an IUnknown interface.

   Returns: A unique RCW for the specified IUnknown interface.
  """
  pass
 @staticmethod
 def GetUnmanagedThunkForManagedMethodPtr(pfnMethodToWrap,pbSignature,cbSignature):
  """
  GetUnmanagedThunkForManagedMethodPtr(pfnMethodToWrap: IntPtr,pbSignature: IntPtr,cbSignature: int) -> IntPtr

  

   Gets a pointer to a runtime-generated function that marshals a call from unmanaged to managed 

    code.

  

  

   pfnMethodToWrap: A pointer to the method to marshal.

   pbSignature: A pointer to the method signature.

   cbSignature: The number of bytes in pbSignature.

   Returns: A pointer to a function that will marshal a call from pfnMethodToWrap to managed code.
  """
  pass
 @staticmethod
 def IsComObject(o):
  """
  IsComObject(o: object) -> bool

  

   Indicates whether a specified object represents a COM object.

  

   o: The object to check.

   Returns: true if the o parameter is a COM type; otherwise,false.
  """
  pass
 @staticmethod
 def IsTypeVisibleFromCom(t):
  """
  IsTypeVisibleFromCom(t: Type) -> bool

  

   Indicates whether a type is visible to COM clients.

  

   t: The type to check for COM visibility.

   Returns: true if the type is visible to COM; otherwise,false.
  """
  pass
 @staticmethod
 def NumParamBytes(m):
  """
  NumParamBytes(m: MethodInfo) -> int

  

   Calculates the number of bytes in unmanaged memory that are required to hold the parameters for 

    the specified method.

  

  

   m: The method to be checked.

   Returns: The number of bytes required to represent the method parameters in unmanaged memory.
  """
  pass
 @staticmethod
 def OffsetOf(*__args):
  """
  OffsetOf[T](fieldName: str) -> IntPtr

  OffsetOf(t: Type,fieldName: str) -> IntPtr

  

   Returns the field offset of the unmanaged form of the managed class.

  

   t: A value type or formatted reference type that specifies the managed class. You must apply the 

    System.Runtime.InteropServices.StructLayoutAttribute to the class.

  

   fieldName: The field within the t parameter.

   Returns: The offset,in bytes,for the fieldName parameter within the specified class that is declared by 

    platform invoke.
  """
  pass
 @staticmethod
 def Prelink(m):
  """
  Prelink(m: MethodInfo)

   Executes one-time method setup tasks without calling the method.

  

   m: The method to be checked.
  """
  pass
 @staticmethod
 def PrelinkAll(c):
  """
  PrelinkAll(c: Type)

   Performs a pre-link check for all methods on a class.

  

   c: The class whose methods are to be checked.
  """
  pass
 @staticmethod
 def PtrToStringAnsi(ptr,len=None):
  """
  PtrToStringAnsi(ptr: IntPtr,len: int) -> str

  

   Allocates a managed System.String,copies a specified number of characters from an unmanaged 

    ANSI string into it,and widens each ANSI character to Unicode.

  

  

   ptr: The address of the first character of the unmanaged string.

   len: The byte count of the input string to copy.

   Returns: A managed string that holds a copy of the native ANSI string if the value of the ptr parameter 

    is not null; otherwise,this method returns null.

  

  PtrToStringAnsi(ptr: IntPtr) -> str

  

   Copies all characters up to the first null character from an unmanaged ANSI string to a managed 

    System.String,and widens each ANSI character to Unicode.

  

  

   ptr: The address of the first character of the unmanaged string.

   Returns: A managed string that holds a copy of the unmanaged ANSI string. If ptr is null,the method 

    returns a null string.
  """
  pass
 @staticmethod
 def PtrToStringAuto(ptr,len=None):
  """
  PtrToStringAuto(ptr: IntPtr) -> str

  

   Allocates a managed System.String and copies all characters up to the first null character from 

    a string stored in unmanaged memory into it.

  

  

   ptr: For Unicode platforms,the address of the first Unicode character.-or- For ANSI plaforms,the 

    address of the first ANSI character.

  

   Returns: A managed string that holds a copy of the unmanaged string if the value of the ptr parameter is 

    not null; otherwise,this method returns null.

  

  PtrToStringAuto(ptr: IntPtr,len: int) -> str

  

   Allocates a managed System.String and copies the specified number of characters from a string 

    stored in unmanaged memory into it.

  

  

   ptr: For Unicode platforms,the address of the first Unicode character.-or- For ANSI plaforms,the 

    address of the first ANSI character.

  

   len: The number of characters to copy.

   Returns: A managed string that holds a copy of the native string if the value of the ptr parameter is not 

    null; otherwise,this method returns null.
  """
  pass
 @staticmethod
 def PtrToStringBSTR(ptr):
  """
  PtrToStringBSTR(ptr: IntPtr) -> str

  

   Allocates a managed System.String and copies a BSTR Data Type string stored in unmanaged memory 

    into it.

  

  

   ptr: The address of the first character of the unmanaged string.

   Returns: A managed string that holds a copy of the unmanaged string if the value of the ptr parameter is 

    not null; otherwise,this method returns null.
  """
  pass
 @staticmethod
 def PtrToStringUni(ptr,len=None):
  """
  PtrToStringUni(ptr: IntPtr) -> str

  

   Allocates a managed System.String and copies all characters up to the first null character from 

    an unmanaged Unicode string into it.

  

  

   ptr: The address of the first character of the unmanaged string.

   Returns: A managed string that holds a copy of the unmanaged string if the value of the ptr parameter is 

    not null; otherwise,this method returns null.

  

  PtrToStringUni(ptr: IntPtr,len: int) -> str

  

   Allocates a managed System.String and copies a specified number of characters from an unmanaged 

    Unicode string into it.

  

  

   ptr: The address of the first character of the unmanaged string.

   len: The number of Unicode characters to copy.

   Returns: A managed string that holds a copy of the unmanaged string if the value of the ptr parameter is 

    not null; otherwise,this method returns null.
  """
  pass
 @staticmethod
 def PtrToStructure(ptr,*__args):
  """
  PtrToStructure(ptr: IntPtr,structureType: Type) -> object

  

   Marshals data from an unmanaged block of memory to a newly allocated managed object of the 

    specified type.

  

  

   ptr: A pointer to an unmanaged block of memory.

   structureType: The type of object to be created. This object must represent a formatted class or a structure.

   Returns: A managed object containing the data pointed to by the ptr parameter.

  PtrToStructure[T](ptr: IntPtr) -> T

  PtrToStructure(ptr: IntPtr,structure: object)

   Marshals data from an unmanaged block of memory to a managed object.

  

   ptr: A pointer to an unmanaged block of memory.

   structure: The object to which the data is to be copied. This must be an instance of a formatted class.

  PtrToStructure[T](ptr: IntPtr,structure: T)
  """
  pass
 @staticmethod
 def QueryInterface(pUnk,iid,ppv):
  """
  QueryInterface(pUnk: IntPtr,iid: Guid) -> (int,Guid,IntPtr)

  

   Requests a pointer to a specified interface from a COM object.

  

   pUnk: The interface to be queried.

   iid: The interface identifier (IID) of the requested interface.

   Returns: An HRESULT that indicates the success or failure of the call.
  """
  pass
 @staticmethod
 def ReadByte(ptr,ofs=None):
  """
  ReadByte(ptr: IntPtr) -> Byte

  

   Reads a single byte from unmanaged memory.

  

   ptr: The address in unmanaged memory from which to read.

   Returns: The byte read from unmanaged memory.

  ReadByte(ptr: IntPtr,ofs: int) -> Byte

  

   Reads a single byte at a given offset (or index) from unmanaged memory.

  

   ptr: The base address in unmanaged memory from which to read.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The byte read from unmanaged memory at the given offset.

  ReadByte(ptr: object,ofs: int) -> Byte

  

   Reads a single byte at a given offset (or index) from unmanaged memory.

  

   ptr: The base address in unmanaged memory of the source object.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The byte read from unmanaged memory at the given offset.
  """
  pass
 @staticmethod
 def ReadInt16(ptr,ofs=None):
  """
  ReadInt16(ptr: IntPtr) -> Int16

  

   Reads a 16-bit signed integer from unmanaged memory.

  

   ptr: The address in unmanaged memory from which to read.

   Returns: The 16-bit signed integer read from unmanaged memory.

  ReadInt16(ptr: IntPtr,ofs: int) -> Int16

  

   Reads a 16-bit signed integer at a given offset from unmanaged memory.

  

   ptr: The base address in unmanaged memory from which to read.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The 16-bit signed integer read from unmanaged memory at the given offset.

  ReadInt16(ptr: object,ofs: int) -> Int16

  

   Reads a 16-bit signed integer at a given offset from unmanaged memory.

  

   ptr: The base address in unmanaged memory of the source object.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The 16-bit signed integer read from unmanaged memory at the given offset.
  """
  pass
 @staticmethod
 def ReadInt32(ptr,ofs=None):
  """
  ReadInt32(ptr: IntPtr) -> int

  

   Reads a 32-bit signed integer from unmanaged memory.

  

   ptr: The address in unmanaged memory from which to read.

   Returns: The 32-bit signed integer read from unmanaged memory.

  ReadInt32(ptr: IntPtr,ofs: int) -> int

  

   Reads a 32-bit signed integer at a given offset from unmanaged memory.

  

   ptr: The base address in unmanaged memory from which to read.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The 32-bit signed integer read from unmanaged memory.

  ReadInt32(ptr: object,ofs: int) -> int

  

   Reads a 32-bit signed integer at a given offset from unmanaged memory.

  

   ptr: The base address in unmanaged memory of the source object.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The 32-bit signed integer read from unmanaged memory at the given offset.
  """
  pass
 @staticmethod
 def ReadInt64(ptr,ofs=None):
  """
  ReadInt64(ptr: IntPtr) -> Int64

  

   Reads a 64-bit signed integer from unmanaged memory.

  

   ptr: The address in unmanaged memory from which to read.

   Returns: The 64-bit signed integer read from unmanaged memory.

  ReadInt64(ptr: IntPtr,ofs: int) -> Int64

  

   Reads a 64-bit signed integer at a given offset from unmanaged memory.

  

   ptr: The base address in unmanaged memory from which to read.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The 64-bit signed integer read from unmanaged memory at the given offset.

  ReadInt64(ptr: object,ofs: int) -> Int64

  

   Reads a 64-bit signed integer at a given offset from unmanaged memory.

  

   ptr: The base address in unmanaged memory of the source object.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The 64-bit signed integer read from unmanaged memory at the given offset.
  """
  pass
 @staticmethod
 def ReadIntPtr(ptr,ofs=None):
  """
  ReadIntPtr(ptr: IntPtr) -> IntPtr

  

   Reads a processor native-sized integer from unmanaged memory.

  

   ptr: The address in unmanaged memory from which to read.

   Returns: The integer read from unmanaged memory. A 32 bit integer is returned on 32 bit machines and a 64 

    bit integer is returned on 64 bit machines.

  

  ReadIntPtr(ptr: IntPtr,ofs: int) -> IntPtr

  

   Reads a processor native sized integer at a given offset from unmanaged memory.

  

   ptr: The base address in unmanaged memory from which to read.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The integer read from unmanaged memory at the given offset.

  ReadIntPtr(ptr: object,ofs: int) -> IntPtr

  

   Reads a processor native sized integer from unmanaged memory.

  

   ptr: The base address in unmanaged memory of the source object.

   ofs: An additional byte offset,which is added to the ptr parameter before reading.

   Returns: The integer read from unmanaged memory at the given offset.
  """
  pass
 @staticmethod
 def ReAllocCoTaskMem(pv,cb):
  """
  ReAllocCoTaskMem(pv: IntPtr,cb: int) -> IntPtr

  

   Resizes a block of memory previously allocated with 

    System.Runtime.InteropServices.Marshal.AllocCoTaskMem(System.Int32).

  

  

   pv: A pointer to memory allocated with 

    System.Runtime.InteropServices.Marshal.AllocCoTaskMem(System.Int32).

  

   cb: The new size of the allocated block.

   Returns: An integer representing the address of the reallocated block of memory. This memory must be 

    released with System.Runtime.InteropServices.Marshal.FreeCoTaskMem(System.IntPtr).
  """
  pass
 @staticmethod
 def ReAllocHGlobal(pv,cb):
  """
  ReAllocHGlobal(pv: IntPtr,cb: IntPtr) -> IntPtr

  

   Resizes a block of memory previously allocated with 

    System.Runtime.InteropServices.Marshal.AllocHGlobal(System.IntPtr).

  

  

   pv: A pointer to memory allocated with 

    System.Runtime.InteropServices.Marshal.AllocHGlobal(System.IntPtr).

  

   cb: The new size of the allocated block. This is not a pointer; it is the byte count you are 

    requesting,cast to type System.IntPtr. If you pass a pointer,it is treated as a size.

  

   Returns: A pointer to the reallocated memory. This memory must be released using 

    System.Runtime.InteropServices.Marshal.FreeHGlobal(System.IntPtr).
  """
  pass
 @staticmethod
 def Release(pUnk):
  """
  Release(pUnk: IntPtr) -> int

  

   Decrements the reference count on the specified interface.

  

   pUnk: The interface to release.

   Returns: The new value of the reference count on the interface specified by the pUnk parameter.
  """
  pass
 @staticmethod
 def ReleaseComObject(o):
  """
  ReleaseComObject(o: object) -> int

  

   Decrements the reference count of the specified Runtime Callable Wrapper (RCW) associated with 

    the specified COM object.

  

  

   o: The COM object to release.

   Returns: The new value of the reference count of the RCW associated with o. This value is typically zero 

    since the RCW keeps just one reference to the wrapped COM object regardless of the number of 

    managed clients calling it.
  """
  pass
 @staticmethod
 def ReleaseThreadCache():
  """
  ReleaseThreadCache()

   Releases the thread cache.
  """
  pass
 @staticmethod
 def SecureStringToBSTR(s):
  """
  SecureStringToBSTR(s: SecureString) -> IntPtr

  

   Allocates a BSTR Data Type and copies the contents of a managed System.Security.SecureString 

    object into it.

  

  

   s: The managed object to copy.

   Returns: The address,in unmanaged memory,where the s parameter was copied to,or 0 if a null object was 

    supplied.
  """
  pass
 @staticmethod
 def SecureStringToCoTaskMemAnsi(s):
  """
  SecureStringToCoTaskMemAnsi(s: SecureString) -> IntPtr

  

   Copies the contents of a managed System.Security.SecureString object to a block of memory 

    allocated from the unmanaged COM task allocator.

  

  

   s: The managed object to copy.

   Returns: The address,in unmanaged memory,where the s parameter was copied to,or 0 if a null object was 

    supplied.
  """
  pass
 @staticmethod
 def SecureStringToCoTaskMemUnicode(s):
  """
  SecureStringToCoTaskMemUnicode(s: SecureString) -> IntPtr

  

   Copies the contents of a managed System.Security.SecureString object to a block of memory 

    allocated from the unmanaged COM task allocator.

  

  

   s: The managed object to copy.

   Returns: The address,in unmanaged memory,where the s parameter was copied to,or 0 if a null object was 

    supplied.
  """
  pass
 @staticmethod
 def SecureStringToGlobalAllocAnsi(s):
  """
  SecureStringToGlobalAllocAnsi(s: SecureString) -> IntPtr

  

   Copies the contents of a managed System.Security.SecureString into unmanaged memory,converting 

    into ANSI format as it copies.

  

  

   s: The managed object to copy.

   Returns: The address,in unmanaged memory,to where the s parameter was copied,or 0 if a null object was 

    supplied.
  """
  pass
 @staticmethod
 def SecureStringToGlobalAllocUnicode(s):
  """
  SecureStringToGlobalAllocUnicode(s: SecureString) -> IntPtr

  

   Copies the contents of a managed System.Security.SecureString object into unmanaged memory.

  

   s: The managed object to copy.

   Returns: The address,in unmanaged memory,where s was copied,or 0 if s is a 

    System.Security.SecureString object whose length is 0.
  """
  pass
 @staticmethod
 def SetComObjectData(obj,key,data):
  """
  SetComObjectData(obj: object,key: object,data: object) -> bool

  

   Sets data referenced by the specified key in the specified COM object.

  

   obj: The COM object in which to store the data.

   key: The key in the internal hash table of the COM object in which to store the data.

   data: The data to set.

   Returns: true if the data was set successfully; otherwise,false.
  """
  pass
 @staticmethod
 def SizeOf(*__args):
  """
  SizeOf(t: Type) -> int

  

   Returns the size of an unmanaged type in bytes.

  

   t: The type whose size is to be returned.

   Returns: The size of the specified type in unmanaged code.

  SizeOf[T]() -> int

  SizeOf(structure: object) -> int

  

   Returns the unmanaged size of an object in bytes.

  

   structure: The object whose size is to be returned.

   Returns: The size of the specified object in unmanaged code.

  SizeOf[T](structure: T) -> int
  """
  pass
 @staticmethod
 def StringToBSTR(s):
  """
  StringToBSTR(s: str) -> IntPtr

  

   Allocates a BSTR Data Type and copies the contents of a managed System.String into it.

  

   s: The managed string to be copied.

   Returns: An unmanaged pointer to the BSTR,or 0 if s is null.
  """
  pass
 @staticmethod
 def StringToCoTaskMemAnsi(s):
  """
  StringToCoTaskMemAnsi(s: str) -> IntPtr

  

   Copies the contents of a managed System.String to a block of memory allocated from the unmanaged 

    COM task allocator.

  

  

   s: A managed string to be copied.

   Returns: An integer representing a pointer to the block of memory allocated for the string,or 0 if s is 

    null.
  """
  pass
 @staticmethod
 def StringToCoTaskMemAuto(s):
  """
  StringToCoTaskMemAuto(s: str) -> IntPtr

  

   Copies the contents of a managed System.String to a block of memory allocated from the unmanaged 

    COM task allocator.

  

  

   s: A managed string to be copied.

   Returns: The allocated memory block,or 0 if s is null.
  """
  pass
 @staticmethod
 def StringToCoTaskMemUni(s):
  """
  StringToCoTaskMemUni(s: str) -> IntPtr

  

   Copies the contents of a managed System.String to a block of memory allocated from the unmanaged 

    COM task allocator.

  

  

   s: A managed string to be copied.

   Returns: An integer representing a pointer to the block of memory allocated for the string,or 0 if s is 

    null.
  """
  pass
 @staticmethod
 def StringToHGlobalAnsi(s):
  """
  StringToHGlobalAnsi(s: str) -> IntPtr

  

   Copies the contents of a managed System.String into unmanaged memory,converting into ANSI 

    format as it copies.

  

  

   s: A managed string to be copied.

   Returns: The address,in unmanaged memory,to where s was copied,or 0 if s is null.
  """
  pass
 @staticmethod
 def StringToHGlobalAuto(s):
  """
  StringToHGlobalAuto(s: str) -> IntPtr

  

   Copies the contents of a managed System.String into unmanaged memory,converting into ANSI 

    format if required.

  

  

   s: A managed string to be copied.

   Returns: The address,in unmanaged memory,to where the string was copied,or 0 if s is null.
  """
  pass
 @staticmethod
 def StringToHGlobalUni(s):
  """
  StringToHGlobalUni(s: str) -> IntPtr

  

   Copies the contents of a managed System.String into unmanaged memory.

  

   s: A managed string to be copied.

   Returns: The address,in unmanaged memory,to where the s was copied,or 0 if s is null.
  """
  pass
 @staticmethod
 def StructureToPtr(structure,ptr,fDeleteOld):
  """
  StructureToPtr[T](structure: T,ptr: IntPtr,fDeleteOld: bool)StructureToPtr(structure: object,ptr: IntPtr,fDeleteOld: bool)

   Marshals data from a managed object to an unmanaged block of memory.

  

   structure: A managed object holding the data to be marshaled. This object must be an instance of a 

    formatted class.

  

   ptr: A pointer to an unmanaged block of memory,which must be allocated before this method is called.

   fDeleteOld: true to have the 

    System.Runtime.InteropServices.Marshal.DestroyStructure(System.IntPtr,System.Type) method called 

    on the ptr parameter before this method executes. Note that passing false can lead to a memory 

    leak.
  """
  pass
 @staticmethod
 def ThrowExceptionForHR(errorCode,errorInfo=None):
  """
  ThrowExceptionForHR(errorCode: int,errorInfo: IntPtr)

   Throws an exception with a specific failure HRESULT,based on the specified IErrorInfo Interface 

    interface.

  

  

   errorCode: The HRESULT corresponding to the desired exception.

   errorInfo: A pointer to the IErrorInfo interface that provides more information about the error. You can 

    specify IntPtr(0) to use the current IErrorInfo interface,or IntPtr(-1) to ignore the current 

    IErrorInfo interface and construct the exception just from the error code.

  

  ThrowExceptionForHR(errorCode: int)

   Throws an exception with a specific failure HRESULT value.

  

   errorCode: The HRESULT corresponding to the desired exception.
  """
  pass
 @staticmethod
 def UnsafeAddrOfPinnedArrayElement(arr,index):
  """
  UnsafeAddrOfPinnedArrayElement[T](arr: Array[T],index: int) -> IntPtr

  UnsafeAddrOfPinnedArrayElement(arr: Array,index: int) -> IntPtr

  

   Gets the address of the element at the specified index inside the specified array.

  

   arr: The array that contains the desired element.

   index: The index in the arr parameter of the desired element.

   Returns: The address of index inside arr.
  """
  pass
 @staticmethod
 def WriteByte(ptr,*__args):
  """
  WriteByte(ptr: IntPtr,val: Byte)

   Writes a single byte value to unmanaged memory.

  

   ptr: The address in unmanaged memory to write to.

   val: The value to write.

  WriteByte(ofs: int,val: Byte) -> object

  

   Writes a single byte value to unmanaged memory at a specified offset.

  

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.

  WriteByte(ptr: IntPtr,ofs: int,val: Byte)

   Writes a single byte value to unmanaged memory at a specified offset.

  

   ptr: The base address in unmanaged memory to write to.

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.
  """
  pass
 @staticmethod
 def WriteInt16(ptr,*__args):
  """
  WriteInt16(ptr: IntPtr,ofs: int,val: Char)

   Writes a 16-bit signed integer value to unmanaged memory at a specified offset.

  

   ptr: The base address in the native heap to write to.

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.

  WriteInt16(ofs: int,val: Char) -> object

  

   Writes a 16-bit signed integer value to unmanaged memory at a specified offset.

  

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.

  WriteInt16(ptr: IntPtr,val: Char)

   Writes a character as a 16-bit integer value to unmanaged memory.

  

   ptr: The address in unmanaged memory to write to.

   val: The value to write.

  WriteInt16(ptr: IntPtr,ofs: int,val: Int16)

   Writes a 16-bit signed integer value into unmanaged memory at a specified offset.

  

   ptr: The base address in unmanaged memory to write to.

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.

  WriteInt16(ofs: int,val: Int16) -> object

  

   Writes a 16-bit signed integer value to unmanaged memory at a specified offset.

  

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.

  WriteInt16(ptr: IntPtr,val: Int16)

   Writes a 16-bit integer value to unmanaged memory.

  

   ptr: The address in unmanaged memory to write to.

   val: The value to write.
  """
  pass
 @staticmethod
 def WriteInt32(ptr,*__args):
  """
  WriteInt32(ptr: IntPtr,val: int)

   Writes a 32-bit signed integer value to unmanaged memory.

  

   ptr: The address in unmanaged memory to write to.

   val: The value to write.

  WriteInt32(ofs: int,val: int) -> object

  

   Writes a 32-bit signed integer value to unmanaged memory at a specified offset.

  

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.

  WriteInt32(ptr: IntPtr,ofs: int,val: int)

   Writes a 32-bit signed integer value into unmanaged memory at a specified offset.

  

   ptr: The base address in unmanaged memory to write to.

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.
  """
  pass
 @staticmethod
 def WriteInt64(ptr,*__args):
  """
  WriteInt64(ptr: IntPtr,val: Int64)

   Writes a 64-bit signed integer value to unmanaged memory.

  

   ptr: The address in unmanaged memory to write to.

   val: The value to write.

  WriteInt64(ofs: int,val: Int64) -> object

  

   Writes a 64-bit signed integer value to unmanaged memory at a specified offset.

  

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.

  WriteInt64(ptr: IntPtr,ofs: int,val: Int64)

   Writes a 64-bit signed integer value to unmanaged memory at a specified offset.

  

   ptr: The base address in unmanaged memory to write.

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.
  """
  pass
 @staticmethod
 def WriteIntPtr(ptr,*__args):
  """
  WriteIntPtr(ptr: IntPtr,val: IntPtr)

   Writes a processor native sized integer value into unmanaged memory.

  

   ptr: The address in unmanaged memory to write to.

   val: The value to write.

  WriteIntPtr(ofs: int,val: IntPtr) -> object

  

   Writes a processor native sized integer value to unmanaged memory.

  

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.

  WriteIntPtr(ptr: IntPtr,ofs: int,val: IntPtr)

   Writes a processor native-sized integer value to unmanaged memory at a specified offset.

  

   ptr: The base address in unmanaged memory to write to.

   ofs: An additional byte offset,which is added to the ptr parameter before writing.

   val: The value to write.
  """
  pass
 @staticmethod
 def ZeroFreeBSTR(s):
  """
  ZeroFreeBSTR(s: IntPtr)

   Frees a BSTR Data Type pointer that was allocated using the 

    System.Runtime.InteropServices.Marshal.SecureStringToBSTR(System.Security.SecureString) method.

  

  

   s: The address of the BSTR to free.
  """
  pass
 @staticmethod
 def ZeroFreeCoTaskMemAnsi(s):
  """
  ZeroFreeCoTaskMemAnsi(s: IntPtr)

   Frees an unmanaged string pointer that was allocated using the 

    System.Runtime.InteropServices.Marshal.SecureStringToCoTaskMemAnsi(System.Security.SecureString) 

    method.

  

  

   s: The address of the unmanaged string to free.
  """
  pass
 @staticmethod
 def ZeroFreeCoTaskMemUnicode(s):
  """
  ZeroFreeCoTaskMemUnicode(s: IntPtr)

   Frees an unmanaged string pointer that was allocated using the 

    System.Runtime.InteropServices.Marshal.SecureStringToCoTaskMemUnicode(System.Security.SecureStrin

    g) method.

  

  

   s: The address of the unmanaged string to free.
  """
  pass
 @staticmethod
 def ZeroFreeGlobalAllocAnsi(s):
  """
  ZeroFreeGlobalAllocAnsi(s: IntPtr)

   Frees an unmanaged string pointer that was allocated using the 

    System.Runtime.InteropServices.Marshal.SecureStringToGlobalAllocAnsi(System.Security.SecureString

    ) method.

  

  

   s: The address of the unmanaged string to free.
  """
  pass
 @staticmethod
 def ZeroFreeGlobalAllocUnicode(s):
  """
  ZeroFreeGlobalAllocUnicode(s: IntPtr)

   Frees an unmanaged string pointer that was allocated using the 

    System.Runtime.InteropServices.Marshal.SecureStringToGlobalAllocUnicode(System.Security.SecureStr

    ing) method.

  

  

   s: The address of the unmanaged string to free.
  """
  pass
 SystemDefaultCharSize=2
 SystemMaxDBCSCharSize=1
 __all__=[
  'AddRef',
  'AllocCoTaskMem',
  'AllocHGlobal',
  'AreComObjectsAvailableForCleanup',
  'BindToMoniker',
  'ChangeWrapperHandleStrength',
  'CleanupUnusedObjectsInCurrentContext',
  'Copy',
  'CreateAggregatedObject',
  'CreateWrapperOfType',
  'DestroyStructure',
  'FinalReleaseComObject',
  'FreeBSTR',
  'FreeCoTaskMem',
  'FreeHGlobal',
  'GenerateGuidForType',
  'GenerateProgIdForType',
  'GetActiveObject',
  'GetComInterfaceForObject',
  'GetComInterfaceForObjectInContext',
  'GetComObjectData',
  'GetComSlotForMethodInfo',
  'GetDelegateForFunctionPointer',
  'GetEndComSlot',
  'GetExceptionCode',
  'GetExceptionForHR',
  'GetExceptionPointers',
  'GetFunctionPointerForDelegate',
  'GetHINSTANCE',
  'GetHRForException',
  'GetHRForLastWin32Error',
  'GetIDispatchForObject',
  'GetIDispatchForObjectInContext',
  'GetITypeInfoForType',
  'GetIUnknownForObject',
  'GetIUnknownForObjectInContext',
  'GetLastWin32Error',
  'GetManagedThunkForUnmanagedMethodPtr',
  'GetMethodInfoForComSlot',
  'GetNativeVariantForObject',
  'GetObjectForIUnknown',
  'GetObjectForNativeVariant',
  'GetObjectsForNativeVariants',
  'GetStartComSlot',
  'GetThreadFromFiberCookie',
  'GetTypedObjectForIUnknown',
  'GetTypeForITypeInfo',
  'GetTypeFromCLSID',
  'GetTypeInfoName',
  'GetTypeLibGuid',
  'GetTypeLibGuidForAssembly',
  'GetTypeLibLcid',
  'GetTypeLibName',
  'GetTypeLibVersionForAssembly',
  'GetUniqueObjectForIUnknown',
  'GetUnmanagedThunkForManagedMethodPtr',
  'IsComObject',
  'IsTypeVisibleFromCom',
  'NumParamBytes',
  'OffsetOf',
  'Prelink',
  'PrelinkAll',
  'PtrToStringAnsi',
  'PtrToStringAuto',
  'PtrToStringBSTR',
  'PtrToStringUni',
  'PtrToStructure',
  'QueryInterface',
  'ReadByte',
  'ReadInt16',
  'ReadInt32',
  'ReadInt64',
  'ReadIntPtr',
  'ReAllocCoTaskMem',
  'ReAllocHGlobal',
  'Release',
  'ReleaseComObject',
  'ReleaseThreadCache',
  'SecureStringToBSTR',
  'SecureStringToCoTaskMemAnsi',
  'SecureStringToCoTaskMemUnicode',
  'SecureStringToGlobalAllocAnsi',
  'SecureStringToGlobalAllocUnicode',
  'SetComObjectData',
  'SizeOf',
  'StringToBSTR',
  'StringToCoTaskMemAnsi',
  'StringToCoTaskMemAuto',
  'StringToCoTaskMemUni',
  'StringToHGlobalAnsi',
  'StringToHGlobalAuto',
  'StringToHGlobalUni',
  'StructureToPtr',
  'SystemDefaultCharSize',
  'SystemMaxDBCSCharSize',
  'ThrowExceptionForHR',
  'UnsafeAddrOfPinnedArrayElement',
  'WriteByte',
  'WriteInt16',
  'WriteInt32',
  'WriteInt64',
  'WriteIntPtr',
  'ZeroFreeBSTR',
  'ZeroFreeCoTaskMemAnsi',
  'ZeroFreeCoTaskMemUnicode',
  'ZeroFreeGlobalAllocAnsi',
  'ZeroFreeGlobalAllocUnicode',
 ]

