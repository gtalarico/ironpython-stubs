class D3DImage(ImageSource,ISealable,IAnimatable,IResource,IFormattable,IAppDomainShutdownListener):
 """
 An System.Windows.Media.ImageSource that displays a user-created Direct3D surface.
 
 D3DImage()
 D3DImage(dpiX: float,dpiY: float)
 """
 def AddDirtyRect(self,dirtyRect):
  """
  AddDirtyRect(self: D3DImage,dirtyRect: Int32Rect)
   Specifies the area of the back buffer that changed.
  
   dirtyRect: An System.Windows.Int32Rect that represents the area that changed.
  """
  pass
 def Clone(self):
  """
  Clone(self: D3DImage) -> D3DImage
  
   Creates a modifiable clone of this System.Windows.Interop.D3DImage object,
    making deep copies of this object's values. When copying dependency properties,
    this method copies resource references and data bindings (which may no longer 
    resolve),but not animations or their current values.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCore(self,*args):
  """
  CloneCore(self: D3DImage,sourceFreezable: Freezable)
   sourceFreezable: The object to clone.
  """
  pass
 def CloneCurrentValue(self):
  """
  CloneCurrentValue(self: D3DImage) -> D3DImage
  
   Creates a modifiable clone of this System.Windows.Interop.D3DImage object,
    making deep copies of this object's current values. Resource references,data 
    bindings,and animations are not copied,but their current values are copied.
  
   Returns: A modifiable clone of the current object. The cloned object's 
    System.Windows.Freezable.IsFrozen property will be false even if the source's 
    System.Windows.Freezable.IsFrozen property was true.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """
  CloneCurrentValueCore(self: D3DImage,sourceFreezable: Freezable)
   sourceFreezable: The System.Windows.Freezable to be cloned.
  """
  pass
 def CopyBackBuffer(self,*args):
  """
  CopyBackBuffer(self: D3DImage) -> BitmapSource
  
   Creates a software copy of the System.Windows.Interop.D3DImage.
   Returns: A System.Windows.Media.Imaging.BitmapSource that is a software copy of the 
    current state of the back buffer; otherwise,null if the back buffer cannot be 
    read.
  """
  pass
 def CreateInstance(self,*args):
  """
  CreateInstance(self: Freezable) -> Freezable
  
   Initializes a new instance of the System.Windows.Freezable class.
   Returns: The new instance.
  """
  pass
 def CreateInstanceCore(self,*args):
  """
  CreateInstanceCore(self: D3DImage) -> Freezable
  
   When implemented in a derived class,creates a new instance of the 
    System.Windows.Interop.D3DImage derived class.
  
   Returns: The new instance.
  """
  pass
 def FreezeCore(self,*args):
  """
  FreezeCore(self: D3DImage,isChecking: bool) -> bool
  
   Makes the System.Windows.Interop.D3DImage unmodifiable or determines whether it 
    can be made unmodifiable.
  
  
   isChecking: Has no effect.
   Returns: false in all cases.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: D3DImage,sourceFreezable: Freezable)
   sourceFreezable: The instance to copy.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: D3DImage,sourceFreezable: Freezable)
   sourceFreezable: The System.Windows.Freezable to copy and freeze.
  """
  pass
 def Lock(self):
  """
  Lock(self: D3DImage)
   Locks the System.Windows.Interop.D3DImage and enables operations on the back 
    buffer.
  """
  pass
 def OnChanged(self,*args):
  """
  OnChanged(self: Freezable)
   Called when the current System.Windows.Freezable object is modified.
  """
  pass
 def OnFreezablePropertyChanged(self,*args):
  """
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject,property: DependencyProperty)
   This member supports the Windows Presentation Foundation (WPF) infrastructure 
    and is not intended to be used directly from your code.
  
  
   oldValue: The previous value of the data member.
   newValue: The current value of the data member.
   property: The property that changed.
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject)
   Ensures that appropriate context pointers are established for a 
    System.Windows.DependencyObjectType data member that has just been set.
  
  
   oldValue: The previous value of the data member.
   newValue: The current value of the data member.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: Freezable,e: DependencyPropertyChangedEventArgs)
   Overrides the System.Windows.DependencyObject implementation of 
    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
    rtyChangedEventArgs) to also invoke any System.Windows.Freezable.Changed 
    handlers in response to a changing dependency property of type 
    System.Windows.Freezable.
  
  
   e: Event data that contains information about which property changed,and its old 
    and new values.
  """
  pass
 def ReadPreamble(self,*args):
  """
  ReadPreamble(self: Freezable)
   Ensures that the System.Windows.Freezable is being accessed from a valid 
    thread. Inheritors of System.Windows.Freezable must call this method at the 
    beginning of any API that reads data members that are not dependency 
    properties.
  """
  pass
 def SetBackBuffer(self,backBufferType,backBuffer,enableSoftwareFallback=None):
  """
  SetBackBuffer(self: D3DImage,backBufferType: D3DResourceType,backBuffer: IntPtr,enableSoftwareFallback: bool)SetBackBuffer(self: D3DImage,backBufferType: D3DResourceType,backBuffer: IntPtr)
   Assigns a Direct3D surface as the source of the back buffer.
  
   backBufferType: The type of Direct3D surface. Must be a valid 
    System.Windows.Interop.D3DResourceType.
  
   backBuffer: The Direct3D surface to assign as the back buffer.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def TryLock(self,timeout):
  """
  TryLock(self: D3DImage,timeout: Duration) -> bool
  
   Attempts to lock the System.Windows.Interop.D3DImage and waits for the 
    specified duration.
  
  
   timeout: The duration to wait for the lock to be acquired.
   Returns: true if the lock was acquired; otherwise,false.
  """
  pass
 def Unlock(self):
  """
  Unlock(self: D3DImage)
   Decrements the lock count for the System.Windows.Interop.D3DImage.
  """
  pass
 def WritePostscript(self,*args):
  """
  WritePostscript(self: Freezable)
   Raises the System.Windows.Freezable.Changed event for the 
    System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged 
    method. Classes that derive from System.Windows.Freezable should call this 
    method at the end of any API that modifies class members that are not stored as 
    dependency properties.
  """
  pass
 def WritePreamble(self,*args):
  """
  WritePreamble(self: Freezable)
   Verifies that the System.Windows.Freezable is not frozen and that it is being 
    accessed from a valid threading context. System.Windows.Freezable inheritors 
    should call this method at the beginning of any API that writes to data members 
    that are not dependency properties.
  """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,dpiX=None,dpiY=None):
  """
  __new__(cls: type)
  __new__(cls: type,dpiX: float,dpiY: float)
  """
  pass
 def __str__(self,*args):
  pass
 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height of the System.Windows.Interop.D3DImage.

Get: Height(self: D3DImage) -> float

"""

 IsFrontBufferAvailable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether a front buffer exists.

Get: IsFrontBufferAvailable(self: D3DImage) -> bool

"""

 Metadata=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the metadata associated with the image source.

Get: Metadata(self: D3DImage) -> ImageMetadata

"""

 PixelHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the height of the System.Windows.Interop.D3DImage,in pixels.

Get: PixelHeight(self: D3DImage) -> int

"""

 PixelWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width of the System.Windows.Interop.D3DImage,in pixels.

Get: PixelWidth(self: D3DImage) -> int

"""

 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the width of the System.Windows.Interop.D3DImage.

Get: Width(self: D3DImage) -> float

"""


 IsFrontBufferAvailableChanged=None
 IsFrontBufferAvailableProperty=None

