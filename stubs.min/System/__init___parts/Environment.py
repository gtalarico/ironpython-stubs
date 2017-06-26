class Environment(object):
    """ Provides information about, and means to manipulate, the current environment and platform. This class cannot be inherited. """
    @staticmethod
    def Exit(exitCode):
        """
        Exit(exitCode: int)
            Terminates this process and gives the underlying operating system the specified exit code.
        
            exitCode: Exit code to be given to the operating system.
        """
        pass

    @staticmethod
    def ExpandEnvironmentVariables(name):
        """
        ExpandEnvironmentVariables(name: str) -> str
        
            Replaces the name of each environment variable embedded in the specified string with the string equivalent of the value of the variable, then returns the resulting string.
        
            name: A string containing the names of zero or more environment variables. Each environment variable is quoted with the percent sign character (%).
            Returns: A string with each environment variable replaced by its value.
        """
        pass

    @staticmethod
    def FailFast(message, exception=None):
        """
        FailFast(message: str, exception: Exception)
            Immediately terminates a process after writing a message to the Windows Application event log, and then includes the message and exception information in error reporting to Microsoft.
        
            message: A message that explains why the process was terminated, or null if no explanation is provided.
            exception: An exception that represents the error that caused the termination. This is typically the exception in a catch block.
        FailFast(message: str)
            Immediately terminates a process after writing a message to the Windows Application event log, and then includes the message in error reporting to Microsoft.
        
            message: A message that explains why the process was terminated, or null if no explanation is provided.
        """
        pass

    @staticmethod
    def GetCommandLineArgs():
        """
        GetCommandLineArgs() -> Array[str]
        
            Returns a string array containing the command-line arguments for the current process.
            Returns: An array of string where each element contains a command-line argument. The first element is the executable file name, and the following zero or more elements contain the remaining command-line arguments.
        """
        pass

    @staticmethod
    def GetEnvironmentVariable(variable, target=None):
        """
        GetEnvironmentVariable(variable: str, target: EnvironmentVariableTarget) -> str
        
            Retrieves the value of an environment variable from the current process or from the Windows operating system registry key for the current user or local machine.
        
            variable: The name of an environment variable.
            target: One of the System.EnvironmentVariableTarget values.
            Returns: The value of the environment variable specified by the variable and target parameters, or null if the environment variable is not found.
        GetEnvironmentVariable(variable: str) -> str
        
            Retrieves the value of an environment variable from the current process.
        
            variable: The name of the environment variable.
            Returns: The value of the environment variable specified by variable, or null if the environment variable is not found.
        """
        pass

    @staticmethod
    def GetEnvironmentVariables(target=None):
        """
        GetEnvironmentVariables(target: EnvironmentVariableTarget) -> IDictionary
        
            Retrieves all environment variable names and their values from the current process, or from the Windows operating system registry key for the current user or local machine.
        
            target: One of the System.EnvironmentVariableTarget values.
            Returns: A dictionary that contains all environment variable names and their values from the source specified by the target parameter; otherwise, an empty dictionary if no environment variables are found.
        GetEnvironmentVariables() -> IDictionary
        
            Retrieves all environment variable names and their values from the current process.
            Returns: A dictionary that contains all environment variable names and their values; otherwise, an empty dictionary if no environment variables are found.
        """
        pass

    @staticmethod
    def GetFolderPath(folder, option=None):
        """
        GetFolderPath(folder: SpecialFolder, option: SpecialFolderOption) -> str
        GetFolderPath(folder: SpecialFolder) -> str
        """
        pass

    @staticmethod
    def GetLogicalDrives():
        """
        GetLogicalDrives() -> Array[str]
        
            Returns an array of string containing the names of the logical drives on the current computer.
            Returns: An array of strings where each element contains the name of a logical drive. For example, if the computer's hard drive is the first logical drive, the first element returned is "C:\".
        """
        pass

    @staticmethod
    def SetEnvironmentVariable(variable, value, target=None):
        """
        SetEnvironmentVariable(variable: str, value: str, target: EnvironmentVariableTarget)
            Creates, modifies, or deletes an environment variable stored in the current process or in the Windows operating system registry key reserved for the current user or local machine.
        
            variable: The name of an environment variable.
            value: A value to assign to variable.
            target: One of the System.EnvironmentVariableTarget values.
        SetEnvironmentVariable(variable: str, value: str)
            Creates, modifies, or deletes an environment variable stored in the current process.
        
            variable: The name of an environment variable.
            value: A value to assign to variable.
        """
        pass

    CommandLine = 'ipy64  make_stubs.py '
    CurrentDirectory = 'D:\\Dropbox\\Shared\\dev\\repos\\ironpython-stubs'
    CurrentManagedThreadId = 1
    ExitCode = 0
    HasShutdownStarted = False
    Is64BitOperatingSystem = True
    Is64BitProcess = True
    MachineName = 'STUDIO-SSD'
    NewLine = '\r\n'
    OSVersion = None
    ProcessorCount = 8
    SpecialFolder = None
    SpecialFolderOption = None
    StackTrace = '   at System.Environment.GetStackTrace(Exception e, Boolean needFileInfo)\r\n   at System.Environment.get_StackTrace()\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`1.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0, T1 arg1, T2 arg2)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site, T0 arg0, T1 arg1)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`5.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0, T1 arg1, T2 arg2)\r\n   at IronPython.Runtime.Types.BuiltinFunction.Call0(CodeContext context, SiteLocalStorage`1 storage, Object instance)\r\n   at IronPython.Runtime.Types.ReflectedProperty.CallGetter(CodeContext context, PythonType owner, SiteLocalStorage`1 storage, Object instance)\r\n   at IronPython.Runtime.Types.ReflectedProperty.TryGetValue(CodeContext context, Object instance, PythonType owner, Object& value)\r\n   at IronPython.Runtime.Binding.MetaPythonType.FastGetBinderHelper.SlotAccessDelegate.Target(CodeContext context, Object self, Object& result)\r\n   at IronPython.Runtime.Types.TypeGetBase.RunDelegates(Object self, CodeContext context)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site, T0 arg0, T1 arg1)\r\n   at IronPython.Runtime.Types.PythonType.TryGetBoundAttr(CodeContext context, Object o, String name, Object& ret)\r\n   at IronPython.Runtime.Operations.PythonOps.GetBoundAttr(CodeContext context, Object o, String name)\r\n   at redo_class$266(Closure , PythonFunction , Object , Object , Object , Object , Object , Object , Object , Object )\r\n   at CallSite.Target(Closure , CallSite , CodeContext , Object , Object , Object , Object , Object , Object , Object , Object )\r\n   at redo$247(Closure , PythonFunction , Object , Object , Object )\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute5[T0,T1,T2,T3,T4,TRet](CallSite site, T0 arg0, T1 arg1, T2 arg2, T3 arg3, T4 arg4)\r\n   at IronPython.Runtime.Method.MethodBinding`2.SelfTarget(CallSite site, CodeContext context, Object target, T0 arg0, T1 arg1)\r\n   at redo_module$244(Closure , PythonFunction , Object , Object , Object , Object )\r\n   at process_one$237(Closure , PythonFunction , Object , Object , Object , Object , Object )\r\n   at lambda_method(Closure , Object[] , StrongBox`1[] , InterpretedFrame )\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run1[T0,TRet](T0 arg0)\r\n   at IronPython.Compiler.RuntimeScriptCode.InvokeTarget(Scope scope)\r\n   at IronPython.Hosting.PythonCommandLine.RunFileWorker(String fileName)\r\n   at IronPython.Hosting.PythonCommandLine.RunFile(String fileName)\r\n   at Microsoft.Scripting.Hosting.Shell.CommandLine.Run()\r\n   at IronPython.Hosting.PythonCommandLine.Run()\r\n   at Microsoft.Scripting.Hosting.Shell.CommandLine.Run(ScriptEngine engine, IConsole console, ConsoleOptions options)\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.RunCommandLine()\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.ExecuteInternal()\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.Run(String[] args)\r\n   at PythonConsoleHost.Main(String[] args)'
    SystemDirectory = 'C:\\WINDOWS\\system32'
    SystemPageSize = 4096
    TickCount = 272578921
    UserDomainName = 'STUDIO-SSD'
    UserInteractive = True
    UserName = 'gtalarico'
    Version = None
    WorkingSet = None
    __all__ = [
        'Exit',
        'ExpandEnvironmentVariables',
        'FailFast',
        'GetCommandLineArgs',
        'GetEnvironmentVariable',
        'GetEnvironmentVariables',
        'GetFolderPath',
        'GetLogicalDrives',
        'SetEnvironmentVariable',
        'SpecialFolder',
        'SpecialFolderOption',
    ]

