class Environment(object):
 """ Provides information about,and means to manipulate,the current environment and platform. This class cannot be inherited. """
 @staticmethod
 def Exit(exitCode):
  """
  Exit(exitCode: int)
   Terminates this process and gives the underlying operating system the specified 
    exit code.
  
  
   exitCode: Exit code to be given to the operating system.
  """
  pass
 @staticmethod
 def ExpandEnvironmentVariables(name):
  """
  ExpandEnvironmentVariables(name: str) -> str
  
   Replaces the name of each environment variable embedded in the specified string 
    with the string equivalent of the value of the variable,then returns the 
    resulting string.
  
  
   name: A string containing the names of zero or more environment variables. Each 
    environment variable is quoted with the percent sign character (%).
  
   Returns: A string with each environment variable replaced by its value.
  """
  pass
 @staticmethod
 def FailFast(message,exception=None):
  """
  FailFast(message: str,exception: Exception)
   Immediately terminates a process after writing a message to the Windows 
    Application event log,and then includes the message and exception information 
    in error reporting to Microsoft.
  
  
   message: A message that explains why the process was terminated,or null if no 
    explanation is provided.
  
   exception: An exception that represents the error that caused the termination. This is 
    typically the exception in a catch block.
  
  FailFast(message: str)
   Immediately terminates a process after writing a message to the Windows 
    Application event log,and then includes the message in error reporting to 
    Microsoft.
  
  
   message: A message that explains why the process was terminated,or null if no 
    explanation is provided.
  """
  pass
 @staticmethod
 def GetCommandLineArgs():
  """
  GetCommandLineArgs() -> Array[str]
  
   Returns a string array containing the command-line arguments for the current 
    process.
  
   Returns: An array of string where each element contains a command-line argument. The 
    first element is the executable file name,and the following zero or more 
    elements contain the remaining command-line arguments.
  """
  pass
 @staticmethod
 def GetEnvironmentVariable(variable,target=None):
  """
  GetEnvironmentVariable(variable: str,target: EnvironmentVariableTarget) -> str
  
   Retrieves the value of an environment variable from the current process or from 
    the Windows operating system registry key for the current user or local 
    machine.
  
  
   variable: The name of an environment variable.
   target: One of the System.EnvironmentVariableTarget values.
   Returns: The value of the environment variable specified by the variable and target 
    parameters,or null if the environment variable is not found.
  
  GetEnvironmentVariable(variable: str) -> str
  
   Retrieves the value of an environment variable from the current process.
  
   variable: The name of the environment variable.
   Returns: The value of the environment variable specified by variable,or null if the 
    environment variable is not found.
  """
  pass
 @staticmethod
 def GetEnvironmentVariables(target=None):
  """
  GetEnvironmentVariables(target: EnvironmentVariableTarget) -> IDictionary
  
   Retrieves all environment variable names and their values from the current 
    process,or from the Windows operating system registry key for the current user 
    or local machine.
  
  
   target: One of the System.EnvironmentVariableTarget values.
   Returns: A dictionary that contains all environment variable names and their values from 
    the source specified by the target parameter; otherwise,an empty dictionary if 
    no environment variables are found.
  
  GetEnvironmentVariables() -> IDictionary
  
   Retrieves all environment variable names and their values from the current 
    process.
  
   Returns: A dictionary that contains all environment variable names and their values; 
    otherwise,an empty dictionary if no environment variables are found.
  """
  pass
 @staticmethod
 def GetFolderPath(folder,option=None):
  """
  GetFolderPath(folder: SpecialFolder,option: SpecialFolderOption) -> str
  GetFolderPath(folder: SpecialFolder) -> str
  """
  pass
 @staticmethod
 def GetLogicalDrives():
  """
  GetLogicalDrives() -> Array[str]
  
   Returns an array of string containing the names of the logical drives on the 
    current computer.
  
   Returns: An array of strings where each element contains the name of a logical drive. 
    For example,if the computer's hard drive is the first logical drive,the first 
    element returned is "C:\".
  """
  pass
 @staticmethod
 def SetEnvironmentVariable(variable,value,target=None):
  """
  SetEnvironmentVariable(variable: str,value: str,target: EnvironmentVariableTarget)
   Creates,modifies,or deletes an environment variable stored in the current 
    process or in the Windows operating system registry key reserved for the 
    current user or local machine.
  
  
   variable: The name of an environment variable.
   value: A value to assign to variable.
   target: One of the System.EnvironmentVariableTarget values.
  SetEnvironmentVariable(variable: str,value: str)
   Creates,modifies,or deletes an environment variable stored in the current 
    process.
  
  
   variable: The name of an environment variable.
   value: A value to assign to variable.
  """
  pass
 CommandLine='"C:\\Program Files\\Autodesk\\Revit 2017\\Revit.exe" /language ENU'
 CurrentDirectory='D:\\Dropbox\\Shared\\dev\\repos\\ironpython-stubs'
 CurrentManagedThreadId=1
 ExitCode=0
 HasShutdownStarted=False
 Is64BitOperatingSystem=True
 Is64BitProcess=True
 MachineName='STUDIO-SSD'
 NewLine='\r\n'
 OSVersion=None
 ProcessorCount=8
 SpecialFolder=None
 SpecialFolderOption=None
 StackTrace='   at System.Environment.GetStackTrace(Exception e,Boolean needFileInfo)\r\n   at System.Environment.get_StackTrace()\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`1.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0,T1 arg1,T2 arg2)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site,T0 arg0,T1 arg1)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`5.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0,T1 arg1,T2 arg2)\r\n   at IronPython.Runtime.Types.BuiltinFunction.Call0(CodeContext context,SiteLocalStorage`1 storage,Object instance)\r\n   at IronPython.Runtime.Types.ReflectedProperty.CallGetter(CodeContext context,PythonType owner,SiteLocalStorage`1 storage,Object instance)\r\n   at IronPython.Runtime.Types.ReflectedProperty.TryGetValue(CodeContext context,Object instance,PythonType owner,Object& value)\r\n   at IronPython.Runtime.Binding.MetaPythonType.FastGetBinderHelper.SlotAccessDelegate.Target(CodeContext context,Object self,Object& result)\r\n   at IronPython.Runtime.Types.TypeGetBase.RunDelegates(Object self,CodeContext context)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site,T0 arg0,T1 arg1)\r\n   at IronPython.Runtime.Types.PythonType.TryGetBoundAttr(CodeContext context,Object o,String name,Object& ret)\r\n   at IronPython.Runtime.Operations.PythonOps.GetBoundAttr(CodeContext context,Object o,String name)\r\n   at redo_class$768(Closure ,PythonFunction ,Object ,Object ,Object ,Object ,Object ,Object ,Object ,Object )\r\n   at CallSite.Target(Closure ,CallSite ,CodeContext ,Object ,Object ,Object ,Object ,Object ,Object ,Object ,Object )\r\n   at redo$749(Closure ,PythonFunction ,Object ,Object ,Object )\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute5[T0,T1,T2,T3,T4,TRet](CallSite site,T0 arg0,T1 arg1,T2 arg2,T3 arg3,T4 arg4)\r\n   at IronPython.Runtime.Method.MethodBinding`2.SelfTarget(CallSite site,CodeContext context,Object target,T0 arg0,T1 arg1)\r\n   at redo_module$746(Closure ,PythonFunction ,Object ,Object ,Object ,Object )\r\n   at process_one$736(Closure ,PythonFunction ,Object ,Object ,Object ,Object ,Object )\r\n   at lambda_method(Closure ,Object[] ,StrongBox`1[] ,InterpretedFrame )\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run1[T0,TRet](T0 arg0)\r\n   at System.Dynamic.UpdateDelegates.UpdateAndExecute2[T0,T1,TRet](CallSite site,T0 arg0,T1 arg1)\r\n   at Microsoft.Scripting.Interpreter.FuncCallInstruction`5.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run3[T0,T1,T2,TRet](T0 arg0,T1 arg1,T2 arg2)\r\n   at IronPython.Compiler.Ast.CallExpression.Invoke0Instruction.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.Interpreter.Run(InterpretedFrame frame)\r\n   at Microsoft.Scripting.Interpreter.LightLambda.Run2[T0,T1,TRet](T0 arg0,T1 arg1)\r\n   at IronPython.Compiler.PythonScriptCode.RunWorker(CodeContext ctx)\r\n   at Microsoft.Scripting.Hosting.ScriptSource.Execute(ScriptScope scope)\r\n   at Microsoft.Scripting.Hosting.ScriptSource.ExecuteAndWrap(ScriptScope scope,ObjectHandle& exception)\r\n   at PythonConsoleControl.PythonConsole.<>c__DisplayClass56_1.<ExecuteStatements>b__0()\r\n   at System.Windows.Threading.ExceptionWrapper.InternalRealCall(Delegate callback,Object args,Int32 numArgs)\r\n   at System.Windows.Threading.ExceptionWrapper.TryCatchWhen(Object source,Delegate callback,Object args,Int32 numArgs,Delegate catchHandler)\r\n   at System.Windows.Threading.DispatcherOperation.InvokeImpl()\r\n   at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext,ContextCallback callback,Object state,Boolean preserveSyncCtx)\r\n   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext,ContextCallback callback,Object state,Boolean preserveSyncCtx)\r\n   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext,ContextCallback callback,Object state)\r\n   at MS.Internal.CulturePreservingExecutionContext.Run(CulturePreservingExecutionContext executionContext,ContextCallback callback,Object state)\r\n   at System.Windows.Threading.DispatcherOperation.Invoke()\r\n   at System.Windows.Threading.Dispatcher.ProcessQueue()\r\n   at System.Windows.Threading.Dispatcher.WndProcHook(IntPtr hwnd,Int32 msg,IntPtr wParam,IntPtr lParam,Boolean& handled)\r\n   at MS.Win32.HwndWrapper.WndProc(IntPtr hwnd,Int32 msg,IntPtr wParam,IntPtr lParam,Boolean& handled)\r\n   at MS.Win32.HwndSubclass.DispatcherCallbackOperation(Object o)\r\n   at System.Windows.Threading.ExceptionWrapper.InternalRealCall(Delegate callback,Object args,Int32 numArgs)\r\n   at System.Windows.Threading.ExceptionWrapper.TryCatchWhen(Object source,Delegate callback,Object args,Int32 numArgs,Delegate catchHandler)\r\n   at System.Windows.Threading.Dispatcher.LegacyInvokeImpl(DispatcherPriority priority,TimeSpan timeout,Delegate method,Object args,Int32 numArgs)\r\n   at MS.Win32.HwndSubclass.SubclassWndProc(IntPtr hwnd,Int32 msg,IntPtr wParam,IntPtr lParam)\r\n   at MS.Win32.UnsafeNativeMethods.DispatchMessage(MSG& msg)\r\n   at MS.Win32.UnsafeNativeMethods.DispatchMessage(MSG& msg)\r\n   at System.Windows.Threading.Dispatcher.PushFrameImpl(DispatcherFrame frame)\r\n   at System.Windows.Window.ShowHelper(Object booleanBox)\r\n   at System.Windows.Window.ShowDialog()\r\n   at RevitPythonShell.IronPythonConsoleCommand.Execute(ExternalCommandData commandData,String& message,ElementSet elements)\r\n   at apiManagedExecuteCommand(AString* assemblyName,AString* className,AString* vendorDescription,MFCApp* pMFCApp,DBView* pDBView,AString* message,Set<ElementId\\,std::less<ElementId>\\,tnallc<ElementId> >* ids,Map<AString\\,AString\\,std::less<AString>\\,tnallc<std::pair<AString const \\,AString> > >* data,AString* exceptionName,AString* exceptionMessage)\r\n   at RevitAPIUILinkBinder.revitAPIExecuteCommand(AString* )\r\n   at RevitAPIUILinkBinder.revitAPIExecuteCommand(AString* )\r\n   at UIFrameworkServices.ExternalCommandHelper.executeExternalCommand(String commandId)\r\n   at UIFramework.CustomRibbonItemHandler.Execute(Object parameter)\r\n   at Autodesk.Windows.InternalCommands.OnExecuteGenericCommand(Object sender,ExecutedRoutedEventArgs args)\r\n   at System.Windows.Input.CommandBinding.OnExecuted(Object sender,ExecutedRoutedEventArgs e)\r\n   at System.Windows.Input.CommandManager.ExecuteCommandBinding(Object sender,ExecutedRoutedEventArgs e,CommandBinding commandBinding)\r\n   at System.Windows.Input.CommandManager.FindCommandBinding(Object sender,RoutedEventArgs e,ICommand command,Boolean execute)\r\n   at System.Windows.Input.CommandManager.OnExecuted(Object sender,ExecutedRoutedEventArgs e)\r\n   at System.Windows.RoutedEventArgs.InvokeHandler(Delegate handler,Object target)\r\n   at System.Windows.RoutedEventHandlerInfo.InvokeHandler(Object target,RoutedEventArgs routedEventArgs)\r\n   at System.Windows.EventRoute.InvokeHandlersImpl(Object source,RoutedEventArgs args,Boolean reRaised)\r\n   at System.Windows.UIElement.RaiseEventImpl(DependencyObject sender,RoutedEventArgs args)\r\n   at System.Windows.Input.RoutedCommand.ExecuteImpl(Object parameter,IInputElement target,Boolean userInitiated)\r\n   at MS.Internal.Commands.CommandHelpers.CriticalExecuteCommandSource(ICommandSource commandSource,Boolean userInitiated)\r\n   at System.Windows.Controls.Primitives.ButtonBase.OnClick()\r\n   at Autodesk.Private.Windows.ComboButton.OnClick()\r\n   at System.Windows.Controls.Primitives.ButtonBase.OnMouseLeftButtonUp(MouseButtonEventArgs e)\r\n   at System.Windows.RoutedEventArgs.InvokeHandler(Delegate handler,Object target)\r\n   at System.Windows.RoutedEventHandlerInfo.InvokeHandler(Object target,RoutedEventArgs routedEventArgs)\r\n   at System.Windows.EventRoute.InvokeHandlersImpl(Object source,RoutedEventArgs args,Boolean reRaised)\r\n   at System.Windows.UIElement.ReRaiseEventAs(DependencyObject sender,RoutedEventArgs args,RoutedEvent newEvent)\r\n   at System.Windows.UIElement.OnMouseUpThunk(Object sender,MouseButtonEventArgs e)\r\n   at System.Windows.RoutedEventArgs.InvokeHandler(Delegate handler,Object target)\r\n   at System.Windows.RoutedEventHandlerInfo.InvokeHandler(Object target,RoutedEventArgs routedEventArgs)\r\n   at System.Windows.EventRoute.InvokeHandlersImpl(Object source,RoutedEventArgs args,Boolean reRaised)\r\n   at System.Windows.UIElement.RaiseEventImpl(DependencyObject sender,RoutedEventArgs args)\r\n   at System.Windows.UIElement.RaiseTrustedEvent(RoutedEventArgs args)\r\n   at System.Windows.Input.InputManager.ProcessStagingArea()\r\n   at System.Windows.Input.InputManager.ProcessInput(InputEventArgs input)\r\n   at System.Windows.Input.InputProviderSite.ReportInput(InputReport inputReport)\r\n   at System.Windows.Interop.HwndMouseInputProvider.ReportInput(IntPtr hwnd,InputMode mode,Int32 timestamp,RawMouseActions actions,Int32 x,Int32 y,Int32 wheel)\r\n   at System.Windows.Interop.HwndMouseInputProvider.FilterMessage(IntPtr hwnd,WindowMessage msg,IntPtr wParam,IntPtr lParam,Boolean& handled)\r\n   at System.Windows.Interop.HwndSource.InputFilterMessage(IntPtr hwnd,Int32 msg,IntPtr wParam,IntPtr lParam,Boolean& handled)\r\n   at MS.Win32.HwndWrapper.WndProc(IntPtr hwnd,Int32 msg,IntPtr wParam,IntPtr lParam,Boolean& handled)\r\n   at MS.Win32.HwndSubclass.DispatcherCallbackOperation(Object o)\r\n   at System.Windows.Threading.ExceptionWrapper.InternalRealCall(Delegate callback,Object args,Int32 numArgs)\r\n   at System.Windows.Threading.ExceptionWrapper.TryCatchWhen(Object source,Delegate callback,Object args,Int32 numArgs,Delegate catchHandler)\r\n   at System.Windows.Threading.Dispatcher.LegacyInvokeImpl(DispatcherPriority priority,TimeSpan timeout,Delegate method,Object args,Int32 numArgs)\r\n   at MS.Win32.HwndSubclass.SubclassWndProc(IntPtr hwnd,Int32 msg,IntPtr wParam,IntPtr lParam)'
 SystemDirectory='C:\\WINDOWS\\system32'
 SystemPageSize=4096
 TickCount=10105453
 UserDomainName='STUDIO-SSD'
 UserInteractive=True
 UserName='gtalarico'
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

