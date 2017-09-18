class ServicePoint(object):
 """ Provides connection management for HTTP connections. """
 def CloseConnectionGroup(self,connectionGroupName):
  """
  CloseConnectionGroup(self: ServicePoint,connectionGroupName: str) -> bool

  

   Removes the specified connection group from this System.Net.ServicePoint object.

  

   connectionGroupName: The name of the connection group that contains the connections to close and remove from this 

    service point.

  

   Returns: A System.Boolean value that indicates whether the connection group was closed.
  """
  pass
 def SetTcpKeepAlive(self,enabled,keepAliveTime,keepAliveInterval):
  """
  SetTcpKeepAlive(self: ServicePoint,enabled: bool,keepAliveTime: int,keepAliveInterval: int)

   Enables or disables the keep-alive option on a TCP connection.

  

   enabled: If set to true,then the TCP keep-alive option on a TCP connection will be enabled using the 

    specified keepAliveTime and keepAliveInterval values. If set to false,then the TCP keep-alive 

    option is disabled and the remaining parameters are ignored.The default value is false.

  

   keepAliveTime: Specifies the timeout,in milliseconds,with no activity until the first keep-alive packet is 

    sent. The value must be greater than 0.  If a value of less than or equal to zero is passed an 

    System.ArgumentOutOfRangeException is thrown.

  

   keepAliveInterval: Specifies the interval,in milliseconds,between when successive keep-alive packets are sent if 

    no acknowledgement is received.The value must be greater than 0.  If a value of less than or 

    equal to zero is passed an System.ArgumentOutOfRangeException is thrown.
  """
  pass
 Address=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Uniform Resource Identifier (URI) of the server that this System.Net.ServicePoint object connects to.



Get: Address(self: ServicePoint) -> Uri



"""

 BindIPEndPointDelegate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the delegate to associate a local System.Net.IPEndPoint with a System.Net.ServicePoint.



Get: BindIPEndPointDelegate(self: ServicePoint) -> BindIPEndPoint



Set: BindIPEndPointDelegate(self: ServicePoint)=value

"""

 Certificate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the certificate received for this System.Net.ServicePoint object.



Get: Certificate(self: ServicePoint) -> X509Certificate



"""

 ClientCertificate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the last client certificate sent to the server.



Get: ClientCertificate(self: ServicePoint) -> X509Certificate



"""

 ConnectionLeaseTimeout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of milliseconds after which an active System.Net.ServicePoint connection is closed.



Get: ConnectionLeaseTimeout(self: ServicePoint) -> int



Set: ConnectionLeaseTimeout(self: ServicePoint)=value

"""

 ConnectionLimit=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of connections allowed on this System.Net.ServicePoint object.



Get: ConnectionLimit(self: ServicePoint) -> int



Set: ConnectionLimit(self: ServicePoint)=value

"""

 ConnectionName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the connection name.



Get: ConnectionName(self: ServicePoint) -> str



"""

 CurrentConnections=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of open connections associated with this System.Net.ServicePoint object.



Get: CurrentConnections(self: ServicePoint) -> int



"""

 Expect100Continue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that determines whether 100-Continue behavior is used.



Get: Expect100Continue(self: ServicePoint) -> bool



Set: Expect100Continue(self: ServicePoint)=value

"""

 IdleSince=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the date and time that the System.Net.ServicePoint object was last connected to a host.



Get: IdleSince(self: ServicePoint) -> DateTime



"""

 MaxIdleTime=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the amount of time a connection associated with the System.Net.ServicePoint object can remain idle before the connection is closed.



Get: MaxIdleTime(self: ServicePoint) -> int



Set: MaxIdleTime(self: ServicePoint)=value

"""

 ProtocolVersion=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the version of the HTTP protocol that the System.Net.ServicePoint object uses.



Get: ProtocolVersion(self: ServicePoint) -> Version



"""

 ReceiveBufferSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the size of the receiving buffer for the socket used by this System.Net.ServicePoint.



Get: ReceiveBufferSize(self: ServicePoint) -> int



Set: ReceiveBufferSize(self: ServicePoint)=value

"""

 SupportsPipelining=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the System.Net.ServicePoint object supports pipelined connections.



Get: SupportsPipelining(self: ServicePoint) -> bool



"""

 UseNagleAlgorithm=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a System.Boolean value that determines whether the Nagle algorithm is used on connections managed by this System.Net.ServicePoint object.



Get: UseNagleAlgorithm(self: ServicePoint) -> bool



Set: UseNagleAlgorithm(self: ServicePoint)=value

"""


