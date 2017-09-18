class IFormattable:
 """ Provides functionality to format the value of an object into a string representation. """
 def ToString(self,format,formatProvider):
  """
  ToString(self: IFormattable,format: str,formatProvider: IFormatProvider) -> str

  

   Formats the value of the current instance using the specified format.

  

   format: The format to use.-or- A null reference (Nothing in Visual Basic) to use the default format 

    defined for the type of the System.IFormattable implementation.

  

   formatProvider: The provider to use to format the value.-or- A null reference (Nothing in Visual Basic) to 

    obtain the numeric format information from the current locale setting of the operating system.

  

   Returns: The value of the current instance in the specified format.
  """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
