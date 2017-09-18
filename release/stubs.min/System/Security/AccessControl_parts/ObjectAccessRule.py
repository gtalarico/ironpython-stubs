class ObjectAccessRule(AccessRule):
 """ Represents a combination of a user's identity,an access mask,and an access control type (allow or deny). An System.Security.AccessControl.ObjectAccessRule object also contains information about the type of object to which the rule applies,the type of child object that can inherit the rule,how the rule is inherited by child objects,and how that inheritance is propagated. """
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,identity: IdentityReference,accessMask: int,isInherited: bool,inheritanceFlags: InheritanceFlags,propagationFlags: PropagationFlags,objectType: Guid,inheritedObjectType: Guid,type: AccessControlType) """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 InheritedObjectType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of child object that can inherit the stem.Security.AccessControl.ObjectAccessRule object.



Get: InheritedObjectType(self: ObjectAccessRule) -> Guid



"""

 ObjectFlags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets flags that specify if the System.Security.AccessControl.ObjectAccessRule.ObjectType and System.Security.AccessControl.ObjectAccessRule.InheritedObjectType properties of the stem.Security.AccessControl.ObjectAccessRule object contain valid values.



Get: ObjectFlags(self: ObjectAccessRule) -> ObjectAceFlags



"""

 ObjectType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of object to which the stem.Security.AccessControl.ObjectAccessRule applies.



Get: ObjectType(self: ObjectAccessRule) -> Guid



"""


