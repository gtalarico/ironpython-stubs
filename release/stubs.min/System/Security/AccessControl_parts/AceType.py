class AceType(Enum,IComparable,IFormattable,IConvertible):
 """
 Defines the available access control entry (ACE) types.

 

 enum AceType,values: AccessAllowed (0),AccessAllowedCallback (9),AccessAllowedCallbackObject (11),AccessAllowedCompound (4),AccessAllowedObject (5),AccessDenied (1),AccessDeniedCallback (10),AccessDeniedCallbackObject (12),AccessDeniedObject (6),MaxDefinedAceType (16),SystemAlarm (3),SystemAlarmCallback (14),SystemAlarmCallbackObject (16),SystemAlarmObject (8),SystemAudit (2),SystemAuditCallback (13),SystemAuditCallbackObject (15),SystemAuditObject (7)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AccessAllowed=None
 AccessAllowedCallback=None
 AccessAllowedCallbackObject=None
 AccessAllowedCompound=None
 AccessAllowedObject=None
 AccessDenied=None
 AccessDeniedCallback=None
 AccessDeniedCallbackObject=None
 AccessDeniedObject=None
 MaxDefinedAceType=None
 SystemAlarm=None
 SystemAlarmCallback=None
 SystemAlarmCallbackObject=None
 SystemAlarmObject=None
 SystemAudit=None
 SystemAuditCallback=None
 SystemAuditCallbackObject=None
 SystemAuditObject=None
 value__=None

