class DataFormats(object):
 """ Provides static,predefined System.Windows.Forms.Clipboard format names. Use them to identify the format of data that you store in an System.Windows.Forms.IDataObject. """
 @staticmethod
 def GetFormat(*__args):
  """
  GetFormat(id: int) -> Format

  

   Returns a System.Windows.Forms.DataFormats.Format with the Windows Clipboard numeric ID and name 

    for the specified ID.

  

  

   id: The format ID.

   Returns: A System.Windows.Forms.DataFormats.Format that has the Windows Clipboard numeric ID and the name 

    of the format.

  

  GetFormat(format: str) -> Format

  

   Returns a System.Windows.Forms.DataFormats.Format with the Windows Clipboard numeric ID and name 

    for the specified format.

  

  

   format: The format name.

   Returns: A System.Windows.Forms.DataFormats.Format that has the Windows Clipboard numeric ID and the name 

    of the format.
  """
  pass
 Bitmap='Bitmap'
 CommaSeparatedValue='Csv'
 Dib='DeviceIndependentBitmap'
 Dif='DataInterchangeFormat'
 EnhancedMetafile='EnhancedMetafile'
 FileDrop='FileDrop'
 Format=None
 Html='HTML Format'
 Locale='Locale'
 MetafilePict='MetaFilePict'
 OemText='OEMText'
 Palette='Palette'
 PenData='PenData'
 Riff='RiffAudio'
 Rtf='Rich Text Format'
 Serializable='WindowsForms10PersistentObject'
 StringFormat='System.String'
 SymbolicLink='SymbolicLink'
 Text='Text'
 Tiff='TaggedImageFileFormat'
 UnicodeText='UnicodeText'
 WaveAudio='WaveAudio'

