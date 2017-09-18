class QuestionEventArgs(EventArgs):
 """
 Provides data for events that need a true or false answer to a question.

 

 QuestionEventArgs()

 QuestionEventArgs(response: bool)
 """
 @staticmethod
 def __new__(self,response=None):
  """
  __new__(cls: type)

  __new__(cls: type,response: bool)
  """
  pass
 Response=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the response to a question represented by the event.



Get: Response(self: QuestionEventArgs) -> bool



Set: Response(self: QuestionEventArgs)=value

"""


