class DnsPermissionAttribute(CodeAccessSecurityAttribute):
 """
 Specifies permission to request information from Domain Name Servers.
 
 DnsPermissionAttribute(action: SecurityAction)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DnsPermissionAttribute()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CreatePermission(self):
  """
  CreatePermission(self: DnsPermissionAttribute) -> IPermission
  
   Creates and returns a new instance of the System.Net.DnsPermission class.
   Returns: A System.Net.DnsPermission that corresponds to the security declaration.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,action):
  """ __new__(cls: type,action: SecurityAction) """
  pass
 def __reduce_ex__(self,*args):
  pass
