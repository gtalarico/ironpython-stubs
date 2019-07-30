# encoding: utf-8
# module Wms.RemotingObjects.ScriptTasks calls itself ScriptTasks
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class ScriptTask(DbObject):
 """ ScriptTask() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ScriptTask()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __reduce_ex__(self,*args):
  pass
 Active=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Active(self: ScriptTask) -> bool

Set: Active(self: ScriptTask)=value
"""

 Days=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Days(self: ScriptTask) -> str

Set: Days(self: ScriptTask)=value
"""

 DaysToExecute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: DaysToExecute(self: ScriptTask) -> List[str]

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Description(self: ScriptTask) -> str

Set: Description(self: ScriptTask)=value
"""

 EndDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: EndDate(self: ScriptTask) -> Nullable[DateTime]

Set: EndDate(self: ScriptTask)=value
"""

 ExecuteOnFriday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteOnFriday(self: ScriptTask) -> bool

Set: ExecuteOnFriday(self: ScriptTask)=value
"""

 ExecuteOnMonday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteOnMonday(self: ScriptTask) -> bool

Set: ExecuteOnMonday(self: ScriptTask)=value
"""

 ExecuteOnSaturday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteOnSaturday(self: ScriptTask) -> bool

Set: ExecuteOnSaturday(self: ScriptTask)=value
"""

 ExecuteOnSunday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteOnSunday(self: ScriptTask) -> bool

Set: ExecuteOnSunday(self: ScriptTask)=value
"""

 ExecuteOnThursday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteOnThursday(self: ScriptTask) -> bool

Set: ExecuteOnThursday(self: ScriptTask)=value
"""

 ExecuteOnTuesday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteOnTuesday(self: ScriptTask) -> bool

Set: ExecuteOnTuesday(self: ScriptTask)=value
"""

 ExecuteOnWednesday=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: ExecuteOnWednesday(self: ScriptTask) -> bool

Set: ExecuteOnWednesday(self: ScriptTask)=value
"""

 Hours=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Hours(self: ScriptTask) -> str

Set: Hours(self: ScriptTask)=value
"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Id(self: ScriptTask) -> int

Set: Id(self: ScriptTask)=value
"""

 Interval=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Interval(self: ScriptTask) -> int

Set: Interval(self: ScriptTask)=value
"""

 Minutes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Minutes(self: ScriptTask) -> str

Set: Minutes(self: ScriptTask)=value
"""

 Months=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Months(self: ScriptTask) -> str

Set: Months(self: ScriptTask)=value
"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Name(self: ScriptTask) -> str

Set: Name(self: ScriptTask)=value
"""

 Priority=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Priority(self: ScriptTask) -> ScriptTaskPriority

Set: Priority(self: ScriptTask)=value
"""

 Script=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: Script(self: ScriptTask) -> str

Set: Script(self: ScriptTask)=value
"""

 StartDate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """

Get: StartDate(self: ScriptTask) -> DateTime

Set: StartDate(self: ScriptTask)=value
"""

 UserId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the account under wich this task will run.

Get: UserId(self: ScriptTask) -> int

Set: UserId(self: ScriptTask)=value
"""

 ZoneId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The id of the zone on wich this task will run.

Get: ZoneId(self: ScriptTask) -> int

Set: ZoneId(self: ScriptTask)=value
"""



class ScriptTaskPriority:
 """ enum ScriptTaskPriority,values: High (3),Low (1),Normal (2) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ScriptTaskPriority()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
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
 High=None
 Low=None
 Normal=None
 value__=None


class ScriptTasks(FindableList):
 """ ScriptTasks() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ScriptTasks()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __iter__(self,*args):
  """ __iter__(self: IEnumerable) -> object """
  pass
 def __reduce_ex__(self,*args):
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 DisplayMember='Name'
 ValueMember='Id'


