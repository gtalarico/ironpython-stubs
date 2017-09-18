# encoding: utf-8
# module Grasshopper.Kernel.Expressions calls itself Expressions
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_CharType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_CharType, values: bracket_close (24), bracket_open (23), colon (4), comma (3), commentbody (62), commentend (61), commentstart (60), continuation (6), dot (2), newline (7), operator (20), parenthesis_close (22), parenthesis_open (21), semicolon (5), stringbody (52), stringend (51), stringstart (50), undefined (0), whitespace (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    bracket_close = None
    bracket_open = None
    colon = None
    comma = None
    commentbody = None
    commentend = None
    commentstart = None
    continuation = None
    dot = None
    newline = None
    operator = None
    parenthesis_close = None
    parenthesis_open = None
    semicolon = None
    stringbody = None
    stringend = None
    stringstart = None
    undefined = None
    value__ = None
    whitespace = None


class GH_CodeString(object):
    """ GH_CodeString(input: str) """
    def Flatten(self):
        """ Flatten(self: GH_CodeString) -> str """
        pass

    def ParseNewString(self, input):
        """ ParseNewString(self: GH_CodeString, input: str) """
        pass

    def Replace(self, search, replace, bIgnoreCase, bOmitNonCode):
        """ Replace(self: GH_CodeString, search: str, replace: str, bIgnoreCase: bool, bOmitNonCode: bool) """
        pass

    def ReplaceToken(self, search, replace, bIgnoreCase, bOmitNonCode):
        """ ReplaceToken(self: GH_CodeString, search: str, replace: str, bIgnoreCase: bool, bOmitNonCode: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, input):
        """ __new__(cls: type, input: str) """
        pass

    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: GH_CodeString) -> List[GH_CodeStringSegment]

"""


    DoubleQuote = None
    m_Segments = None


class GH_CodeStringSegment(object):
    """ GH_CodeStringSegment(nString: str, bIsCode: bool) """
    def IsAlpha(self, *args): #cannot find CLR method
        """ IsAlpha(self: GH_CodeStringSegment, C: Char) -> bool """
        pass

    def Replace(self, search, replace, bIgnoreCase):
        """ Replace(self: GH_CodeStringSegment, search: str, replace: str, bIgnoreCase: bool) """
        pass

    def ReplaceToken(self, token, replace, bIgnoreCase):
        """ ReplaceToken(self: GH_CodeStringSegment, token: str, replace: str, bIgnoreCase: bool) """
        pass

    def ToString(self):
        """ ToString(self: GH_CodeStringSegment) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nString, bIsCode):
        """ __new__(cls: type, nString: str, bIsCode: bool) """
        pass

    IsCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCode(self: GH_CodeStringSegment) -> bool

Set: IsCode(self: GH_CodeStringSegment) = value
"""

    String = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: String(self: GH_CodeStringSegment) -> str

Set: String(self: GH_CodeStringSegment) = value
"""

    StringValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StringValue(self: GH_CodeStringSegment) -> str

"""


    m_IsCode = None
    m_String = None


class GH_ExpressionParser(object):
    """
    GH_ExpressionParser()
    GH_ExpressionParser(bThrowExceptions: bool)
    """
    def AddVariable(self, name, val):
        """ AddVariable(self: GH_ExpressionParser, name: str, val: Vector3d)AddVariable(self: GH_ExpressionParser, name: str, val: str)AddVariable(self: GH_ExpressionParser, name: str, val: Plane)AddVariable(self: GH_ExpressionParser, name: str, val: Point3d)AddVariable(self: GH_ExpressionParser, name: str, val: int)AddVariable(self: GH_ExpressionParser, name: str, val: bool)AddVariable(self: GH_ExpressionParser, name: str, val: Complex)AddVariable(self: GH_ExpressionParser, name: str, val: float) """
        pass

    def AddVariableEx(self, name, val):
        """ AddVariableEx(self: GH_ExpressionParser, name: str, val: IGH_Goo)AddVariableEx(self: GH_ExpressionParser, name: str, val: GH_Variant) """
        pass

    @staticmethod
    def BalancedCharTest(str, char_open, char_close, error_at):
        """ BalancedCharTest(str: str, char_open: Char, char_close: Char) -> (bool, int) """
        pass

    def CachedSymbols(self):
        """ CachedSymbols(self: GH_ExpressionParser) -> Queue[GH_ParserSymbol] """
        pass

    def CacheSymbols(self, Expression):
        """ CacheSymbols(self: GH_ExpressionParser, Expression: str) -> bool """
        pass

    def ClearSymbols(self):
        """ ClearSymbols(self: GH_ExpressionParser) """
        pass

    def ClearVariables(self):
        """ ClearVariables(self: GH_ExpressionParser) """
        pass

    def DisplayFunctionList(self, wnd):
        """ DisplayFunctionList(self: GH_ExpressionParser, wnd: IWin32Window) """
        pass

    def Evaluate(self, *__args):
        """
        Evaluate(self: GH_ExpressionParser, Expression: str) -> GH_Variant
        Evaluate(self: GH_ExpressionParser, qHint: Queue[GH_ParserSymbol]) -> GH_Variant
        Evaluate(self: GH_ExpressionParser) -> GH_Variant
        """
        pass

    @staticmethod
    def IsValidVariableName(name):
        """ IsValidVariableName(name: str) -> bool """
        pass

    def Op_BinaryAddition(self, *args): #cannot find CLR method
        """ Op_BinaryAddition(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryAmpersand(self, *args): #cannot find CLR method
        """ Op_BinaryAmpersand(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryAND(self, *args): #cannot find CLR method
        """ Op_BinaryAND(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryAngle(self, *args): #cannot find CLR method
        """ Op_BinaryAngle(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryCircumflex(self, *args): #cannot find CLR method
        """ Op_BinaryCircumflex(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryCrossProduct(self, *args): #cannot find CLR method
        """ Op_BinaryCrossProduct(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryDistance(self, *args): #cannot find CLR method
        """ Op_BinaryDistance(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryDivision(self, *args): #cannot find CLR method
        """ Op_BinaryDivision(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryEquality(self, *args): #cannot find CLR method
        """ Op_BinaryEquality(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryIntegerDivision(self, *args): #cannot find CLR method
        """ Op_BinaryIntegerDivision(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryLargerThan(self, *args): #cannot find CLR method
        """ Op_BinaryLargerThan(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryLargerThanOrEqual(self, *args): #cannot find CLR method
        """ Op_BinaryLargerThanOrEqual(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryModulus(self, *args): #cannot find CLR method
        """ Op_BinaryModulus(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryMultiplication(self, *args): #cannot find CLR method
        """ Op_BinaryMultiplication(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryNearEquality(self, *args): #cannot find CLR method
        """ Op_BinaryNearEquality(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryOR(self, *args): #cannot find CLR method
        """ Op_BinaryOR(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryPull(self, *args): #cannot find CLR method
        """ Op_BinaryPull(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryPush(self, *args): #cannot find CLR method
        """ Op_BinaryPush(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinarySmallerThan(self, *args): #cannot find CLR method
        """ Op_BinarySmallerThan(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinarySmallerThanOrEqual(self, *args): #cannot find CLR method
        """ Op_BinarySmallerThanOrEqual(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinarySubtraction(self, *args): #cannot find CLR method
        """ Op_BinarySubtraction(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_BinaryXOR(self, *args): #cannot find CLR method
        """ Op_BinaryXOR(self: GH_ExpressionParser, A: GH_Variant, B: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryBang(self, *args): #cannot find CLR method
        """ Op_UnaryBang(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryCube(self, *args): #cannot find CLR method
        """ Op_UnaryCube(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryDeg2Rad(self, *args): #cannot find CLR method
        """ Op_UnaryDeg2Rad(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryImaginary(self, *args): #cannot find CLR method
        """ Op_UnaryImaginary(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryMinus(self, *args): #cannot find CLR method
        """ Op_UnaryMinus(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryNOT(self, *args): #cannot find CLR method
        """ Op_UnaryNOT(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryOComponent(self, *args): #cannot find CLR method
        """ Op_UnaryOComponent(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryPlus(self, *args): #cannot find CLR method
        """ Op_UnaryPlus(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnarySquare(self, *args): #cannot find CLR method
        """ Op_UnarySquare(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryXComponent(self, *args): #cannot find CLR method
        """ Op_UnaryXComponent(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryYComponent(self, *args): #cannot find CLR method
        """ Op_UnaryYComponent(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    def Op_UnaryZComponent(self, *args): #cannot find CLR method
        """ Op_UnaryZComponent(self: GH_ExpressionParser, V: GH_Variant) -> GH_Variant """
        pass

    @staticmethod # known case of __new__
    def __new__(self, bThrowExceptions=None):
        """
        __new__(cls: type)
        __new__(cls: type, bThrowExceptions: bool)
        """
        pass

    ThrowExceptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThrowExceptions(self: GH_ExpressionParser) -> bool

Set: ThrowExceptions(self: GH_ExpressionParser) = value
"""

    Variables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Variables(self: GH_ExpressionParser) -> SortedDictionary[str, GH_Variant]

"""



class GH_ExpressionString(List[Char], IList[Char], ICollection[Char], IEnumerable[Char], IEnumerable, IList, ICollection, IReadOnlyList[Char], IReadOnlyCollection[Char]):
    """ GH_ExpressionString(in: str) """
    def BuildLUT(self):
        """ BuildLUT(self: GH_ExpressionString) """
        pass

    def IsWhiteSpace(self, index):
        """ IsWhiteSpace(self: GH_ExpressionString, index: int) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_ExpressionString) -> str """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, in):
        """ __new__(cls: type, in: str) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    bracket_closed = None
    bracket_open = None
    colon = None
    comma = None
    dot = None
    dquote = None
    invalid = None
    linefeed = None
    m_t = None
    paren_close = None
    paren_open = None
    quote = None
    scolon = None
    space = None
    tab = None
    underbar = None


class GH_ExpressionSyntaxWriter(object):
    # no doc
    @staticmethod
    def RewriteAll(Expression):
        """ RewriteAll(Expression: str) -> str """
        pass

    @staticmethod
    def RewriteForEvaluator(*__args):
        """ RewriteForEvaluator(sCode: GH_CodeString)RewriteForEvaluator(Expression: str) -> str """
        pass

    @staticmethod
    def RewriteForGraphicInterface(*__args):
        """ RewriteForGraphicInterface(code: GH_CodeString)RewriteForGraphicInterface(expression: str) -> str """
        pass


class GH_OperatorType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_OperatorType, values: Binary (2), UnaryOnLeft (0), UnaryOnRight (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Binary = None
    UnaryOnLeft = None
    UnaryOnRight = None
    value__ = None


class GH_ParserOperator(object, IComparable[GH_ParserOperator]):
    """ GH_ParserOperator(name: str, symbol: Char, precedence: GH_ParserPrecedence, type: GH_OperatorType, description: str) """
    def CompareTo(self, other):
        """ CompareTo(self: GH_ParserOperator, other: GH_ParserOperator) -> int """
        pass

    def Equals(self, obj):
        """ Equals(self: GH_ParserOperator, obj: object) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, symbol, precedence, type, description):
        """ __new__(cls: type, name: str, symbol: Char, precedence: GH_ParserPrecedence, type: GH_OperatorType, description: str) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    m_description = None
    m_name = None
    m_precedence = None
    m_symbol = None
    m_type = None


class GH_ParserPrecedence(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_ParserPrecedence, values: Invalid (-1), Level0 (1), Level1 (2), Level2 (3), Level3 (4), Level4 (5), Level5 (6), None (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Invalid = None
    Level0 = None
    Level1 = None
    Level2 = None
    Level3 = None
    Level4 = None
    Level5 = None
    None = None
    value__ = None


class GH_ParserSymbol(object, IComparable[GH_ParserSymbol]):
    """
    GH_ParserSymbol()
    GH_ParserSymbol(token: str, class: GH_ParserTokenClass, level: GH_ParserPrecedence)
    """
    def CompareTo(self, other):
        """ CompareTo(self: GH_ParserSymbol, other: GH_ParserSymbol) -> int """
        pass

    def Equals(self, obj):
        """ Equals(self: GH_ParserSymbol, obj: object) -> bool """
        pass

    def ToString(self):
        """ ToString(self: GH_ParserSymbol) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, token=None, class=None, level=None):
        """
        __new__(cls: type)
        __new__(cls: type, token: str, class: GH_ParserTokenClass, level: GH_ParserPrecedence)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    m_class = None
    m_level = None
    m_token = None


class GH_ParserTokenClass(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_ParserTokenClass, values: Identifier (2), Keyword (1), Literal (4), Numeric (3), Operator (5), Punctuation (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Identifier = None
    Keyword = None
    Literal = None
    Numeric = None
    Operator = None
    Punctuation = None
    value__ = None


class GH_ScriptVariant(object):
    """
    GH_ScriptVariant()
    GH_ScriptVariant(val: float)
    GH_ScriptVariant(val: int)
    GH_ScriptVariant(val: Byte)
    GH_ScriptVariant(val: bool)
    GH_ScriptVariant(val: str)
    GH_ScriptVariant(val: DateTime)
    GH_ScriptVariant(val: Point3d)
    GH_ScriptVariant(val: Vector3d)
    GH_ScriptVariant(val: Plane)
    """
    def ThrowNullOperatorException(self, *args): #cannot find CLR method
        """ ThrowNullOperatorException(sName: str) """
        pass

    def ThrowOperatorException(self, *args): #cannot find CLR method
        """ ThrowOperatorException(op_name: str, A: GH_ScriptVariantType, B: GH_ScriptVariantType)ThrowOperatorException(op_name: str, A: str, B: str)ThrowOperatorException(op_name: str, A: GH_ScriptVariantType)ThrowOperatorException(op_name: str, A: str) """
        pass

    def ToString(self):
        """ ToString(self: GH_ScriptVariant) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """ __and__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool """
        pass

    def __complex__(self, *args): #cannot find CLR method
        """ __complex__(in: GH_ScriptVariant) -> float """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __complex__(in: GH_ScriptVariant) -> float """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(in: GH_ScriptVariant) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(A: GH_ScriptVariant) -> GH_ScriptVariant """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __int__(in: GH_ScriptVariant) -> int """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<y """
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, val=None):
        """
        __new__(cls: type)
        __new__(cls: type, val: float)
        __new__(cls: type, val: int)
        __new__(cls: type, val: Byte)
        __new__(cls: type, val: bool)
        __new__(cls: type, val: str)
        __new__(cls: type, val: DateTime)
        __new__(cls: type, val: Point3d)
        __new__(cls: type, val: Vector3d)
        __new__(cls: type, val: Plane)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __or__(self, *args): #cannot find CLR method
        """ __or__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(A: GH_ScriptVariant) -> GH_ScriptVariant """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool """
        pass

    Boolean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boolean(self: GH_ScriptVariant) -> bool

"""

    DateTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateTime(self: GH_ScriptVariant) -> DateTime

"""

    Double = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Double(self: GH_ScriptVariant) -> float

"""

    Integer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Integer(self: GH_ScriptVariant) -> int

"""

    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: GH_ScriptVariant) -> object

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: GH_ScriptVariant) -> Plane

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: GH_ScriptVariant) -> Point3d

"""

    String = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: String(self: GH_ScriptVariant) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: GH_ScriptVariant) -> GH_ScriptVariantType

"""

    Vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vector(self: GH_ScriptVariant) -> Vector3d

"""


    m_type = None
    m_value = None


class GH_ScriptVariantType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_ScriptVariantType, values: boolean (1), datetime (6), double (3), integer (2), nothing (0), object (20), plane (12), point (10), string (5), vector (11) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    boolean = None
    datetime = None
    double = None
    integer = None
    nothing = None
    object = None
    plane = None
    point = None
    string = None
    value__ = None
    vector = None


class GH_SignatureException(Exception, ISerializable, _Exception):
    """ GH_SignatureException(args: List[GH_Variant], name: str) """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, args, name):
        """ __new__(cls: type, args: List[GH_Variant], name: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: GH_SignatureException) -> str

"""



class GH_SolverException(Exception, ISerializable, _Exception):
    """ GH_SolverException(nMessage: str) """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nMessage):
        """ __new__(cls: type, nMessage: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class GH_SyntaxException(Exception, ISerializable, _Exception):
    """ GH_SyntaxException(nMessage: str) """
    def add_SerializeObjectState(self, *args): #cannot find CLR method
        """ add_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def remove_SerializeObjectState(self, *args): #cannot find CLR method
        """ remove_SerializeObjectState(self: Exception, value: EventHandler[SafeSerializationEventArgs]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nMessage):
        """ __new__(cls: type, nMessage: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class GH_Variant(object):
    """
    GH_Variant()
    GH_Variant(value: bool)
    GH_Variant(value: int)
    GH_Variant(value: float)
    GH_Variant(value: str)
    GH_Variant(value: Complex)
    GH_Variant(value: Point3d)
    GH_Variant(value: Vector3d)
    GH_Variant(value: Plane)
    GH_Variant(other: GH_Variant)
    """
    def Data(self):
        """ Data[T](self: GH_Variant) -> T """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_Variant) -> GH_Variant """
        pass

    def Evaluate(self):
        """ Evaluate(self: GH_Variant) -> bool """
        pass

    def ToGoo(self):
        """ ToGoo(self: GH_Variant) -> IGH_Goo """
        pass

    def ToString(self):
        """ ToString(self: GH_Variant) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, value: bool)
        __new__(cls: type, value: int)
        __new__(cls: type, value: float)
        __new__(cls: type, value: str)
        __new__(cls: type, value: Complex)
        __new__(cls: type, value: Point3d)
        __new__(cls: type, value: Vector3d)
        __new__(cls: type, value: Plane)
        __new__(cls: type, other: GH_Variant)
        """
        pass

    IsNumeric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNumeric(self: GH_Variant) -> bool

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: GH_Variant) -> GH_VariantType

"""

    _Bool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _Bool(self: GH_Variant) -> bool

"""

    _Complex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _Complex(self: GH_Variant) -> Complex

"""

    _Double = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _Double(self: GH_Variant) -> float

"""

    _Int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _Int(self: GH_Variant) -> int

"""

    _Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _Plane(self: GH_Variant) -> Plane

"""

    _Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _Point(self: GH_Variant) -> Point3d

"""

    _String = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _String(self: GH_Variant) -> str

"""

    _Vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: _Vector(self: GH_Variant) -> Vector3d

"""



class GH_VariantType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_VariantType, values: bool (1), complex (64), double (4), int (2), null (0), plane (32), point (16), string (8), unknown (-1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    bool = None
    complex = None
    double = None
    int = None
    null = None
    plane = None
    point = None
    string = None
    unknown = None
    value__ = None


