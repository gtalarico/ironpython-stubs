class HwndSourceParameters(object):
 """
 Contains the parameters that are used to create an System.Windows.Interop.HwndSource object using the System.Windows.Interop.HwndSource.#ctor(System.Windows.Interop.HwndSourceParameters) constructor.
 
 HwndSourceParameters(name: str)
 HwndSourceParameters(name: str,width: int,height: int)
 """
 def Equals(self,obj):
  """
  Equals(self: HwndSourceParameters,obj: HwndSourceParameters) -> bool
  
   Determines whether this structure is equal to a specified 
    System.Windows.Interop.HwndSourceParameters structure.
  
  
   obj: The structure to be tested for equality.
   Returns: true if the structures are equal; otherwise,false.
  Equals(self: HwndSourceParameters,obj: object) -> bool
  
   Determines whether this structure is equal to a specified object.
  
   obj: The objects to be tested for equality.
   Returns: true if the comparison is equal; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: HwndSourceParameters) -> int
  
   Returns the hash code for this System.Windows.Interop.HwndSourceParameters 
    instance.
  
   Returns: A 32-bit signed integer hash code.
  """
  pass
 def SetPosition(self,x,y):
  """
  SetPosition(self: HwndSourceParameters,x: int,y: int)
   Sets the values that are used for the screen position of the window for the 
    System.Windows.Interop.HwndSource.
  
  
   x: The position of the left edge of the window.
   y: The position of the upper edge of the window.
  """
  pass
 def SetSize(self,width,height):
  """
  SetSize(self: HwndSourceParameters,width: int,height: int)
   Sets the values that are used for the window size of the 
    System.Windows.Interop.HwndSource.
  
  
   width: The width of the window,in device pixels.
   height: The height of the window,in device pixels.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,name,width=None,height=None):
  """
  __new__[HwndSourceParameters]() -> HwndSourceParameters
  
  __new__(cls: type,name: str)
  __new__(cls: type,name: str,width: int,height: int)
  """
  pass
 def __ne__(self,*args):
  pass
 AcquireHwndFocusInMenuMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value that determines whether to acquire Win32 focus for the WPF containing window when an System.Windows.Interop.HwndSource is created.

Get: AcquireHwndFocusInMenuMode(self: HwndSourceParameters) -> bool

Set: AcquireHwndFocusInMenuMode(self: HwndSourceParameters)=value
"""

 AdjustSizingForNonClientArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether to include the nonclient area for sizing.

Get: AdjustSizingForNonClientArea(self: HwndSourceParameters) -> bool

Set: AdjustSizingForNonClientArea(self: HwndSourceParameters)=value
"""

 ExtendedWindowStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the extended Microsoft Windows styles for the window.

Get: ExtendedWindowStyle(self: HwndSourceParameters) -> int

Set: ExtendedWindowStyle(self: HwndSourceParameters)=value
"""

 HasAssignedSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether a size was assigned.

Get: HasAssignedSize(self: HwndSourceParameters) -> bool

"""

 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates the height of the window.

Get: Height(self: HwndSourceParameters) -> int

Set: Height(self: HwndSourceParameters)=value
"""

 HwndSourceHook=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the message hook for the window.

Get: HwndSourceHook(self: HwndSourceParameters) -> HwndSourceHook

Set: HwndSourceHook(self: HwndSourceParameters)=value
"""

 ParentWindow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the window handle (HWND) of the parent for the created window.

Get: ParentWindow(self: HwndSourceParameters) -> IntPtr

Set: ParentWindow(self: HwndSourceParameters)=value
"""

 PositionX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the left-edge position of the window.

Get: PositionX(self: HwndSourceParameters) -> int

Set: PositionX(self: HwndSourceParameters)=value
"""

 PositionY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the upper-edge position of the window.

Get: PositionY(self: HwndSourceParameters) -> int

Set: PositionY(self: HwndSourceParameters)=value
"""

 RestoreFocusMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets how WPF handles restoring focus to the window.

Get: RestoreFocusMode(self: HwndSourceParameters) -> RestoreFocusMode

Set: RestoreFocusMode(self: HwndSourceParameters)=value
"""

 TreatAncestorsAsNonClientArea=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TreatAncestorsAsNonClientArea(self: HwndSourceParameters) -> bool

Set: TreatAncestorsAsNonClientArea(self: HwndSourceParameters)=value
"""

 TreatAsInputRoot=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: TreatAsInputRoot(self: HwndSourceParameters) -> bool

Set: TreatAsInputRoot(self: HwndSourceParameters)=value
"""

 UsesPerPixelOpacity=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that declares whether the per-pixel opacity of the source window content is respected.

Get: UsesPerPixelOpacity(self: HwndSourceParameters) -> bool

Set: UsesPerPixelOpacity(self: HwndSourceParameters)=value
"""

 UsesPerPixelTransparency=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UsesPerPixelTransparency(self: HwndSourceParameters) -> bool

Set: UsesPerPixelTransparency(self: HwndSourceParameters)=value
"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates the width of the window.

Get: Width(self: HwndSourceParameters) -> int

Set: Width(self: HwndSourceParameters)=value
"""

 WindowClassStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Microsoft Windows class style for the window.

Get: WindowClassStyle(self: HwndSourceParameters) -> int

Set: WindowClassStyle(self: HwndSourceParameters)=value
"""

 WindowName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of the window.

Get: WindowName(self: HwndSourceParameters) -> str

Set: WindowName(self: HwndSourceParameters)=value
"""

 WindowStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style for the window.

Get: WindowStyle(self: HwndSourceParameters) -> int

Set: WindowStyle(self: HwndSourceParameters)=value
"""


