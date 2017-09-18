class SpellingError(object):
 """ Represents a misspelled word in an editing control (i.e. System.Windows.Controls.TextBox or System.Windows.Controls.RichTextBox). """
 def Correct(self,correctedText):
  """
  Correct(self: SpellingError,correctedText: str)

   Replaces the spelling error text with the specified correction.

  

   correctedText: The text used to replace the misspelled text.
  """
  pass
 def IgnoreAll(self):
  """
  IgnoreAll(self: SpellingError)

   Instructs the control to ignore this error and any duplicates for the remainder of the lifetime 

    of the control.
  """
  pass
 Suggestions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a list of suggested spelling replacements for the misspelled word.



Get: Suggestions(self: SpellingError) -> IEnumerable[str]



"""


