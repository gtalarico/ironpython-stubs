class InputLanguageEventArgs(EventArgs):
 """ Provides a base class for arguments for events dealing with a change in input language. """
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,newLanguageId: CultureInfo,previousLanguageId: CultureInfo) """
  pass
 NewLanguage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Globalization.CultureInfo object representing the new current input language.

Get: NewLanguage(self: InputLanguageEventArgs) -> CultureInfo

"""

 PreviousLanguage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Globalization.CultureInfo object representing the previous current input language.

Get: PreviousLanguage(self: InputLanguageEventArgs) -> CultureInfo

"""


