class RuntimeEnvironment(object):
 """
 Provides a collection of static methods that return information about the common language runtime environment.

 

 RuntimeEnvironment()
 """
 @staticmethod
 def FromGlobalAccessCache(a):
  """
  FromGlobalAccessCache(a: Assembly) -> bool

  

   Tests whether the specified assembly is loaded in the global assembly cache.

  

   a: The assembly to test.

   Returns: true if the assembly is loaded in the global assembly cache; otherwise,false.
  """
  pass
 @staticmethod
 def GetRuntimeDirectory():
  """
  GetRuntimeDirectory() -> str

  

   Returns the directory where the common language runtime is installed.

   Returns: A string that contains the path to the directory where the common language runtime is installed.
  """
  pass
 @staticmethod
 def GetRuntimeInterfaceAsIntPtr(clsid,riid):
  """
  GetRuntimeInterfaceAsIntPtr(clsid: Guid,riid: Guid) -> IntPtr

  

   Returns the specified interface on the specified class.

  

   clsid: The identifier for the desired class.

   riid: The identifier for the desired interface.

   Returns: An unmanaged pointer to the requested interface.
  """
  pass
 @staticmethod
 def GetRuntimeInterfaceAsObject(clsid,riid):
  """
  GetRuntimeInterfaceAsObject(clsid: Guid,riid: Guid) -> object

  

   Returns an instance of a type that represents a COM object by a pointer to its IUnknown 

    interface.

  

  

   clsid: The identifier for the desired class.

   riid: The identifier for the desired interface.

   Returns: An object that represents the specified unmanaged COM object.
  """
  pass
 @staticmethod
 def GetSystemVersion():
  """
  GetSystemVersion() -> str

  

   Gets the version number of the common language runtime that is running the current process.

   Returns: A string containing the version number of the common language runtime.
  """
  pass
 SystemConfigurationFile='C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\config\\machine.config'

