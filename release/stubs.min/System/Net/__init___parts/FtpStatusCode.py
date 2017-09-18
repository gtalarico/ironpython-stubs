class FtpStatusCode(Enum,IComparable,IFormattable,IConvertible):
 """
 Specifies the status codes returned for a File Transfer Protocol (FTP) operation.

 

 enum FtpStatusCode,values: AccountNeeded (532),ActionAbortedLocalProcessingError (451),ActionAbortedUnknownPageType (551),ActionNotTakenFilenameNotAllowed (553),ActionNotTakenFileUnavailable (550),ActionNotTakenFileUnavailableOrBusy (450),ActionNotTakenInsufficientSpace (452),ArgumentSyntaxError (501),BadCommandSequence (503),CantOpenData (425),ClosingControl (221),ClosingData (226),CommandExtraneous (202),CommandNotImplemented (502),CommandOK (200),CommandSyntaxError (500),ConnectionClosed (426),DataAlreadyOpen (125),DirectoryStatus (212),EnteringPassive (227),FileActionAborted (552),FileActionOK (250),FileCommandPending (350),FileStatus (213),LoggedInProceed (230),NeedLoginAccount (332),NotLoggedIn (530),OpeningData (150),PathnameCreated (257),RestartMarker (110),SendPasswordCommand (331),SendUserCommand (220),ServerWantsSecureSession (234),ServiceNotAvailable (421),ServiceTemporarilyNotAvailable (120),SystemType (215),Undefined (0)
 """
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
  pass
 def __format__(self,*args):
  """ __format__(formattable: IFormattable,format: str) -> str """
  pass
 def __ge__(self,*args):
  pass
 def __gt__(self,*args):
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __le__(self,*args):
  pass
 def __lt__(self,*args):
  pass
 def __ne__(self,*args):
  pass
 def __reduce_ex__(self,*args):
  pass
 def __str__(self,*args):
  pass
 AccountNeeded=None
 ActionAbortedLocalProcessingError=None
 ActionAbortedUnknownPageType=None
 ActionNotTakenFilenameNotAllowed=None
 ActionNotTakenFileUnavailable=None
 ActionNotTakenFileUnavailableOrBusy=None
 ActionNotTakenInsufficientSpace=None
 ArgumentSyntaxError=None
 BadCommandSequence=None
 CantOpenData=None
 ClosingControl=None
 ClosingData=None
 CommandExtraneous=None
 CommandNotImplemented=None
 CommandOK=None
 CommandSyntaxError=None
 ConnectionClosed=None
 DataAlreadyOpen=None
 DirectoryStatus=None
 EnteringPassive=None
 FileActionAborted=None
 FileActionOK=None
 FileCommandPending=None
 FileStatus=None
 LoggedInProceed=None
 NeedLoginAccount=None
 NotLoggedIn=None
 OpeningData=None
 PathnameCreated=None
 RestartMarker=None
 SendPasswordCommand=None
 SendUserCommand=None
 ServerWantsSecureSession=None
 ServiceNotAvailable=None
 ServiceTemporarilyNotAvailable=None
 SystemType=None
 Undefined=None
 value__=None

