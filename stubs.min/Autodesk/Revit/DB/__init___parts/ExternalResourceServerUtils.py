class ExternalResourceServerUtils(object):
 """ Contains utilities related to external resource server. """
 @staticmethod
 def IsValidShortName(serverId,serverName):
  """
  IsValidShortName(serverId: Guid,serverName: str) -> bool
  
   Checks whether the name is a valid short name for the external resource server.
  
   serverId: The id of the external resource server.
   serverName: The short name of the external resource server.
   Returns: True if the name is a valid short name,false otherwise.
  """
  pass
 @staticmethod
 def ServerSupportsAssemblyCodeData(extRef):
  """
  ServerSupportsAssemblyCodeData(extRef: ExternalResourceReference) -> bool
  
   Checks that the server referenced by the given ExternalResourceReference 
    supports
     AssemblyCodeData.
  
  
   extRef: The ExternalResourceReference to check.
   Returns: True if the ExternalResourceReference refers to a server that supports 
    AssemblyCodeData. False otherwise.
  """
  pass
 @staticmethod
 def ServerSupportsKeynotes(extRef):
  """
  ServerSupportsKeynotes(extRef: ExternalResourceReference) -> bool
  
   Checks that the server referenced by the given ExternalResourceReference 
    supports
     KeynoteTable data.
  
  
   extRef: The ExternalResourceReference to check.
   Returns: True if the ExternalResourceReference refers to a server that supports 
    keynotes.  False otherwise.
  """
  pass
 @staticmethod
 def ServerSupportsRevitLinks(extRef):
  """
  ServerSupportsRevitLinks(extRef: ExternalResourceReference) -> bool
  
   Checks that the server referenced by the given ExternalResourceReference 
    supports
     Revit links.
  
  
   extRef: The ExternalResourceReference to check.
   Returns: True if the ExternalResourceReference refers to a server that supports Revit 
    links. False otherwise.
  """
  pass
 __all__=[
  'IsValidShortName',
  'ServerSupportsAssemblyCodeData',
  'ServerSupportsKeynotes',
  'ServerSupportsRevitLinks',
 ]

