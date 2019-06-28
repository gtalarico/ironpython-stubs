# encoding: utf-8
# module System.Web calls itself Web
# from System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AspNetHostingPermission:
 """
 Controls access permissions in ASP.NET hosted environments. This class cannot be inherited.
 
 AspNetHostingPermission(state: PermissionState)
 AspNetHostingPermission(level: AspNetHostingPermissionLevel)
 """
 def Copy(self):
  """
  Copy(self: AspNetHostingPermission) -> IPermission
  
   When implemented by a derived class,creates and returns an identical copy of the current 
    permission object.
  
   Returns: A copy of the current permission object.
  """
  pass
 def FromXml(self,securityElement):
  """
  FromXml(self: AspNetHostingPermission,securityElement: SecurityElement)
   Reconstructs a permission object with a specified state from an XML encoding.
  
   securityElement: The System.Security.SecurityElement containing the XML encoding to use to reconstruct the 
    permission object.
  """
  pass
 def Intersect(self,target):
  """
  Intersect(self: AspNetHostingPermission,target: IPermission) -> IPermission
  
   When implemented by a derived class,creates and returns a permission that is the 
    intersection of the current permission and the specified permission.
  
  
   target: A permission to combine with the current permission. It must be of the same type as the 
    current permission.
  
   Returns: An System.Security.IPermission that represents the intersection of the current permission 
    and the specified permission; otherwise,null if the intersection is empty.
  """
  pass
 def IsSubsetOf(self,target):
  """
  IsSubsetOf(self: AspNetHostingPermission,target: IPermission) -> bool
  
   Returns a value indicating whether the current permission is a subset of the specified 
    permission.
  
  
   target: The System.Security.IPermission to combine with the current permission. It must be of the 
    same type as the current System.Security.IPermission.
  
   Returns: true if the current System.Security.IPermission is a subset of the specified 
    System.Security.IPermission; otherwise,false.
  """
  pass
 def IsUnrestricted(self):
  """
  IsUnrestricted(self: AspNetHostingPermission) -> bool
  
   Returns a value indicating whether unrestricted access to the resource that is protected 
    by the current permission is allowed.
  
   Returns: true if unrestricted use of the resource protected by the permission is allowed; 
    otherwise,false.
  """
  pass
 def ToXml(self):
  """
  ToXml(self: AspNetHostingPermission) -> SecurityElement
  
   Creates an XML encoding of the permission object and its current state.
   Returns: A System.Security.SecurityElement containing the XML encoding of the permission object,
    including any state information.
  """
  pass
 def Union(self,target):
  """
  Union(self: AspNetHostingPermission,target: IPermission) -> IPermission
  
   Creates a permission that is the union of the current permission and the specified 
    permission.
  
  
   target: A permission to combine with the current permission. It must be of the same type as the 
    current permission.
  
   Returns: An System.Security.IPermission that represents the union of the current permission and 
    the specified permission.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,state: PermissionState)
  __new__(cls: type,level: AspNetHostingPermissionLevel)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current hosting permission level for an ASP.NET application.

Get: Level(self: AspNetHostingPermission) -> AspNetHostingPermissionLevel

Set: Level(self: AspNetHostingPermission)=value
"""



class AspNetHostingPermissionAttribute:
 """
 Allows security actions for System.Web.AspNetHostingPermission to be applied to code using declarative security. This class cannot be inherited.
 
 AspNetHostingPermissionAttribute(action: SecurityAction)
 """
 def CreatePermission(self):
  """
  CreatePermission(self: AspNetHostingPermissionAttribute) -> IPermission
  
   Creates a new System.Web.AspNetHostingPermission with the permission level previously set 
    by the System.Web.AspNetHostingPermissionAttribute.Level property.
  
   Returns: An System.Security.IPermission that is the new System.Web.AspNetHostingPermission.
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
 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current hosting permission level.

Get: Level(self: AspNetHostingPermissionAttribute) -> AspNetHostingPermissionLevel

Set: Level(self: AspNetHostingPermissionAttribute)=value
"""



class AspNetHostingPermissionLevel:
 """
 Specifies the trust level that is granted to an ASP.NET Web application.
 
 enum AspNetHostingPermissionLevel,values: High (500),Low (300),Medium (400),Minimal (200),None (100),Unrestricted (600)
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
 High=None
 Low=None
 Medium=None
 Minimal=None
 None_ =None
 Unrestricted=None
 value__=None


