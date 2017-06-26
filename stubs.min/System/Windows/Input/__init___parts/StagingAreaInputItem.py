class StagingAreaInputItem(object):
 """ Encapsulates an input event when it is being processed by the input manager. """
 def GetData(self,key):
  """
  GetData(self: StagingAreaInputItem,key: object) -> object
  
   Gets the input data associated with the specified key.
  
   key: An arbitrary key for the data. This cannot be null.
   Returns: The data for this key,or null.
  """
  pass
 def SetData(self,key,value):
  """
  SetData(self: StagingAreaInputItem,key: object,value: object)
   Creates a dictionary entry by using the specified key and the specified data.
  
   key: An arbitrary key for the data. This cannot be null.
   value: The data to set for this key. This can be null.
  """
  pass
 Input=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the input event data associated with this System.Windows.Input.StagingAreaInputItem object

Get: Input(self: StagingAreaInputItem) -> InputEventArgs

"""


