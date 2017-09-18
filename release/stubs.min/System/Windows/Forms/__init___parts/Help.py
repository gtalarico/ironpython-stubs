class Help(object):
 """ Encapsulates the HTML Help 1.0 engine. """
 @staticmethod
 def ShowHelp(parent,url,*__args):
  """
  ShowHelp(parent: Control,url: str,keyword: str)

   Displays the contents of the Help file found at the specified URL for a specific keyword.

  

   parent: A System.Windows.Forms.Control that identifies the parent of the Help dialog box.

   url: The path and name of the Help file.

   keyword: The keyword to display Help for.

  ShowHelp(parent: Control,url: str,command: HelpNavigator,parameter: object)

   Displays the contents of the Help file located at the URL supplied by the user.

  

   parent: A System.Windows.Forms.Control that identifies the parent of the Help dialog box.

   url: The path and name of the Help file.

   command: One of the System.Windows.Forms.HelpNavigator values.

   parameter: A string that contains the topic identifier.

  ShowHelp(parent: Control,url: str)

   Displays the contents of the Help file at the specified URL.

  

   parent: A System.Windows.Forms.Control that identifies the parent of the Help dialog box.

   url: The path and name of the Help file.

  ShowHelp(parent: Control,url: str,navigator: HelpNavigator)

   Displays the contents of the Help file found at the specified URL for a specific topic.

  

   parent: A System.Windows.Forms.Control that identifies the parent of the Help dialog box.

   url: The path and name of the Help file.

   navigator: One of the System.Windows.Forms.HelpNavigator values.
  """
  pass
 @staticmethod
 def ShowHelpIndex(parent,url):
  """
  ShowHelpIndex(parent: Control,url: str)

   Displays the index of the specified Help file.

  

   parent: A System.Windows.Forms.Control that identifies the parent of the Help dialog box.

   url: The path and name of the Help file.
  """
  pass
 @staticmethod
 def ShowPopup(parent,caption,location):
  """
  ShowPopup(parent: Control,caption: str,location: Point)

   Displays a Help pop-up window.

  

   parent: A System.Windows.Forms.Control that identifies the parent of the Help dialog box.

   caption: The message to display in the pop-up window.

   location: A value that specifies the horizontal and vertical coordinates at which to display the pop-up 

    window,relative to the upper-left corner of the screen.
  """
  pass
