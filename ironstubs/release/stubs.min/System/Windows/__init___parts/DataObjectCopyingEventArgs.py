class DataObjectCopyingEventArgs(DataObjectEventArgs):
 """
 Arguments for the System.Windows.DataObject.System.Windows.DataObject.Copying event.
 
 DataObjectCopyingEventArgs(dataObject: IDataObject,isDragDrop: bool)
 """
 @staticmethod
 def __new__(self,dataObject,isDragDrop):
  """ __new__(cls: type,dataObject: IDataObject,isDragDrop: bool) """
  pass
 DataObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the data object associated with the System.Windows.DataObject.Copying event.

Get: DataObject(self: DataObjectCopyingEventArgs) -> IDataObject

"""


