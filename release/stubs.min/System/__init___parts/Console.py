class Console(object):
 """ Represents the standard input,output,and error streams for console applications. This class cannot be inherited. """
 @staticmethod
 def Beep(frequency=None,duration=None):
  """
  Beep(frequency: int,duration: int)

   Plays the sound of a beep of a specified frequency and duration through the console speaker.

  

   frequency: The frequency of the beep,ranging from 37 to 32767 hertz.

   duration: The duration of the beep measured in milliseconds.

  Beep()

   Plays the sound of a beep through the console speaker.
  """
  pass
 @staticmethod
 def Clear():
  """
  Clear()

   Clears the console buffer and corresponding console window of display information.
  """
  pass
 @staticmethod
 def MoveBufferArea(sourceLeft,sourceTop,sourceWidth,sourceHeight,targetLeft,targetTop,sourceChar=None,sourceForeColor=None,sourceBackColor=None):
  """
  MoveBufferArea(sourceLeft: int,sourceTop: int,sourceWidth: int,sourceHeight: int,targetLeft: int,targetTop: int,sourceChar: Char,sourceForeColor: ConsoleColor,sourceBackColor: ConsoleColor)

   Copies a specified source area of the screen buffer to a specified destination area.

  

   sourceLeft: The leftmost column of the source area.

   sourceTop: The topmost row of the source area.

   sourceWidth: The number of columns in the source area.

   sourceHeight: The number of rows in the source area.

   targetLeft: The leftmost column of the destination area.

   targetTop: The topmost row of the destination area.

   sourceChar: The character used to fill the source area.

   sourceForeColor: The foreground color used to fill the source area.

   sourceBackColor: The background color used to fill the source area.

  MoveBufferArea(sourceLeft: int,sourceTop: int,sourceWidth: int,sourceHeight: int,targetLeft: int,targetTop: int)

   Copies a specified source area of the screen buffer to a specified destination area.

  

   sourceLeft: The leftmost column of the source area.

   sourceTop: The topmost row of the source area.

   sourceWidth: The number of columns in the source area.

   sourceHeight: The number of rows in the source area.

   targetLeft: The leftmost column of the destination area.

   targetTop: The topmost row of the destination area.
  """
  pass
 @staticmethod
 def OpenStandardError(bufferSize=None):
  """
  OpenStandardError(bufferSize: int) -> Stream

  

   Acquires the standard error stream,which is set to a specified buffer size.

  

   bufferSize: The internal stream buffer size.

   Returns: The standard error stream.

  OpenStandardError() -> Stream

  

   Acquires the standard error stream.

   Returns: The standard error stream.
  """
  pass
 @staticmethod
 def OpenStandardInput(bufferSize=None):
  """
  OpenStandardInput(bufferSize: int) -> Stream

  

   Acquires the standard input stream,which is set to a specified buffer size.

  

   bufferSize: The internal stream buffer size.

   Returns: The standard input stream.

  OpenStandardInput() -> Stream

  

   Acquires the standard input stream.

   Returns: The standard input stream.
  """
  pass
 @staticmethod
 def OpenStandardOutput(bufferSize=None):
  """
  OpenStandardOutput(bufferSize: int) -> Stream

  

   Acquires the standard output stream,which is set to a specified buffer size.

  

   bufferSize: The internal stream buffer size.

   Returns: The standard output stream.

  OpenStandardOutput() -> Stream

  

   Acquires the standard output stream.

   Returns: The standard output stream.
  """
  pass
 @staticmethod
 def Read():
  """
  Read() -> int

  

   Reads the next character from the standard input stream.

   Returns: The next character from the input stream,or negative one (-1) if there are currently no more 

    characters to be read.
  """
  pass
 @staticmethod
 def ReadKey(intercept=None):
  """
  ReadKey(intercept: bool) -> ConsoleKeyInfo

  

   Obtains the next character or function key pressed by the user. The pressed key is optionally 

    displayed in the console window.

  

  

   intercept: Determines whether to display the pressed key in the console window. true to not display the 

    pressed key; otherwise,false.

  

   Returns: A System.ConsoleKeyInfo object that describes the System.ConsoleKey constant and Unicode 

    character,if any,that correspond to the pressed console key. The System.ConsoleKeyInfo object 

    also describes,in a bitwise combination of System.ConsoleModifiers values,whether one or more 

    SHIFT,ALT,or CTRL modifier keys was pressed simultaneously with the console key.

  

  ReadKey() -> ConsoleKeyInfo

  

   Obtains the next character or function key pressed by the user. The pressed key is displayed in 

    the console window.

  

   Returns: A System.ConsoleKeyInfo object that describes the System.ConsoleKey constant and Unicode 

    character,if any,that correspond to the pressed console key. The System.ConsoleKeyInfo object 

    also describes,in a bitwise combination of System.ConsoleModifiers values,whether one or more 

    SHIFT,ALT,or CTRL modifier keys was pressed simultaneously with the console key.
  """
  pass
 @staticmethod
 def ReadLine():
  """
  ReadLine() -> str

  

   Reads the next line of characters from the standard input stream.

   Returns: The next line of characters from the input stream,or null if no more lines are available.
  """
  pass
 @staticmethod
 def ResetColor():
  """
  ResetColor()

   Sets the foreground and background console colors to their defaults.
  """
  pass
 @staticmethod
 def SetBufferSize(width,height):
  """
  SetBufferSize(width: int,height: int)

   Sets the height and width of the screen buffer area to the specified values.

  

   width: The width of the buffer area measured in columns.

   height: The height of the buffer area measured in rows.
  """
  pass
 @staticmethod
 def SetCursorPosition(left,top):
  """
  SetCursorPosition(left: int,top: int)

   Sets the position of the cursor.

  

   left: The column position of the cursor.

   top: The row position of the cursor.
  """
  pass
 @staticmethod
 def SetError(newError):
  """
  SetError(newError: TextWriter)

   Sets the System.Console.Error property to the specified System.IO.TextWriter object.

  

   newError: A stream that is the new standard error output.
  """
  pass
 @staticmethod
 def SetIn(newIn):
  """
  SetIn(newIn: TextReader)

   Sets the System.Console.In property to the specified System.IO.TextReader object.

  

   newIn: A stream that is the new standard input.
  """
  pass
 @staticmethod
 def SetOut(newOut):
  """
  SetOut(newOut: TextWriter)

   Sets the System.Console.Out property to the specified System.IO.TextWriter object.

  

   newOut: A stream that is the new standard output.
  """
  pass
 @staticmethod
 def SetWindowPosition(left,top):
  """
  SetWindowPosition(left: int,top: int)

   Sets the position of the console window relative to the screen buffer.

  

   left: The column position of the upper left  corner of the console window.

   top: The row position of the upper left corner of the console window.
  """
  pass
 @staticmethod
 def SetWindowSize(width,height):
  """
  SetWindowSize(width: int,height: int)

   Sets the height and width of the console window to the specified values.

  

   width: The width of the console window measured in columns.

   height: The height of the console window measured in rows.
  """
  pass
 @staticmethod
 def Write(*__args):
  """
  Write(value: Single)

   Writes the text representation of the specified single-precision floating-point value to the 

    standard output stream.

  

  

   value: The value to write.

  Write(value: int)

   Writes the text representation of the specified 32-bit signed integer value to the standard 

    output stream.

  

  

   value: The value to write.

  Write(value: float)

   Writes the text representation of the specified double-precision floating-point value to the 

    standard output stream.

  

  

   value: The value to write.

  Write(value: Decimal)

   Writes the text representation of the specified System.Decimal value to the standard output 

    stream.

  

  

   value: The value to write.

  Write(value: UInt32)

   Writes the text representation of the specified 32-bit unsigned integer value to the standard 

    output stream.

  

  

   value: The value to write.

  Write(value: object)

   Writes the text representation of the specified object to the standard output stream.

  

   value: The value to write,or null.

  Write(value: str)

   Writes the specified string value to the standard output stream.

  

   value: The value to write.

  Write(value: Int64)

   Writes the text representation of the specified 64-bit signed integer value to the standard 

    output stream.

  

  

   value: The value to write.

  Write(value: UInt64)

   Writes the text representation of the specified 64-bit unsigned integer value to the standard 

    output stream.

  

  

   value: The value to write.

  Write(format: str,arg0: object,arg1: object,arg2: object)

   Writes the text representation of the specified objects to the standard output stream using the 

    specified format information.

  

  

   format: A composite format string (see Remarks).

   arg0: The first object to write using format.

   arg1: The second object to write using format.

   arg2: The third object to write using format.

  Write(format: str,arg0: object,arg1: object,arg2: object,arg3: object)

   Writes the text representation of the specified objects and variable-length parameter list to 

    the standard output stream using the specified format information.

  

  

   format: A composite format string (see Remarks).

   arg0: The first object to write using format.

   arg1: The second object to write using format.

   arg2: The third object to write using format.

   arg3: The fourth object to write using format.

  Write(format: str,arg0: object)

   Writes the text representation of the specified object to the standard output stream using the 

    specified format information.

  

  

   format: A composite format string (see Remarks).

   arg0: An object to write using format.

  Write(format: str,arg0: object,arg1: object)

   Writes the text representation of the specified objects to the standard output stream using the 

    specified format information.

  

  

   format: A composite format string (see Remarks).

   arg0: The first object to write using format.

   arg1: The second object to write using format.

  Write(format: str,*arg: Array[object])

   Writes the text representation of the specified array of objects to the standard output stream 

    using the specified format information.

  

  

   format: A composite format string (see Remarks).

   arg: An array of objects to write using format.

  Write(buffer: Array[Char])

   Writes the specified array of Unicode characters to the standard output stream.

  

   buffer: A Unicode character array.

  Write(buffer: Array[Char],index: int,count: int)

   Writes the specified subarray of Unicode characters to the standard output stream.

  

   buffer: An array of Unicode characters.

   index: The starting position in buffer.

   count: The number of characters to write.

  Write(value: bool)

   Writes the text representation of the specified Boolean value to the standard output stream.

  

   value: The value to write.

  Write(value: Char)

   Writes the specified Unicode character value to the standard output stream.

  

   value: The value to write.
  """
  pass
 @staticmethod
 def WriteLine(*__args):
  """
  WriteLine(value: object)

   Writes the text representation of the specified object,followed by the current line terminator,

    to the standard output stream.

  

  

   value: The value to write.

  WriteLine(value: str)

   Writes the specified string value,followed by the current line terminator,to the standard 

    output stream.

  

  

   value: The value to write.

  WriteLine(value: Int64)

   Writes the text representation of the specified 64-bit signed integer value,followed by the 

    current line terminator,to the standard output stream.

  

  

   value: The value to write.

  WriteLine(value: UInt64)

   Writes the text representation of the specified 64-bit unsigned integer value,followed by the 

    current line terminator,to the standard output stream.

  

  

   value: The value to write.

  WriteLine(format: str,arg0: object)

   Writes the text representation of the specified object,followed by the current line terminator,

    to the standard output stream using the specified format information.

  

  

   format: A composite format string (see Remarks).

   arg0: An object to write using format.

  WriteLine(format: str,arg0: object,arg1: object,arg2: object,arg3: object)

   Writes the text representation of the specified objects and variable-length parameter list,

    followed by the current line terminator,to the standard output stream using the specified 

    format information.

  

  

   format: A composite format string (see Remarks).

   arg0: The first object to write using format.

   arg1: The second object to write using format.

   arg2: The third object to write using format.

   arg3: The fourth object to write using format.

  WriteLine(format: str,*arg: Array[object])

   Writes the text representation of the specified array of objects,followed by the current line 

    terminator,to the standard output stream using the specified format information.

  

  

   format: A composite format string (see Remarks).

   arg: An array of objects to write using format.

  WriteLine(format: str,arg0: object,arg1: object)

   Writes the text representation of the specified objects,followed by the current line 

    terminator,to the standard output stream using the specified format information.

  

  

   format: A composite format string (see Remarks).

   arg0: The first object to write using format.

   arg1: The second object to write using format.

  WriteLine(format: str,arg0: object,arg1: object,arg2: object)

   Writes the text representation of the specified objects,followed by the current line 

    terminator,to the standard output stream using the specified format information.

  

  

   format: A composite format string (see Remarks).

   arg0: The first object to write using format.

   arg1: The second object to write using format.

   arg2: The third object to write using format.

  WriteLine(value: UInt32)

   Writes the text representation of the specified 32-bit unsigned integer value,followed by the 

    current line terminator,to the standard output stream.

  

  

   value: The value to write.

  WriteLine(value: Char)

   Writes the specified Unicode character,followed by the current line terminator,value to the 

    standard output stream.

  

  

   value: The value to write.

  WriteLine(buffer: Array[Char])

   Writes the specified array of Unicode characters,followed by the current line terminator,to 

    the standard output stream.

  

  

   buffer: A Unicode character array.

  WriteLine()

   Writes the current line terminator to the standard output stream.

  WriteLine(value: bool)

   Writes the text representation of the specified Boolean value,followed by the current line 

    terminator,to the standard output stream.

  

  

   value: The value to write.

  WriteLine(buffer: Array[Char],index: int,count: int)

   Writes the specified subarray of Unicode characters,followed by the current line terminator,to 

    the standard output stream.

  

  

   buffer: An array of Unicode characters.

   index: The starting position in buffer.

   count: The number of characters to write.

  WriteLine(value: Single)

   Writes the text representation of the specified single-precision floating-point value,followed 

    by the current line terminator,to the standard output stream.

  

  

   value: The value to write.

  WriteLine(value: int)

   Writes the text representation of the specified 32-bit signed integer value,followed by the 

    current line terminator,to the standard output stream.

  

  

   value: The value to write.

  WriteLine(value: Decimal)

   Writes the text representation of the specified System.Decimal value,followed by the current 

    line terminator,to the standard output stream.

  

  

   value: The value to write.

  WriteLine(value: float)

   Writes the text representation of the specified double-precision floating-point value,followed 

    by the current line terminator,to the standard output stream.

  

  

   value: The value to write.
  """
  pass
 BackgroundColor=None
 BufferHeight=1000
 BufferWidth=127
 CancelKeyPress=None
 CapsLock=False
 CursorLeft=0
 CursorSize=25
 CursorTop=999
 CursorVisible=True
 Error=None
 ForegroundColor=None
 In=None
 InputEncoding=None
 IsErrorRedirected=False
 IsInputRedirected=False
 IsOutputRedirected=False
 KeyAvailable=False
 LargestWindowHeight=60
 LargestWindowWidth=127
 NumberLock=True
 Out=None
 OutputEncoding=None
 Title='cmd - ipy  -m ironstubs make System --folder=stubs2 --overwrite'
 TreatControlCAsInput=False
 WindowHeight=60
 WindowLeft=0
 WindowTop=940
 WindowWidth=127
 __all__=[
  'Beep',
  'CancelKeyPress',
  'Clear',
  'MoveBufferArea',
  'OpenStandardError',
  'OpenStandardInput',
  'OpenStandardOutput',
  'Read',
  'ReadKey',
  'ReadLine',
  'ResetColor',
  'SetBufferSize',
  'SetCursorPosition',
  'SetError',
  'SetIn',
  'SetOut',
  'SetWindowPosition',
  'SetWindowSize',
  'Write',
  'WriteLine',
 ]

