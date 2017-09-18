class ProcessStartInfo(object):
 """
 Specifies a set of values that are used when you start a process.

 

 ProcessStartInfo()

 ProcessStartInfo(fileName: str)

 ProcessStartInfo(fileName: str,arguments: str)
 """
 @staticmethod
 def __new__(self,fileName=None,arguments=None):
  """
  __new__(cls: type)

  __new__(cls: type,fileName: str)

  __new__(cls: type,fileName: str,arguments: str)
  """
  pass
 Arguments=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the set of command-line arguments to use when starting the application.



Get: Arguments(self: ProcessStartInfo) -> str



Set: Arguments(self: ProcessStartInfo)=value

"""

 CreateNoWindow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to start the process in a new window.



Get: CreateNoWindow(self: ProcessStartInfo) -> bool



Set: CreateNoWindow(self: ProcessStartInfo)=value

"""

 Domain=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that identifies the domain to use when starting the process.



Get: Domain(self: ProcessStartInfo) -> str



Set: Domain(self: ProcessStartInfo)=value

"""

 Environment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Environment(self: ProcessStartInfo) -> IDictionary[str,str]



"""

 EnvironmentVariables=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets search paths for files,directories for temporary files,application-specific options,and other similar information.



Get: EnvironmentVariables(self: ProcessStartInfo) -> StringDictionary



"""

 ErrorDialog=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether an error dialog box is displayed to the user if the process cannot be started.



Get: ErrorDialog(self: ProcessStartInfo) -> bool



Set: ErrorDialog(self: ProcessStartInfo)=value

"""

 ErrorDialogParentHandle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the window handle to use when an error dialog box is shown for a process that cannot be started.



Get: ErrorDialogParentHandle(self: ProcessStartInfo) -> IntPtr



Set: ErrorDialogParentHandle(self: ProcessStartInfo)=value

"""

 FileName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the application or document to start.



Get: FileName(self: ProcessStartInfo) -> str



Set: FileName(self: ProcessStartInfo)=value

"""

 LoadUserProfile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the Windows user profile is to be loaded from the registry.



Get: LoadUserProfile(self: ProcessStartInfo) -> bool



Set: LoadUserProfile(self: ProcessStartInfo)=value

"""

 Password=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a secure string that contains the user password to use when starting the process.



Get: Password(self: ProcessStartInfo) -> SecureString



Set: Password(self: ProcessStartInfo)=value

"""

 PasswordInClearText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PasswordInClearText(self: ProcessStartInfo) -> str



Set: PasswordInClearText(self: ProcessStartInfo)=value

"""

 RedirectStandardError=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the error output of an application is written to the System.Diagnostics.Process.StandardError stream.



Get: RedirectStandardError(self: ProcessStartInfo) -> bool



Set: RedirectStandardError(self: ProcessStartInfo)=value

"""

 RedirectStandardInput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the input for an application is read from the System.Diagnostics.Process.StandardInput stream.



Get: RedirectStandardInput(self: ProcessStartInfo) -> bool



Set: RedirectStandardInput(self: ProcessStartInfo)=value

"""

 RedirectStandardOutput=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the output of an application is written to the System.Diagnostics.Process.StandardOutput stream.



Get: RedirectStandardOutput(self: ProcessStartInfo) -> bool



Set: RedirectStandardOutput(self: ProcessStartInfo)=value

"""

 StandardErrorEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the preferred encoding for error output.



Get: StandardErrorEncoding(self: ProcessStartInfo) -> Encoding



Set: StandardErrorEncoding(self: ProcessStartInfo)=value

"""

 StandardOutputEncoding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the preferred encoding for standard output.



Get: StandardOutputEncoding(self: ProcessStartInfo) -> Encoding



Set: StandardOutputEncoding(self: ProcessStartInfo)=value

"""

 UserName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the user name to be used when starting the process.



Get: UserName(self: ProcessStartInfo) -> str



Set: UserName(self: ProcessStartInfo)=value

"""

 UseShellExecute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to use the operating system shell to start the process.



Get: UseShellExecute(self: ProcessStartInfo) -> bool



Set: UseShellExecute(self: ProcessStartInfo)=value

"""

 Verb=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the verb to use when opening the application or document specified by the System.Diagnostics.ProcessStartInfo.FileName property.



Get: Verb(self: ProcessStartInfo) -> str



Set: Verb(self: ProcessStartInfo)=value

"""

 Verbs=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the set of verbs associated with the type of file specified by the System.Diagnostics.ProcessStartInfo.FileName property.



Get: Verbs(self: ProcessStartInfo) -> Array[str]



"""

 WindowStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the window state to use when the process is started.



Get: WindowStyle(self: ProcessStartInfo) -> ProcessWindowStyle



Set: WindowStyle(self: ProcessStartInfo)=value

"""

 WorkingDirectory=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the initial directory for the process to be started.



Get: WorkingDirectory(self: ProcessStartInfo) -> str



Set: WorkingDirectory(self: ProcessStartInfo)=value

"""


