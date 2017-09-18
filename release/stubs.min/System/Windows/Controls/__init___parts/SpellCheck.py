class SpellCheck(object):
 """ Provides real-time spell-checking functionality to text-editing controls,such as System.Windows.Controls.TextBox and System.Windows.Controls.RichTextBox. """
 @staticmethod
 def GetCustomDictionaries(textBoxBase):
  """
  GetCustomDictionaries(textBoxBase: TextBoxBase) -> IList

  

   Gets the collection of lexicon file locations that are used for custom spelling checkers on a 

    specified text-editing control.

  

  

   textBoxBase: The text-editing control whose collection of lexicon files is retrieved.

   Returns: The collection of lexicon file locations.
  """
  pass
 @staticmethod
 def GetIsEnabled(textBoxBase):
  """
  GetIsEnabled(textBoxBase: TextBoxBase) -> bool

  

   Returns a value that indicates whether the spelling checker is enabled on the specified 

    text-editing control.

  

  

   textBoxBase: The text-editing control to check. Example controls include System.Windows.Controls.TextBox and 

    System.Windows.Controls.RichTextBox.

  

   Returns: true if the spelling checker is enabled on the text-editing control; otherwise,false.
  """
  pass
 @staticmethod
 def SetIsEnabled(textBoxBase,value):
  """
  SetIsEnabled(textBoxBase: TextBoxBase,value: bool)

   Enables or disables the spelling checker on the specified text-editing control,such as 

    System.Windows.Controls.TextBox or System.Windows.Controls.RichTextBox.

  

  

   textBoxBase: The text-editing control on which to enable or disable the spelling checker. Example controls 

    include System.Windows.Controls.TextBox and System.Windows.Controls.RichTextBox.

  

   value: A Boolean value that specifies whether the spelling checker is enabled on the text-editing 

    control.
  """
  pass
 @staticmethod
 def SetSpellingReform(textBoxBase,value):
  """
  SetSpellingReform(textBoxBase: TextBoxBase,value: SpellingReform)

   Determines the spelling reform rules that are used by the spelling checker.

  

   textBoxBase: The text-editing control to which the spelling checker is applied. Example controls include 

    System.Windows.Controls.TextBox and System.Windows.Controls.RichTextBox.

  

   value: The System.Windows.Controls.SpellCheck.SpellingReform value that determines the spelling reform 

    rules.
  """
  pass
 CustomDictionaries=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of lexicon file locations that are used for custom spell checking.



Get: CustomDictionaries(self: SpellCheck) -> IList



"""

 IsEnabled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines whether the spelling checker is enabled on this text-editing control,such as System.Windows.Controls.TextBox or System.Windows.Controls.RichTextBox.



Get: IsEnabled(self: SpellCheck) -> bool



Set: IsEnabled(self: SpellCheck)=value

"""

 SpellingReform=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the spelling reform rules that are used by the spelling checker.



Get: SpellingReform(self: SpellCheck) -> SpellingReform



Set: SpellingReform(self: SpellCheck)=value

"""


 CustomDictionariesProperty=None
 IsEnabledProperty=None
 SpellingReformProperty=None

