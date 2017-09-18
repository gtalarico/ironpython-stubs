class ToolboxBitmapAttribute(Attribute,_Attribute):
 """
 Allows you to specify an icon to represent a control in a container,such as the Microsoft Visual Studio Form Designer.

 

 ToolboxBitmapAttribute(imageFile: str)

 ToolboxBitmapAttribute(t: Type)

 ToolboxBitmapAttribute(t: Type,name: str)
 """
 def Equals(self,value):
  """
  Equals(self: ToolboxBitmapAttribute,value: object) -> bool

  

   Indicates whether the specified object is a System.Drawing.ToolboxBitmapAttribute object and is 

    identical to this System.Drawing.ToolboxBitmapAttribute object.

  

  

   value: The System.Object to test.

   Returns: This method returns true if value is both a System.Drawing.ToolboxBitmapAttribute object and is 

    identical to this System.Drawing.ToolboxBitmapAttribute object.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ToolboxBitmapAttribute) -> int

  

   Gets a hash code for this System.Drawing.ToolboxBitmapAttribute object.

   Returns: The hash code for this System.Drawing.ToolboxBitmapAttribute object.
  """
  pass
 def GetImage(self,*__args):
  """
  GetImage(self: ToolboxBitmapAttribute,type: Type,large: bool) -> Image

  

   Gets the small or large System.Drawing.Image associated with this 

    System.Drawing.ToolboxBitmapAttribute object.

  

  

   type: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image,this 

    method searches for a bitmap resource in the assembly that defines the type specified by the 

    component type. For example,if you pass typeof(ControlA) to the type parameter,then this 

    method searches the assembly that defines ControlA.

  

   large: Specifies whether this method returns a large image (true) or a small image (false). The small 

    image is 16 by 16,and the large image is 32 by 32.

  

   Returns: An System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute object.

  GetImage(self: ToolboxBitmapAttribute,type: Type,imgName: str,large: bool) -> Image

  

   Gets the small or large System.Drawing.Image associated with this 

    System.Drawing.ToolboxBitmapAttribute object.

  

  

   type: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image,this 

    method searches for an embedded bitmap resource in the assembly that defines the type specified 

    by the component type. For example,if you pass typeof(ControlA) to the type parameter,then 

    this method searches the assembly that defines ControlA.

  

   imgName: The name of the embedded bitmap resource.

   large: Specifies whether this method returns a large image (true) or a small image (false). The small 

    image is 16 by 16,and the large image is 32 by 32.

  

   Returns: An System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute object.

  GetImage(self: ToolboxBitmapAttribute,type: Type) -> Image

  

   Gets the small System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute 

    object.

  

  

   type: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image,this 

    method searches for a bitmap resource in the assembly that defines the type specified by the 

    type parameter. For example,if you pass typeof(ControlA) to the type parameter,then this 

    method searches the assembly that defines ControlA.

  

   Returns: The small System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute object.

  GetImage(self: ToolboxBitmapAttribute,component: object) -> Image

  

   Gets the small System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute 

    object.

  

  

   component: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image,this 

    method searches for a bitmap resource in the assembly that defines the type of the object 

    specified by the component parameter. For example,if you pass an object of type ControlA to the 

    component parameter,then this method searches the assembly that defines ControlA.

  

   Returns: The small System.Drawing.Image associated with this System.Drawing.ToolboxBitmapAttribute object.

  GetImage(self: ToolboxBitmapAttribute,component: object,large: bool) -> Image

  

   Gets the small or large System.Drawing.Image associated with this 

    System.Drawing.ToolboxBitmapAttribute object.

  

  

   component: If this System.Drawing.ToolboxBitmapAttribute object does not already have a small image,this 

    method searches for a bitmap resource in the assembly that defines the type of the object 

    specified by the component parameter. For example,if you pass an object of type ControlA to the 

    component parameter,then this method searches the assembly that defines ControlA.

  

   large: Specifies whether this method returns a large image (true) or a small image (false). The small 

    image is 16 by 16,and the large image is 32 by 32.

  

   Returns: An System.Drawing.Image object associated with this System.Drawing.ToolboxBitmapAttribute object.
  """
  pass
 @staticmethod
 def GetImageFromResource(t,imageName,large):
  """
  GetImageFromResource(t: Type,imageName: str,large: bool) -> Image

  

   Returns an System.Drawing.Image object based on a bitmap resource that is embedded in an 

    assembly.

  

  

   t: This method searches for an embedded bitmap resource in the assembly that defines the type 

    specified by the t parameter. For example,if you pass typeof(ControlA) to the t parameter,then 

    this method searches the assembly that defines ControlA.

  

   imageName: The name of the embedded bitmap resource.

   large: Specifies whether this method returns a large image (true)or a small image (false). The small 

    image is 16 by 16,and the large image is 32 x 32.

  

   Returns: An System.Drawing.Image object based on the retrieved bitmap.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,imageFile: str)

  __new__(cls: type,t: Type)

  __new__(cls: type,t: Type,name: str)
  """
  pass
 def __ne__(self,*args):
  pass
 Default=None


# variables with complex values

