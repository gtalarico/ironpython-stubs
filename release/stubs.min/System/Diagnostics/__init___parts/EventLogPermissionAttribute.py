class EventLogPermissionAttribute(CodeAccessSecurityAttribute,_Attribute):
 """
 Allows declaritive permission checks for event logging.

 

 EventLogPermissionAttribute(action: SecurityAction)
 """
 def CreatePermission(self):
  """
  CreatePermission(self: EventLogPermissionAttribute) -> IPermission

  

   Creates the permission based on the System.Diagnostics.EventLogPermissionAttribute.MachineName 

    property and the requested access levels that are set through the 

    System.Diagnostics.EventLogPermissionAttribute.PermissionAccess property on the attribute.

  

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
 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the computer on which events might be read.



Get: MachineName(self: EventLogPermissionAttribute) -> str



Set: MachineName(self: EventLogPermissionAttribute)=value

"""

 PermissionAccess=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the access levels used in the permissions request.



Get: PermissionAccess(self: EventLogPermissionAttribute) -> EventLogPermissionAccess



Set: PermissionAccess(self: EventLogPermissionAttribute)=value

"""


