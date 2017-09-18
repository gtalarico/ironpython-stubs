class ImeContext(object):
 """ Contains static methods that interact directly with the IME API. """
 @staticmethod
 def Disable(handle):
  """
  Disable(handle: IntPtr)

   Disables the specified IME.

  

   handle: A pointer to the IME to disable.
  """
  pass
 @staticmethod
 def Enable(handle):
  """
  Enable(handle: IntPtr)

   Enables the specified IME.

  

   handle: A pointer to the IME to enable.
  """
  pass
 @staticmethod
 def GetImeMode(handle):
  """
  GetImeMode(handle: IntPtr) -> ImeMode

  

   Returns the System.Windows.Forms.ImeMode of the specified IME.

  

   handle: A pointer to the IME to query.

   Returns: The System.Windows.Forms.ImeMode of the specified IME.
  """
  pass
 @staticmethod
 def IsOpen(handle):
  """
  IsOpen(handle: IntPtr) -> bool

  

   Returns a value that indicates whether the specified IME is open.

  

   handle: A pointer to the IME to query.

   Returns: true if the specified IME is open; otherwise,false.
  """
  pass
 @staticmethod
 def SetImeStatus(imeMode,handle):
  """
  SetImeStatus(imeMode: ImeMode,handle: IntPtr)

   Sets the status of the specified IME.

  

   imeMode: The status to set.

   handle: A pointer to the IME to set status of.
  """
  pass
 @staticmethod
 def SetOpenStatus(open,handle):
  """
  SetOpenStatus(open: bool,handle: IntPtr)

   Opens or closes the IME context.

  

   open: true to open the IME or false to close it.

   handle: A pointer to the IME to open or close.
  """
  pass
 __all__=[
  'Disable',
  'Enable',
  'GetImeMode',
  'IsOpen',
  'SetImeStatus',
  'SetOpenStatus',
 ]

