class MessageBox(object):
 """ Displays a message box that can contain text,buttons,and symbols that inform and instruct the user. """
 @staticmethod
 def Show(*__args):
  """
  Show(text: str) -> DialogResult

  

   Displays a message box with specified text.

  

   text: The text to display in the message box.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions) -> DialogResult

  

   Displays a message box in front of the specified object and with the specified text,caption,

    buttons,icon,default button,and options.

  

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values the specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str) -> DialogResult

  

   Displays a message box with specified text and caption.

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon) -> DialogResult

  

   Displays a message box with specified text,caption,buttons,and icon.

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons) -> DialogResult

  

   Displays a message box with specified text,caption,and buttons.

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str) -> DialogResult

  

   Displays a message box in front of the specified object and with the specified text and caption.

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str) -> DialogResult

  

   Displays a message box in front of the specified object and with the specified text.

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str,buttons: MessageBoxButtons) -> DialogResult

  

   Displays a message box in front of the specified object and with the specified text,caption,

    and buttons.

  

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton) -> DialogResult

  

   Displays a message box in front of the specified object and with the specified text,caption,

    buttons,icon,and default button.

  

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon) -> DialogResult

  

   Displays a message box in front of the specified object and with the specified text,caption,

    buttons,and icon.

  

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,and default button.

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,helpFilePath: str,keyword: str) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button,using the specified Help file and Help keyword.

  

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   helpFilePath: The path and name of the Help file to display when the user clicks the Help button.

   keyword: The Help keyword to display when the user clicks the Help button.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,helpFilePath: str,keyword: str) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button,using the specified Help file and Help keyword.

  

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   helpFilePath: The path and name of the Help file to display when the user clicks the Help button.

   keyword: The Help keyword to display when the user clicks the Help button.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,helpFilePath: str) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button,using the specified Help file.

  

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   helpFilePath: The path and name of the Help file to display when the user clicks the Help button.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,displayHelpButton: bool) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button.

  

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   displayHelpButton: true to show the Help button; otherwise,false. The default is false.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,helpFilePath: str) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button,using the specified Help file.

  

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   helpFilePath: The path and name of the Help file to display when the user clicks the Help button.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,helpFilePath: str,navigator: HelpNavigator,param: object) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button,using the specified Help file,HelpNavigator,and Help topic.

  

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   helpFilePath: The path and name of the Help file to display when the user clicks the Help button.

   navigator: One of the System.Windows.Forms.HelpNavigator values.

   param: The numeric ID of the Help topic to display when the user clicks the Help button.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,and 

    options.

  

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,helpFilePath: str,navigator: HelpNavigator,param: object) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button,using the specified Help file,HelpNavigator,and Help topic.

  

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   helpFilePath: The path and name of the Help file to display when the user clicks the Help button.

   navigator: One of the System.Windows.Forms.HelpNavigator values.

   param: The numeric ID of the Help topic to display when the user clicks the Help button.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,helpFilePath: str,navigator: HelpNavigator) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button,using the specified Help file and HelpNavigator.

  

  

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   helpFilePath: The path and name of the Help file to display when the user clicks the Help button.

   navigator: One of the System.Windows.Forms.HelpNavigator values.

   Returns: One of the System.Windows.Forms.DialogResult values.

  Show(owner: IWin32Window,text: str,caption: str,buttons: MessageBoxButtons,icon: MessageBoxIcon,defaultButton: MessageBoxDefaultButton,options: MessageBoxOptions,helpFilePath: str,navigator: HelpNavigator) -> DialogResult

  

   Displays a message box with the specified text,caption,buttons,icon,default button,options,

    and Help button,using the specified Help file and HelpNavigator.

  

  

   owner: An implementation of System.Windows.Forms.IWin32Window that will own the modal dialog box.

   text: The text to display in the message box.

   caption: The text to display in the title bar of the message box.

   buttons: One of the System.Windows.Forms.MessageBoxButtons values that specifies which buttons to display 

    in the message box.

  

   icon: One of the System.Windows.Forms.MessageBoxIcon values that specifies which icon to display in 

    the message box.

  

   defaultButton: One of the System.Windows.Forms.MessageBoxDefaultButton values that specifies the default button 

    for the message box.

  

   options: One of the System.Windows.Forms.MessageBoxOptions values that specifies which display and 

    association options will be used for the message box. You may pass in 0 if you wish to use the 

    defaults.

  

   helpFilePath: The path and name of the Help file to display when the user clicks the Help button.

   navigator: One of the System.Windows.Forms.HelpNavigator values.

   Returns: One of the System.Windows.Forms.DialogResult values.
  """
  pass
