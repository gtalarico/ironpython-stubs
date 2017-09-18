class ICertificatePolicy:
 """ Validates a server certificate. """
 def CheckValidationResult(self,srvPoint,certificate,request,certificateProblem):
  """
  CheckValidationResult(self: ICertificatePolicy,srvPoint: ServicePoint,certificate: X509Certificate,request: WebRequest,certificateProblem: int) -> bool

  

   Validates a server certificate.

  

   srvPoint: The System.Net.ServicePoint that will use the certificate.

   certificate: The certificate to validate.

   request: The request that received the certificate.

   certificateProblem: The problem that was encountered when using the certificate.

   Returns: true if the certificate should be honored; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
