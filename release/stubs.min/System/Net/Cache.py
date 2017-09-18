# encoding: utf-8
# module System.Net.Cache calls itself Cache
# from System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class HttpCacheAgeControl(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the meaning of time values that control caching behavior for resources obtained using System.Net.HttpWebRequest objects.

 

 enum HttpCacheAgeControl,values: MaxAge (2),MaxAgeAndMaxStale (6),MaxAgeAndMinFresh (3),MaxStale (4),MinFresh (1),None (0)
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
 MaxAge=None
 MaxAgeAndMaxStale=None
 MaxAgeAndMinFresh=None
 MaxStale=None
 MinFresh=None
 None=None
 value__=None


class HttpRequestCacheLevel(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies caching behavior for resources obtained using the Hypertext Transfer protocol (HTTP).

 

 enum HttpRequestCacheLevel,values: BypassCache (1),CacheIfAvailable (3),CacheOnly (2),CacheOrNextCacheOnly (7),Default (0),NoCacheNoStore (6),Refresh (8),Reload (5),Revalidate (4)
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
 BypassCache=None
 CacheIfAvailable=None
 CacheOnly=None
 CacheOrNextCacheOnly=None
 Default=None
 NoCacheNoStore=None
 Refresh=None
 Reload=None
 Revalidate=None
 value__=None


class RequestCachePolicy(object):
 """
 Defines an application's caching requirements for resources obtained by using System.Net.WebRequest objects.

 

 RequestCachePolicy(level: RequestCacheLevel)

 RequestCachePolicy()
 """
 def ToString(self):
  """
  ToString(self: RequestCachePolicy) -> str

  

   Returns a string representation of this instance.

   Returns: A System.String containing the System.Net.Cache.RequestCachePolicy.Level for this instance.
  """
  pass
 @staticmethod
 def __new__(self,level=None):
  """
  __new__(cls: type)

  __new__(cls: type,level: RequestCacheLevel)
  """
  pass
 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Net.Cache.RequestCacheLevel value specified when this instance was constructed.



Get: Level(self: RequestCachePolicy) -> RequestCacheLevel



"""



class HttpRequestCachePolicy(RequestCachePolicy):
 """
 Defines an application's caching requirements for resources obtained by using System.Net.HttpWebRequest objects.

 

 HttpRequestCachePolicy()

 HttpRequestCachePolicy(level: HttpRequestCacheLevel)

 HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl,ageOrFreshOrStale: TimeSpan)

 HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl,maxAge: TimeSpan,freshOrStale: TimeSpan)

 HttpRequestCachePolicy(cacheSyncDate: DateTime)

 HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl,maxAge: TimeSpan,freshOrStale: TimeSpan,cacheSyncDate: DateTime)
 """
 def ToString(self):
  """
  ToString(self: HttpRequestCachePolicy) -> str

  

   Returns a string representation of this instance.

   Returns: A System.String value that contains the property values for this instance.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,level: HttpRequestCacheLevel)

  __new__(cls: type,cacheAgeControl: HttpCacheAgeControl,ageOrFreshOrStale: TimeSpan)

  __new__(cls: type,cacheAgeControl: HttpCacheAgeControl,maxAge: TimeSpan,freshOrStale: TimeSpan)

  __new__(cls: type,cacheSyncDate: DateTime)

  __new__(cls: type,cacheAgeControl: HttpCacheAgeControl,maxAge: TimeSpan,freshOrStale: TimeSpan,cacheSyncDate: DateTime)
  """
  pass
 CacheSyncDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cache synchronization date for this instance.



Get: CacheSyncDate(self: HttpRequestCachePolicy) -> DateTime



"""

 Level=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Net.Cache.HttpRequestCacheLevel value that was specified when this instance was created.



Get: Level(self: HttpRequestCachePolicy) -> HttpRequestCacheLevel



"""

 MaxAge=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum age permitted for a resource returned from the cache.



Get: MaxAge(self: HttpRequestCachePolicy) -> TimeSpan



"""

 MaxStale=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum staleness value that is permitted for a resource returned from the cache.



Get: MaxStale(self: HttpRequestCachePolicy) -> TimeSpan



"""

 MinFresh=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minimum freshness that is permitted for a resource returned from the cache.



Get: MinFresh(self: HttpRequestCachePolicy) -> TimeSpan



"""



class RequestCacheLevel(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies caching behavior for resources obtained using System.Net.WebRequest and its derived classes.

 

 enum RequestCacheLevel,values: BypassCache (1),CacheIfAvailable (3),CacheOnly (2),Default (0),NoCacheNoStore (6),Reload (5),Revalidate (4)
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
 BypassCache=None
 CacheIfAvailable=None
 CacheOnly=None
 Default=None
 NoCacheNoStore=None
 Reload=None
 Revalidate=None
 value__=None


