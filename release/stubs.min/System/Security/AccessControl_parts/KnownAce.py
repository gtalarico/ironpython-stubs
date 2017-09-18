class KnownAce(GenericAce):
 """ Encapsulates all Access Control Entry (ACE) types currently defined by Microsoft Corporation. All System.Security.AccessControl.KnownAce objects contain a 32-bit access mask and a System.Security.Principal.SecurityIdentifier object. """
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the access mask for this System.Security.AccessControl.KnownAce object.



Get: AccessMask(self: KnownAce) -> int



Set: AccessMask(self: KnownAce)=value

"""

 SecurityIdentifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Security.Principal.SecurityIdentifier object associated with this System.Security.AccessControl.KnownAce object.



Get: SecurityIdentifier(self: KnownAce) -> SecurityIdentifier



Set: SecurityIdentifier(self: KnownAce)=value

"""


