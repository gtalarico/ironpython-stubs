class InputLanguageManager(DispatcherObject):
    """ Provides facilities for managing input languages in Windows Presentation Foundation (WPF). """
    @staticmethod
    def GetInputLanguage(target):
        """
        GetInputLanguage(target: DependencyObject) -> CultureInfo
        
            Returns the value of the System.Windows.Input.InputLanguageManager.InputLanguage �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the input language.
            Returns: A System.Globalization.CultureInfo object representing the input language for the specified dependency object.
        """
        pass

    @staticmethod
    def GetRestoreInputLanguage(target):
        """
        GetRestoreInputLanguage(target: DependencyObject) -> bool
        
            Returns the value of System.Windows.Input.InputLanguageManager.RestoreInputLanguage �attached property for a specified dependency object.
        
            target: The dependency object for which to retrieve the value of System.Windows.Input.InputLanguageManager.RestoreInputLanguage.
            Returns: The current value of System.Windows.Input.InputLanguageManager.RestoreInputLanguage for the specified dependency object.
        """
        pass

    def RegisterInputLanguageSource(self, inputLanguageSource):
        """
        RegisterInputLanguageSource(self: InputLanguageManager, inputLanguageSource: IInputLanguageSource)
            Registers an input language source with the System.Windows.Input.InputLanguageManager.
        
            inputLanguageSource: An object that specifies the input language to register.  This object must implement the System.Windows.Input.IInputLanguageSource interface.
        """
        pass

    def ReportInputLanguageChanged(self, newLanguageId, previousLanguageId):
        """
        ReportInputLanguageChanged(self: InputLanguageManager, newLanguageId: CultureInfo, previousLanguageId: CultureInfo)
            Report the completion of a change of input language to the System.Windows.Input.InputLanguageManager.
        
            newLanguageId: A System.Globalization.CultureInfo object representing the new input language.
            previousLanguageId: A System.Globalization.CultureInfo object representing the previous input language.
        """
        pass

    def ReportInputLanguageChanging(self, newLanguageId, previousLanguageId):
        """
        ReportInputLanguageChanging(self: InputLanguageManager, newLanguageId: CultureInfo, previousLanguageId: CultureInfo) -> bool
        
            Report the initiation of a change of input language to the System.Windows.Input.InputLanguageManager.
        
            newLanguageId: A System.Globalization.CultureInfo object representing the new input language.
            previousLanguageId: A System.Globalization.CultureInfo object representing the previous input language.
            Returns: true to indicate that the reported change of input language was accepted; otherwise, false.
        """
        pass

    @staticmethod
    def SetInputLanguage(target, inputLanguage):
        """
        SetInputLanguage(target: DependencyObject, inputLanguage: CultureInfo)
            Sets the value of the System.Windows.Input.InputLanguageManager.InputLanguage attached property on the specified dependency object.
        
            target: The dependency object on which to set the System.Windows.Input.InputLanguageManager.InputLanguage attached property.
            inputLanguage: A System.Globalization.CultureInfo object representing the new value for the System.Windows.Input.InputLanguageManager.InputLanguage attached property.
        """
        pass

    @staticmethod
    def SetRestoreInputLanguage(target, restore):
        """
        SetRestoreInputLanguage(target: DependencyObject, restore: bool)
            Sets the value of the System.Windows.Input.InputLanguageManager.RestoreInputLanguage dependency property on the specified dependency object.
        
            target: The dependency object for which to set the value of System.Windows.Input.InputLanguageManager.RestoreInputLanguage.
            restore: A Boolean value to set the System.Windows.Input.InputLanguageManager.RestoreInputLanguage attached property to.
        """
        pass

    AvailableInputLanguages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for currently available input languages.

Get: AvailableInputLanguages(self: InputLanguageManager) -> IEnumerable

"""

    CurrentInputLanguage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the current input language.

Get: CurrentInputLanguage(self: InputLanguageManager) -> CultureInfo

Set: CurrentInputLanguage(self: InputLanguageManager) = value
"""


    Current = None
    InputLanguageChanged = None
    InputLanguageChanging = None
    InputLanguageProperty = None
    RestoreInputLanguageProperty = None

