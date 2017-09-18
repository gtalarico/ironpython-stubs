class QualifiedAce(KnownAce):
 """ Represents an Access Control Entry (ACE) that contains a qualifier. The qualifier,represented by an System.Security.AccessControl.AceQualifier object,specifies whether the ACE allows access,denies access,causes system audits,or causes system alarms. The System.Security.AccessControl.QualifiedAce class is the abstract base class for the System.Security.AccessControl.CommonAce and System.Security.AccessControl.ObjectAce classes. """
 def GetOpaque(self):
  """
  GetOpaque(self: QualifiedAce) -> Array[Byte]

  

   Returns the opaque callback data associated with this System.Security.AccessControl.QualifiedAce 

    object.

  

   Returns: An array of byte values that represents the opaque callback data associated with this 

    System.Security.AccessControl.QualifiedAce object.
  """
  pass
 def SetOpaque(self,opaque):
  """
  SetOpaque(self: QualifiedAce,opaque: Array[Byte])

   Sets the opaque callback data associated with this System.Security.AccessControl.QualifiedAce 

    object.

  

  

   opaque: An array of byte values that represents the opaque callback data for this 

    System.Security.AccessControl.QualifiedAce object.
  """
  pass
 AceQualifier=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies whether the ACE allows access,denies access,causes system audits,or causes system alarms.



Get: AceQualifier(self: QualifiedAce) -> AceQualifier



"""

 IsCallback=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether this System.Security.AccessControl.QualifiedAce object contains callback data.



Get: IsCallback(self: QualifiedAce) -> bool



"""

 OpaqueLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the length of the opaque callback data associated with this System.Security.AccessControl.QualifiedAce object. This property is valid only for callback Access Control Entries (ACEs).



Get: OpaqueLength(self: QualifiedAce) -> int



"""


