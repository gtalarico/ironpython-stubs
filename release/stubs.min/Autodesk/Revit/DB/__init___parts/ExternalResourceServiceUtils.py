class ExternalResourceServiceUtils(object):
 """ Contains utilities related to external resource service. """
 @staticmethod
 def GetServersByType(type):
  """
  GetServersByType(type: ExternalResourceType) -> IList[IExternalResourceServer]

  

   Gets registered external resource servers which support the external resource 

    type.

  

  

   type: The external resource type for the servers to match

   Returns: A list of matched external resource servers
  """
  pass
 __all__=[
  'GetServersByType',
 ]

