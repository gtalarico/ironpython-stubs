class DataObjectSettingDataEventArgs(DataObjectEventArgs):
 """
 Contains arguments for the System.Windows.DataObject.System.Windows.DataObject.SettingData event.
 
 DataObjectSettingDataEventArgs(dataObject: IDataObject,format: str)
 """
 @staticmethod
 def __new__(self,dataObject,format):
  """ __new__(cls: type,dataObject: IDataObject,format: str) """
  pass
 DataObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.DataObject associated with the System.Windows.DataObject.SettingData event.

Get: DataObject(self: DataObjectSettingDataEventArgs) -> IDataObject

"""

 Format=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string specifying the new data format that is being added to the accompanying data object.

Get: Format(self: DataObjectSettingDataEventArgs) -> str

"""


