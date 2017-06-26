class InputLanguageChangingEventArgs(InputLanguageEventArgs):
    """
    Contains arguments associated with the System.Windows.Input.InputLanguageManager.InputLanguageChanging event.
    
    InputLanguageChangingEventArgs(newLanguageId: CultureInfo, previousLanguageId: CultureInfo)
    """
    @staticmethod # known case of __new__
    def __new__(self, newLanguageId, previousLanguageId):
        """ __new__(cls: type, newLanguageId: CultureInfo, previousLanguageId: CultureInfo) """
        pass

    Rejected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the initiated change of input language should be accepted or rejected.

Get: Rejected(self: InputLanguageChangingEventArgs) -> bool

Set: Rejected(self: InputLanguageChangingEventArgs) = value
"""


