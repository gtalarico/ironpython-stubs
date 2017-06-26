class MediaScriptCommandRoutedEventArgs(RoutedEventArgs):
    """ Provides data for the System.Windows.Controls.MediaElement.ScriptCommand and System.Windows.Media.MediaPlayer.ScriptCommand events. """
    ParameterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of script command that was raised.

Get: ParameterType(self: MediaScriptCommandRoutedEventArgs) -> str

"""

    ParameterValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the arguments associated with the script command type.

Get: ParameterValue(self: MediaScriptCommandRoutedEventArgs) -> str

"""


