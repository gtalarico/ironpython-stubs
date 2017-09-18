class WebExceptionStatus(Enum,IComparable,IFormattable,IConvertible):
 """
 Defines status codes for the System.Net.WebException class.

 

 enum WebExceptionStatus,values: CacheEntryNotFound (18),ConnectFailure (2),ConnectionClosed (8),KeepAliveFailure (12),MessageLengthLimitExceeded (17),NameResolutionFailure (1),Pending (13),PipelineFailure (5),ProtocolError (7),ProxyNameResolutionFailure (15),ReceiveFailure (3),RequestCanceled (6),RequestProhibitedByCachePolicy (19),RequestProhibitedByProxy (20),SecureChannelFailure (10),SendFailure (4),ServerProtocolViolation (11),Success (0),Timeout (14),TrustFailure (9),UnknownError (16)
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
 CacheEntryNotFound=None
 ConnectFailure=None
 ConnectionClosed=None
 KeepAliveFailure=None
 MessageLengthLimitExceeded=None
 NameResolutionFailure=None
 Pending=None
 PipelineFailure=None
 ProtocolError=None
 ProxyNameResolutionFailure=None
 ReceiveFailure=None
 RequestCanceled=None
 RequestProhibitedByCachePolicy=None
 RequestProhibitedByProxy=None
 SecureChannelFailure=None
 SendFailure=None
 ServerProtocolViolation=None
 Success=None
 Timeout=None
 TrustFailure=None
 UnknownError=None
 value__=None

