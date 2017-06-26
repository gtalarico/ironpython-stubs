class ExitEventArgs(EventArgs):
 """ Event arguments for the System.Windows.Application.Exit event. """
 ApplicationExitCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the exit code that an application returns to the operating system when the application exits.

Get: ApplicationExitCode(self: ExitEventArgs) -> int

Set: ApplicationExitCode(self: ExitEventArgs)=value
"""


