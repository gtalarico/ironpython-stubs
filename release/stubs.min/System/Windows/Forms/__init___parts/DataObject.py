class DataObject(object,IDataObject,IDataObject):
 """
 Implements a basic data transfer mechanism.

 

 DataObject()

 DataObject(data: object)

 DataObject(format: str,data: object)
 """
 def ContainsAudio(self):
  """
  ContainsAudio(self: DataObject) -> bool

  

   Indicates whether the data object contains data in the 

    System.Windows.Forms.DataFormats.WaveAudio format.

  

   Returns: true if the data object contains audio data; otherwise,false.
  """
  pass
 def ContainsFileDropList(self):
  """
  ContainsFileDropList(self: DataObject) -> bool

  

   Indicates whether the data object contains data that is in the 

    System.Windows.Forms.DataFormats.FileDrop format or can be converted to that format.

  

   Returns: true if the data object contains a file drop list; otherwise,false.
  """
  pass
 def ContainsImage(self):
  """
  ContainsImage(self: DataObject) -> bool

  

   Indicates whether the data object contains data that is in the 

    System.Windows.Forms.DataFormats.Bitmap format or can be converted to that format.

  

   Returns: true if the data object contains image data; otherwise,false.
  """
  pass
 def ContainsText(self,format=None):
  """
  ContainsText(self: DataObject,format: TextDataFormat) -> bool

  

   Indicates whether the data object contains text data in the format indicated by the specified 

    System.Windows.Forms.TextDataFormat value.

  

  

   format: One of the System.Windows.Forms.TextDataFormat values.

   Returns: true if the data object contains text data in the specified format; otherwise,false.

  ContainsText(self: DataObject) -> bool

  

   Indicates whether the data object contains data in the 

    System.Windows.Forms.TextDataFormat.UnicodeText format.

  

   Returns: true if the data object contains text data; otherwise,false.
  """
  pass
 def GetAudioStream(self):
  """
  GetAudioStream(self: DataObject) -> Stream

  

   Retrieves an audio stream from the data object.

   Returns: A System.IO.Stream containing audio data or null if the data object does not contain any data in 

    the System.Windows.Forms.DataFormats.WaveAudio format.
  """
  pass
 def GetData(self,format,autoConvert=None):
  """
  GetData(self: DataObject,format: Type) -> object

  

   Returns the data associated with the specified class type format.

  

   format: A System.Type representing the format of the data to retrieve.

   Returns: The data associated with the specified format,or null.

  GetData(self: DataObject,format: str) -> object

  

   Returns the data associated with the specified data format.

  

   format: The format of the data to retrieve. See System.Windows.Forms.DataFormats for predefined formats.

   Returns: The data associated with the specified format,or null.

  GetData(self: DataObject,format: str,autoConvert: bool) -> object

  

   Returns the data associated with the specified data format,using an automated conversion 

    parameter to determine whether to convert the data to the format.

  

  

   format: The format of the data to retrieve. See System.Windows.Forms.DataFormats for predefined formats.

   autoConvert: true to the convert data to the specified format; otherwise,false.

   Returns: The data associated with the specified format,or null.
  """
  pass
 def GetDataPresent(self,format,autoConvert=None):
  """
  GetDataPresent(self: DataObject,format: str) -> bool

  

   Determines whether data stored in this System.Windows.Forms.DataObject is associated with,or 

    can be converted to,the specified format.

  

  

   format: The format to check for. See System.Windows.Forms.DataFormats for predefined formats.

   Returns: true if data stored in this System.Windows.Forms.DataObject is associated with,or can be 

    converted to,the specified format; otherwise,false.

  

  GetDataPresent(self: DataObject,format: str,autoConvert: bool) -> bool

  

   Determines whether this System.Windows.Forms.DataObject contains data in the specified format 

    or,optionally,contains data that can be converted to the specified format.

  

  

   format: The format to check for. See System.Windows.Forms.DataFormats for predefined formats.

   autoConvert: true to determine whether data stored in this System.Windows.Forms.DataObject can be converted 

    to the specified format; false to check whether the data is in the specified format.

  

   Returns: true if the data is in,or can be converted to,the specified format; otherwise,false.

  GetDataPresent(self: DataObject,format: Type) -> bool

  

   Determines whether data stored in this System.Windows.Forms.DataObject is associated with,or 

    can be converted to,the specified format.

  

  

   format: A System.Type representing the format to check for.

   Returns: true if data stored in this System.Windows.Forms.DataObject is associated with,or can be 

    converted to,the specified format; otherwise,false.
  """
  pass
 def GetFileDropList(self):
  """
  GetFileDropList(self: DataObject) -> StringCollection

  

   Retrieves a collection of file names from the data object.

   Returns: A System.Collections.Specialized.StringCollection containing file names or null if the data 

    object does not contain any data that is in the System.Windows.Forms.DataFormats.FileDrop format 

    or can be converted to that format.
  """
  pass
 def GetFormats(self,autoConvert=None):
  """
  GetFormats(self: DataObject) -> Array[str]

  

   Returns a list of all formats that data stored in this System.Windows.Forms.DataObject is 

    associated with or can be converted to.

  

   Returns: An array of type System.String,containing a list of all formats that are supported by the data 

    stored in this object.

  

  GetFormats(self: DataObject,autoConvert: bool) -> Array[str]

  

   Returns a list of all formats that data stored in this System.Windows.Forms.DataObject is 

    associated with or can be converted to,using an automatic conversion parameter to determine 

    whether to retrieve only native data formats or all formats that the data can be converted to.

  

  

   autoConvert: true to retrieve all formats that data stored in this System.Windows.Forms.DataObject is 

    associated with,or can be converted to; false to retrieve only native data formats.

  

   Returns: An array of type System.String,containing a list of all formats that are supported by the data 

    stored in this object.
  """
  pass
 def GetImage(self):
  """
  GetImage(self: DataObject) -> Image

  

   Retrieves an image from the data object.

   Returns: An System.Drawing.Image representing the image data in the data object or null if the data 

    object does not contain any data that is in the System.Windows.Forms.DataFormats.Bitmap format 

    or can be converted to that format.
  """
  pass
 def GetText(self,format=None):
  """
  GetText(self: DataObject,format: TextDataFormat) -> str

  

   Retrieves text data from the data object in the format indicated by the specified 

    System.Windows.Forms.TextDataFormat value.

  

  

   format: One of the System.Windows.Forms.TextDataFormat values.

   Returns: The text data in the data object or System.String.Empty if the data object does not contain data 

    in the specified format.

  

  GetText(self: DataObject) -> str

  

   Retrieves text data from the data object in the System.Windows.Forms.TextDataFormat.UnicodeText 

    format.

  

   Returns: The text data in the data object or System.String.Empty if the data object does not contain data 

    in the System.Windows.Forms.TextDataFormat.UnicodeText format.
  """
  pass
 def SetAudio(self,*__args):
  """
  SetAudio(self: DataObject,audioStream: Stream)

   Adds a System.IO.Stream to the data object in the System.Windows.Forms.DataFormats.WaveAudio 

    format.

  

  

   audioStream: A System.IO.Stream containing the audio data.

  SetAudio(self: DataObject,audioBytes: Array[Byte])

   Adds a System.Byte array to the data object in the System.Windows.Forms.DataFormats.WaveAudio 

    format after converting it to a System.IO.Stream.

  

  

   audioBytes: A System.Byte array containing the audio data.
  """
  pass
 def SetData(self,*__args):
  """
  SetData(self: DataObject,format: Type,data: object)

   Adds the specified object to the System.Windows.Forms.DataObject using the specified type as the 

    format.

  

  

   format: A System.Type representing the format associated with the data.

   data: The data to store.

  SetData(self: DataObject,data: object)

   Adds the specified object to the System.Windows.Forms.DataObject using the object type as the 

    data format.

  

  

   data: The data to store.

  SetData(self: DataObject,format: str,autoConvert: bool,data: object)

   Adds the specified object to the System.Windows.Forms.DataObject using the specified format and 

    indicating whether the data can be converted to another format.

  

  

   format: The format associated with the data. See System.Windows.Forms.DataFormats for predefined formats.

   autoConvert: true to allow the data to be converted to another format; otherwise,false.

   data: The data to store.

  SetData(self: DataObject,format: str,data: object)

   Adds the specified object to the System.Windows.Forms.DataObject using the specified format.

  

   format: The format associated with the data. See System.Windows.Forms.DataFormats for predefined formats.

   data: The data to store.
  """
  pass
 def SetFileDropList(self,filePaths):
  """
  SetFileDropList(self: DataObject,filePaths: StringCollection)

   Adds a collection of file names to the data object in the 

    System.Windows.Forms.DataFormats.FileDrop format.

  

  

   filePaths: A System.Collections.Specialized.StringCollection containing the file names.
  """
  pass
 def SetImage(self,image):
  """
  SetImage(self: DataObject,image: Image)

   Adds an System.Drawing.Image to the data object in the System.Windows.Forms.DataFormats.Bitmap 

    format.

  

  

   image: The System.Drawing.Image to add to the data object.
  """
  pass
 def SetText(self,textData,format=None):
  """
  SetText(self: DataObject,textData: str,format: TextDataFormat)

   Adds text data to the data object in the format indicated by the specified 

    System.Windows.Forms.TextDataFormat value.

  

  

   textData: The text to add to the data object.

   format: One of the System.Windows.Forms.TextDataFormat values.

  SetText(self: DataObject,textData: str)

   Adds text data to the data object in the System.Windows.Forms.TextDataFormat.UnicodeText format.

  

   textData: The text to add to the data object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,data: object)

  __new__(cls: type,format: str,data: object)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
