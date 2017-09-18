class TessellatedBuildIssue(object,IDisposable):
 """
 Types of issues encountered while constructing geometrical objects

    from the tessellated face sets.
 """
 def Dispose(self):
  """ Dispose(self: TessellatedBuildIssue) """
  pass
 def GetIssueDescription(self):
  """
  GetIssueDescription(self: TessellatedBuildIssue) -> str

  

   Gets a string describing the issue. If the issue does

     not present a 

    problem,then an empty string is returned.

  

   Returns: Description of the issue.
  """
  pass
 def IsValidIssue(self):
  """
  IsValidIssue(self: TessellatedBuildIssue) -> bool

  

   Reports whether the issue is well-formed,valid and does

     describe a real 

    problem.

  

   Returns: Whether the issue is well formed and does describe a real problem.
  """
  pass
 def MakesDataUnusable(self):
  """
  MakesDataUnusable(self: TessellatedBuildIssue) -> bool

  

   Reports whether this issue makes some data unusable ('true')

     or is only 

    shows that data format conventions were broken,

     but the data are still 

    usable (false).
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TessellatedBuildIssue,disposing: bool) """
  pass
 def ReportIssueToDataSource(self):
  """
  ReportIssueToDataSource(self: TessellatedBuildIssue) -> bool

  

   Reports whether this issue should be reported to the

     company which wrote 

    the software which produced the face set data

     (true),or to Autodesk 

    (false).
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
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: TessellatedBuildIssue) -> bool



"""

 NumberEncountered=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """How many times this issue was encountered in its face set

   during the face set processing. This number can be less

   than the total number of such issues in the face set,as

   the face set processing could be aborted due to

   the presence of the issues which could not be handled.



Get: NumberEncountered(self: TessellatedBuildIssue) -> int



"""


