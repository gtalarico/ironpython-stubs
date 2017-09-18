class UCOMIBindCtx:
 """ Use System.Runtime.InteropServices.ComTypes.BIND_OPTS instead. """
 def EnumObjectParam(self,ppenum):
  """
  EnumObjectParam(self: UCOMIBindCtx) -> UCOMIEnumString

  

   Enumerate the strings which are the keys of the internally-maintained table of contextual object 

    parameters.
  """
  pass
 def GetBindOptions(self,pbindopts):
  """
  GetBindOptions(self: UCOMIBindCtx,pbindopts: BIND_OPTS) -> BIND_OPTS

  

   Return the current binding options stored in this bind context.

  

   pbindopts: A pointer to the structure to receive the binding options.
  """
  pass
 def GetObjectParam(self,pszKey,ppunk):
  """
  GetObjectParam(self: UCOMIBindCtx,pszKey: str) -> object

  

   Lookup the given key in the internally-maintained table of contextual object parameters and 

    return the corresponding object,if one exists.

  

  

   pszKey: The name of the object to search for.
  """
  pass
 def GetRunningObjectTable(self,pprot):
  """
  GetRunningObjectTable(self: UCOMIBindCtx) -> UCOMIRunningObjectTable

  

   Return access to the Running Object Table (ROT) relevant to this binding process.
  """
  pass
 def RegisterObjectBound(self,punk):
  """
  RegisterObjectBound(self: UCOMIBindCtx,punk: object)

   Register the passed object as one of the objects that has been bound during a moniker operation 

    and which should be released when it is complete.

  

  

   punk: The object to register for release.
  """
  pass
 def RegisterObjectParam(self,pszKey,punk):
  """
  RegisterObjectParam(self: UCOMIBindCtx,pszKey: str,punk: object)

   Register the given object pointer under the specified name in the internally-maintained table of 

    object pointers.

  

  

   pszKey: The name to register punk with.

   punk: The object to register.
  """
  pass
 def ReleaseBoundObjects(self):
  """
  ReleaseBoundObjects(self: UCOMIBindCtx)

   Releases all the objects currently registered with the bind context by 

    System.Runtime.InteropServices.UCOMIBindCtx.RegisterObjectBound(System.Object).
  """
  pass
 def RevokeObjectBound(self,punk):
  """
  RevokeObjectBound(self: UCOMIBindCtx,punk: object)

   Removes the object from the set of registered objects that need to be released.

  

   punk: The object to unregister for release.
  """
  pass
 def RevokeObjectParam(self,pszKey):
  """
  RevokeObjectParam(self: UCOMIBindCtx,pszKey: str)

   Revoke the registration of the object currently found under this key in the 

    internally-maintained table of contextual object parameters,if any such key is currently 

    registered.

  

  

   pszKey: The key to unregister.
  """
  pass
 def SetBindOptions(self,pbindopts):
  """
  SetBindOptions(self: UCOMIBindCtx,pbindopts: BIND_OPTS) -> BIND_OPTS

  

   Store in the bind context a block of parameters that will apply to later UCOMIMoniker operations 

    using this bind context.

  

  

   pbindopts: The structure containing the binding options to set.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
