class TypeLibConverter(object,ITypeLibConverter):
 """
 Provides a set of services that convert a managed assembly to a COM type library and vice versa.

 

 TypeLibConverter()
 """
 def ConvertAssemblyToTypeLib(self,assembly,strTypeLibName,flags,notifySink):
  """
  ConvertAssemblyToTypeLib(self: TypeLibConverter,assembly: Assembly,strTypeLibName: str,flags: TypeLibExporterFlags,notifySink: ITypeLibExporterNotifySink) -> object

  

   Converts an assembly to a COM type library.

  

   assembly: The assembly to convert.

   strTypeLibName: The file name of the resulting type library.

   flags: A System.Runtime.InteropServices.TypeLibExporterFlags value indicating any special settings.

   notifySink: The System.Runtime.InteropServices.ITypeLibExporterNotifySink interface implemented by the 

    caller.

  

   Returns: An object that implements the ITypeLib interface.
  """
  pass
 def ConvertTypeLibToAssembly(self,typeLib,asmFileName,flags,notifySink,publicKey,keyPair,*__args):
  """
  ConvertTypeLibToAssembly(self: TypeLibConverter,typeLib: object,asmFileName: str,flags: TypeLibImporterFlags,notifySink: ITypeLibImporterNotifySink,publicKey: Array[Byte],keyPair: StrongNameKeyPair,asmNamespace: str,asmVersion: Version) -> AssemblyBuilder

  

   Converts a COM type library to an assembly.

  

   typeLib: The object that implements the ITypeLib interface.

   asmFileName: The file name of the resulting assembly.

   flags: A System.Runtime.InteropServices.TypeLibImporterFlags value indicating any special settings.

   notifySink: System.Runtime.InteropServices.ITypeLibImporterNotifySink interface implemented by the caller.

   publicKey: A byte array containing the public key.

   keyPair: A System.Reflection.StrongNameKeyPair object containing the public and private cryptographic key 

    pair.

  

   asmNamespace: The namespace for the resulting assembly.

   asmVersion: The version of the resulting assembly. If null,the version of the type library is used.

   Returns: An System.Reflection.Emit.AssemblyBuilder object containing the converted type library.

  ConvertTypeLibToAssembly(self: TypeLibConverter,typeLib: object,asmFileName: str,flags: int,notifySink: ITypeLibImporterNotifySink,publicKey: Array[Byte],keyPair: StrongNameKeyPair,unsafeInterfaces: bool) -> AssemblyBuilder

  

   Converts a COM type library to an assembly.

  

   typeLib: The object that implements the ITypeLib interface.

   asmFileName: The file name of the resulting assembly.

   flags: A System.Runtime.InteropServices.TypeLibImporterFlags value indicating any special settings.

   notifySink: System.Runtime.InteropServices.ITypeLibImporterNotifySink interface implemented by the caller.

   publicKey: A byte array containing the public key.

   keyPair: A System.Reflection.StrongNameKeyPair object containing the public and private cryptographic key 

    pair.

  

   unsafeInterfaces: If true,the interfaces require link time checks for 

    System.Security.Permissions.SecurityPermissionFlag.UnmanagedCode permission. If false,the 

    interfaces require run time checks that require a stack walk and are more expensive,but help 

    provide greater protection.

  

   Returns: An System.Reflection.Emit.AssemblyBuilder object containing the converted type library.
  """
  pass
 def GetPrimaryInteropAssembly(self,g,major,minor,lcid,asmName,asmCodeBase):
  """
  GetPrimaryInteropAssembly(self: TypeLibConverter,g: Guid,major: int,minor: int,lcid: int) -> (bool,str,str)

  

   Gets the name and code base of a primary interop assembly for a specified type library.

  

   g: The GUID of the type library.

   major: The major version number of the type library.

   minor: The minor version number of the type library.

   lcid: The LCID of the type library.

   Returns: true if the primary interop assembly was found in the registry; otherwise false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
