class MessageBox(object):
 """ Displays a message box. """
 @staticmethod
 def Show(*__args):
  """
  Show(owner: Window,messageBoxText: str,caption: str,button: MessageBoxButton,icon: MessageBoxImage) -> MessageBoxResult
  
   Displays a message box in front of the specified window. The message box 
    displays a message,title bar caption,button,and icon; and it also returns a 
    result.
  
  
   owner: A System.Windows.Window that represents the owner window of the message box.
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   button: A System.Windows.MessageBoxButton value that specifies which button or buttons 
    to display.
  
   icon: A System.Windows.MessageBoxImage value that specifies the icon to display.
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(owner: Window,messageBoxText: str,caption: str,button: MessageBoxButton,icon: MessageBoxImage,defaultResult: MessageBoxResult) -> MessageBoxResult
  
   Displays a message box in front of the specified window. The message box 
    displays a message,title bar caption,button,and icon; and accepts a default 
    message box result and returns a result.
  
  
   owner: A System.Windows.Window that represents the owner window of the message box.
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   button: A System.Windows.MessageBoxButton value that specifies which button or buttons 
    to display.
  
   icon: A System.Windows.MessageBoxImage value that specifies the icon to display.
   defaultResult: A System.Windows.MessageBoxResult value that specifies the default result of 
    the message box.
  
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(owner: Window,messageBoxText: str,caption: str,button: MessageBoxButton,icon: MessageBoxImage,defaultResult: MessageBoxResult,options: MessageBoxOptions) -> MessageBoxResult
  
   Displays a message box in front of the specified window. The message box 
    displays a message,title bar caption,button,and icon; and accepts a default 
    message box result,complies with the specified options,and returns a result.
  
  
   owner: A System.Windows.Window that represents the owner window of the message box.
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   button: A System.Windows.MessageBoxButton value that specifies which button or buttons 
    to display.
  
   icon: A System.Windows.MessageBoxImage value that specifies the icon to display.
   defaultResult: A System.Windows.MessageBoxResult value that specifies the default result of 
    the message box.
  
   options: A System.Windows.MessageBoxOptions value object that specifies the options.
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(owner: Window,messageBoxText: str) -> MessageBoxResult
  
   Displays a message box in front of the specified window. The message box 
    displays a message and returns a result.
  
  
   owner: A System.Windows.Window that represents the owner window of the message box.
   messageBoxText: A System.String that specifies the text to display.
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(owner: Window,messageBoxText: str,caption: str) -> MessageBoxResult
  
   Displays a message box in front of the specified window. The message box 
    displays a message and title bar caption; and it returns a result.
  
  
   owner: A System.Windows.Window that represents the owner window of the message box.
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(owner: Window,messageBoxText: str,caption: str,button: MessageBoxButton) -> MessageBoxResult
  
   Displays a message box in front of the specified window. The message box 
    displays a message,title bar caption,and button; and it also returns a 
    result.
  
  
   owner: A System.Windows.Window that represents the owner window of the message box.
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   button: A System.Windows.MessageBoxButton value that specifies which button or buttons 
    to display.
  
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(messageBoxText: str,caption: str,button: MessageBoxButton,icon: MessageBoxImage) -> MessageBoxResult
  
   Displays a message box that has a message,title bar caption,button,and icon; 
    and that returns a result.
  
  
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   button: A System.Windows.MessageBoxButton value that specifies which button or buttons 
    to display.
  
   icon: A System.Windows.MessageBoxImage value that specifies the icon to display.
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(messageBoxText: str,caption: str,button: MessageBoxButton,icon: MessageBoxImage,defaultResult: MessageBoxResult) -> MessageBoxResult
  
   Displays a message box that has a message,title bar caption,button,and icon; 
    and that accepts a default message box result and returns a result.
  
  
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   button: A System.Windows.MessageBoxButton value that specifies which button or buttons 
    to display.
  
   icon: A System.Windows.MessageBoxImage value that specifies the icon to display.
   defaultResult: A System.Windows.MessageBoxResult value that specifies the default result of 
    the message box.
  
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(messageBoxText: str,caption: str,button: MessageBoxButton,icon: MessageBoxImage,defaultResult: MessageBoxResult,options: MessageBoxOptions) -> MessageBoxResult
  
   Displays a message box that has a message,title bar caption,button,and icon; 
    and that accepts a default message box result,complies with the specified 
    options,and returns a result.
  
  
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   button: A System.Windows.MessageBoxButton value that specifies which button or buttons 
    to display.
  
   icon: A System.Windows.MessageBoxImage value that specifies the icon to display.
   defaultResult: A System.Windows.MessageBoxResult value that specifies the default result of 
    the message box.
  
   options: A System.Windows.MessageBoxOptions value object that specifies the options.
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(messageBoxText: str) -> MessageBoxResult
  
   Displays a message box that has a message and that returns a result.
  
   messageBoxText: A System.String that specifies the text to display.
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(messageBoxText: str,caption: str) -> MessageBoxResult
  
   Displays a message box that has a message and title bar caption; and that 
    returns a result.
  
  
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  
  Show(messageBoxText: str,caption: str,button: MessageBoxButton) -> MessageBoxResult
  
   Displays a message box that has a message,title bar caption,and button; and 
    that returns a result.
  
  
   messageBoxText: A System.String that specifies the text to display.
   caption: A System.String that specifies the title bar caption to display.
   button: A System.Windows.MessageBoxButton value that specifies which button or buttons 
    to display.
  
   Returns: A System.Windows.MessageBoxResult value that specifies which message box button 
    is clicked by the user.
  """
  pass
