class SynchronizeWithCentralOptions(object,IDisposable):
 """
 Options to control behavior of synchronization with central.

 

 SynchronizeWithCentralOptions()
 """
 def Dispose(self):
  """ Dispose(self: SynchronizeWithCentralOptions) """
  pass
 def GetRelinquishOptions(self):
  """
  GetRelinquishOptions(self: SynchronizeWithCentralOptions) -> RelinquishOptions

  

   Gets the options which govern whether or not to relinquish elements and workset 

    types.

  

   Returns: The options.  If ll,synchronize with central will relinquish the current 

    user's ownership of all worksets and all elements.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: SynchronizeWithCentralOptions,disposing: bool) """
  pass
 def SetRelinquishOptions(self,relinquishOptions):
  """
  SetRelinquishOptions(self: SynchronizeWithCentralOptions,relinquishOptions: RelinquishOptions)

   Sets the options which govern whether or not to relinquish elements and workset 

    types.

  

  

   relinquishOptions: The options.  If ll,synchronize with central will relinquish the current 

    user's ownership of all worksets and all elements.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Comment=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """User description of changes made since the last Sync with Central.  Empty by default.



Get: Comment(self: SynchronizeWithCentralOptions) -> str



Set: Comment(self: SynchronizeWithCentralOptions)=value

"""

 Compact=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether Revit should compact the central model while synchronizing with central.

   This option reduces the size of the central model but many increase the time it takes to perform the save.

   False by default.



Get: Compact(self: SynchronizeWithCentralOptions) -> bool



Set: Compact(self: SynchronizeWithCentralOptions)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: SynchronizeWithCentralOptions) -> bool



"""

 RelinquishBorrowedElements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether Revit should relinquish borrowed elements after synchronizing with central.



Get: RelinquishBorrowedElements(self: SynchronizeWithCentralOptions) -> bool



"""

 RelinquishFamilyWorksets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether Revit should relinquish Family worksets after synchronizing with central.



Get: RelinquishFamilyWorksets(self: SynchronizeWithCentralOptions) -> bool



"""

 RelinquishProjectStandardWorksets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether Revit should relinquish Project Standard worksets after synchronizing with central.



Get: RelinquishProjectStandardWorksets(self: SynchronizeWithCentralOptions) -> bool



"""

 RelinquishUserCreatedWorksets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether Revit should relinquish user-created Standard worksets after synchronizing with central.



Get: RelinquishUserCreatedWorksets(self: SynchronizeWithCentralOptions) -> bool



"""

 RelinquishViewWorksets=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether Revit should relinquish View worksets after synchronizing with central.



Get: RelinquishViewWorksets(self: SynchronizeWithCentralOptions) -> bool



"""

 SaveLocalAfter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True means to save local after saving changes to central.  True by default.

   Silently ignored if the model in the current session is central rather than local.



Get: SaveLocalAfter(self: SynchronizeWithCentralOptions) -> bool



Set: SaveLocalAfter(self: SynchronizeWithCentralOptions)=value

"""

 SaveLocalBefore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """True means to save local before the first reload latest if there are changes not yet saved to local.

   True by default.  Silently ignored if the model in the current session is central rather than local.



Get: SaveLocalBefore(self: SynchronizeWithCentralOptions) -> bool



Set: SaveLocalBefore(self: SynchronizeWithCentralOptions)=value

"""

 SaveLocalFile=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether Revit will save the local file at least once while synchronizing with central.



Get: SaveLocalFile(self: SynchronizeWithCentralOptions) -> bool



"""


