class AccessibleObject(StandardOleMarshalObject,IMarshal,IReflect,IAccessible,IEnumVariant,IOleWindow):
 """
 Provides information that accessibility applications use to adjust an application's user interface (UI) for users with impairments.

 

 AccessibleObject()
 """
 def DoDefaultAction(self):
  """
  DoDefaultAction(self: AccessibleObject)

   Performs the default action associated with this accessible object.
  """
  pass
 def GetChild(self,index):
  """
  GetChild(self: AccessibleObject,index: int) -> AccessibleObject

  

   Retrieves the accessible child corresponding to the specified index.

  

   index: The zero-based index of the accessible child.

   Returns: An System.Windows.Forms.AccessibleObject that represents the accessible child corresponding to 

    the specified index.
  """
  pass
 def GetChildCount(self):
  """
  GetChildCount(self: AccessibleObject) -> int

  

   Retrieves the number of children belonging to an accessible object.

   Returns: The number of children belonging to an accessible object.
  """
  pass
 def GetFocused(self):
  """
  GetFocused(self: AccessibleObject) -> AccessibleObject

  

   Retrieves the object that has the keyboard focus.

   Returns: An System.Windows.Forms.AccessibleObject that specifies the currently focused child. This method 

    returns the calling object if the object itself is focused. Returns null if no object has focus.
  """
  pass
 def GetHelpTopic(self,fileName):
  """
  GetHelpTopic(self: AccessibleObject) -> (int,str)

  

   Gets an identifier for a Help topic identifier and the path to the Help file associated with 

    this accessible object.

  

   Returns: An identifier for a Help topic,or -1 if there is no Help topic. On return,the fileName 

    parameter contains the path to the Help file associated with this accessible object.
  """
  pass
 def GetSelected(self):
  """
  GetSelected(self: AccessibleObject) -> AccessibleObject

  

   Retrieves the currently selected child.

   Returns: An System.Windows.Forms.AccessibleObject that represents the currently selected child. This 

    method returns the calling object if the object itself is selected. Returns null if is no child 

    is currently selected and the object itself does not have focus.
  """
  pass
 def HitTest(self,x,y):
  """
  HitTest(self: AccessibleObject,x: int,y: int) -> AccessibleObject

  

   Retrieves the child object at the specified screen coordinates.

  

   x: The horizontal screen coordinate.

   y: The vertical screen coordinate.

   Returns: An System.Windows.Forms.AccessibleObject that represents the child object at the given screen 

    coordinates. This method returns the calling object if the object itself is at the location 

    specified. Returns null if no object is at the tested location.
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
 def Navigate(self,navdir):
  """
  Navigate(self: AccessibleObject,navdir: AccessibleNavigation) -> AccessibleObject

  

   Navigates to another accessible object.

  

   navdir: One of the System.Windows.Forms.AccessibleNavigation values.

   Returns: An System.Windows.Forms.AccessibleObject that represents one of the 

    System.Windows.Forms.AccessibleNavigation values.
  """
  pass
 def Select(self,flags):
  """
  Select(self: AccessibleObject,flags: AccessibleSelection)

   Modifies the selection or moves the keyboard focus of the accessible object.

  

   flags: One of the System.Windows.Forms.AccessibleSelection values.
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
 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location and size of the accessible object.



Get: Bounds(self: AccessibleObject) -> Rectangle



"""

 DefaultAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string that describes the default action of the object. Not all objects have a default action.



Get: DefaultAction(self: AccessibleObject) -> str



"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string that describes the visual appearance of the specified object. Not all objects have a description.



Get: Description(self: AccessibleObject) -> str



"""

 Help=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a description of what the object does or how the object is used.



Get: Help(self: AccessibleObject) -> str



"""

 KeyboardShortcut=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the shortcut key or access key for the accessible object.



Get: KeyboardShortcut(self: AccessibleObject) -> str



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object name.



Get: Name(self: AccessibleObject) -> str



Set: Name(self: AccessibleObject)=value

"""

 Parent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent of an accessible object.



Get: Parent(self: AccessibleObject) -> AccessibleObject



"""

 Role=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the role of this accessible object.



Get: Role(self: AccessibleObject) -> AccessibleRole



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of this accessible object.



Get: State(self: AccessibleObject) -> AccessibleStates



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of an accessible object.



Get: Value(self: AccessibleObject) -> str



Set: Value(self: AccessibleObject)=value

"""


