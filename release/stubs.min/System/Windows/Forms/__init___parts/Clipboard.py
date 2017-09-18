class Clipboard(object):
 """ Provides methods to place data on and retrieve data from the system Clipboard. This class cannot be inherited. """
 @staticmethod
 def Clear():
  """
  Clear()

   Removes all data from the Clipboard.
  """
  pass
 @staticmethod
 def ContainsAudio():
  """
  ContainsAudio() -> bool

  

   Indicates whether there is data on the Clipboard in the 

    System.Windows.Forms.DataFormats.WaveAudio format.

  

   Returns: true if there is audio data on the Clipboard; otherwise,false.
  """
  pass
 @staticmethod
 def ContainsData(format):
  """
  ContainsData(format: str) -> bool

  

   Indicates whether there is data on the Clipboard that is in the specified format or can be 

    converted to that format.

  

  

   format: The format of the data to look for. See System.Windows.Forms.DataFormats for predefined formats.

   Returns: true if there is data on the Clipboard that is in the specified format or can be converted to 

    that format; otherwise,false.
  """
  pass
 @staticmethod
 def ContainsFileDropList():
  """
  ContainsFileDropList() -> bool

  

   Indicates whether there is data on the Clipboard that is in the 

    System.Windows.Forms.DataFormats.FileDrop format or can be converted to that format.

  

   Returns: true if there is a file drop list on the Clipboard; otherwise,false.
  """
  pass
 @staticmethod
 def ContainsImage():
  """
  ContainsImage() -> bool

  

   Indicates whether there is data on the Clipboard that is in the 

    System.Windows.Forms.DataFormats.Bitmap format or can be converted to that format.

  

   Returns: true if there is image data on the Clipboard; otherwise,false.
  """
  pass
 @staticmethod
 def ContainsText(format=None):
  """
  ContainsText(format: TextDataFormat) -> bool

  

   Indicates whether there is text data on the Clipboard in the format indicated by the specified 

    System.Windows.Forms.TextDataFormat value.

  

  

   format: One of the System.Windows.Forms.TextDataFormat values.

   Returns: true if there is text data on the Clipboard in the value specified for format; otherwise,false.

  ContainsText() -> bool

  

   Indicates whether there is data on the Clipboard in the System.Windows.Forms.TextDataFormat.Text 

    or System.Windows.Forms.TextDataFormat.UnicodeText format,depending on the operating system.

  

   Returns: true if there is text data on the Clipboard; otherwise,false.
  """
  pass
 @staticmethod
 def GetAudioStream():
  """
  GetAudioStream() -> Stream

  

   Retrieves an audio stream from the Clipboard.

   Returns: A System.IO.Stream containing audio data or null if the Clipboard does not contain any data in 

    the System.Windows.Forms.DataFormats.WaveAudio format.
  """
  pass
 @staticmethod
 def GetData(format):
  """
  GetData(format: str) -> object

  

   Retrieves data from the Clipboard in the specified format.

  

   format: The format of the data to retrieve. See System.Windows.Forms.DataFormats for predefined formats.

   Returns: An System.Object representing the Clipboard data or null if the Clipboard does not contain any 

    data that is in the specified format or can be converted to that format.
  """
  pass
 @staticmethod
 def GetDataObject():
  """
  GetDataObject() -> IDataObject

  

   Retrieves the data that is currently on the system Clipboard.

   Returns: An System.Windows.Forms.IDataObject that represents the data currently on the Clipboard,or null 

    if there is no data on the Clipboard.
  """
  pass
 @staticmethod
 def GetFileDropList():
  """
  GetFileDropList() -> StringCollection

  

   Retrieves a collection of file names from the Clipboard.

   Returns: A System.Collections.Specialized.StringCollection containing file names or null if the Clipboard 

    does not contain any data that is in the System.Windows.Forms.DataFormats.FileDrop format or can 

    be converted to that format.
  """
  pass
 @staticmethod
 def GetImage():
  """
  GetImage() -> Image

  

   Retrieves an image from the Clipboard.

   Returns: An System.Drawing.Image representing the Clipboard image data or null if the Clipboard does not 

    contain any data that is in the System.Windows.Forms.DataFormats.Bitmap format or can be 

    converted to that format.
  """
  pass
 @staticmethod
 def GetText(format=None):
  """
  GetText(format: TextDataFormat) -> str

  

   Retrieves text data from the Clipboard in the format indicated by the specified 

    System.Windows.Forms.TextDataFormat value.

  

  

   format: One of the System.Windows.Forms.TextDataFormat values.

   Returns: The Clipboard text data or System.String.Empty if the Clipboard does not contain data in the 

    specified format.

  

  GetText() -> str

  

   Retrieves text data from the Clipboard in the System.Windows.Forms.TextDataFormat.Text or 

    System.Windows.Forms.TextDataFormat.UnicodeText format,depending on the operating system.

  

   Returns: The Clipboard text data or System.String.Empty if the Clipboard does not contain data in the 

    System.Windows.Forms.TextDataFormat.Text or System.Windows.Forms.TextDataFormat.UnicodeText 

    format,depending on the operating system.
  """
  pass
 @staticmethod
 def SetAudio(*__args):
  """
  SetAudio(audioStream: Stream)

   Clears the Clipboard and then adds a System.IO.Stream in the 

    System.Windows.Forms.DataFormats.WaveAudio format.

  

  

   audioStream: A System.IO.Stream containing the audio data.

  SetAudio(audioBytes: Array[Byte])

   Clears the Clipboard and then adds a System.Byte array in the 

    System.Windows.Forms.DataFormats.WaveAudio format after converting it to a System.IO.Stream.

  

  

   audioBytes: A System.Byte array containing the audio data.
  """
  pass
 @staticmethod
 def SetData(format,data):
  """
  SetData(format: str,data: object)

   Clears the Clipboard and then adds data in the specified format.

  

   format: The format of the data to set. See System.Windows.Forms.DataFormats for predefined formats.

   data: An System.Object representing the data to add.
  """
  pass
 @staticmethod
 def SetDataObject(data,copy=None,retryTimes=None,retryDelay=None):
  """
  SetDataObject(data: object,copy: bool,retryTimes: int,retryDelay: int)

   Clears the Clipboard and then attempts to place data on it the specified number of times and 

    with the specified delay between attempts,optionally leaving the data on the Clipboard after 

    the application exits.

  

  

   data: The data to place on the Clipboard.

   copy: true if you want data to remain on the Clipboard after this application exits; otherwise,false.

   retryTimes: The number of times to attempt placing the data on the Clipboard.

   retryDelay: The number of milliseconds to pause between attempts.

  SetDataObject(data: object,copy: bool)

   Clears the Clipboard and then places data on it and specifies whether the data should remain 

    after the application exits.

  

  

   data: The data to place on the Clipboard.

   copy: true if you want data to remain on the Clipboard after this application exits; otherwise,false.

  SetDataObject(data: object)

   Clears the Clipboard and then places nonpersistent data on it.

  

   data: The data to place on the Clipboard.
  """
  pass
 @staticmethod
 def SetFileDropList(filePaths):
  """
  SetFileDropList(filePaths: StringCollection)

   Clears the Clipboard and then adds a collection of file names in the 

    System.Windows.Forms.DataFormats.FileDrop format.

  

  

   filePaths: A System.Collections.Specialized.StringCollection containing the file names.
  """
  pass
 @staticmethod
 def SetImage(image):
  """
  SetImage(image: Image)

   Clears the Clipboard and then adds an System.Drawing.Image in the 

    System.Windows.Forms.DataFormats.Bitmap format.

  

  

   image: The System.Drawing.Image to add to the Clipboard.
  """
  pass
 @staticmethod
 def SetText(text,format=None):
  """
  SetText(text: str,format: TextDataFormat)

   Clears the Clipboard and then adds text data in the format indicated by the specified 

    System.Windows.Forms.TextDataFormat value.

  

  

   text: The text to add to the Clipboard.

   format: One of the System.Windows.Forms.TextDataFormat values.

  SetText(text: str)

   Clears the Clipboard and then adds text data in the System.Windows.Forms.TextDataFormat.Text or 

    System.Windows.Forms.TextDataFormat.UnicodeText format,depending on the operating system.

  

  

   text: The text to add to the Clipboard.
  """
  pass
