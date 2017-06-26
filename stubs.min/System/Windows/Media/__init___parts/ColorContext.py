class ColorContext(object):
 """
 Represents the International Color Consortium (ICC) or Image Color Management (ICM) color profile that is associated with a bitmap image.
 
 ColorContext(profileUri: Uri)
 ColorContext(pixelFormat: PixelFormat)
 """
 def Equals(self,obj):
  """
  Equals(self: ColorContext,obj: object) -> bool
  
   Determines whether an System.Object is equal to an instance of 
    System.Windows.Media.ColorContext.
  
  
   obj: Identifies the System.Object to compare for equality.
   Returns: true if the supplied System.Object is equal to this instance of 
    System.Windows.Media.ColorContext; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: ColorContext) -> int
  
   Gets the hash code for this instance of System.Windows.Media.ColorContext.
   Returns: An System.Int32 that represents the hash code for the object.
  """
  pass
 def OpenProfileStream(self):
  """
  OpenProfileStream(self: ColorContext) -> Stream
  
   Returns a readable System.IO.Stream of raw color profile data.
   Returns: A readable System.IO.Stream of raw color profile data.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,profileUri: Uri)
  __new__(cls: type,pixelFormat: PixelFormat)
  """
  pass
 def __ne__(self,*args):
  pass
 ProfileUri=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a System.Uri that represents the location of a International Color Consortium (ICC) or Image Color Management (ICM) color profile.

Get: ProfileUri(self: ColorContext) -> Uri

"""


