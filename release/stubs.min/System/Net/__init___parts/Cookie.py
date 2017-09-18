class Cookie(object):
 """
 Provides a set of properties and methods that are used to manage cookies. This class cannot be inherited.

 

 Cookie()

 Cookie(name: str,value: str)

 Cookie(name: str,value: str,path: str)

 Cookie(name: str,value: str,path: str,domain: str)
 """
 def Equals(self,comparand):
  """
  Equals(self: Cookie,comparand: object) -> bool

  

   Overrides the System.Object.Equals(System.Object) method.

  

   comparand: A reference to a System.Net.Cookie.

   Returns: Returns true if the System.Net.Cookie is equal to comparand. Two System.Net.Cookie instances are 

    equal if their System.Net.Cookie.Name,System.Net.Cookie.Value,System.Net.Cookie.Path,

    System.Net.Cookie.Domain,and System.Net.Cookie.Version properties are equal. 

    System.Net.Cookie.Name and System.Net.Cookie.Domain string comparisons are case-insensitive.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Cookie) -> int

  

   Overrides the System.Object.GetHashCode method.

   Returns: The 32-bit signed integer hash code for this instance.
  """
  pass
 def ToString(self):
  """
  ToString(self: Cookie) -> str

  

   Overrides the System.Object.ToString method.

   Returns: Returns a string representation of this System.Net.Cookie object that is suitable for including 

    in a HTTP Cookie: request header.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,name=None,value=None,path=None,domain=None):
  """
  __new__(cls: type)

  __new__(cls: type,name: str,value: str)

  __new__(cls: type,name: str,value: str,path: str)

  __new__(cls: type,name: str,value: str,path: str,domain: str)
  """
  pass
 def __ne__(self,*args):
  pass
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a comment that the server can add to a System.Net.Cookie.



Get: Comment(self: Cookie) -> str



Set: Comment(self: Cookie)=value

"""

 CommentUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a URI comment that the server can provide with a System.Net.Cookie.



Get: CommentUri(self: Cookie) -> Uri



Set: CommentUri(self: Cookie)=value

"""

 Discard=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the discard flag set by the server.



Get: Discard(self: Cookie) -> bool



Set: Discard(self: Cookie)=value

"""

 Domain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the URI for which the System.Net.Cookie is valid.



Get: Domain(self: Cookie) -> str



Set: Domain(self: Cookie)=value

"""

 Expired=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current state of the System.Net.Cookie.



Get: Expired(self: Cookie) -> bool



Set: Expired(self: Cookie)=value

"""

 Expires=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the expiration date and time for the System.Net.Cookie as a System.DateTime.



Get: Expires(self: Cookie) -> DateTime



Set: Expires(self: Cookie)=value

"""

 HttpOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether a page script or other active content can access this cookie.



Get: HttpOnly(self: Cookie) -> bool



Set: HttpOnly(self: Cookie)=value

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name for the System.Net.Cookie.



Get: Name(self: Cookie) -> str



Set: Name(self: Cookie)=value

"""

 Path=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the URIs to which the System.Net.Cookie applies.



Get: Path(self: Cookie) -> str



Set: Path(self: Cookie)=value

"""

 Port=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a list of TCP ports that the System.Net.Cookie applies to.



Get: Port(self: Cookie) -> str



Set: Port(self: Cookie)=value

"""

 Secure=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the security level of a System.Net.Cookie.



Get: Secure(self: Cookie) -> bool



Set: Secure(self: Cookie)=value

"""

 TimeStamp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the time when the cookie was issued as a System.DateTime.



Get: TimeStamp(self: Cookie) -> DateTime



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Net.Cookie.Value for the System.Net.Cookie.



Get: Value(self: Cookie) -> str



Set: Value(self: Cookie)=value

"""

 Version=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the version of HTTP state maintenance to which the cookie conforms.



Get: Version(self: Cookie) -> int



Set: Version(self: Cookie)=value

"""


