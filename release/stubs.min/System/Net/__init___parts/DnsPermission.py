class DnsPermission(CodeAccessPermission,IPermission,ISecurityEncodable,IStackWalk,IUnrestrictedPermission):
 """
 Controls rights to access Domain Name System (DNS) servers on the network.

 

 DnsPermission(state: PermissionState)
 """
 def Copy(self):
  """
  Copy(self: DnsPermission) -> IPermission

  

   Creates an identical copy of the current permission instance.

   Returns: A new instance of the System.Net.DnsPermission class that is an identical copy of the current 

    instance.
  """
  pass
 def FromXml(self,securityElement):
  """
  FromXml(self: DnsPermission,securityElement: SecurityElement)

   Reconstructs a System.Net.DnsPermission instance from an XML encoding.

  

   securityElement: The XML encoding to use to reconstruct the System.Net.DnsPermission instance.
  """
  pass
 def Intersect(self,target):
  """
  Intersect(self: DnsPermission,target: IPermission) -> IPermission

  

   Creates a permission instance that is the intersection of the current permission instance and 

    the specified permission instance.

  

  

   target: The System.Net.DnsPermission instance to intersect with the current instance.

   Returns: A System.Net.DnsPermission instance that represents the intersection of the current 

    System.Net.DnsPermission instance with the specified System.Net.DnsPermission instance,or null 

    if the intersection is empty. If both the current instance and target are unrestricted,this 

    method returns a new System.Net.DnsPermission instance that is unrestricted; otherwise,it 

    returns null.
  """
  pass
 def IsSubsetOf(self,target):
  """
  IsSubsetOf(self: DnsPermission,target: IPermission) -> bool

  

   Determines whether the current permission instance is a subset of the specified permission 

    instance.

  

  

   target: The second System.Net.DnsPermission instance to be tested for the subset relationship.

   Returns: false if the current instance is unrestricted and target is either null or unrestricted; 

    otherwise,true.
  """
  pass
 def IsUnrestricted(self):
  """
  IsUnrestricted(self: DnsPermission) -> bool

  

   Checks the overall permission state of the object.

   Returns: true if the System.Net.DnsPermission instance was created with 

    System.Security.Permissions.PermissionState.Unrestricted; otherwise,false.
  """
  pass
 def ToXml(self):
  """
  ToXml(self: DnsPermission) -> SecurityElement

  

   Creates an XML encoding of a System.Net.DnsPermission instance and its current state.

   Returns: A System.Security.SecurityElement instance that contains an XML-encoded representation of the 

    security object,including state information.
  """
  pass
 def Union(self,target):
  """
  Union(self: DnsPermission,target: IPermission) -> IPermission

  

   Creates a permission instance that is the union of the current permission instance and the 

    specified permission instance.

  

  

   target: The System.Net.DnsPermission instance to combine with the current instance.

   Returns: A System.Net.DnsPermission instance that represents the union of the current 

    System.Net.DnsPermission instance with the specified System.Net.DnsPermission instance. If 

    target is null,this method returns a copy of the current instance. If the current instance or 

    target is unrestricted,this method returns a System.Net.DnsPermission instance that is 

    unrestricted; otherwise,it returns a System.Net.DnsPermission instance that is restricted.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,state):
  """ __new__(cls: type,state: PermissionState) """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
