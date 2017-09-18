class ObjectAuditRule(AuditRule):
 """ Represents a combination of a user's identity,an access mask,and audit conditions. An System.Security.AccessControl.ObjectAuditRule object also contains information about the type of object to which the rule applies,the type of child object that can inherit the rule,how the rule is inherited by child objects,and how that inheritance is propagated. """
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,identity: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectType: Guid,inheritedObjectType: Guid,auditFlags: AuditFlags) """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 InheritedObjectType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of child object that can inherit the stem.Security.AccessControl.ObjectAuditRule object.



Get: InheritedObjectType(self: ObjectAuditRule) -> Guid



"""

 ObjectFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """System.Security.AccessControl.ObjectAuditRule.ObjectType and System.Security.AccessControl.ObjectAuditRule.InheritedObjectType properties of the stem.Security.AccessControl.ObjectAuditRule object contain valid values.



Get: ObjectFlags(self: ObjectAuditRule) -> ObjectAceFlags



"""

 ObjectType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of object to which the stem.Security.AccessControl.ObjectAuditRule applies.



Get: ObjectType(self: ObjectAuditRule) -> Guid



"""


