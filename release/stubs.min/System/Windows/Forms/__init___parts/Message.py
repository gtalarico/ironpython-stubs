class Message(object):
 """ Implements a Windows message. """
 @staticmethod
 def Create(hWnd,msg,wparam,lparam):
  """
  Create(hWnd: IntPtr,msg: int,wparam: IntPtr,lparam: IntPtr) -> Message

  

   Creates a new System.Windows.Forms.Message.

  

   hWnd: The window handle that the message is for.

   msg: The message ID.

   wparam: The message wparam field.

   lparam: The message lparam field.

   Returns: A System.Windows.Forms.Message that represents the message that was created.
  """
  pass
 def Equals(self,o):
  """
  Equals(self: Message,o: object) -> bool

  

   Determines whether the specified object is equal to the current object.

  

   o: The object to compare with the current object.

   Returns: true if the specified object is equal to the current object; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Message) -> int

   Returns: A 32-bit signed integer that is the hash code for this instance.
  """
  pass
 def GetLParam(self,cls):
  """
  GetLParam(self: Message,cls: Type) -> object

  

   Gets the System.Windows.Forms.Message.LParam value and converts the value to an object.

  

   cls: The type to use to create an instance. This type must be declared as a structure type.

   Returns: An System.Object that represents an instance of the class specified by the cls parameter,with 

    the data from the System.Windows.Forms.Message.LParam field of the message.
  """
  pass
 def ToString(self):
  """
  ToString(self: Message) -> str

  

   Returns a System.String that represents the current System.Windows.Forms.Message.

   Returns: A System.String that represents the current System.Windows.Forms.Message.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 HWnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the window handle of the message.



Get: HWnd(self: Message) -> IntPtr



Set: HWnd(self: Message)=value

"""

 LParam=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the System.Windows.Forms.Message.LParam field of the message.



Get: LParam(self: Message) -> IntPtr



Set: LParam(self: Message)=value

"""

 Msg=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the ID number for the message.



Get: Msg(self: Message) -> int



Set: Msg(self: Message)=value

"""

 Result=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies the value that is returned to Windows in response to handling the message.



Get: Result(self: Message) -> IntPtr



Set: Result(self: Message)=value

"""

 WParam=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.Message.WParam field of the message.



Get: WParam(self: Message) -> IntPtr



Set: WParam(self: Message)=value

"""


