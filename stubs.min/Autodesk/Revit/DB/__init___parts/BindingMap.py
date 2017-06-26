class BindingMap(DefinitionBindingMap,IDisposable,IEnumerable):
 """
 The parameters BindingMap contains all the parameter bindings that exist in the
 Autodesk Revit project.
 """
 def Clear(self):
  """
  Clear(self: BindingMap)
   This method is used to remove all the items in the map.
  """
  pass
 def Contains(self,key):
  """
  Contains(self: BindingMap,key: Definition) -> bool
  
   The Contains method is used to check if the parameter binding exists for one 
    definition.
  
  
   key: A parameter definition which can be an existing definition or one from a shared 
    parameters file.
  """
  pass
 def Dispose(self):
  """ Dispose(self: BindingMap,A_0: bool) """
  pass
 def Erase(self,key):
  """
  Erase(self: BindingMap,key: Definition) -> int
  
   This method is used to erase one item in the map.
  """
  pass
 def Insert(self,key,item,parameterGroup=None):
  """
  Insert(self: BindingMap,key: Definition,item: Binding) -> bool
  
   Creates a new parameter binding between a parameter and a set of categories.
  
   key: A parameter definition which can be an existing definition or one from a shared 
    parameters file.
  
   item: An InstanceBinding or TypeBinding object which contains the set of categories 
    to which the parameter should be bound.
  
  Insert(self: BindingMap,key: Definition,item: Binding,parameterGroup: BuiltInParameterGroup) -> bool
  
   Creates a new parameter binding between a parameter and a set of categories in 
    a specified group.
  
  
   key: A parameter definition which can be an existing definition or one from a shared 
    parameters file.
  
   item: An InstanceBinding or TypeBinding object which contains the set of categories 
    to which the parameter should be bound.
  
   parameterGroup: The GroupID of the parameter definition.
  """
  pass
 def ReInsert(self,key,item,parameterGroup=None):
  """
  ReInsert(self: BindingMap,key: Definition,item: Binding) -> bool
  
   Removes an existing parameter and creates a new binding for a given parameter.
  
   key: A parameter definition which can be an existing definition or one from a shared 
    parameters file.
  
   item: An InstanceBinding or TypeBinding object which contains the set of categories 
    to which the parameter should be bound.
  
  ReInsert(self: BindingMap,key: Definition,item: Binding,parameterGroup: BuiltInParameterGroup) -> bool
  
   Removes an existing parameter and creates a new binding for a given parameter 
    in a specified group.
  
  
   key: A parameter definition which can be an existing definition or one from a shared 
    parameters file.
  
   item: An InstanceBinding or TypeBinding object which contains the set of categories 
    to which the parameter should be bound.
  
   parameterGroup: The GroupID of the parameter definition.
  """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def Remove(self,key):
  """
  Remove(self: BindingMap,key: Definition) -> bool
  
   The Remove method is used to remove a parameter binding.
  
   key: A parameter definition which can be an existing definition or one from a shared 
    parameters file.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
