class Screen(object):
 """ Represents a display device or multiple display devices on a single system. """
 def Equals(self,obj):
  """
  Equals(self: Screen,obj: object) -> bool

  

   Gets or sets a value indicating whether the specified object is equal to this Screen.

  

   obj: The object to compare to this System.Windows.Forms.Screen.

   Returns: true if the specified object is equal to this System.Windows.Forms.Screen; otherwise,false.
  """
  pass
 @staticmethod
 def FromControl(control):
  """
  FromControl(control: Control) -> Screen

  

   Retrieves a System.Windows.Forms.Screen for the display that contains the largest portion of the 

    specified control.

  

  

   control: A System.Windows.Forms.Control for which to retrieve a System.Windows.Forms.Screen.

   Returns: A System.Windows.Forms.Screen for the display that contains the largest region of the specified 

    control. In multiple display environments where no display contains the control,the display 

    closest to the specified control is returned.
  """
  pass
 @staticmethod
 def FromHandle(hwnd):
  """
  FromHandle(hwnd: IntPtr) -> Screen

  

   Retrieves a System.Windows.Forms.Screen for the display that contains the largest portion of the 

    object referred to by the specified handle.

  

  

   hwnd: The window handle for which to retrieve the System.Windows.Forms.Screen.

   Returns: A System.Windows.Forms.Screen for the display that contains the largest region of the object. In 

    multiple display environments where no display contains any portion of the specified window,the 

    display closest to the object is returned.
  """
  pass
 @staticmethod
 def FromPoint(point):
  """
  FromPoint(point: Point) -> Screen

  

   Retrieves a System.Windows.Forms.Screen for the display that contains the specified point.

  

   point: A System.Drawing.Point that specifies the location for which to retrieve a 

    System.Windows.Forms.Screen.

  

   Returns: A System.Windows.Forms.Screen for the display that contains the point. In multiple display 

    environments where no display contains the point,the display closest to the specified point is 

    returned.
  """
  pass
 @staticmethod
 def FromRectangle(rect):
  """
  FromRectangle(rect: Rectangle) -> Screen

  

   Retrieves a System.Windows.Forms.Screen for the display that contains the largest portion of the 

    rectangle.

  

  

   rect: A System.Drawing.Rectangle that specifies the area for which to retrieve the display.

   Returns: A System.Windows.Forms.Screen for the display that contains the largest region of the specified 

    rectangle. In multiple display environments where no display contains the rectangle,the display 

    closest to the rectangle is returned.
  """
  pass
 @staticmethod
 def GetBounds(*__args):
  """
  GetBounds(ctl: Control) -> Rectangle

  

   Retrieves the bounds of the display that contains the largest portion of the specified control.

  

   ctl: The System.Windows.Forms.Control for which to retrieve the display bounds.

   Returns: A System.Drawing.Rectangle that specifies the bounds of the display that contains the specified 

    control. In multiple display environments where no display contains the specified control,the 

    display closest to the control is returned.

  

  GetBounds(rect: Rectangle) -> Rectangle

  

   Retrieves the bounds of the display that contains the largest portion of the specified rectangle.

  

   rect: A System.Drawing.Rectangle that specifies the area for which to retrieve the display bounds.

   Returns: A System.Drawing.Rectangle that specifies the bounds of the display that contains the specified 

    rectangle. In multiple display environments where no monitor contains the specified rectangle,

    the monitor closest to the rectangle is returned.

  

  GetBounds(pt: Point) -> Rectangle

  

   Retrieves the bounds of the display that contains the specified point.

  

   pt: A System.Drawing.Point that specifies the coordinates for which to retrieve the display bounds.

   Returns: A System.Drawing.Rectangle that specifies the bounds of the display that contains the specified 

    point. In multiple display environments where no display contains the specified point,the 

    display closest to the point is returned.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Screen) -> int

  

   Computes and retrieves a hash code for an object.

   Returns: A hash code for an object.
  """
  pass
 @staticmethod
 def GetWorkingArea(*__args):
  """
  GetWorkingArea(ctl: Control) -> Rectangle

  

   Retrieves the working area for the display that contains the largest region of the specified 

    control. The working area is the desktop area of the display,excluding taskbars,docked 

    windows,and docked tool bars.

  

  

   ctl: The System.Windows.Forms.Control for which to retrieve the working area.

   Returns: A System.Drawing.Rectangle that specifies the working area. In multiple display environments 

    where no display contains the specified control,the display closest to the control is returned.

  

  GetWorkingArea(rect: Rectangle) -> Rectangle

  

   Retrieves the working area for the display that contains the largest portion of the specified 

    rectangle. The working area is the desktop area of the display,excluding taskbars,docked 

    windows,and docked tool bars.

  

  

   rect: The System.Drawing.Rectangle that specifies the area for which to retrieve the working area.

   Returns: A System.Drawing.Rectangle that specifies the working area. In multiple display environments 

    where no display contains the specified rectangle,the display closest to the rectangle is 

    returned.

  

  GetWorkingArea(pt: Point) -> Rectangle

  

   Retrieves the working area closest to the specified point. The working area is the desktop area 

    of the display,excluding taskbars,docked windows,and docked tool bars.

  

  

   pt: A System.Drawing.Point that specifies the coordinates for which to retrieve the working area.

   Returns: A System.Drawing.Rectangle that specifies the working area. In multiple display environments 

    where no display contains the specified point,the display closest to the point is returned.
  """
  pass
 def ToString(self):
  """
  ToString(self: Screen) -> str

  

   Retrieves a string representing this object.

   Returns: A string representation of the object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __ne__(self,*args):
  pass
 BitsPerPixel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of bits of memory,associated with one pixel of data.



Get: BitsPerPixel(self: Screen) -> int



"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounds of the display.



Get: Bounds(self: Screen) -> Rectangle



"""

 DeviceName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the device name associated with a display.



Get: DeviceName(self: Screen) -> str



"""

 Primary=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a particular display is the primary device.



Get: Primary(self: Screen) -> bool



"""

 WorkingArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the working area of the display. The working area is the desktop area of the display,excluding taskbars,docked windows,and docked tool bars.



Get: WorkingArea(self: Screen) -> Rectangle



"""


 AllScreens=None
 PrimaryScreen=None

