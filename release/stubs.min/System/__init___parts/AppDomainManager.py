class AppDomainManager(MarshalByRefObject):
 """
 Provides a managed equivalent of an unmanaged host.

 

 AppDomainManager()
 """
 def CheckSecuritySettings(self,state):
  """
  CheckSecuritySettings(self: AppDomainManager,state: SecurityState) -> bool

  

   Indicates whether the specified operation is allowed in the application domain.

  

   state: A subclass of System.Security.SecurityState that identifies the operation whose security status 

    is requested.

  

   Returns: true if the host allows the operation specified by state to be performed in the application 

    domain; otherwise,false.
  """
  pass
 def CreateDomain(self,friendlyName,securityInfo,appDomainInfo):
  """
  CreateDomain(self: AppDomainManager,friendlyName: str,securityInfo: Evidence,appDomainInfo: AppDomainSetup) -> AppDomain

  

   Returns a new or existing application domain.

  

   friendlyName: The friendly name of the domain.

   securityInfo: An object that contains evidence mapped through the security policy to establish a top-of-stack 

    permission set.

  

   appDomainInfo: An object that contains application domain initialization information.

   Returns: A new or existing application domain.
  """
  pass
 def CreateDomainHelper(self,*args):
  """
  CreateDomainHelper(friendlyName: str,securityInfo: Evidence,appDomainInfo: AppDomainSetup) -> AppDomain

  

   Provides a helper method to create an application domain.

  

   friendlyName: The friendly name of the domain.

   securityInfo: An object that contains evidence mapped through the security policy to establish a top-of-stack 

    permission set.

  

   appDomainInfo: An object that contains application domain initialization information.

   Returns: A newly created application domain.
  """
  pass
 def InitializeNewDomain(self,appDomainInfo):
  """
  InitializeNewDomain(self: AppDomainManager,appDomainInfo: AppDomainSetup)

   Initializes the new application domain.

  

   appDomainInfo: An object that contains application domain initialization information.
  """
  pass
 ApplicationActivator=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the application activator that handles the activation of add-ins and manifest-based applications for the domain.



Get: ApplicationActivator(self: AppDomainManager) -> ApplicationActivator



"""

 EntryAssembly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the entry assembly for an application.



Get: EntryAssembly(self: AppDomainManager) -> Assembly



"""

 HostExecutionContextManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the host execution context manager that manages the flow of the execution context.



Get: HostExecutionContextManager(self: AppDomainManager) -> HostExecutionContextManager



"""

 HostSecurityManager=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the host security manager that participates in security decisions for the application domain.



Get: HostSecurityManager(self: AppDomainManager) -> HostSecurityManager



"""

 InitializationFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the initialization flags for custom application domain managers.



Get: InitializationFlags(self: AppDomainManager) -> AppDomainManagerInitializationOptions



Set: InitializationFlags(self: AppDomainManager)=value

"""


