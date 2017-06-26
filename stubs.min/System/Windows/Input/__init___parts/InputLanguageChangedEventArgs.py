class InputLanguageChangedEventArgs(InputLanguageEventArgs):
    """
    Contains arguments associated with the System.Windows.Input.InputLanguageManager.InputLanguageChanged event.
    
    InputLanguageChangedEventArgs(newLanguageId: CultureInfo, previousLanguageId: CultureInfo)
    """
    @staticmethod # known case of __new__
    def __new__(self, newLanguageId, previousLanguageId):
        """ __new__(cls: type, newLanguageId: CultureInfo, previousLanguageId: CultureInfo) """
        pass

