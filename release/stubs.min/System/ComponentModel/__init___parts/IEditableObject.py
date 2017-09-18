class IEditableObject:
 """ Provides functionality to commit or rollback changes to an object that is used as a data source. """
 def BeginEdit(self):
  """
  BeginEdit(self: IEditableObject)

   Begins an edit on an object.
  """
  pass
 def CancelEdit(self):
  """
  CancelEdit(self: IEditableObject)

   Discards changes since the last System.ComponentModel.IEditableObject.BeginEdit call.
  """
  pass
 def EndEdit(self):
  """
  EndEdit(self: IEditableObject)

   Pushes changes since the last System.ComponentModel.IEditableObject.BeginEdit or 

    System.ComponentModel.IBindingList.AddNew call into the underlying object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
