class Application(object):
 """ Provides static methods and properties to manage an application,such as methods to start and stop an application,to process Windows messages,and properties to get information about an application. This class cannot be inherited. """
 @staticmethod
 def AddMessageFilter(value):
  """
  AddMessageFilter(value: IMessageFilter)

   Adds a message filter to monitor Windows messages as they are routed to their destinations.

  

   value: The implementation of the System.Windows.Forms.IMessageFilter interface you want to install.
  """
  pass
 @staticmethod
 def DoEvents():
  """
  DoEvents()

   Processes all Windows messages currently in the message queue.
  """
  pass
 @staticmethod
 def EnableVisualStyles():
  """
  EnableVisualStyles()

   Enables visual styles for the application.
  """
  pass
 @staticmethod
 def Exit(e=None):
  """
  Exit(e: CancelEventArgs)

   Informs all message pumps that they must terminate,and then closes all application windows 

    after the messages have been processed.

  

  

   e: Returns whether any System.Windows.Forms.Form within the application cancelled the exit.

  Exit()

   Informs all message pumps that they must terminate,and then closes all application windows 

    after the messages have been processed.
  """
  pass
 @staticmethod
 def ExitThread():
  """
  ExitThread()

   Exits the message loop on the current thread and closes all windows on the thread.
  """
  pass
 @staticmethod
 def FilterMessage(message):
  """
  FilterMessage(message: Message) -> (bool,Message)

  

   Runs any filters against a window message,and returns a copy of the modified message.

  

   message: The Windows event message to filter.

   Returns: True if the filters were processed; otherwise,false.
  """
  pass
 @staticmethod
 def OleRequired():
  """
  OleRequired() -> ApartmentState

  

   Initializes OLE on the current thread.

   Returns: One of the System.Threading.ApartmentState values.
  """
  pass
 @staticmethod
 def OnThreadException(t):
  """
  OnThreadException(t: Exception)

   Raises the System.Windows.Forms.Application.ThreadException event.

  

   t: An System.Exception that represents the exception that was thrown.
  """
  pass
 @staticmethod
 def RaiseIdle(e):
  """
  RaiseIdle(e: EventArgs)

   Raises the System.Windows.Forms.Application.Idle event in hosted scenarios.

  

   e: The System.EventArgs objects to pass to the System.Windows.Forms.Application.Idle event.
  """
  pass
 @staticmethod
 def RegisterMessageLoop(callback):
  """ RegisterMessageLoop(callback: MessageLoopCallback) """
  pass
 @staticmethod
 def RemoveMessageFilter(value):
  """
  RemoveMessageFilter(value: IMessageFilter)

   Removes a message filter from the message pump of the application.

  

   value: The implementation of the System.Windows.Forms.IMessageFilter to remove from the application.
  """
  pass
 @staticmethod
 def Restart():
  """
  Restart()

   Shuts down the application and starts a new instance immediately.
  """
  pass
 @staticmethod
 def Run(*__args):
  """
  Run(context: ApplicationContext)

   Begins running a standard application message loop on the current thread,with an 

    System.Windows.Forms.ApplicationContext.

  

  

   context: An System.Windows.Forms.ApplicationContext in which the application is run.

  Run(mainForm: Form)

   Begins running a standard application message loop on the current thread,and makes the 

    specified form visible.

  

  

   mainForm: A System.Windows.Forms.Form that represents the form to make visible.

  Run()

   Begins running a standard application message loop on the current thread,without a form.
  """
  pass
 @staticmethod
 def SetCompatibleTextRenderingDefault(defaultValue):
  """
  SetCompatibleTextRenderingDefault(defaultValue: bool)

   Sets the application-wide default for the UseCompatibleTextRendering property defined on certain 

    controls.

  

  

   defaultValue: The default value to use for new controls. If true,new controls that support 

    UseCompatibleTextRendering use the GDI+ based System.Drawing.Graphics class for text rendering; 

    if false,new controls use the GDI�based System.Windows.Forms.TextRenderer class.
  """
  pass
 @staticmethod
 def SetSuspendState(state,force,disableWakeEvent):
  """
  SetSuspendState(state: PowerState,force: bool,disableWakeEvent: bool) -> bool

  

   Suspends or hibernates the system,or requests that the system be suspended or hibernated.

  

   state: A System.Windows.Forms.PowerState indicating the power activity mode to which to transition.

   force: true to force the suspended mode immediately; false to cause Windows to send a suspend request 

    to every application.

  

   disableWakeEvent: true to disable restoring the system's power status to active on a wake event,false to enable 

    restoring the system's power status to active on a wake event.

  

   Returns: true if the system is being suspended,otherwise,false.
  """
  pass
 @staticmethod
 def SetUnhandledExceptionMode(mode,threadScope=None):
  """
  SetUnhandledExceptionMode(mode: UnhandledExceptionMode,threadScope: bool)

   Instructs the application how to respond to unhandled exceptions,optionally applying 

    thread-specific behavior.

  

  

   mode: An System.Windows.Forms.UnhandledExceptionMode value describing how the application should 

    behave if an exception is thrown without being caught.

  

   threadScope: true to set the thread exception mode; otherwise,false.

  SetUnhandledExceptionMode(mode: UnhandledExceptionMode)

   Instructs the application how to respond to unhandled exceptions.

  

   mode: An System.Windows.Forms.UnhandledExceptionMode value describing how the application should 

    behave if an exception is thrown without being caught.
  """
  pass
 @staticmethod
 def UnregisterMessageLoop():
  """
  UnregisterMessageLoop()

   Unregisters the message loop callback made with 

    System.Windows.Forms.Application.RegisterMessageLoop(System.Windows.Forms.Application.MessageLoop

    Callback).
  """
  pass
 AllowQuit=False
 ApplicationExit=None
 CommonAppDataPath='C:\\ProgramData\\IronPython Team\\IronPython\\IronPython 2.7.7 final 0'
 CompanyName='IronPython Team'
 CurrentCulture=None
 CurrentInputLanguage=None
 EnterThreadModal=None
 ExecutablePath='C:\\Program Files (x86)\\IronPython-2.7.7\\ipy.exe'
 Idle=None
 LeaveThreadModal=None
 LocalUserAppDataPath='C:\\Users\\gtalarico\\AppData\\Local\\IronPython Team\\IronPython\\IronPython 2.7.7 final 0'
 MessageLoop=False
 MessageLoopCallback=None
 OpenForms=None
 ProductName='IronPython'
 ProductVersion='IronPython 2.7.7 final 0'
 RenderWithVisualStyles=False
 SafeTopLevelCaptionFormat='{1} - {0} - {2}'
 StartupPath='C:\\Program Files (x86)\\IronPython-2.7.7'
 ThreadException=None
 ThreadExit=None
 UserAppDataPath='C:\\Users\\gtalarico\\AppData\\Roaming\\IronPython Team\\IronPython\\IronPython 2.7.7 final 0'
 UserAppDataRegistry=None
 UseWaitCursor=False
 VisualStyleState=None

