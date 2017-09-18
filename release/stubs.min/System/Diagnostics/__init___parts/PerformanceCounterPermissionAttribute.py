class PerformanceCounterPermissionAttribute(CodeAccessSecurityAttribute,_Attribute):
 """
 Allows declaritive performance counter permission checks.

 

 PerformanceCounterPermissionAttribute(action: SecurityAction)
 """
 def CreatePermission(self):
  """
  CreatePermission(self: PerformanceCounterPermissionAttribute) -> IPermission

  

   Creates the permission based on the requested access levels that are set through the 

    System.Diagnostics.PerformanceCounterPermissionAttribute.PermissionAccess property on the 

    attribute.

  

   Returns: An System.Security.IPermission that represents the created permission.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,action):
  """ __new__(cls: type,action: SecurityAction) """
  pass
 def __reduce_ex__(self,*args):
  pass
 CategoryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the performance counter category.



Get: CategoryName(self: PerformanceCounterPermissionAttribute) -> str



Set: CategoryName(self: PerformanceCounterPermissionAttribute)=value

"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the computer name for the performance counter.



Get: MachineName(self: PerformanceCounterPermissionAttribute) -> str



Set: MachineName(self: PerformanceCounterPermissionAttribute)=value

"""

 PermissionAccess=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the access levels used in the permissions request.



Get: PermissionAccess(self: PerformanceCounterPermissionAttribute) -> PerformanceCounterPermissionAccess



Set: PermissionAccess(self: PerformanceCounterPermissionAttribute)=value

"""


