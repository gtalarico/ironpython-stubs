class RegistrationServices(object,IRegistrationServices):
 """
 Provides a set of services for registering and unregistering managed assemblies for use from COM.

 

 RegistrationServices()
 """
 def GetManagedCategoryGuid(self):
  """
  GetManagedCategoryGuid(self: RegistrationServices) -> Guid

  

   Returns the GUID of the COM category that contains the managed classes.

   Returns: The GUID of the COM category that contains the managed classes.
  """
  pass
 def GetProgIdForType(self,type):
  """
  GetProgIdForType(self: RegistrationServices,type: Type) -> str

  

   Retrieves the COM ProgID for the specified type.

  

   type: The type corresponding to the ProgID that is being requested.

   Returns: The ProgID for the specified type.
  """
  pass
 def GetRegistrableTypesInAssembly(self,assembly):
  """
  GetRegistrableTypesInAssembly(self: RegistrationServices,assembly: Assembly) -> Array[Type]

  

   Retrieves a list of classes in an assembly that would be registered by a call to 

    System.Runtime.InteropServices.RegistrationServices.RegisterAssembly(System.Reflection.Assembly,S

    ystem.Runtime.InteropServices.AssemblyRegistrationFlags).

  

  

   assembly: The assembly to search for classes.

   Returns: A System.Type array containing a list of classes in assembly.
  """
  pass
 def RegisterAssembly(self,assembly,flags):
  """
  RegisterAssembly(self: RegistrationServices,assembly: Assembly,flags: AssemblyRegistrationFlags) -> bool

  

   Registers the classes in a managed assembly to enable creation from COM.

  

   assembly: The assembly to be registered.

   flags: An System.Runtime.InteropServices.AssemblyRegistrationFlags value indicating any special 

    settings used when registering assembly.

  

   Returns: true if assembly contains types that were successfully registered; otherwise false if the 

    assembly contains no eligible types.
  """
  pass
 def RegisterTypeForComClients(self,type,*__args):
  """
  RegisterTypeForComClients(self: RegistrationServices,type: Type,classContext: RegistrationClassContext,flags: RegistrationConnectionType) -> int

  

   Registers the specified type with COM using the specified execution context and connection type.

  

   type: The System.Type object to register for use from COM.

   classContext: One of the System.Runtime.InteropServices.RegistrationClassContext values that indicates the 

    context in which the executable code will be run.

  

   flags: One of the System.Runtime.InteropServices.RegistrationConnectionType values that specifies how 

    connections are made to the class object.

  

   Returns: An integer that represents a cookie value.

  RegisterTypeForComClients(self: RegistrationServices,type: Type,g: Guid) -> Guid

  

   Registers the specified type with COM using the specified GUID.

  

   type: The System.Type to be registered for use from COM.

   g: The System.Guid used to register the specified type.
  """
  pass
 def TypeRepresentsComType(self,type):
  """
  TypeRepresentsComType(self: RegistrationServices,type: Type) -> bool

  

   Indicates whether a type is marked with the System.Runtime.InteropServices.ComImportAttribute,

    or derives from a type marked with the System.Runtime.InteropServices.ComImportAttribute and 

    shares the same GUID as the parent.

  

  

   type: The type to check for being a COM type.

   Returns: true if a type is marked with the System.Runtime.InteropServices.ComImportAttribute,or derives 

    from a type marked with the System.Runtime.InteropServices.ComImportAttribute and shares the 

    same GUID as the parent; otherwise false.
  """
  pass
 def TypeRequiresRegistration(self,type):
  """
  TypeRequiresRegistration(self: RegistrationServices,type: Type) -> bool

  

   Determines whether the specified type requires registration.

  

   type: The type to check for COM registration requirements.

   Returns: true if the type must be registered for use from COM; otherwise false.
  """
  pass
 def UnregisterAssembly(self,assembly):
  """
  UnregisterAssembly(self: RegistrationServices,assembly: Assembly) -> bool

  

   Unregisters the classes in a managed assembly.

  

   assembly: The assembly to be unregistered.

   Returns: true if assembly contains types that were successfully unregistered; otherwise false if the 

    assembly contains no eligible types.
  """
  pass
 def UnregisterTypeForComClients(self,cookie):
  """
  UnregisterTypeForComClients(self: RegistrationServices,cookie: int)

   Removes references to a type registered with the 

    System.Runtime.InteropServices.RegistrationServices.RegisterTypeForComClients(System.Type,System.

    Runtime.InteropServices.RegistrationClassContext,System.Runtime.InteropServices.RegistrationConne

    ctionType) method.

  

  

   cookie: The cookie value returned by a previous call to the 

    System.Runtime.InteropServices.RegistrationServices.RegisterTypeForComClients(System.Type,System.

    Runtime.InteropServices.RegistrationClassContext,System.Runtime.InteropServices.RegistrationConne

    ctionType) method overload.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
