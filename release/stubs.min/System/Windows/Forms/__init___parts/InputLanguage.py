class InputLanguage(object):
 """ Provides methods and fields to manage the input language. This class cannot be inherited. """
 def Equals(self,value):
  """
  Equals(self: InputLanguage,value: object) -> bool

  

   Specifies whether two input languages are equal.

  

   value: The language to test for equality.

   Returns: true if the two languages are equal; otherwise,false.
  """
  pass
 @staticmethod
 def FromCulture(culture):
  """
  FromCulture(culture: CultureInfo) -> InputLanguage

  

   Returns the input language associated with the specified culture.

  

   culture: The System.Globalization.CultureInfo that specifies the culture to convert from.

   Returns: An System.Windows.Forms.InputLanguage that represents the previously selected input language.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: InputLanguage) -> int

  

   Returns the hash code for this input language.

   Returns: The hash code for this input language.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 Culture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the culture of the current input language.



Get: Culture(self: InputLanguage) -> CultureInfo



"""

 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the handle for the input language.



Get: Handle(self: InputLanguage) -> IntPtr



"""

 LayoutName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the current keyboard layout as it appears in the regional settings of the operating system on the computer.



Get: LayoutName(self: InputLanguage) -> str



"""


 CurrentInputLanguage=None
 DefaultInputLanguage=None
 InstalledInputLanguages=None

