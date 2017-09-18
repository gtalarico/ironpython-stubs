class AuthorizationRule(object):
 """ Determines access to securable objects. The derived classes System.Security.AccessControl.AccessRule and System.Security.AccessControl.AuditRule offer specializations for access and audit functionality. """
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,identity: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags) """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 IdentityReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Security.Principal.IdentityReference to which this rule applies.



Get: IdentityReference(self: AuthorizationRule) -> IdentityReference



"""

 InheritanceFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of flags that determine how this rule is inherited by child objects.



Get: InheritanceFlags(self: AuthorizationRule) -> InheritanceFlags



"""

 IsInherited=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this rule is explicitly set or is inherited from a parent container object.



Get: IsInherited(self: AuthorizationRule) -> bool



"""

 PropagationFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the propagation flags,which determine how inheritance of this rule is propagated to child objects. This property is significant only when the value of the System.Security.AccessControl.InheritanceFlags enumeration is not System.Security.AccessControl.InheritanceFlags.None.



Get: PropagationFlags(self: AuthorizationRule) -> PropagationFlags



"""


