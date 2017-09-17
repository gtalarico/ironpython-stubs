class DataFormats(object):
 """ Provides a set of predefined data format names that can be used to identify data formats available in the clipboard or drag-and-drop operations. """
 @staticmethod
 def GetDataFormat(*__args):
  """
  GetDataFormat(format: str) -> DataFormat
  
   Returns a System.Windows.DataFormat object that defines a name and numeric ID 
    for the specified data format. The desired data format is specified by name (a 
    string).
  
  
   format: The name of the data format to request a System.Windows.DataFormat object for.
   Returns: A System.Windows.DataFormat object that contains the numeric ID and the name of 
    the requested data format.
  
  GetDataFormat(id: int) -> DataFormat
  
   Returns a System.Windows.DataFormat object that defines a name and numeric ID 
    for the specified data format. The desired data format is specified by numeric 
    ID.
  
  
   id: The numeric ID of the data format to request a System.Windows.DataFormat object 
    for.
  
   Returns: A System.Windows.DataFormat object that contains the numeric ID and the name of 
    the requested data format.
  """
  pass
 Bitmap='Bitmap'
 CommaSeparatedValue='CSV'
 Dib='DeviceIndependentBitmap'
 Dif='DataInterchangeFormat'
 EnhancedMetafile='EnhancedMetafile'
 FileDrop='FileDrop'
 Html='HTML Format'
 Locale='Locale'
 MetafilePicture='MetaFilePict'
 OemText='OEMText'
 Palette='Palette'
 PenData='PenData'
 Riff='RiffAudio'
 Rtf='Rich Text Format'
 Serializable='PersistentObject'
 StringFormat='System.String'
 SymbolicLink='SymbolicLink'
 Text='Text'
 Tiff='TaggedImageFileFormat'
 UnicodeText='UnicodeText'
 WaveAudio='WaveAudio'
 Xaml='Xaml'
 XamlPackage='XamlPackage'
 __all__=[
  'Bitmap',
  'CommaSeparatedValue',
  'Dib',
  'Dif',
  'EnhancedMetafile',
  'FileDrop',
  'GetDataFormat',
  'Html',
  'Locale',
  'MetafilePicture',
  'OemText',
  'Palette',
  'PenData',
  'Riff',
  'Rtf',
  'Serializable',
  'StringFormat',
  'SymbolicLink',
  'Text',
  'Tiff',
  'UnicodeText',
  'WaveAudio',
  'Xaml',
  'XamlPackage',
 ]

