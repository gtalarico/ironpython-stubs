class CryptoKeyAccessRule(AccessRule):
 """
 Represents an access rule for a cryptographic key. An access rule represents a combination of a user's identity,an access mask,and an access control type (allow or deny). An access rule object also contains information about the how the rule is inherited by child objects and how that inheritance is propagated.

 

 CryptoKeyAccessRule(identity: IdentityReference,cryptoKeyRights: CryptoKeyRights,type: AccessControlType)

 CryptoKeyAccessRule(identity: str,cryptoKeyRights: CryptoKeyRights,type: AccessControlType)
 """
 @staticmethod
 def __new__(self,identity,cryptoKeyRights,type):
  """
  __new__(cls: type,identity: IdentityReference,cryptoKeyRights: CryptoKeyRights,type: AccessControlType)

  __new__(cls: type,identity: str,cryptoKeyRights: CryptoKeyRights,type: AccessControlType)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 CryptoKeyRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cryptographic key operation to which this access rule controls access.



Get: CryptoKeyRights(self: CryptoKeyAccessRule) -> CryptoKeyRights



"""


