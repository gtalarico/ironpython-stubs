class IPHostEntry(object):
 """
 Provides a container class for Internet host address information.

 

 IPHostEntry()
 """
 AddressList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a list of IP addresses that are associated with a host.



Get: AddressList(self: IPHostEntry) -> Array[IPAddress]



Set: AddressList(self: IPHostEntry)=value

"""

 Aliases=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a list of aliases that are associated with a host.



Get: Aliases(self: IPHostEntry) -> Array[str]



Set: Aliases(self: IPHostEntry)=value

"""

 HostName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the DNS name of the host.



Get: HostName(self: IPHostEntry) -> str



Set: HostName(self: IPHostEntry)=value

"""


