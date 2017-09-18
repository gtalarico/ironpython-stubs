class UCOMITypeLib:
 """ Use System.Runtime.InteropServices.ComTypes.ITypeLib instead. """
 def FindName(self,szNameBuf,lHashVal,ppTInfo,rgMemId,pcFound):
  """
  FindName(self: UCOMITypeLib,szNameBuf: str,lHashVal: int,pcFound: Int16) -> (Array[UCOMITypeInfo],Array[int],Int16)

  

   Finds occurrences of a type description in a type library.

  

   szNameBuf: The name to search for.

   lHashVal: A hash value to speed up the search,computed by the LHashValOfNameSys function. If lHashVal is 

    0,a value is computed.

  

   pcFound: On entry,indicates how many instances to look for. For example,pcFound=1 can be called to 

    find the first occurrence. The search stops when one instance is found.On exit,indicates the 

    number of instances that were found. If the in and out values of pcFound are identical,there 

    might be more type descriptions that contain the name.
  """
  pass
 def GetDocumentation(self,index,strName,strDocString,dwHelpContext,strHelpFile):
  """
  GetDocumentation(self: UCOMITypeLib,index: int) -> (str,str,int,str)

  

   Retrieves the library's documentation string,the complete Help file name and path,and the 

    context identifier for the library Help topic in the Help file.

  

  

   index: Index of the type description whose documentation is to be returned.
  """
  pass
 def GetLibAttr(self,ppTLibAttr):
  """
  GetLibAttr(self: UCOMITypeLib) -> IntPtr

  

   Retrieves the structure that contains the library's attributes.
  """
  pass
 def GetTypeComp(self,ppTComp):
  """
  GetTypeComp(self: UCOMITypeLib) -> UCOMITypeComp

  

   Enables a client compiler to bind to a library's types,variables,constants,and global 

    functions.
  """
  pass
 def GetTypeInfo(self,index,ppTI):
  """
  GetTypeInfo(self: UCOMITypeLib,index: int) -> UCOMITypeInfo

  

   Retrieves the specified type description in the library.

  

   index: Index of the UCOMITypeInfo interface to return.
  """
  pass
 def GetTypeInfoCount(self):
  """
  GetTypeInfoCount(self: UCOMITypeLib) -> int

  

   Returns the number of type descriptions in the type library.

   Returns: The number of type descriptions in the type library.
  """
  pass
 def GetTypeInfoOfGuid(self,guid,ppTInfo):
  """
  GetTypeInfoOfGuid(self: UCOMITypeLib,guid: Guid) -> (Guid,UCOMITypeInfo)

  

   Retrieves the type description that corresponds to the specified GUID.

  

   guid: IID of the interface of CLSID of the class whose type info is requested.
  """
  pass
 def GetTypeInfoType(self,index,pTKind):
  """
  GetTypeInfoType(self: UCOMITypeLib,index: int) -> TYPEKIND

  

   Retrieves the type of a type description.

  

   index: The index of the type description within the type library.
  """
  pass
 def IsName(self,szNameBuf,lHashVal):
  """
  IsName(self: UCOMITypeLib,szNameBuf: str,lHashVal: int) -> bool

  

   Indicates whether a passed-in string contains the name of a type or member described in the 

    library.

  

  

   szNameBuf: The string to test.

   lHashVal: The hash value of szNameBuf.

   Returns: true if szNameBuf was found in the type library; otherwise false.
  """
  pass
 def ReleaseTLibAttr(self,pTLibAttr):
  """
  ReleaseTLibAttr(self: UCOMITypeLib,pTLibAttr: IntPtr)

   Releases the System.Runtime.InteropServices.TYPELIBATTR originally obtained from 

    System.Runtime.InteropServices.UCOMITypeLib.GetLibAttr(System.IntPtr@).

  

  

   pTLibAttr: The TLIBATTR to release.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
