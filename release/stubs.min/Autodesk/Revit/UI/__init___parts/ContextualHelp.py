class ContextualHelp(object):
 """
 Contains the details for how Revit should allow invocation of contextual help for an item added by an application.
 
 ContextualHelp(helpType: ContextualHelpType,helpPath: str)
 """
 def Launch(self):
  """
  Launch(self: ContextualHelp)
   Launches and displays the help topic specified by the contents of this 
    ContextualHelp object.
  """
  pass
 @staticmethod
 def __new__(self,helpType,helpPath):
  """ __new__(cls: type,helpType: ContextualHelpType,helpPath: str) """
  pass
 HelpPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The context id,help URL,or help file path.

Get: HelpPath(self: ContextualHelp) -> str

Set: HelpPath(self: ContextualHelp)=value
"""

 HelpTopicUrl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The help topic URL.

Get: HelpTopicUrl(self: ContextualHelp) -> str

Set: HelpTopicUrl(self: ContextualHelp)=value
"""

 HelpType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The contextual help type.

Get: HelpType(self: ContextualHelp) -> ContextualHelpType

Set: HelpType(self: ContextualHelp)=value
"""


