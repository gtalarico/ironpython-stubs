class SocketAddress(object):
 """
 Stores serialized information from System.Net.EndPoint derived classes.

 

 SocketAddress(family: AddressFamily,size: int)

 SocketAddress(family: AddressFamily)
 """
 def Equals(self,comparand):
  """
  Equals(self: SocketAddress,comparand: object) -> bool

  

   Determines whether the specified System.Object is equal to the current System.Net.SocketAddress 

    instance.

  

  

   comparand: The specified System.Object to compare with the current System.Net.SocketAddress instance.

   Returns: true if the specified System.Object is equal to the current System.Object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: SocketAddress) -> int

  

   Serves as a hash function for a particular type,suitable for use in hashing algorithms and data 

    structures like a hash table.

  

   Returns: A hash code for the current System.Object.
  """
  pass
 def ToString(self):
  """
  ToString(self: SocketAddress) -> str

  

   Returns information about the socket address.

   Returns: A string that contains information about the System.Net.SocketAddress.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,family,size=None):
  """
  __new__(cls: type,family: AddressFamily)

  __new__(cls: type,family: AddressFamily,size: int)
  """
  pass
 def __ne__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 Family=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Net.Sockets.AddressFamily enumerated value of the current System.Net.SocketAddress.



Get: Family(self: SocketAddress) -> AddressFamily



"""

 Size=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the underlying buffer size of the System.Net.SocketAddress.



Get: Size(self: SocketAddress) -> int



"""


