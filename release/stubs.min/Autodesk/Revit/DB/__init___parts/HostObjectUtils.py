class HostObjectUtils(object):
 """ These are generic host object utilities. """
 @staticmethod
 def GetBottomFaces(hostObject):
  """
  GetBottomFaces(hostObject: HostObject) -> IList[Reference]

  

   Returns the bottom faces for this host object.

  

   hostObject: The host object.

   Returns: An array of references to the faces which are at the bottom of this element.
  """
  pass
 @staticmethod
 def GetSideFaces(hostObject,side):
  """
  GetSideFaces(hostObject: HostObject,side: ShellLayerType) -> IList[Reference]

  

   Returns the major side faces for this host object.

  

   hostObject: The host object.

   side: The side of the host object.

   Returns: An array of references to the faces which are on the given side of this element.
  """
  pass
 @staticmethod
 def GetTopFaces(hostObject):
  """
  GetTopFaces(hostObject: HostObject) -> IList[Reference]

  

   Returns the top faces for this host object.

  

   hostObject: The host object.

   Returns: An array of references to the faces which are at the top of this element.
  """
  pass
 __all__=[
  'GetBottomFaces',
  'GetSideFaces',
  'GetTopFaces',
 ]

