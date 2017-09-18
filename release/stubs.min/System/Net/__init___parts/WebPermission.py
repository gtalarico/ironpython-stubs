class WebPermission(CodeAccessPermission,IPermission,ISecurityEncodable,IStackWalk,IUnrestrictedPermission):
 """
 Controls rights to access HTTP Internet resources.

 

 WebPermission(state: PermissionState)

 WebPermission()

 WebPermission(access: NetworkAccess,uriRegex: Regex)

 WebPermission(access: NetworkAccess,uriString: str)
 """
 def AddPermission(self,access,*__args):
  """
  AddPermission(self: WebPermission,access: NetworkAccess,uriRegex: Regex)

   Adds the specified URI with the specified access rights to the current System.Net.WebPermission.

  

   access: A NetworkAccess that specifies the access rights that are granted to the URI.

   uriRegex: A regular expression that describes the set of URIs to which access rights are granted.

  AddPermission(self: WebPermission,access: NetworkAccess,uriString: str)

   Adds the specified URI string with the specified access rights to the current 

    System.Net.WebPermission.

  

  

   access: A System.Net.NetworkAccess that specifies the access rights that are granted to the URI.

   uriString: A string that describes the URI to which access rights are granted.
  """
  pass
 def Copy(self):
  """
  Copy(self: WebPermission) -> IPermission

  

   Creates a copy of a System.Net.WebPermission.

   Returns: A new instance of the System.Net.WebPermission class that has the same values as the original.
  """
  pass
 def FromXml(self,securityElement):
  """
  FromXml(self: WebPermission,securityElement: SecurityElement)

   Reconstructs a System.Net.WebPermission from an XML encoding.

  

   securityElement: The XML encoding from which to reconstruct the System.Net.WebPermission.
  """
  pass
 def Intersect(self,target):
  """
  Intersect(self: WebPermission,target: IPermission) -> IPermission

  

   Returns the logical intersection of two System.Net.WebPermission instances.

  

   target: The System.Net.WebPermission to compare with the current instance.

   Returns: A new System.Net.WebPermission that represents the intersection of the current instance and the 

    target parameter. If the intersection is empty,the method returns null.
  """
  pass
 def IsSubsetOf(self,target):
  """
  IsSubsetOf(self: WebPermission,target: IPermission) -> bool

  

   Determines whether the current System.Net.WebPermission is a subset of the specified object.

  

   target: The System.Net.WebPermission to compare to the current System.Net.WebPermission.

   Returns: true if the current instance is a subset of the target parameter; otherwise,false. If the 

    target is null,the method returns true for an empty current permission that is not unrestricted 

    and false otherwise.
  """
  pass
 def IsUnrestricted(self):
  """
  IsUnrestricted(self: WebPermission) -> bool

  

   Checks the overall permission state of the System.Net.WebPermission.

   Returns: true if the System.Net.WebPermission was created with the 

    System.Security.Permissions.PermissionState.UnrestrictedSystem.Security.Permissions.PermissionSta

    te; otherwise,false.
  """
  pass
 def ToXml(self):
  """
  ToXml(self: WebPermission) -> SecurityElement

  

   Creates an XML encoding of a System.Net.WebPermission and its current state.

   Returns: A System.Security.SecurityElement that contains an XML-encoded representation of the 

    System.Net.WebPermission,including state information.
  """
  pass
 def Union(self,target):
  """
  Union(self: WebPermission,target: IPermission) -> IPermission

  

   Returns the logical union between two instances of the System.Net.WebPermission class.

  

   target: The System.Net.WebPermission to combine with the current System.Net.WebPermission.

   Returns: A System.Net.WebPermission that represents the union of the current instance and the target 

    parameter. If either WebPermission is System.Security.Permissions.PermissionState.Unrestricted,

    the method returns a System.Net.WebPermission that is 

    System.Security.Permissions.PermissionState.Unrestricted. If the target is null,the method 

    returns a copy of the current System.Net.WebPermission.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,state: PermissionState)

  __new__(cls: type)

  __new__(cls: type,access: NetworkAccess,uriRegex: Regex)

  __new__(cls: type,access: NetworkAccess,uriString: str)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AcceptList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property returns an enumeration of a single accept permissions held by this System.Net.WebPermission. The possible objects types contained in the returned enumeration are System.String and System.Text.RegularExpressions.Regex.



Get: AcceptList(self: WebPermission) -> IEnumerator



"""

 ConnectList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property returns an enumeration of a single connect permissions held by this System.Net.WebPermission. The possible objects types contained in the returned enumeration are System.String and System.Text.RegularExpressions.Regex.



Get: ConnectList(self: WebPermission) -> IEnumerator



"""


