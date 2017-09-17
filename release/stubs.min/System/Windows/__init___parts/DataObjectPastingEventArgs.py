class DataObjectPastingEventArgs(DataObjectEventArgs):
 """
 Contains arguments for the System.Windows.DataObject.System.Windows.DataObject.Pasting event.
 
 DataObjectPastingEventArgs(dataObject: IDataObject,isDragDrop: bool,formatToApply: str)
 """
 @staticmethod
 def __new__(self,dataObject,isDragDrop,formatToApply):
  """ __new__(cls: type,dataObject: IDataObject,isDragDrop: bool,formatToApply: str) """
  pass
 DataObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a suggested System.Windows.DataObject to use for the paste operation.

Get: DataObject(self: DataObjectPastingEventArgs) -> IDataObject

Set: DataObject(self: DataObjectPastingEventArgs)=value
"""

 FormatToApply=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string specifying the suggested data format to use for the paste operation.

Get: FormatToApply(self: DataObjectPastingEventArgs) -> str

Set: FormatToApply(self: DataObjectPastingEventArgs)=value
"""

 SourceDataObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a copy of the original data object associated with the paste operation.

Get: SourceDataObject(self: DataObjectPastingEventArgs) -> IDataObject

"""


