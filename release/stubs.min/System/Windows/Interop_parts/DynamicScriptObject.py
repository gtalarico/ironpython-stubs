class DynamicScriptObject(DynamicObject,IDynamicMetaObjectProvider):
 """ Enables calls from a XAML browser application (XBAP) to the HTML window that hosts the application. """
 def ToString(self):
  """
  ToString(self: DynamicScriptObject) -> str
  
   Attempts to convert the script object to a string representation.
   Returns: A string representation of the script object,if the object can be converted; 
    otherwise,a string representation of the object's default property or method.
  """
  pass
 def TryGetIndex(self,binder,indexes,result):
  """
  TryGetIndex(self: DynamicScriptObject,binder: GetIndexBinder,indexes: Array[object]) -> (bool,object)
  
   Gets an indexed value from the script object by using the first index value 
    from the indexes collection.
  
  
   binder: The binder provided by the call site.
   indexes: The index to be retrieved.
   Returns: Always returns true.
  """
  pass
 def TryGetMember(self,binder,result):
  """
  TryGetMember(self: DynamicScriptObject,binder: GetMemberBinder) -> (bool,object)
  
   Gets an member value from the script object.
  
   binder: The binder provided by the call site.
   Returns: Always returns true.
  """
  pass
 def TryInvoke(self,binder,args,result):
  """
  TryInvoke(self: DynamicScriptObject,binder: InvokeBinder,args: Array[object]) -> (bool,object)
  
   Calls the default script method.
  
   binder: The binder provided by the call site.
   args: The arguments to pass to the default method.
   Returns: Always return true.
  """
  pass
 def TryInvokeMember(self,binder,args,result):
  """
  TryInvokeMember(self: DynamicScriptObject,binder: InvokeMemberBinder,args: Array[object]) -> (bool,object)
  
   Calls a method on the script object.
  
   binder: The binder provided by the call site.
   args: The arguments to pass to the default method.
   Returns: Always return true.
  """
  pass
 def TrySetIndex(self,binder,indexes,value):
  """
  TrySetIndex(self: DynamicScriptObject,binder: SetIndexBinder,indexes: Array[object],value: object) -> bool
  
   Sets a member on the script object by using the first index specified in the 
    indexes collection.
  
  
   binder: The binder provided by the call site.
   indexes: The index to be retrieved.
   value: The method result
   Returns: Always returns true.
  """
  pass
 def TrySetMember(self,binder,value):
  """
  TrySetMember(self: DynamicScriptObject,binder: SetMemberBinder,value: object) -> bool
  
   Sets a member on the script object to the specified value.
  
   binder: The binder provided by the call site.
   value: The value to set for the member.
   Returns: Always returns true.
  """
  pass
 def __dir__(self,*args):
  """ __dir__(self: IDynamicMetaObjectProvider) -> list """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
