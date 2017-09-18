class Trace(object):
 """ Provides a set of methods and properties that help you trace the execution of your code. This class cannot be inherited. """
 @staticmethod
 def Assert(condition,message=None,detailMessage=None):
  """
  Assert(condition: bool,message: str,detailMessage: str)

   Checks for a condition; if the condition is false,outputs two specified messages and displays a 

    message box that shows the call stack.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the specified messages are not 

    sent and the message box is not displayed.

  

   message: The message to send to the System.Diagnostics.Trace.Listeners collection.

   detailMessage: The detailed message to send to the System.Diagnostics.Trace.Listeners collection.

  Assert(condition: bool,message: str)

   Checks for a condition; if the condition is false,outputs a specified message and displays a 

    message box that shows the call stack.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the specified message is not 

    sent and the message box is not displayed.

  

   message: The message to send to the System.Diagnostics.Trace.Listeners collection.

  Assert(condition: bool)

   Checks for a condition; if the condition is false,displays a message box that shows the call 

    stack.

  

  

   condition: The conditional expression to evaluate. If the condition is true,a failure message is not sent 

    and the message box is not displayed.
  """
  pass
 @staticmethod
 def Close():
  """
  Close()

   Flushes the output buffer,and then closes the System.Diagnostics.Trace.Listeners.
  """
  pass
 @staticmethod
 def Fail(message,detailMessage=None):
  """
  Fail(message: str,detailMessage: str)

   Emits an error message,and a detailed error message.

  

   message: A message to emit.

   detailMessage: A detailed message to emit.

  Fail(message: str)

   Emits the specified error message.

  

   message: A message to emit.
  """
  pass
 @staticmethod
 def Flush():
  """
  Flush()

   Flushes the output buffer,and causes buffered data to be written to the 

    System.Diagnostics.Trace.Listeners.
  """
  pass
 @staticmethod
 def Indent():
  """
  Indent()

   Increases the current System.Diagnostics.Trace.IndentLevel by one.
  """
  pass
 @staticmethod
 def Refresh():
  """
  Refresh()

   Refreshes the trace configuration data.
  """
  pass
 @staticmethod
 def TraceError(*__args):
  """
  TraceError(format: str,*args: Array[object])

   Writes an error message to the trace listeners in the System.Diagnostics.Trace.Listeners 

    collection using the specified array of objects and formatting information.

  

  

   format: A format string that contains zero or more format items,which correspond to objects in the args 

    array.

  

   args: An object array containing zero or more objects to format.

  TraceError(message: str)

   Writes an error message to the trace listeners in the System.Diagnostics.Trace.Listeners 

    collection using the specified message.

  

  

   message: The informative message to write.
  """
  pass
 @staticmethod
 def TraceInformation(*__args):
  """
  TraceInformation(format: str,*args: Array[object])

   Writes an informational message to the trace listeners in the System.Diagnostics.Trace.Listeners 

    collection using the specified array of objects and formatting information.

  

  

   format: A format string that contains zero or more format items,which correspond to objects in the args 

    array.

  

   args: An object array containing zero or more objects to format.

  TraceInformation(message: str)

   Writes an informational message to the trace listeners in the System.Diagnostics.Trace.Listeners 

    collection using the specified message.

  

  

   message: The informative message to write.
  """
  pass
 @staticmethod
 def TraceWarning(*__args):
  """
  TraceWarning(format: str,*args: Array[object])

   Writes a warning message to the trace listeners in the System.Diagnostics.Trace.Listeners 

    collection using the specified array of objects and formatting information.

  

  

   format: A format string that contains zero or more format items,which correspond to objects in the args 

    array.

  

   args: An object array containing zero or more objects to format.

  TraceWarning(message: str)

   Writes a warning message to the trace listeners in the System.Diagnostics.Trace.Listeners 

    collection using the specified message.

  

  

   message: The informative message to write.
  """
  pass
 @staticmethod
 def Unindent():
  """
  Unindent()

   Decreases the current System.Diagnostics.Trace.IndentLevel by one.
  """
  pass
 @staticmethod
 def Write(*__args):
  """
  Write(message: str,category: str)

   Writes a category name and a message to the trace listeners in the 

    System.Diagnostics.Trace.Listeners collection.

  

  

   message: A message to write.

   category: A category name used to organize the output.

  Write(value: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the trace 

    listeners in the System.Diagnostics.Trace.Listeners collection.

  

  

   value: An System.Object name is sent to the System.Diagnostics.Trace.Listeners.

   category: A category name used to organize the output.

  Write(message: str)

   Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

  

   message: A message to write.

  Write(value: object)

   Writes the value of the object's System.Object.ToString method to the trace listeners in the 

    System.Diagnostics.Trace.Listeners collection.

  

  

   value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
  """
  pass
 @staticmethod
 def WriteIf(condition,*__args):
  """
  WriteIf(condition: bool,message: str,category: str)

   Writes a category name and message to the trace listeners in the 

    System.Diagnostics.Trace.Listeners collection if a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   message: A message to write.

   category: A category name used to organize the output.

  WriteIf(condition: bool,value: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the trace 

    listeners in the System.Diagnostics.Trace.Listeners collection if a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

   category: A category name used to organize the output.

  WriteIf(condition: bool,message: str)

   Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection if 

    a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   message: A message to write.

  WriteIf(condition: bool,value: object)

   Writes the value of the object's System.Object.ToString method to the trace listeners in the 

    System.Diagnostics.Trace.Listeners collection if a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
  """
  pass
 @staticmethod
 def WriteLine(*__args):
  """
  WriteLine(message: str,category: str)

   Writes a category name and message to the trace listeners in the 

    System.Diagnostics.Trace.Listeners collection.

  

  

   message: A message to write.

   category: A category name used to organize the output.

  WriteLine(value: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the trace 

    listeners in the System.Diagnostics.Trace.Listeners collection.

  

  

   value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

   category: A category name used to organize the output.

  WriteLine(message: str)

   Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection.

  

   message: A message to write.

  WriteLine(value: object)

   Writes the value of the object's System.Object.ToString method to the trace listeners in the 

    System.Diagnostics.Trace.Listeners collection.

  

  

   value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
  """
  pass
 @staticmethod
 def WriteLineIf(condition,*__args):
  """
  WriteLineIf(condition: bool,message: str,category: str)

   Writes a category name and message to the trace listeners in the 

    System.Diagnostics.Trace.Listeners collection if a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   message: A message to write.

   category: A category name used to organize the output.

  WriteLineIf(condition: bool,value: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the trace 

    listeners in the System.Diagnostics.Trace.Listeners collection if a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.

   category: A category name used to organize the output.

  WriteLineIf(condition: bool,message: str)

   Writes a message to the trace listeners in the System.Diagnostics.Trace.Listeners collection if 

    a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   message: A message to write.

  WriteLineIf(condition: bool,value: object)

   Writes the value of the object's System.Object.ToString method to the trace listeners in the 

    System.Diagnostics.Trace.Listeners collection if a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   value: An System.Object whose name is sent to the System.Diagnostics.Trace.Listeners.
  """
  pass
 AutoFlush=False
 CorrelationManager=None
 IndentLevel=0
 IndentSize=4
 Listeners=None
 UseGlobalLock=True

