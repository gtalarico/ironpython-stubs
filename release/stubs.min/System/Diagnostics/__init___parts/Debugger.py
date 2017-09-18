class Debugger(object):
 """
 Enables communication with a debugger. This class cannot be inherited.

 

 Debugger()
 """
 @staticmethod
 def Break():
  """
  Break()

   Signals a breakpoint to an attached debugger.
  """
  pass
 @staticmethod
 def IsLogging():
  """
  IsLogging() -> bool

  

   Checks to see if logging is enabled by an attached debugger.

   Returns: true if a debugger is attached and logging is enabled; otherwise,false. The attached debugger 

    is the registered managed debugger in the DbgManagedDebugger registry key. For more information 

    on this key,see Enabling JIT-Attach Debugging.
  """
  pass
 @staticmethod
 def Launch():
  """
  Launch() -> bool

  

   Launches and attaches a debugger to the process.

   Returns: true if the startup is successful or if the debugger is already attached; otherwise,false.
  """
  pass
 @staticmethod
 def Log(level,category,message):
  """
  Log(level: int,category: str,message: str)

   Posts a message for the attached debugger.

  

   level: A description of the importance of the message.

   category: The category of the message.

   message: The message to show.
  """
  pass
 @staticmethod
 def NotifyOfCrossThreadDependency():
  """
  NotifyOfCrossThreadDependency()

   Notifies a debugger that execution is about to enter a path that involves a cross-thread 

    dependency.
  """
  pass
 DefaultCategory=None
 IsAttached=False

