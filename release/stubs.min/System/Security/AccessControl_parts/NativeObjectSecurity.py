class NativeObjectSecurity(CommonObjectSecurity):
 """ Provides the ability to control access to native objects without direct manipulation of Access Control Lists (ACLs). Native object types are defined by the System.Security.AccessControl.ResourceType enumeration. """
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """
  __new__(cls: type,isContainer: bool,resourceType: ResourceType)

  __new__(cls: type,isContainer: bool,resourceType: ResourceType,exceptionFromErrorCode: ExceptionFromErrorCode,exceptionContext: object)

  __new__(cls: type,isContainer: bool,resourceType: ResourceType,name: str,includeSections: AccessControlSections,exceptionFromErrorCode: ExceptionFromErrorCode,exceptionContext: object)

  __new__(cls: type,isContainer: bool,resourceType: ResourceType,name: str,includeSections: AccessControlSections)

  __new__(cls: type,isContainer: bool,resourceType: ResourceType,handle: SafeHandle,includeSections: AccessControlSections,exceptionFromErrorCode: ExceptionFromErrorCode,exceptionContext: object)

  __new__(cls: type,isContainer: bool,resourceType: ResourceType,handle: SafeHandle,includeSections: AccessControlSections)
  """
  pass
 AccessRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the access rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 AuditRulesModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the audit rules associated with this System.Security.AccessControl.ObjectSecurity object have been modified.



"""

 GroupModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the group associated with the securable object has been modified.



"""

 IsContainer=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a container object.



"""

 IsDS=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a Boolean value that specifies whether this System.Security.AccessControl.ObjectSecurity object is a directory object.



"""

 OwnerModified=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that specifies whether the owner of the securable object has been modified.



"""


 ExceptionFromErrorCode=None

