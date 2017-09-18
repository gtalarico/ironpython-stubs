class ICustomFormatter:
 """ Defines a method that supports custom formatting of the value of an object. """
 def Format(self,format,arg,formatProvider):
  """
  Format(self: ICustomFormatter,format: str,arg: object,formatProvider: IFormatProvider) -> str

  

   Converts the value of a specified object to an equivalent string representation using specified 

    format and culture-specific formatting information.

  

  

   format: A format string containing formatting specifications.

   arg: An object to format.

   formatProvider: An object that supplies format information about the current instance.

   Returns: The string representation of the value of arg,formatted as specified by format and 

    formatProvider.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
