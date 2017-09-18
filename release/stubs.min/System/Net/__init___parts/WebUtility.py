class WebUtility(object):
 """ Provides methods for encoding and decoding URLs when processing Web requests. """
 @staticmethod
 def HtmlDecode(value,output=None):
  """
  HtmlDecode(value: str,output: TextWriter)

   Converts a string that has been HTML-encoded into a decoded string,and sends the decoded string 

    to a System.IO.TextWriter output stream.

  

  

   value: The string to decode.

   output: A System.IO.TextWriter stream of output.

  HtmlDecode(value: str) -> str

  

   Converts a string that has been HTML-encoded for HTTP transmission into a decoded string.

  

   value: The string to decode.

   Returns: A decoded string.
  """
  pass
 @staticmethod
 def HtmlEncode(value,output=None):
  """
  HtmlEncode(value: str,output: TextWriter)

   Converts a string into an HTML-encoded string,and returns the output as a System.IO.TextWriter 

    stream of output.

  

  

   value: The string to encode.

   output: A System.IO.TextWriter output stream.

  HtmlEncode(value: str) -> str

  

   Converts a string to an HTML-encoded string.

  

   value: The string to encode.

   Returns: An encoded string.
  """
  pass
 @staticmethod
 def UrlDecode(encodedValue):
  """ UrlDecode(encodedValue: str) -> str """
  pass
 @staticmethod
 def UrlDecodeToBytes(encodedValue,offset,count):
  """ UrlDecodeToBytes(encodedValue: Array[Byte],offset: int,count: int) -> Array[Byte] """
  pass
 @staticmethod
 def UrlEncode(value):
  """ UrlEncode(value: str) -> str """
  pass
 @staticmethod
 def UrlEncodeToBytes(value,offset,count):
  """ UrlEncodeToBytes(value: Array[Byte],offset: int,count: int) -> Array[Byte] """
  pass
 __all__=[
  'HtmlDecode',
  'HtmlEncode',
  'UrlDecode',
  'UrlDecodeToBytes',
  'UrlEncode',
  'UrlEncodeToBytes',
 ]

