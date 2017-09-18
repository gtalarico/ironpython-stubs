class CookieContainer(object):
 """
 Provides a container for a collection of System.Net.CookieCollection objects.

 

 CookieContainer()

 CookieContainer(capacity: int)

 CookieContainer(capacity: int,perDomainCapacity: int,maxCookieSize: int)
 """
 def Add(self,*__args):
  """
  Add(self: CookieContainer,uri: Uri,cookie: Cookie)

   Adds a System.Net.Cookie to the System.Net.CookieContainer for a particular URI.

  

   uri: The URI of the System.Net.Cookie to be added to the System.Net.CookieContainer.

   cookie: The System.Net.Cookie to be added to the System.Net.CookieContainer.

  Add(self: CookieContainer,uri: Uri,cookies: CookieCollection)

   Adds the contents of a System.Net.CookieCollection to the System.Net.CookieContainer for a 

    particular URI.

  

  

   uri: The URI of the System.Net.CookieCollection to be added to the System.Net.CookieContainer.

   cookies: The System.Net.CookieCollection to be added to the System.Net.CookieContainer.

  Add(self: CookieContainer,cookie: Cookie)

   Adds a System.Net.Cookie to a System.Net.CookieContainer. This method uses the domain from the 

    System.Net.Cookie to determine which domain collection to associate the System.Net.Cookie with.

  

  

   cookie: The System.Net.Cookie to be added to the System.Net.CookieContainer.

  Add(self: CookieContainer,cookies: CookieCollection)

   Adds the contents of a System.Net.CookieCollection to the System.Net.CookieContainer.

  

   cookies: The System.Net.CookieCollection to be added to the System.Net.CookieContainer.
  """
  pass
 def GetCookieHeader(self,uri):
  """
  GetCookieHeader(self: CookieContainer,uri: Uri) -> str

  

   Gets the HTTP cookie header that contains the HTTP cookies that represent the System.Net.Cookie 

    instances that are associated with a specific URI.

  

  

   uri: The URI of the System.Net.Cookie instances desired.

   Returns: An HTTP cookie header,with strings representing System.Net.Cookie instances delimited by 

    semicolons.
  """
  pass
 def GetCookies(self,uri):
  """
  GetCookies(self: CookieContainer,uri: Uri) -> CookieCollection

  

   Gets a System.Net.CookieCollection that contains the System.Net.Cookie instances that are 

    associated with a specific URI.

  

  

   uri: The URI of the System.Net.Cookie instances desired.

   Returns: A System.Net.CookieCollection that contains the System.Net.Cookie instances that are associated 

    with a specific URI.
  """
  pass
 def SetCookies(self,uri,cookieHeader):
  """
  SetCookies(self: CookieContainer,uri: Uri,cookieHeader: str)

   Adds System.Net.Cookie instances for one or more cookies from an HTTP cookie header to the 

    System.Net.CookieContainer for a specific URI.

  

  

   uri: The URI of the System.Net.CookieCollection.

   cookieHeader: The contents of an HTTP set-cookie header as returned by a HTTP server,with System.Net.Cookie 

    instances delimited by commas.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
  pass
 @staticmethod
 def __new__(self,capacity=None,perDomainCapacity=None,maxCookieSize=None):
  """
  __new__(cls: type)

  __new__(cls: type,capacity: int)

  __new__(cls: type,capacity: int,perDomainCapacity: int,maxCookieSize: int)
  """
  pass
 Capacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the number of System.Net.Cookie instances that a System.Net.CookieContainer can hold.



Get: Capacity(self: CookieContainer) -> int



Set: Capacity(self: CookieContainer)=value

"""

 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of System.Net.Cookie instances that a System.Net.CookieContainer currently holds.



Get: Count(self: CookieContainer) -> int



"""

 MaxCookieSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Represents the maximum allowed length of a System.Net.Cookie.



Get: MaxCookieSize(self: CookieContainer) -> int



Set: MaxCookieSize(self: CookieContainer)=value

"""

 PerDomainCapacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets and sets the number of System.Net.Cookie instances that a System.Net.CookieContainer can hold per domain.



Get: PerDomainCapacity(self: CookieContainer) -> int



Set: PerDomainCapacity(self: CookieContainer)=value

"""


 DefaultCookieLengthLimit=4096
 DefaultCookieLimit=300
 DefaultPerDomainCookieLimit=20

