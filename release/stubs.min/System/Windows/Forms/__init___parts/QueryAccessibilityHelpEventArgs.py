class QueryAccessibilityHelpEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.QueryAccessibilityHelp event.

 

 QueryAccessibilityHelpEventArgs()

 QueryAccessibilityHelpEventArgs(helpNamespace: str,helpString: str,helpKeyword: str)
 """
 @staticmethod
 def __new__(self,helpNamespace=None,helpString=None,helpKeyword=None):
  """
  __new__(cls: type)

  __new__(cls: type,helpNamespace: str,helpString: str,helpKeyword: str)
  """
  pass
 HelpKeyword=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Help keyword for the specified control.



Get: HelpKeyword(self: QueryAccessibilityHelpEventArgs) -> str



Set: HelpKeyword(self: QueryAccessibilityHelpEventArgs)=value

"""

 HelpNamespace=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value specifying the name of the Help file.



Get: HelpNamespace(self: QueryAccessibilityHelpEventArgs) -> str



Set: HelpNamespace(self: QueryAccessibilityHelpEventArgs)=value

"""

 HelpString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the string defining what Help to get for the System.Windows.Forms.AccessibleObject.



Get: HelpString(self: QueryAccessibilityHelpEventArgs) -> str



Set: HelpString(self: QueryAccessibilityHelpEventArgs)=value

"""


