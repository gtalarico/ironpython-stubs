class Environment(object):
 """ Provides information about,and means to manipulate,the current environment and platform. This class cannot be inherited. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Environment()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
  
   Replaces the name of each environment variable embedded in the specified string with the string equivalent of the value of the variable,then returns the resulting string.
  
   name: A string containing the names of zero or more environment variables. Each environment variable is quoted with the percent sign character (%).
   Returns: A string with each environment variable replaced by its value.
  """
  pass
 @staticmethod
 def FailFast(message,exception=None):
  """
  FailFast(message: str)
   Immediately terminates a process after writing a message to the Windows Application event log,and then includes the message in error reporting to Microsoft.
  
   message: A message that explains why the process was terminated,or null if no explanation is provided.
  FailFast(message: str,exception: Exception)
   Immediately terminates a process after writing a message to the Windows Application event log,and then includes the message and exception information in error reporting to 
    Microsoft.
  
  
   message: A message that explains why the process was terminated,or null if no explanation is provided.
   exception: An exception that represents the error that caused the termination. This is typically the exception in a catch block.
  """
  pass
 @staticmethod
 def GetCommandLineArgs():
  """
  GetCommandLineArgs() -> Array[str]
  
   Returns a string array containing the command-line arguments for the current process.
   Returns: An array of string where each element contains a command-line argument. The first element is the executable file name,and the following zero or more elements contain the 
    remaining command-line arguments.
  """
  pass
 @staticmethod
 def GetEnvironmentVariable(variable,target=None):
  """
  GetEnvironmentVariable(variable: str) -> str
  
   Retrieves the value of an environment variable from the current process.
  
   variable: The name of the environment variable.
   Returns: The value of the environment variable specified by variable,or null if the environment variable is not found.
  GetEnvironmentVariable(variable: str,target: EnvironmentVariableTarget) -> str
  
   Retrieves the value of an environment variable from the current process or from the Windows operating system registry key for the current user or local machine.
  
   variable: The name of an environment variable.
   target: One of the System.EnvironmentVariableTarget values.
   Returns: The value of the environment variable specified by the variable and target parameters,or null if the environment variable is not found.
  """
  pass
 @staticmethod
 def GetEnvironmentVariables(target=None):
  """
  GetEnvironmentVariables() -> IDictionary
  
   Retrieves all environment variable names and their values from the current process.
   Returns: A dictionary that contains all environment variable names and their values; otherwise,an empty dictionary if no environment variables are found.
  GetEnvironmentVariables(target: EnvironmentVariableTarget) -> IDictionary
  
   Retrieves all environment variable names and their values from the current process,or from the Windows operating system registry key for the current user or local machine.
  
   target: One of the System.EnvironmentVariableTarget values.
   Returns: A dictionary that contains all environment variable names and their values from the source specified by the target parameter; otherwise,an empty dictionary if no 
    environment variables are found.
  """
  pass
 @staticmethod
 def GetFolderPath(folder,option=None):
  """
  GetFolderPath(folder: SpecialFolder) -> str
  GetFolderPath(folder: SpecialFolder,option: SpecialFolderOption) -> str
  """
  pass
 @staticmethod
 def GetLogicalDrives():
  """
  GetLogicalDrives() -> Array[str]
  
   Returns an array of string containing the names of the logical drives on the current computer.
   Returns: An array of strings where each element contains the name of a logical drive. For example,if the computer's hard drive is the first logical drive,the first element 
    returned is "C:\".
  """
  pass
 @staticmethod
 def SetEnvironmentVariable(variable,value,target=None):
  """
  SetEnvironmentVariable(variable: str,value: str)
   Creates,modifies,or deletes an environment variable stored in the current process.
  
   variable: The name of an environment variable.
   value: A value to assign to variable.
  SetEnvironmentVariable(variable: str,value: str,target: EnvironmentVariableTarget)
   Creates,modifies,or deletes an environment variable stored in the current process or in the Windows operating system registry key reserved for the current user or local 
    machine.
  
  
   variable: The name of an environment variable.
   value: A value to assign to variable.
   target: One of the System.EnvironmentVariableTarget values.
  """
  pass
 CommandLine='"C:\\Users\\k.pawiroredjo\\Downloads\\IronPython.2.7.9\\net45\\ipy.exe" -m ironstubs make --all --overwrite'
 CurrentDirectory='C:\\dev\\ironpython-stubs'
 CurrentManagedThreadId=1
 ExitCode=0
 HasShutdownStarted=False
 Is64BitOperatingSystem=True
 Is64BitProcess=True
 MachineName='PC018'
 NewLine='\r\n'
 OSVersion=None
 ProcessorCount=12
 SpecialFolder=None
 SpecialFolderOption=None
 StackTrace='   at System.Environment.GetStackTrace(Exception e,Boolean needFileInfo)\r\n   at System.Environment.get_StackTrace()\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`1.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0,T1 arg1,T2 arg2)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site,T0 arg0,T1 arg1)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`5.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0,T1 arg1,T2 arg2)\r\n   at IronPython.Runtime.Types.BuiltinFunction.Call0(CodeContext context,SiteLocalStorage`1 storage,Object instance)\r\n   at IronPython.Runtime.Types.ReflectedProperty.CallGetter(CodeContext context,PythonType owner,SiteLocalStorage`1 storage,Object instance)\r\n   at IronPython.Runtime.Types.ReflectedProperty.TryGetValue(CodeContext context,Object instance,PythonType owner,Object& value)\r\n   at IronPython.Runtime.Binding.MetaPythonType.FastGetBinderHelper.SlotAccessDelegate.Target(CodeContext context,Object self,Object& result)\r\n   at IronPython.Runtime.Types.TypeGetBase.RunDelegates(Object self,CodeContext context)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site,T0 arg0,T1 arg1)\r\n   at IronPython.Runtime.Types.PythonType.TryGetBoundAttr(CodeContext context,Object o,String name,Object& ret)\r\n   at IronPython.Runtime.Operations.PythonOps.GetBoundAttr(CodeContext context,Object o,String name)\r\n   at redo_class$449(Closure ,PythonFunction ,Object ,Object ,Object ,Object ,Object ,Object ,Object ,Object )\r\n   at CallSite.Target(Closure ,CallSite ,CodeContext ,Object ,Object ,Object ,Object ,Object ,Object ,Object ,Object )\r\n   at redo$437(Closure ,PythonFunction ,Object ,Object ,Object )\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute5[T0,T1,T2,T3,T4,TRet](CallSite site,T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4)\r\n   at IronPython.Runtime.Method.MethodBinding`2.SelfTarget(CallSite site,CodeContext context,Object target,T0 arg0,T1 arg1)\r\n   at redo_module$434(Closure ,PythonFunction ,Object ,Object ,Object ,Object )\r\n   at process_one$427(Closure ,PythonFunction ,Object ,Object ,Object ,Object ,Object )\r\n   at create_stubs$426(Closure ,PythonFunction ,Object ,Object )\r\n   at lambda_method(Closure ,Object[] ,StrongBox`1[] ,InterpretedFrame )\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run5[T0,T1,T2,T3,T4,TRet](T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`7.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run7[T0,T1,T2,T3,T4,T5,T6,TRet](T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4,T5 arg5,T6 arg6)\r\n   at Microsoft.Scripting.Interpreter.DynamicInstruction`7.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run2[T0,T1,TRet](T0 arg0,T1 arg1)\r\n   at IronPython.Runtime.Operations.PythonOps.QualifiedExec(CodeContext context,Object code,PythonDictionary globals,Object locals)\r\n   at Microsoft.Scripting.Interpreter.ActionCallInstruction`4.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run8[T0,T1,T2,T3,T4,T5,T6,T7,TRet](T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4,T5 arg5,T6 arg6,T7 arg7)\r\n   at IronPython.Compiler.PythonCallTargets.OriginalCallTarget7(PythonFunction function,Object arg0,Object arg1,Object arg2,Object arg3,Object arg4,Object arg5,Object arg6)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute9[T0,T1,T2,T3,T4,T5,T6,T7,T8,TRet](CallSite site,T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4,T5 arg5,T6 arg6,T7 arg7,T8 arg8)\r\n   at Microsoft.Scripting.Interpreter.DynamicInstruction`10.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run7[T0,T1,T2,T3,T4,T5,T6,TRet](T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4,T5 arg5,T6 arg6)\r\n   at IronPython.Compiler.PythonCallTargets.OriginalCallTarget6(PythonFunction function,Object arg0,Object arg1,Object arg2,Object arg3,Object arg4,Object arg5)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute8[T0,T1,T2,T3,T4,T5,T6,T7,TRet](CallSite site,T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4,T5 arg5,T6 arg6,T7 arg7)\r\n   at IronPython.Compiler.Ast.CallExpression.Invoke6Instruction.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run5[T0,T1,T2,T3,T4,TRet](T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4)\r\n   at IronPython.Compiler.PythonCallTargets.OriginalCallTarget4(PythonFunction function,Object arg0,Object arg1,Object arg2,Object arg3)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`7.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run5[T0,T1,T2,T3,T4,TRet](T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute4[T0,T1,T2,T3,TRet](CallSite site,T0 arg0,T1 arg1,T2 arg2,T3 arg3)\r\n   at IronPython.Runtime.PythonContext.CallWithKeywords(Object func,Object[] args,IDictionary`2 dict)\r\n   at IronPython.Runtime.Operations.PythonCalls.CallWithKeywordArgs(CodeContext context,Object func,Object[] args,String[] names)\r\n   at IronPython.Hosting.PythonCommandLine.Run()\r\n   at Microsoft.Scripting.Hosting.Shell.CommandLine.Run(ScriptEngine engine,IConsole console,ConsoleOptions options)\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.RunCommandLine()\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.ExecuteInternal()\r\n   at Microsoft.Scripting.Hosting.Shell.ConsoleHost.Run(String[] args)\r\n   at PythonConsoleHost.Main(String[] args)'
 SystemDirectory='C:\\windows\\system32'
 SystemPageSize=4096
 TickCount=-2137155281
 UserDomainName='TRANCON'
 UserInteractive=True
 UserName='k.pawiroredjo'
 Version=None
 WorkingSet=None
 __all__=[
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

