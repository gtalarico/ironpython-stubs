class IDataObject:
 """ Provides a format-independent mechanism for transferring data. """
 def GetData(self,format,autoConvert=None):
  """
  GetData(self: IDataObject,format: Type) -> object

  

   Retrieves the data associated with the specified class type format.

  

   format: A System.Type representing the format of the data to retrieve. See 

    System.Windows.Forms.DataFormats for predefined formats.

  

   Returns: The data associated with the specified format,or null.

  GetData(self: IDataObject,format: str) -> object

  

   Retrieves the data associated with the specified data format.

  

   format: The format of the data to retrieve. See System.Windows.Forms.DataFormats for predefined formats.

   Returns: The data associated with the specified format,or null.

  GetData(self: IDataObject,format: str,autoConvert: bool) -> object

  

   Retrieves the data associated with the specified data format,using a Boolean to determine 

    whether to convert the data to the format.

  

  

   format: The format of the data to retrieve. See System.Windows.Forms.DataFormats for predefined formats.

   autoConvert: true to convert the data to the specified format; otherwise,false.

   Returns: The data associated with the specified format,or null.
  """
  pass
 def GetDataPresent(self,format,autoConvert=None):
  """
  GetDataPresent(self: IDataObject,format: Type) -> bool

  

   Determines whether data stored in this instance is associated with,or can be converted to,the 

    specified format.

  

  

   format: A System.Type representing the format for which to check. See System.Windows.Forms.DataFormats 

    for predefined formats.

  

   Returns: true if data stored in this instance is associated with,or can be converted to,the specified 

    format; otherwise,false.

  

  GetDataPresent(self: IDataObject,format: str) -> bool

  

   Determines whether data stored in this instance is associated with,or can be converted to,the 

    specified format.

  

  

   format: The format for which to check. See System.Windows.Forms.DataFormats for predefined formats.

   Returns: true if data stored in this instance is associated with,or can be converted to,the specified 

    format; otherwise false.

  

  GetDataPresent(self: IDataObject,format: str,autoConvert: bool) -> bool

  

   Determines whether data stored in this instance is associated with the specified format,using a 

    Boolean value to determine whether to convert the data to the format.

  

  

   format: The format for which to check. See System.Windows.Forms.DataFormats for predefined formats.

   autoConvert: true to determine whether data stored in this instance can be converted to the specified format; 

    false to check whether the data is in the specified format.

  

   Returns: true if the data is in,or can be converted to,the specified format; otherwise,false.
  """
  pass
 def GetFormats(self,autoConvert=None):
  """
  GetFormats(self: IDataObject) -> Array[str]

  

   Returns a list of all formats that data stored in this instance is associated with or can be 

    converted to.

  

   Returns: An array of the names that represents a list of all formats that are supported by the data 

    stored in this object.

  

  GetFormats(self: IDataObject,autoConvert: bool) -> Array[str]

  

   Gets a list of all formats that data stored in this instance is associated with or can be 

    converted to,using a Boolean value to determine whether to retrieve all formats that the data 

    can be converted to or only native data formats.

  

  

   autoConvert: true to retrieve all formats that data stored in this instance is associated with or can be 

    converted to; false to retrieve only native data formats.

  

   Returns: An array of the names that represents a list of all formats that are supported by the data 

    stored in this object.
  """
  pass
 def SetData(self,*__args):
  """
  SetData(self: IDataObject,format: Type,data: object)

   Stores the specified data and its associated class type in this instance.

  

   format: A System.Type representing the format associated with the data. See 

    System.Windows.Forms.DataFormats for predefined formats.

  

   data: The data to store.

  SetData(self: IDataObject,data: object)

   Stores the specified data in this instance,using the class of the data for the format.

  

   data: The data to store.

  SetData(self: IDataObject,format: str,autoConvert: bool,data: object)

   Stores the specified data and its associated format in this instance,using a Boolean value to 

    specify whether the data can be converted to another format.

  

  

   format: The format associated with the data. See System.Windows.Forms.DataFormats for predefined formats.

   autoConvert: true to allow the data to be converted to another format; otherwise,false.

   data: The data to store.

  SetData(self: IDataObject,format: str,data: object)

   Stores the specified data and its associated format in this instance.

  

   format: The format associated with the data. See System.Windows.Forms.DataFormats for predefined formats.

   data: The data to store.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
