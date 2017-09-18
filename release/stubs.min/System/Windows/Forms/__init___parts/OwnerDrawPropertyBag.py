class OwnerDrawPropertyBag(MarshalByRefObject,ISerializable):
 """ Contains values of properties that a component might need only occasionally. """
 @staticmethod
 def Copy(value):
  """
  Copy(value: OwnerDrawPropertyBag) -> OwnerDrawPropertyBag

  

   Copies an System.Windows.Forms.OwnerDrawPropertyBag.

  

   value: The System.Windows.Forms.OwnerDrawPropertyBag to be copied.

   Returns: A new System.Windows.Forms.OwnerDrawPropertyBag.
  """
  pass
 def IsEmpty(self):
  """
  IsEmpty(self: OwnerDrawPropertyBag) -> bool

  

   Returns whether the System.Windows.Forms.OwnerDrawPropertyBag contains all default values.

   Returns: true if the System.Windows.Forms.OwnerDrawPropertyBag contains all default values; otherwise,

    false.
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
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*args): #cannot find CLR constructor
  """ __new__(cls: type,info: SerializationInfo,context: StreamingContext) """
  pass
 def __reduce_ex__(self,*args):
  pass
 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the background color for the component.



Get: BackColor(self: OwnerDrawPropertyBag) -> Color



Set: BackColor(self: OwnerDrawPropertyBag)=value

"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the font of the text displayed by the component.



Get: Font(self: OwnerDrawPropertyBag) -> Font



Set: Font(self: OwnerDrawPropertyBag)=value

"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the foreground color of the component.



Get: ForeColor(self: OwnerDrawPropertyBag) -> Color



Set: ForeColor(self: OwnerDrawPropertyBag)=value

"""


