class IUpdater:
 """ The interface used to create an updater capable of reacting to changes in the Revit model. """
 def Execute(self,data):
  """
  Execute(self: IUpdater,data: UpdaterData)

   The method that Revit will invoke to perform an update.

  

   data: Provides all necessary data needed to perform the update,including the 

    document and information about

     the changes that triggered the update.
  """
  pass
 def GetAdditionalInformation(self):
  """
  GetAdditionalInformation(self: IUpdater) -> str

  

   Auxiliary text that Revit will use to inform the end user

     when the Updater 

    is not loaded
  """
  pass
 def GetChangePriority(self):
  """
  GetChangePriority(self: IUpdater) -> ChangePriority

  

   Identifies the nature of the change the Updater will be performing

     Used to 

    identify order of execution of updaters

     Called once during registration of 

    the updater
  """
  pass
 def GetUpdaterId(self):
  """
  GetUpdaterId(self: IUpdater) -> UpdaterId

  

   Returns globally unique updater id - used to identify the Updater

     Called 

    once during registration of the updater
  """
  pass
 def GetUpdaterName(self):
  """
  GetUpdaterName(self: IUpdater) -> str

  

   Returns a name that the Updater can be identified by to the user
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
