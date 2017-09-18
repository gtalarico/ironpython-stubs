class UnitFormatUtils(object):
 """ A utility class for formatting and parsing numbers with units. """
 @staticmethod
 def Format(units,unitType,value,maxAccuracy,forEditing,formatValueOptions=None):
  """
  Format(units: Units,unitType: UnitType,value: float,maxAccuracy: bool,forEditing: bool,formatValueOptions: FormatValueOptions) -> str

  

   Formats a number with units into a string.

  

   units: The units formatting settings,typically obtained from 

    Autodesk.Revit.DB.Document.GetUnitsDocument.GetUnits().

  

   unitType: The unit type of the value to format.

   value: The value to format,in Revit's internal units.

   maxAccuracy: True if the value should be rounded to an increased accuracy level appropriate 

    for editing or understanding the precise value stored in the model.  False if 

    the accuracy specified by the FormatOptions should be used,appropriate for 

    printed drawings.

  

   forEditing: True if the formatting should be modified as necessary so that the formatted 

    string can be successfully parsed,for example by suppressing digit grouping.  

    False if unmodified settings should be used,suitable for display only.

  

   formatValueOptions: Additional formatting options.

   Returns: The formatted string.

  Format(units: Units,unitType: UnitType,value: float,maxAccuracy: bool,forEditing: bool) -> str

  

   Formats a number with units into a string.

  

   units: The units formatting settings,typically obtained from 

    Autodesk.Revit.DB.Document.GetUnitsDocument.GetUnits().

  

   unitType: The unit type of the value to format.

   value: The value to format,in Revit's internal units.

   maxAccuracy: True if the value should be rounded to an increased accuracy level appropriate 

    for editing or understanding the precise value stored in the model.  False if 

    the accuracy specified by the FormatOptions should be used,appropriate for 

    printed drawings.

  

   forEditing: True if the formatting should be modified as necessary so that the formatted 

    string can be successfully parsed,for example by suppressing digit grouping.  

    False if unmodified settings should be used,suitable for display only.

  

   Returns: The formatted string.
  """
  pass
 @staticmethod
 def TryParse(units,unitType,stringToParse,*__args):
  """
  TryParse(units: Units,unitType: UnitType,stringToParse: str,valueParsingOptions: ValueParsingOptions) -> (bool,float,str)

  

   Parses a formatted string into a number with units if possible.

  

   units: The units formatting settings,typically obtained from 

    Autodesk.Revit.DB.Document.GetUnitsDocument.GetUnits().

  

   unitType: The target unit type for the value.

   stringToParse: The string to parse.

   valueParsingOptions: Additional parsing options.

   Returns: True if the string can be parsed,false otherwise.

  TryParse(units: Units,unitType: UnitType,stringToParse: str,valueParsingOptions: ValueParsingOptions) -> (bool,float)

  

   Parses a formatted string into a number with units if possible.

  

   units: The units formatting settings,typically obtained from 

    Autodesk.Revit.DB.Document.GetUnitsDocument.GetUnits().

  

   unitType: The target unit type for the value.

   stringToParse: The string to parse.

   valueParsingOptions: Additional parsing options.

   Returns: True if the string can be parsed,false otherwise.

  TryParse(units: Units,unitType: UnitType,stringToParse: str) -> (bool,float,str)

  

   Parses a formatted string into a number with units if possible.

  

   units: The units formatting settings,typically obtained from 

    Autodesk.Revit.DB.Document.GetUnitsDocument.GetUnits().

  

   unitType: The target unit type for the value.

   stringToParse: The string to parse.

   Returns: True if the string can be parsed,false otherwise.

  TryParse(units: Units,unitType: UnitType,stringToParse: str) -> (bool,float)

  

   Parses a formatted string into a number with units if possible.

  

   units: The units formatting settings,typically obtained from 

    Autodesk.Revit.DB.Document.GetUnitsDocument.GetUnits().

  

   unitType: The target unit type for the value.

   stringToParse: The string to parse.

   Returns: True if the string can be parsed,false otherwise.
  """
  pass
 __all__=[
  'Format',
  'TryParse',
 ]

