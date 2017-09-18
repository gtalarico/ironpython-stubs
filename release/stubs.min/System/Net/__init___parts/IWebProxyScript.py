class IWebProxyScript:
 """ Provides the base interface to load and execute scripts for automatic proxy detection. """
 def Close(self):
  """
  Close(self: IWebProxyScript)

   Closes a script.
  """
  pass
 def Load(self,scriptLocation,script,helperType):
  """
  Load(self: IWebProxyScript,scriptLocation: Uri,script: str,helperType: Type) -> bool

  

   Loads a script.

  

   scriptLocation: Internal only.

   script: Internal only.

   helperType: Internal only.

   Returns: A System.Boolean indicating whether the script was successfully loaded.
  """
  pass
 def Run(self,url,host):
  """
  Run(self: IWebProxyScript,url: str,host: str) -> str

  

   Runs a script.

  

   url: Internal only.

   host: Internal only.

   Returns: A System.String.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
