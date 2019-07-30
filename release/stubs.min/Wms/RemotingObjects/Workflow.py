# encoding: utf-8
# module Wms.RemotingObjects.Workflow calls itself Workflow
# from Wms.RemotingObjects,Version=1.23.1.0,Culture=neutral,PublicKeyToken=null
# by generator 1.145
# no doc
# no important
from __init__ import *

# no functions
# classes

class Activity(object):
 """ Activity() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Activity()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The current progress

Get: Current(self: Activity) -> Decimal

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """A description of the activity

Get: Description(self: Activity) -> str

Set: Description(self: Activity)=value
"""

 Progress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Collection with the progress made in different measurements

Get: Progress(self: Activity) -> List[Progress]

"""

 StartedAt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The moment when the activity started

Get: StartedAt(self: Activity) -> DateTime

Set: StartedAt(self: Activity)=value
"""

 TimeSpent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The total amount of time spent on the workflow (in seconds)

Get: TimeSpent(self: Activity) -> int

"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The title to show to the user

Get: Title(self: Activity) -> str

"""

 Total=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The max of the progress

Get: Total(self: Activity) -> Decimal

"""

 Workers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """List of the names of people working at this activity

Get: Workers(self: Activity) -> List[str]

"""



class Progress(object):
 """ Progress() """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return Progress()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Current=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Current(self: Progress) -> Decimal

Set: Current(self: Progress)=value
"""

 GeneratedImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: GeneratedImage(self: Progress) -> Array[Byte]

Set: GeneratedImage(self: Progress)=value
"""

 HasGeneratedImage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasGeneratedImage(self: Progress) -> bool

"""

 IsMainProgress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsMainProgress(self: Progress) -> bool

Set: IsMainProgress(self: Progress)=value
"""

 ProgressColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ProgressColor(self: Progress) -> str

Set: ProgressColor(self: Progress)=value
"""

 Title=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Title(self: Progress) -> str

Set: Title(self: Progress)=value
"""

 Total=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Total(self: Progress) -> Decimal

Set: Total(self: Progress)=value
"""



