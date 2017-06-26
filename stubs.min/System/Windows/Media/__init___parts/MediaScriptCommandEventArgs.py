class MediaScriptCommandEventArgs(EventArgs):
 """ Provides data for the System.Windows.Controls.MediaElement.ScriptCommand and System.Windows.Media.MediaPlayer.ScriptCommand events. """
 ParameterType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of script command that was raised.

Get: ParameterType(self: MediaScriptCommandEventArgs) -> str

"""

 ParameterValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the arguments associated with the script command type.

Get: ParameterValue(self: MediaScriptCommandEventArgs) -> str

"""


