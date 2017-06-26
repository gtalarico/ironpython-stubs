class InputLanguageChangedEventArgs(EventArgs):
    """
    Provides data for the System.Windows.Forms.Form.InputLanguageChanged event.
    
    InputLanguageChangedEventArgs(culture: CultureInfo, charSet: Byte)
    InputLanguageChangedEventArgs(inputLanguage: InputLanguage, charSet: Byte)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, culture: CultureInfo, charSet: Byte)
        __new__(cls: type, inputLanguage: InputLanguage, charSet: Byte)
        """
        pass

    CharSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the character set associated with the new input language.

Get: CharSet(self: InputLanguageChangedEventArgs) -> Byte

"""

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the locale of the input language.

Get: Culture(self: InputLanguageChangedEventArgs) -> CultureInfo

"""

    InputLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating the input language.

Get: InputLanguage(self: InputLanguageChangedEventArgs) -> InputLanguage

"""


