class PerformanceCounterPermissionEntry(object):
 """
 Defines the smallest unit of a code access security permission that is set for a System.Diagnostics.PerformanceCounter.

 

 PerformanceCounterPermissionEntry(permissionAccess: PerformanceCounterPermissionAccess,machineName: str,categoryName: str)
 """
 @staticmethod
 def __new__(self,permissionAccess,machineName,categoryName):
  """ __new__(cls: type,permissionAccess: PerformanceCounterPermissionAccess,machineName: str,categoryName: str) """
  pass
 CategoryName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the performance counter category (performance object).



Get: CategoryName(self: PerformanceCounterPermissionEntry) -> str



"""

 MachineName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the server on which the category of the performance counter resides.



Get: MachineName(self: PerformanceCounterPermissionEntry) -> str



"""

 PermissionAccess=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the permission access level of the entry.



Get: PermissionAccess(self: PerformanceCounterPermissionEntry) -> PerformanceCounterPermissionAccess



"""


