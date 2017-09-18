class TransportContext(object):
 """ The System.Net.TransportContext class provides additional context about the underlying transport layer. """
 def GetChannelBinding(self,kind):
  """
  GetChannelBinding(self: TransportContext,kind: ChannelBindingKind) -> ChannelBinding

  

   Retrieves the requested channel binding.

  

   kind: The type of channel binding to retrieve.

   Returns: The requested System.Security.Authentication.ExtendedProtection.ChannelBinding,or null if the 

    channel binding is not supported by the current transport or by the operating system.
  """
  pass
 def GetTlsTokenBindings(self):
  """ GetTlsTokenBindings(self: TransportContext) -> IEnumerable[TokenBinding] """
  pass
