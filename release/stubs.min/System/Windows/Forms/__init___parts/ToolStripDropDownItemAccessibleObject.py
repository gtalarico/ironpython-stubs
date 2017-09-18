class ToolStripDropDownItemAccessibleObject(ToolStripItemAccessibleObject,IMarshal,IReflect,IAccessible,IEnumVariant,IOleWindow):
 """
 Provides information that accessibility applications use to adjust the user interface of a System.Windows.Forms.ToolStripDropDown for users with impairments.

 

 ToolStripDropDownItemAccessibleObject(item: ToolStripDropDownItem)
 """
 def DoDefaultAction(self):
  """
  DoDefaultAction(self: ToolStripDropDownItemAccessibleObject)

   Performs the default action associated with this accessible object.
  """
  pass
 def GetChild(self,index):
  """
  GetChild(self: ToolStripDropDownItemAccessibleObject,index: int) -> AccessibleObject

  

   Retrieves the accessible child control corresponding to the specified index.

  

   index: The zero-based index of the accessible child control.

   Returns: An System.Windows.Forms.AccessibleObject that represents the accessible child control 

    corresponding to the specified index.
  """
  pass
 def GetChildCount(self):
  """
  GetChildCount(self: ToolStripDropDownItemAccessibleObject) -> int

  

   Retrieves the number of children belonging to an accessible object.

   Returns: The number of children belonging to an accessible object.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject

  

   Creates a shallow copy of the current System.MarshalByRefObject object.

  

   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 

    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 

    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 

    identity to its clone,which will cause remoting client calls to be routed to the remote server 

    object.

  

   Returns: A shallow copy of the current System.MarshalByRefObject object.

  MemberwiseClone(self: object) -> object

  

   Creates a shallow copy of the current System.Object.

   Returns: A shallow copy of the current System.Object.
  """
  pass
 def UseStdAccessibleObjects(self,*args):
  """
  UseStdAccessibleObjects(self: AccessibleObject,handle: IntPtr,objid: int)

   Associates an object with an instance of an System.Windows.Forms.AccessibleObject based on the 

    handle and the object id of the object.

  

  

   handle: An System.IntPtr that contains the handle of the object.

   objid: An Int that defines the type of object that the handle parameter refers to.

  UseStdAccessibleObjects(self: AccessibleObject,handle: IntPtr)

   Associates an object with an instance of an System.Windows.Forms.AccessibleObject based on the 

    handle of the object.

  

  

   handle: An System.IntPtr that contains the handle of the object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,item):
  """ __new__(cls: type,item: ToolStripDropDownItem) """
  pass
 def __str__(self,*args):
  pass
 Role=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the role of this accessible object.



Get: Role(self: ToolStripDropDownItemAccessibleObject) -> AccessibleRole



"""


