class IRegistrationServices:
 """ Provides a set of services for registering and unregistering managed assemblies for use from COM. """
 def GetManagedCategoryGuid(self):
  """
  GetManagedCategoryGuid(self: IRegistrationServices) -> Guid

  

   Returns the GUID of the COM category that contains the managed classes.

   Returns: The GUID of the COM category that contains the managed classes.
  """
  pass
 def GetProgIdForType(self,type):
  """
  GetProgIdForType(self: IRegistrationServices,type: Type) -> str

  

   Retrieves the COM ProgID for a specified type.

  

   type: The type whose ProgID is being requested.

   Returns: The ProgID for the specified type.
  """
  pass
 def GetRegistrableTypesInAssembly(self,assembly):
  """
  GetRegistrableTypesInAssembly(self: IRegistrationServices,assembly: Assembly) -> Array[Type]

  

   Retrieves a list of classes in an assembly that would be registered by a call to 

    System.Runtime.InteropServices.IRegistrationServices.RegisterAssembly(System.Reflection.Assembly,

    System.Runtime.InteropServices.AssemblyRegistrationFlags).

  

  

   assembly: The assembly to search for classes.

   Returns: A System.Type array containing a list of classes in assembly.
  """
  pass
 def RegisterAssembly(self,assembly,flags):
  """
  RegisterAssembly(self: IRegistrationServices,assembly: Assembly,flags: AssemblyRegistrationFlags) -> bool

  

   Registers the classes in a managed assembly to enable creation from COM.

  

   assembly: The assembly to be registered.

   flags: An System.Runtime.InteropServices.AssemblyRegistrationFlags value indicating any special 

    settings needed when registering assembly.

  

   Returns: true if assembly contains types that were successfully registered; otherwise false if the 

    assembly contains no eligible types.
  """
  pass
 def RegisterTypeForComClients(self,type,g):
  """
  RegisterTypeForComClients(self: IRegistrationServices,type: Type,g: Guid) -> Guid

  

   Registers the specified type with COM using the specified GUID.

  

   type: The type to be registered for use from COM.

   g: GUID used to register the specified type.
  """
  pass
 def TypeRepresentsComType(self,type):
  """
  TypeRepresentsComType(self: IRegistrationServices,type: Type) -> bool

  

   Determines whether the specified type is a COM type.

  

   type: The type to determine if it is a COM type.

   Returns: true if the specified type is a COM type; otherwise false.
  """
  pass
 def TypeRequiresRegistration(self,type):
  """
  TypeRequiresRegistration(self: IRegistrationServices,type: Type) -> bool

  

   Determines whether the specified type requires registration.

  

   type: The type to check for COM registration requirements.

   Returns: true if the type must be registered for use from COM; otherwise false.
  """
  pass
 def UnregisterAssembly(self,assembly):
  """
  UnregisterAssembly(self: IRegistrationServices,assembly: Assembly) -> bool

  

   Unregisters the classes in a managed assembly.

  

   assembly: The assembly to be unregistered.

   Returns: true if assembly contains types that were successfully unregistered; otherwise false if the 

    assembly contains no eligible types.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
