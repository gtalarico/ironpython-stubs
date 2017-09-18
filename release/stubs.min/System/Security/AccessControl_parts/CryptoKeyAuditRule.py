class CryptoKeyAuditRule(AuditRule):
 """
 Represents an audit rule for a cryptographic key. An audit rule represents a combination of a user's identity and an access mask. An audit rule also contains information about the how the rule is inherited by child objects,how that inheritance is propagated,and for what conditions it is audited.

 

 CryptoKeyAuditRule(identity: IdentityReference,cryptoKeyRights: CryptoKeyRights,flags: AuditFlags)

 CryptoKeyAuditRule(identity: str,cryptoKeyRights: CryptoKeyRights,flags: AuditFlags)
 """
 @staticmethod
 def __new__(self,identity,cryptoKeyRights,flags):
  """
  __new__(cls: type,identity: IdentityReference,cryptoKeyRights: CryptoKeyRights,flags: AuditFlags)

  __new__(cls: type,identity: str,cryptoKeyRights: CryptoKeyRights,flags: AuditFlags)
  """
  pass
 AccessMask=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the access mask for this rule.



"""

 CryptoKeyRights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cryptographic key operation for which this audit rule generates audits.



Get: CryptoKeyRights(self: CryptoKeyAuditRule) -> CryptoKeyRights



"""


