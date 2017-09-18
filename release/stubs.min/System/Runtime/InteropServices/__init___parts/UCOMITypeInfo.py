class UCOMITypeInfo:
 """ Use System.Runtime.InteropServices.ComTypes.ITypeInfo instead. """
 def AddressOfMember(self,memid,invKind,ppv):
  """
  AddressOfMember(self: UCOMITypeInfo,memid: int,invKind: INVOKEKIND) -> IntPtr

  

   Retrieves the addresses of static functions or variables,such as those defined in a DLL.

  

   memid: Member ID of the static member's address to retrieve.

   invKind: Specifies whether the member is a property,and if so,what kind.
  """
  pass
 def CreateInstance(self,pUnkOuter,riid,ppvObj):
  """
  CreateInstance(self: UCOMITypeInfo,pUnkOuter: object,riid: Guid) -> (Guid,object)

  

   Creates a new instance of a type that describes a component class (coclass).

  

   pUnkOuter: Object which acts as the controlling IUnknown.

   riid: The IID of the interface that the caller will use to communicate with the resulting object.
  """
  pass
 def GetContainingTypeLib(self,ppTLB,pIndex):
  """
  GetContainingTypeLib(self: UCOMITypeInfo) -> (UCOMITypeLib,int)

  

   Retrieves the type library that contains this type description and its index within that type 

    library.
  """
  pass
 def GetDllEntry(self,memid,invKind,pBstrDllName,pBstrName,pwOrdinal):
  """
  GetDllEntry(self: UCOMITypeInfo,memid: int,invKind: INVOKEKIND) -> (str,str,Int16)

  

   Retrieves a description or specification of an entry point for a function in a DLL.

  

   memid: ID of the member function whose DLL entry description is to be returned.

   invKind: Specifies the kind of member identified by memid.
  """
  pass
 def GetDocumentation(self,index,strName,strDocString,dwHelpContext,strHelpFile):
  """
  GetDocumentation(self: UCOMITypeInfo,index: int) -> (str,str,int,str)

  

   Retrieves the documentation string,the complete Help file name and path,and the context ID for 

    the Help topic for a specified type description.

  

  

   index: ID of the member whose documentation is to be returned.
  """
  pass
 def GetFuncDesc(self,index,ppFuncDesc):
  """
  GetFuncDesc(self: UCOMITypeInfo,index: int) -> IntPtr

  

   Retrieves the System.Runtime.InteropServices.FUNCDESC structure that contains information about 

    a specified function.

  

  

   index: Index of the function description to return.
  """
  pass
 def GetIDsOfNames(self,rgszNames,cNames,pMemId):
  """
  GetIDsOfNames(self: UCOMITypeInfo,rgszNames: Array[str],cNames: int) -> Array[int]

  

   Maps between member names and member IDs,and parameter names and parameter IDs.

  

   rgszNames: On succesful return,an array of names to map.

   cNames: Count of names to map.
  """
  pass
 def GetImplTypeFlags(self,index,pImplTypeFlags):
  """
  GetImplTypeFlags(self: UCOMITypeInfo,index: int) -> int

  

   Retrieves the System.Runtime.InteropServices.IMPLTYPEFLAGS value for one implemented interface 

    or base interface in a type description.

  

  

   index: Index of the implemented interface or base interface.
  """
  pass
 def GetMops(self,memid,pBstrMops):
  """
  GetMops(self: UCOMITypeInfo,memid: int) -> str

  

   Retrieves marshaling information.

  

   memid: The member ID that indicates which marshaling information is needed.
  """
  pass
 def GetNames(self,memid,rgBstrNames,cMaxNames,pcNames):
  """
  GetNames(self: UCOMITypeInfo,memid: int,cMaxNames: int) -> (Array[str],int)

  

   Retrieves the variable with the specified member ID (or the name of the property or method and 

    its parameters) that correspond to the specified function ID.

  

  

   memid: The ID of the member whose name (or names) is to be returned.

   cMaxNames: Length of the rgBstrNames array.
  """
  pass
 def GetRefTypeInfo(self,hRef,ppTI):
  """
  GetRefTypeInfo(self: UCOMITypeInfo,hRef: int) -> UCOMITypeInfo

  

   If a type description references other type descriptions,it retrieves the referenced type 

    descriptions.

  

  

   hRef: Handle to the referenced type description to return.
  """
  pass
 def GetRefTypeOfImplType(self,index,href):
  """
  GetRefTypeOfImplType(self: UCOMITypeInfo,index: int) -> int

  

   If a type description describes a COM class,it retrieves the type description of the 

    implemented interface types.

  

  

   index: Index of the implemented type whose handle is returned.
  """
  pass
 def GetTypeAttr(self,ppTypeAttr):
  """
  GetTypeAttr(self: UCOMITypeInfo) -> IntPtr

  

   Retrieves a System.Runtime.InteropServices.TYPEATTR structure that contains the attributes of 

    the type description.
  """
  pass
 def GetTypeComp(self,ppTComp):
  """
  GetTypeComp(self: UCOMITypeInfo) -> UCOMITypeComp

  

   Retrieves the ITypeComp interface for the type description,which enables a client compiler to 

    bind to the type description's members.
  """
  pass
 def GetVarDesc(self,index,ppVarDesc):
  """
  GetVarDesc(self: UCOMITypeInfo,index: int) -> IntPtr

  

   Retrieves a VARDESC structure that describes the specified variable.

  

   index: Index of the variable description to return.
  """
  pass
 def Invoke(self,pvInstance,memid,wFlags,pDispParams,pVarResult,pExcepInfo,puArgErr):
  """
  Invoke(self: UCOMITypeInfo,pvInstance: object,memid: int,wFlags: Int16,pDispParams: DISPPARAMS) -> (DISPPARAMS,object,EXCEPINFO,int)

  

   Invokes a method,or accesses a property of an object,that implements the interface described 

    by the type description.

  

  

   pvInstance: Reference to the interface described by this type description.

   memid: Identifies the interface member.

   wFlags: Flags describing the context of the invoke call.

   pDispParams: Reference to a structure that contains an array of arguments,an array of DISPIDs for named 

    arguments,and counts of the number of elements in each array.
  """
  pass
 def ReleaseFuncDesc(self,pFuncDesc):
  """
  ReleaseFuncDesc(self: UCOMITypeInfo,pFuncDesc: IntPtr)

   Releases a System.Runtime.InteropServices.FUNCDESC previously returned by 

    System.Runtime.InteropServices.UCOMITypeInfo.GetFuncDesc(System.Int32,System.IntPtr@).

  

  

   pFuncDesc: Reference to the FUNCDESC to release.
  """
  pass
 def ReleaseTypeAttr(self,pTypeAttr):
  """
  ReleaseTypeAttr(self: UCOMITypeInfo,pTypeAttr: IntPtr)

   Releases a System.Runtime.InteropServices.TYPEATTR previously returned by 

    System.Runtime.InteropServices.UCOMITypeInfo.GetTypeAttr(System.IntPtr@).

  

  

   pTypeAttr: Reference to the TYPEATTR to release.
  """
  pass
 def ReleaseVarDesc(self,pVarDesc):
  """
  ReleaseVarDesc(self: UCOMITypeInfo,pVarDesc: IntPtr)

   Releases a VARDESC previously returned by 

    System.Runtime.InteropServices.UCOMITypeInfo.GetVarDesc(System.Int32,System.IntPtr@).

  

  

   pVarDesc: Reference to the VARDESC to release.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
