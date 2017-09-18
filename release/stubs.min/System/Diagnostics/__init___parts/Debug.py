class Debug(object):
 """ Provides a set of methods and properties that help debug your code. This class cannot be inherited. """
 @staticmethod
 def Assert(condition,message=None,*__args):
  """
  Assert(condition: bool,message: str,detailMessage: str)

   Checks for a condition; if the condition is false,outputs two specified messages and displays a 

    message box that shows the call stack.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the specified messages are not 

    sent and the message box is not displayed.

  

   message: The message to send to the System.Diagnostics.Trace.Listeners collection.

   detailMessage: The detailed message to send to the System.Diagnostics.Trace.Listeners collection.

  Assert(condition: bool,message: str,detailMessageFormat: str,*args: Array[object])

   Checks for a condition; if the condition is false,outputs two messages (simple and formatted) 

    and displays a message box that shows the call stack.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the specified messages are not 

    sent and the message box is not displayed.

  

   message: The message to send to the System.Diagnostics.Trace.Listeners collection.

   detailMessageFormat: The composite format string (see Remarks) to send to the System.Diagnostics.Trace.Listeners 

    collection. This message contains text intermixed with zero or more format items,which 

    correspond to objects in the args array.

  

   args: An object array that contains zero or more objects to format.

  Assert(condition: bool)

   Checks for a condition; if the condition is false,displays a message box that shows the call 

    stack.

  

  

   condition: The conditional expression to evaluate. If the condition is true,a failure message is not sent 

    and the message box is not displayed.

  

  Assert(condition: bool,message: str)

   Checks for a condition; if the condition is false,outputs a specified message and displays a 

    message box that shows the call stack.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the specified message is not 

    sent and the message box is not displayed.

  

   message: The message to send to the System.Diagnostics.Trace.Listeners collection.
  """
  pass
 @staticmethod
 def Close():
  """
  Close()

   Flushes the output buffer and then calls the Close method on each of the 

    System.Diagnostics.Debug.Listeners.
  """
  pass
 @staticmethod
 def Fail(message,detailMessage=None):
  """
  Fail(message: str,detailMessage: str)

   Emits an error message and a detailed error message.

  

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

   Flushes the output buffer and causes buffered data to write to the 

    System.Diagnostics.Debug.Listeners collection.
  """
  pass
 @staticmethod
 def Indent():
  """
  Indent()

   Increases the current System.Diagnostics.Debug.IndentLevel by one.
  """
  pass
 @staticmethod
 def Print(*__args):
  """
  Print(format: str,*args: Array[object])

   Writes a formatted string followed by a line terminator to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection.

  

  

   format: A composite format string (see Remarks) that contains text intermixed with zero or more format 

    items,which correspond to objects in the args array.

  

   args: An object array containing zero or more objects to format.

  Print(message: str)

   Writes a message followed by a line terminator to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection.

  

  

   message: The message to write.
  """
  pass
 @staticmethod
 def Unindent():
  """
  Unindent()

   Decreases the current System.Diagnostics.Debug.IndentLevel by one.
  """
  pass
 @staticmethod
 def Write(*__args):
  """
  Write(message: str,category: str)

   Writes a category name and message to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection.

  

  

   message: A message to write.

   category: A category name used to organize the output.

  Write(value: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the trace 

    listeners in the System.Diagnostics.Debug.Listeners collection.

  

  

   value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

   category: A category name used to organize the output.

  Write(message: str)

   Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection.

  

   message: A message to write.

  Write(value: object)

   Writes the value of the object's System.Object.ToString method to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection.

  

  

   value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
  """
  pass
 @staticmethod
 def WriteIf(condition,*__args):
  """
  WriteIf(condition: bool,message: str,category: str)

   Writes a category name and message to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection if a condition is true.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the category name and message 

    are written to the trace listeners in the collection.

  

   message: A message to write.

   category: A category name used to organize the output.

  WriteIf(condition: bool,value: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the trace 

    listeners in the System.Diagnostics.Debug.Listeners collection if a condition is true.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the category name and value 

    are written to the trace listeners in the collection.

  

   value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

   category: A category name used to organize the output.

  WriteIf(condition: bool,message: str)

   Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection if 

    a condition is true.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the message is written to the 

    trace listeners in the collection.

  

   message: A message to write.

  WriteIf(condition: bool,value: object)

   Writes the value of the object's System.Object.ToString method to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection if a condition is true.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the value is written to the 

    trace listeners in the collection.

  

   value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
  """
  pass
 @staticmethod
 def WriteLine(*__args):
  """
  WriteLine(value: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the trace 

    listeners in the System.Diagnostics.Debug.Listeners collection.

  

  

   value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

   category: A category name used to organize the output.

  WriteLine(format: str,*args: Array[object])

   Writes a formatted message followed by a line terminator to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection.

  

  

   format: A composite format string (see Remarks) that contains text intermixed with zero or more format 

    items,which correspond to objects in the args array.

  

   args: An object array containing zero or more objects to format.

  WriteLine(message: str,category: str)

   Writes a category name and message to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection.

  

  

   message: A message to write.

   category: A category name used to organize the output.

  WriteLine(message: str)

   Writes a message followed by a line terminator to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection.

  

  

   message: A message to write.

  WriteLine(value: object)

   Writes the value of the object's System.Object.ToString method to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection.

  

  

   value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
  """
  pass
 @staticmethod
 def WriteLineIf(condition,*__args):
  """
  WriteLineIf(condition: bool,message: str,category: str)

   Writes a category name and message to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection if a condition is true.

  

  

   condition: true to cause a message to be written; otherwise,false.

   message: A message to write.

   category: A category name used to organize the output.

  WriteLineIf(condition: bool,value: object,category: str)

   Writes a category name and the value of the object's System.Object.ToString method to the trace 

    listeners in the System.Diagnostics.Debug.Listeners collection if a condition is true.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the category name and value 

    are written to the trace listeners in the collection.

  

   value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.

   category: A category name used to organize the output.

  WriteLineIf(condition: bool,message: str)

   Writes a message to the trace listeners in the System.Diagnostics.Debug.Listeners collection if 

    a condition is true.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the message is written to the 

    trace listeners in the collection.

  

   message: A message to write.

  WriteLineIf(condition: bool,value: object)

   Writes the value of the object's System.Object.ToString method to the trace listeners in the 

    System.Diagnostics.Debug.Listeners collection if a condition is true.

  

  

   condition: The conditional expression to evaluate. If the condition is true,the value is written to the 

    trace listeners in the collection.

  

   value: An object whose name is sent to the System.Diagnostics.Debug.Listeners.
  """
  pass
 AutoFlush=False
 IndentLevel=0
 IndentSize=4
 Listeners=None
 __all__=[
  'Assert',
  'Close',
  'Fail',
  'Flush',
  'Indent',
  'Print',
  'Unindent',
  'Write',
  'WriteIf',
  'WriteLine',
  'WriteLineIf',
 ]

