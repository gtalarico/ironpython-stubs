class EventLogPermissionEntry(object):
 """
 Defines the smallest unit of a code access security permission that is set for an System.Diagnostics.EventLog.

 

 EventLogPermissionEntry(permissionAccess: EventLogPermissionAccess,machineName: str)
 """
 @staticmethod
 def __new__(self,permissionAccess,machineName):
  """ __new__(cls: type,permissionAccess: EventLogPermissionAccess,machineName: str) """
  pass
 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the computer on which to read or write events.



Get: MachineName(self: EventLogPermissionEntry) -> str



"""

 PermissionAccess=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the permission access levels used in the permissions request.



Get: PermissionAccess(self: EventLogPermissionEntry) -> EventLogPermissionAccess



"""


