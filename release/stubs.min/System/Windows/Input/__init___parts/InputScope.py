class InputScope(object):
 """
 Represents information related to the scope of data provided by an input method.
 
 InputScope()
 """
 Names=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the input scope name.

Get: Names(self: InputScope) -> IList

"""

 PhraseList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of phrases to be used as suggested input patterns by input processors.

Get: PhraseList(self: InputScope) -> IList

"""

 RegularExpression=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a regular expression to be used as a suggested text input pattern by input processors.

Get: RegularExpression(self: InputScope) -> str

Set: RegularExpression(self: InputScope)=value
"""

 SrgsMarkup=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string that specifies any Speech Recognition Grammar Specification (SRGS) markup to be used as a suggested input pattern by input processors.

Get: SrgsMarkup(self: InputScope) -> str

Set: SrgsMarkup(self: InputScope)=value
"""


