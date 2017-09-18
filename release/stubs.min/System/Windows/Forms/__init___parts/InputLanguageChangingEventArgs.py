class InputLanguageChangingEventArgs(CancelEventArgs):
 """
 Provides data for the System.Windows.Forms.Form.InputLanguageChanging event.

 

 InputLanguageChangingEventArgs(culture: CultureInfo,sysCharSet: bool)

 InputLanguageChangingEventArgs(inputLanguage: InputLanguage,sysCharSet: bool)
 """
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,culture: CultureInfo,sysCharSet: bool)

  __new__(cls: type,inputLanguage: InputLanguage,sysCharSet: bool)
  """
  pass
 Culture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the locale of the requested input language.



Get: Culture(self: InputLanguageChangingEventArgs) -> CultureInfo



"""

 InputLanguage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating the input language.



Get: InputLanguage(self: InputLanguageChangingEventArgs) -> InputLanguage



"""

 SysCharSet=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the system default font supports the character set required for the requested input language.



Get: SysCharSet(self: InputLanguageChangingEventArgs) -> bool



"""


