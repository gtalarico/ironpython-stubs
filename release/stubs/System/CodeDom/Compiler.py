# encoding: utf-8
# module System.CodeDom.Compiler calls itself Compiler
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class ICodeGenerator:
    """ Defines an interface for generating code. """
    def CreateEscapedIdentifier(self, value):
        """
        CreateEscapedIdentifier(self: ICodeGenerator, value: str) -> str
        
            Creates an escaped identifier for the specified value.
        
            value: The string to create an escaped identifier for.
            Returns: The escaped identifier for the value.
        """
        pass

    def CreateValidIdentifier(self, value):
        """
        CreateValidIdentifier(self: ICodeGenerator, value: str) -> str
        
            Creates a valid identifier for the specified value.
        
            value: The string to generate a valid identifier for.
            Returns: A valid identifier for the specified value.
        """
        pass

    def GenerateCodeFromCompileUnit(self, e, w, o):
        """
        GenerateCodeFromCompileUnit(self: ICodeGenerator, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) compilation unit and 
             outputs it to the specified text writer using the specified options.
        
        
            e: A System.CodeDom.CodeCompileUnit to generate code for.
            w: The System.IO.TextWriter to output code to.
            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromExpression(self, e, w, o):
        """
        GenerateCodeFromExpression(self: ICodeGenerator, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) expression and outputs it 
             to the specified text writer.
        
        
            e: A System.CodeDom.CodeExpression that indicates the expression to generate code for.
            w: The System.IO.TextWriter to output code to.
            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromNamespace(self, e, w, o):
        """
        GenerateCodeFromNamespace(self: ICodeGenerator, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) namespace and outputs it 
             to the specified text writer using the specified options.
        
        
            e: A System.CodeDom.CodeNamespace that indicates the namespace to generate code for.
            w: The System.IO.TextWriter to output code to.
            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromStatement(self, e, w, o):
        """
        GenerateCodeFromStatement(self: ICodeGenerator, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) statement and outputs it 
             to the specified text writer using the specified options.
        
        
            e: A System.CodeDom.CodeStatement containing the CodeDOM elements to translate.
            w: The System.IO.TextWriter to output code to.
            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromType(self, e, w, o):
        """
        GenerateCodeFromType(self: ICodeGenerator, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) type declaration and 
             outputs it to the specified text writer using the specified options.
        
        
            e: A System.CodeDom.CodeTypeDeclaration that indicates the type to generate code for.
            w: The System.IO.TextWriter to output code to.
            o: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GetTypeOutput(self, type):
        """
        GetTypeOutput(self: ICodeGenerator, type: CodeTypeReference) -> str
        
            Gets the type indicated by the specified System.CodeDom.CodeTypeReference.
        
            type: A System.CodeDom.CodeTypeReference that indicates the type to return.
            Returns: A text representation of the specified type for the language this code generator is designed to 
             generate code in. For example, in Visual Basic, passing in type System.Int32 will return 
             "Integer".
        """
        pass

    def IsValidIdentifier(self, value):
        """
        IsValidIdentifier(self: ICodeGenerator, value: str) -> bool
        
            Gets a value that indicates whether the specified value is a valid identifier for the current 
             language.
        
        
            value: The value to test for being a valid identifier.
            Returns: true if the value parameter is a valid identifier; otherwise, false.
        """
        pass

    def Supports(self, supports):
        """
        Supports(self: ICodeGenerator, supports: GeneratorSupport) -> bool
        
            Gets a value indicating whether the generator provides support for the language features 
             represented by the specified System.CodeDom.Compiler.GeneratorSupport object.
        
        
            supports: The capabilities to test the generator for.
            Returns: true if the specified capabilities are supported; otherwise, false.
        """
        pass

    def ValidateIdentifier(self, value):
        """
        ValidateIdentifier(self: ICodeGenerator, value: str)
            Throws an exception if the specified value is not a valid identifier.
        
            value: The identifier to validate.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class CodeGenerator(object, ICodeGenerator):
    """ Provides an example implementation of the System.CodeDom.Compiler.ICodeGenerator interface. This class is abstract. """
    def ContinueOnNewLine(self, *args): #cannot find CLR method
        """
        ContinueOnNewLine(self: CodeGenerator, st: str)
            Generates a line-continuation character and outputs the specified string on a new line.
        
            st: The string to write on the new line.
        """
        pass

    def CreateEscapedIdentifier(self, *args): #cannot find CLR method
        """
        CreateEscapedIdentifier(self: CodeGenerator, value: str) -> str
        
            Creates an escaped identifier for the specified value.
        
            value: The string to create an escaped identifier for.
            Returns: The escaped identifier for the value.
        """
        pass

    def CreateValidIdentifier(self, *args): #cannot find CLR method
        """
        CreateValidIdentifier(self: CodeGenerator, value: str) -> str
        
            Creates a valid identifier for the specified value.
        
            value: A string to create a valid identifier for.
            Returns: A valid identifier for the value.
        """
        pass

    def GenerateArgumentReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateArgumentReferenceExpression(self: CodeGenerator, e: CodeArgumentReferenceExpression)
            Generates code for the specified argument reference expression.
        
            e: A System.CodeDom.CodeArgumentReferenceExpression that indicates the expression to generate code 
             for.
        """
        pass

    def GenerateArrayCreateExpression(self, *args): #cannot find CLR method
        """
        GenerateArrayCreateExpression(self: CodeGenerator, e: CodeArrayCreateExpression)
            Generates code for the specified array creation expression.
        
            e: A System.CodeDom.CodeArrayCreateExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateArrayIndexerExpression(self, *args): #cannot find CLR method
        """
        GenerateArrayIndexerExpression(self: CodeGenerator, e: CodeArrayIndexerExpression)
            Generates code for the specified array indexer expression.
        
            e: A System.CodeDom.CodeArrayIndexerExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateAssignStatement(self, *args): #cannot find CLR method
        """
        GenerateAssignStatement(self: CodeGenerator, e: CodeAssignStatement)
            Generates code for the specified assignment statement.
        
            e: A System.CodeDom.CodeAssignStatement that indicates the statement to generate code for.
        """
        pass

    def GenerateAttachEventStatement(self, *args): #cannot find CLR method
        """
        GenerateAttachEventStatement(self: CodeGenerator, e: CodeAttachEventStatement)
            Generates code for the specified attach event statement.
        
            e: A System.CodeDom.CodeAttachEventStatement that indicates the statement to generate code for.
        """
        pass

    def GenerateAttributeDeclarationsEnd(self, *args): #cannot find CLR method
        """
        GenerateAttributeDeclarationsEnd(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)
            Generates code for the specified attribute block end.
        
            attributes: A System.CodeDom.CodeAttributeDeclarationCollection that indicates the end of the attribute 
             block to generate code for.
        """
        pass

    def GenerateAttributeDeclarationsStart(self, *args): #cannot find CLR method
        """
        GenerateAttributeDeclarationsStart(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)
            Generates code for the specified attribute block start.
        
            attributes: A System.CodeDom.CodeAttributeDeclarationCollection that indicates the start of the attribute 
             block to generate code for.
        """
        pass

    def GenerateBaseReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateBaseReferenceExpression(self: CodeGenerator, e: CodeBaseReferenceExpression)
            Generates code for the specified base reference expression.
        
            e: A System.CodeDom.CodeBaseReferenceExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateBinaryOperatorExpression(self, *args): #cannot find CLR method
        """
        GenerateBinaryOperatorExpression(self: CodeGenerator, e: CodeBinaryOperatorExpression)
            Generates code for the specified binary operator expression.
        
            e: A System.CodeDom.CodeBinaryOperatorExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateCastExpression(self, *args): #cannot find CLR method
        """
        GenerateCastExpression(self: CodeGenerator, e: CodeCastExpression)
            Generates code for the specified cast expression.
        
            e: A System.CodeDom.CodeCastExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateCodeFromMember(self, member, writer, options):
        """
        GenerateCodeFromMember(self: CodeGenerator, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions)
            Generates code for the specified class member using the specified text writer and code generator 
             options.
        
        
            member: The class member to generate code for.
            writer: The text writer to output code to.
            options: The options to use when generating the code.
        """
        pass

    def GenerateComment(self, *args): #cannot find CLR method
        """
        GenerateComment(self: CodeGenerator, e: CodeComment)
            Generates code for the specified comment.
        
            e: A System.CodeDom.CodeComment to generate code for.
        """
        pass

    def GenerateCommentStatement(self, *args): #cannot find CLR method
        """
        GenerateCommentStatement(self: CodeGenerator, e: CodeCommentStatement)
            Generates code for the specified comment statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateCommentStatements(self, *args): #cannot find CLR method
        """
        GenerateCommentStatements(self: CodeGenerator, e: CodeCommentStatementCollection)
            Generates code for the specified comment statements.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateCompileUnit(self, *args): #cannot find CLR method
        """
        GenerateCompileUnit(self: CodeGenerator, e: CodeCompileUnit)
            Generates code for the specified compile unit.
        
            e: The compile unit to generate code for.
        """
        pass

    def GenerateCompileUnitEnd(self, *args): #cannot find CLR method
        """
        GenerateCompileUnitEnd(self: CodeGenerator, e: CodeCompileUnit)
            Generates code for the end of a compile unit.
        
            e: The compile unit to generate code for.
        """
        pass

    def GenerateCompileUnitStart(self, *args): #cannot find CLR method
        """
        GenerateCompileUnitStart(self: CodeGenerator, e: CodeCompileUnit)
            Generates code for the start of a compile unit.
        
            e: The compile unit to generate code for.
        """
        pass

    def GenerateConditionStatement(self, *args): #cannot find CLR method
        """
        GenerateConditionStatement(self: CodeGenerator, e: CodeConditionStatement)
            Generates code for the specified conditional statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateConstructor(self, *args): #cannot find CLR method
        """
        GenerateConstructor(self: CodeGenerator, e: CodeConstructor, c: CodeTypeDeclaration)
            Generates code for the specified constructor.
        
            e: The constructor to generate code for.
            c: The type of the object that this constructor constructs.
        """
        pass

    def GenerateDecimalValue(self, *args): #cannot find CLR method
        """
        GenerateDecimalValue(self: CodeGenerator, d: Decimal)
            Generates code for the specified decimal value.
        
            d: The decimal value to generate code for.
        """
        pass

    def GenerateDefaultValueExpression(self, *args): #cannot find CLR method
        """
        GenerateDefaultValueExpression(self: CodeGenerator, e: CodeDefaultValueExpression)
            Generates code for the specified reference to a default value.
        
            e: The reference to generate code for.
        """
        pass

    def GenerateDelegateCreateExpression(self, *args): #cannot find CLR method
        """
        GenerateDelegateCreateExpression(self: CodeGenerator, e: CodeDelegateCreateExpression)
            Generates code for the specified delegate creation expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateDelegateInvokeExpression(self, *args): #cannot find CLR method
        """
        GenerateDelegateInvokeExpression(self: CodeGenerator, e: CodeDelegateInvokeExpression)
            Generates code for the specified delegate invoke expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateDirectionExpression(self, *args): #cannot find CLR method
        """
        GenerateDirectionExpression(self: CodeGenerator, e: CodeDirectionExpression)
            Generates code for the specified direction expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateDirectives(self, *args): #cannot find CLR method
        """
        GenerateDirectives(self: CodeGenerator, directives: CodeDirectiveCollection)
            Generates code for the specified code directives.
        
            directives: The code directives to generate code for.
        """
        pass

    def GenerateDoubleValue(self, *args): #cannot find CLR method
        """
        GenerateDoubleValue(self: CodeGenerator, d: float)
            Generates code for a double-precision floating point number.
        
            d: The value to generate code for.
        """
        pass

    def GenerateEntryPointMethod(self, *args): #cannot find CLR method
        """
        GenerateEntryPointMethod(self: CodeGenerator, e: CodeEntryPointMethod, c: CodeTypeDeclaration)
            Generates code for the specified entry point method.
        
            e: The entry point for the code.
            c: The code that declares the type.
        """
        pass

    def GenerateEvent(self, *args): #cannot find CLR method
        """
        GenerateEvent(self: CodeGenerator, e: CodeMemberEvent, c: CodeTypeDeclaration)
            Generates code for the specified event.
        
            e: The member event to generate code for.
            c: The type of the object that this event occurs on.
        """
        pass

    def GenerateEventReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateEventReferenceExpression(self: CodeGenerator, e: CodeEventReferenceExpression)
            Generates code for the specified event reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateExpression(self, *args): #cannot find CLR method
        """
        GenerateExpression(self: CodeGenerator, e: CodeExpression)
            Generates code for the specified code expression.
        
            e: The code expression to generate code for.
        """
        pass

    def GenerateExpressionStatement(self, *args): #cannot find CLR method
        """
        GenerateExpressionStatement(self: CodeGenerator, e: CodeExpressionStatement)
            Generates code for the specified expression statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateField(self, *args): #cannot find CLR method
        """
        GenerateField(self: CodeGenerator, e: CodeMemberField)
            Generates code for the specified member field.
        
            e: The field to generate code for.
        """
        pass

    def GenerateFieldReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateFieldReferenceExpression(self: CodeGenerator, e: CodeFieldReferenceExpression)
            Generates code for the specified field reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateGotoStatement(self, *args): #cannot find CLR method
        """
        GenerateGotoStatement(self: CodeGenerator, e: CodeGotoStatement)
            Generates code for the specified goto statement.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateIndexerExpression(self, *args): #cannot find CLR method
        """
        GenerateIndexerExpression(self: CodeGenerator, e: CodeIndexerExpression)
            Generates code for the specified indexer expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateIterationStatement(self, *args): #cannot find CLR method
        """
        GenerateIterationStatement(self: CodeGenerator, e: CodeIterationStatement)
            Generates code for the specified iteration statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateLabeledStatement(self, *args): #cannot find CLR method
        """
        GenerateLabeledStatement(self: CodeGenerator, e: CodeLabeledStatement)
            Generates code for the specified labeled statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateLinePragmaEnd(self, *args): #cannot find CLR method
        """
        GenerateLinePragmaEnd(self: CodeGenerator, e: CodeLinePragma)
            Generates code for the specified line pragma end.
        
            e: The end of the line pragma to generate code for.
        """
        pass

    def GenerateLinePragmaStart(self, *args): #cannot find CLR method
        """
        GenerateLinePragmaStart(self: CodeGenerator, e: CodeLinePragma)
            Generates code for the specified line pragma start.
        
            e: The start of the line pragma to generate code for.
        """
        pass

    def GenerateMethod(self, *args): #cannot find CLR method
        """
        GenerateMethod(self: CodeGenerator, e: CodeMemberMethod, c: CodeTypeDeclaration)
            Generates code for the specified method.
        
            e: The member method to generate code for.
            c: The type of the object that this method occurs on.
        """
        pass

    def GenerateMethodInvokeExpression(self, *args): #cannot find CLR method
        """
        GenerateMethodInvokeExpression(self: CodeGenerator, e: CodeMethodInvokeExpression)
            Generates code for the specified method invoke expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateMethodReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateMethodReferenceExpression(self: CodeGenerator, e: CodeMethodReferenceExpression)
            Generates code for the specified method reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateMethodReturnStatement(self, *args): #cannot find CLR method
        """
        GenerateMethodReturnStatement(self: CodeGenerator, e: CodeMethodReturnStatement)
            Generates code for the specified method return statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateNamespace(self, *args): #cannot find CLR method
        """
        GenerateNamespace(self: CodeGenerator, e: CodeNamespace)
            Generates code for the specified namespace.
        
            e: The namespace to generate code for.
        """
        pass

    def GenerateNamespaceEnd(self, *args): #cannot find CLR method
        """
        GenerateNamespaceEnd(self: CodeGenerator, e: CodeNamespace)
            Generates code for the end of a namespace.
        
            e: The namespace to generate code for.
        """
        pass

    def GenerateNamespaceImport(self, *args): #cannot find CLR method
        """
        GenerateNamespaceImport(self: CodeGenerator, e: CodeNamespaceImport)
            Generates code for the specified namespace import.
        
            e: The namespace import to generate code for.
        """
        pass

    def GenerateNamespaceImports(self, *args): #cannot find CLR method
        """
        GenerateNamespaceImports(self: CodeGenerator, e: CodeNamespace)
            Generates code for the specified namespace import.
        
            e: The namespace import to generate code for.
        """
        pass

    def GenerateNamespaces(self, *args): #cannot find CLR method
        """
        GenerateNamespaces(self: CodeGenerator, e: CodeCompileUnit)
            Generates code for the namespaces in the specified compile unit.
        
            e: The compile unit to generate namespaces for.
        """
        pass

    def GenerateNamespaceStart(self, *args): #cannot find CLR method
        """
        GenerateNamespaceStart(self: CodeGenerator, e: CodeNamespace)
            Generates code for the start of a namespace.
        
            e: The namespace to generate code for.
        """
        pass

    def GenerateObjectCreateExpression(self, *args): #cannot find CLR method
        """
        GenerateObjectCreateExpression(self: CodeGenerator, e: CodeObjectCreateExpression)
            Generates code for the specified object creation expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateParameterDeclarationExpression(self, *args): #cannot find CLR method
        """
        GenerateParameterDeclarationExpression(self: CodeGenerator, e: CodeParameterDeclarationExpression)
            Generates code for the specified parameter declaration expression.
        
            e: The expression to generate code for.
        """
        pass

    def GeneratePrimitiveExpression(self, *args): #cannot find CLR method
        """
        GeneratePrimitiveExpression(self: CodeGenerator, e: CodePrimitiveExpression)
            Generates code for the specified primitive expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateProperty(self, *args): #cannot find CLR method
        """
        GenerateProperty(self: CodeGenerator, e: CodeMemberProperty, c: CodeTypeDeclaration)
            Generates code for the specified property.
        
            e: The property to generate code for.
            c: The type of the object that this property occurs on.
        """
        pass

    def GeneratePropertyReferenceExpression(self, *args): #cannot find CLR method
        """
        GeneratePropertyReferenceExpression(self: CodeGenerator, e: CodePropertyReferenceExpression)
            Generates code for the specified property reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GeneratePropertySetValueReferenceExpression(self, *args): #cannot find CLR method
        """
        GeneratePropertySetValueReferenceExpression(self: CodeGenerator, e: CodePropertySetValueReferenceExpression)
            Generates code for the specified property set value reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateRemoveEventStatement(self, *args): #cannot find CLR method
        """
        GenerateRemoveEventStatement(self: CodeGenerator, e: CodeRemoveEventStatement)
            Generates code for the specified remove event statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateSingleFloatValue(self, *args): #cannot find CLR method
        """
        GenerateSingleFloatValue(self: CodeGenerator, s: Single)
            Generates code for a single-precision floating point number.
        
            s: The value to generate code for.
        """
        pass

    def GenerateSnippetCompileUnit(self, *args): #cannot find CLR method
        """
        GenerateSnippetCompileUnit(self: CodeGenerator, e: CodeSnippetCompileUnit)
            Outputs the code of the specified literal code fragment compile unit.
        
            e: The literal code fragment compile unit to generate code for.
        """
        pass

    def GenerateSnippetExpression(self, *args): #cannot find CLR method
        """
        GenerateSnippetExpression(self: CodeGenerator, e: CodeSnippetExpression)
            Outputs the code of the specified literal code fragment expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateSnippetMember(self, *args): #cannot find CLR method
        """
        GenerateSnippetMember(self: CodeGenerator, e: CodeSnippetTypeMember)
            Outputs the code of the specified literal code fragment class member.
        
            e: The member to generate code for.
        """
        pass

    def GenerateSnippetStatement(self, *args): #cannot find CLR method
        """
        GenerateSnippetStatement(self: CodeGenerator, e: CodeSnippetStatement)
            Outputs the code of the specified literal code fragment statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateStatement(self, *args): #cannot find CLR method
        """
        GenerateStatement(self: CodeGenerator, e: CodeStatement)
            Generates code for the specified statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateStatements(self, *args): #cannot find CLR method
        """
        GenerateStatements(self: CodeGenerator, stms: CodeStatementCollection)
            Generates code for the specified statement collection.
        
            stms: The statements to generate code for.
        """
        pass

    def GenerateThisReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateThisReferenceExpression(self: CodeGenerator, e: CodeThisReferenceExpression)
            Generates code for the specified this reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateThrowExceptionStatement(self, *args): #cannot find CLR method
        """
        GenerateThrowExceptionStatement(self: CodeGenerator, e: CodeThrowExceptionStatement)
            Generates code for the specified throw exception statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateTryCatchFinallyStatement(self, *args): #cannot find CLR method
        """
        GenerateTryCatchFinallyStatement(self: CodeGenerator, e: CodeTryCatchFinallyStatement)
            Generates code for the specified try...catch...finally statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateTypeConstructor(self, *args): #cannot find CLR method
        """
        GenerateTypeConstructor(self: CodeGenerator, e: CodeTypeConstructor)
            Generates code for the specified class constructor.
        
            e: The class constructor to generate code for.
        """
        pass

    def GenerateTypeEnd(self, *args): #cannot find CLR method
        """
        GenerateTypeEnd(self: CodeGenerator, e: CodeTypeDeclaration)
            Generates code for the specified end of the class.
        
            e: The end of the class to generate code for.
        """
        pass

    def GenerateTypeOfExpression(self, *args): #cannot find CLR method
        """
        GenerateTypeOfExpression(self: CodeGenerator, e: CodeTypeOfExpression)
            Generates code for the specified type of expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateTypeReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateTypeReferenceExpression(self: CodeGenerator, e: CodeTypeReferenceExpression)
            Generates code for the specified type reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateTypes(self, *args): #cannot find CLR method
        """
        GenerateTypes(self: CodeGenerator, e: CodeNamespace)
            Generates code for the specified namespace and the classes it contains.
        
            e: The namespace to generate classes for.
        """
        pass

    def GenerateTypeStart(self, *args): #cannot find CLR method
        """
        GenerateTypeStart(self: CodeGenerator, e: CodeTypeDeclaration)
            Generates code for the specified start of the class.
        
            e: The start of the class to generate code for.
        """
        pass

    def GenerateVariableDeclarationStatement(self, *args): #cannot find CLR method
        """
        GenerateVariableDeclarationStatement(self: CodeGenerator, e: CodeVariableDeclarationStatement)
            Generates code for the specified variable declaration statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateVariableReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateVariableReferenceExpression(self: CodeGenerator, e: CodeVariableReferenceExpression)
            Generates code for the specified variable reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GetTypeOutput(self, *args): #cannot find CLR method
        """
        GetTypeOutput(self: CodeGenerator, value: CodeTypeReference) -> str
        
            Gets the name of the specified data type.
        
            value: The type whose name will be returned.
            Returns: The name of the data type reference.
        """
        pass

    def IsValidIdentifier(self, *args): #cannot find CLR method
        """
        IsValidIdentifier(self: CodeGenerator, value: str) -> bool
        
            Gets a value indicating whether the specified value is a valid identifier.
        
            value: The value to test for conflicts with valid identifiers.
            Returns: true if the value is a valid identifier; otherwise, false.
        """
        pass

    @staticmethod
    def IsValidLanguageIndependentIdentifier(value):
        """
        IsValidLanguageIndependentIdentifier(value: str) -> bool
        
            Gets a value indicating whether the specified string is a valid identifier.
        
            value: The string to test for validity.
            Returns: true if the specified string is a valid identifier; otherwise, false.
        """
        pass

    def OutputAttributeArgument(self, *args): #cannot find CLR method
        """
        OutputAttributeArgument(self: CodeGenerator, arg: CodeAttributeArgument)
            Outputs an argument in an attribute block.
        
            arg: The attribute argument to generate code for.
        """
        pass

    def OutputAttributeDeclarations(self, *args): #cannot find CLR method
        """
        OutputAttributeDeclarations(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)
            Generates code for the specified attribute declaration collection.
        
            attributes: The attributes to generate code for.
        """
        pass

    def OutputDirection(self, *args): #cannot find CLR method
        """
        OutputDirection(self: CodeGenerator, dir: FieldDirection)
            Generates code for the specified System.CodeDom.FieldDirection.
        
            dir: One of the enumeration values that indicates the attribute of the field.
        """
        pass

    def OutputExpressionList(self, *args): #cannot find CLR method
        """
        OutputExpressionList(self: CodeGenerator, expressions: CodeExpressionCollection, newlineBetweenItems: bool)
            Generates code for the specified expression list.
        
            expressions: The expressions to generate code for.
            newlineBetweenItems: true to insert a new line after each item; otherwise, false.
        OutputExpressionList(self: CodeGenerator, expressions: CodeExpressionCollection)
            Generates code for the specified expression list.
        
            expressions: The expressions to generate code for.
        """
        pass

    def OutputFieldScopeModifier(self, *args): #cannot find CLR method
        """
        OutputFieldScopeModifier(self: CodeGenerator, attributes: MemberAttributes)
            Outputs a field scope modifier that corresponds to the specified attributes.
        
            attributes: One of the enumeration values that specifies the attributes.
        """
        pass

    def OutputIdentifier(self, *args): #cannot find CLR method
        """
        OutputIdentifier(self: CodeGenerator, ident: str)
            Outputs the specified identifier.
        
            ident: The identifier to output.
        """
        pass

    def OutputMemberAccessModifier(self, *args): #cannot find CLR method
        """
        OutputMemberAccessModifier(self: CodeGenerator, attributes: MemberAttributes)
            Generates code for the specified member access modifier.
        
            attributes: One of the enumeration values that indicates the member access modifier to generate code for.
        """
        pass

    def OutputMemberScopeModifier(self, *args): #cannot find CLR method
        """
        OutputMemberScopeModifier(self: CodeGenerator, attributes: MemberAttributes)
            Generates code for the specified member scope modifier.
        
            attributes: One of the enumeration values that indicates the member scope modifier to generate code for.
        """
        pass

    def OutputOperator(self, *args): #cannot find CLR method
        """
        OutputOperator(self: CodeGenerator, op: CodeBinaryOperatorType)
            Generates code for the specified operator.
        
            op: The operator to generate code for.
        """
        pass

    def OutputParameters(self, *args): #cannot find CLR method
        """
        OutputParameters(self: CodeGenerator, parameters: CodeParameterDeclarationExpressionCollection)
            Generates code for the specified parameters.
        
            parameters: The parameter declaration expressions to generate code for.
        """
        pass

    def OutputType(self, *args): #cannot find CLR method
        """
        OutputType(self: CodeGenerator, typeRef: CodeTypeReference)
            Generates code for the specified type.
        
            typeRef: The type to generate code for.
        """
        pass

    def OutputTypeAttributes(self, *args): #cannot find CLR method
        """
        OutputTypeAttributes(self: CodeGenerator, attributes: TypeAttributes, isStruct: bool, isEnum: bool)
            Generates code for the specified type attributes.
        
            attributes: One of the enumeration values that indicates the type attributes to generate code for.
            isStruct: true if the type is a struct; otherwise, false.
            isEnum: true if the type is an enum; otherwise, false.
        """
        pass

    def OutputTypeNamePair(self, *args): #cannot find CLR method
        """
        OutputTypeNamePair(self: CodeGenerator, typeRef: CodeTypeReference, name: str)
            Generates code for the specified object type and name pair.
        
            typeRef: The type.
            name: The name for the object.
        """
        pass

    def QuoteSnippetString(self, *args): #cannot find CLR method
        """
        QuoteSnippetString(self: CodeGenerator, value: str) -> str
        
            Converts the specified string by formatting it with escape codes.
        
            value: The string to convert.
            Returns: The converted string.
        """
        pass

    def Supports(self, *args): #cannot find CLR method
        """
        Supports(self: CodeGenerator, support: GeneratorSupport) -> bool
        
            Gets a value indicating whether the specified code generation support is provided.
        
            support: The type of code generation support to test for.
            Returns: true if the specified code generation support is provided; otherwise, false.
        """
        pass

    def ValidateIdentifier(self, *args): #cannot find CLR method
        """
        ValidateIdentifier(self: CodeGenerator, value: str)
            Throws an exception if the specified string is not a valid identifier.
        
            value: The identifier to test for validity as an identifier.
        """
        pass

    @staticmethod
    def ValidateIdentifiers(e):
        """
        ValidateIdentifiers(e: CodeObject)
            Attempts to validate each identifier field contained in the specified System.CodeDom.CodeObject 
             or System.CodeDom tree.
        
        
            e: An object to test for invalid identifiers.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurrentClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the code type declaration for the current class.

"""

    CurrentMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current member of the class.

"""

    CurrentMemberName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current member name.

"""

    CurrentTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current class name.

"""

    Indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of spaces to indent each indentation level.

"""

    IsCurrentClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is a class.

"""

    IsCurrentDelegate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is a delegate.

"""

    IsCurrentEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is an enumeration.

"""

    IsCurrentInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is an interface.

"""

    IsCurrentStruct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is a value type or struct.

"""

    NullToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the token that represents null.

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the options to be used by the code generator.

"""

    Output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text writer to use for output.

"""



class ICodeCompiler:
    """ Defines an interface for invoking compilation of source code or a CodeDOM tree using a specific compiler. """
    def CompileAssemblyFromDom(self, options, compilationUnit):
        """
        CompileAssemblyFromDom(self: ICodeCompiler, options: CompilerParameters, compilationUnit: CodeCompileUnit) -> CompilerResults
        
            Compiles an assembly from the System.CodeDom tree contained in the specified 
             System.CodeDom.CodeCompileUnit, using the specified compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.
            compilationUnit: A System.CodeDom.CodeCompileUnit that indicates the code to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        pass

    def CompileAssemblyFromDomBatch(self, options, compilationUnits):
        """
        CompileAssemblyFromDomBatch(self: ICodeCompiler, options: CompilerParameters, compilationUnits: Array[CodeCompileUnit]) -> CompilerResults
        
            Compiles an assembly based on the System.CodeDom trees contained in the specified array of 
             System.CodeDom.CodeCompileUnit objects, using the specified compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.
            compilationUnits: An array of type System.CodeDom.CodeCompileUnit that indicates the code to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        pass

    def CompileAssemblyFromFile(self, options, fileName):
        """
        CompileAssemblyFromFile(self: ICodeCompiler, options: CompilerParameters, fileName: str) -> CompilerResults
        
            Compiles an assembly from the source code contained within the specified file, using the 
             specified compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.
            fileName: The file name of the file that contains the source code to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        pass

    def CompileAssemblyFromFileBatch(self, options, fileNames):
        """
        CompileAssemblyFromFileBatch(self: ICodeCompiler, options: CompilerParameters, fileNames: Array[str]) -> CompilerResults
        
            Compiles an assembly from the source code contained within the specified files, using the 
             specified compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.
            fileNames: The file names of the files to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        pass

    def CompileAssemblyFromSource(self, options, source):
        """
        CompileAssemblyFromSource(self: ICodeCompiler, options: CompilerParameters, source: str) -> CompilerResults
        
            Compiles an assembly from the specified string containing source code, using the specified 
             compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.
            source: The source code to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        pass

    def CompileAssemblyFromSourceBatch(self, options, sources):
        """
        CompileAssemblyFromSourceBatch(self: ICodeCompiler, options: CompilerParameters, sources: Array[str]) -> CompilerResults
        
            Compiles an assembly from the specified array of strings containing source code, using the 
             specified compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for compilation.
            sources: The source code strings to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class CodeCompiler(CodeGenerator, ICodeGenerator, ICodeCompiler):
    """ Provides an example implementation of the System.CodeDom.Compiler.ICodeCompiler interface. """
    def CmdArgsFromParameters(self, *args): #cannot find CLR method
        """
        CmdArgsFromParameters(self: CodeCompiler, options: CompilerParameters) -> str
        
            Gets the command arguments to be passed to the compiler from the specified 
             System.CodeDom.Compiler.CompilerParameters.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters that indicates the compiler options.
            Returns: The command arguments.
        """
        pass

    def ContinueOnNewLine(self, *args): #cannot find CLR method
        """
        ContinueOnNewLine(self: CodeGenerator, st: str)
            Generates a line-continuation character and outputs the specified string on a new line.
        
            st: The string to write on the new line.
        """
        pass

    def CreateEscapedIdentifier(self, *args): #cannot find CLR method
        """
        CreateEscapedIdentifier(self: CodeGenerator, value: str) -> str
        
            Creates an escaped identifier for the specified value.
        
            value: The string to create an escaped identifier for.
            Returns: The escaped identifier for the value.
        """
        pass

    def CreateValidIdentifier(self, *args): #cannot find CLR method
        """
        CreateValidIdentifier(self: CodeGenerator, value: str) -> str
        
            Creates a valid identifier for the specified value.
        
            value: A string to create a valid identifier for.
            Returns: A valid identifier for the value.
        """
        pass

    def FromDom(self, *args): #cannot find CLR method
        """
        FromDom(self: CodeCompiler, options: CompilerParameters, e: CodeCompileUnit) -> CompilerResults
        
            Compiles the specified compile unit using the specified options, and returns the results from 
             the compilation.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.
            e: A System.CodeDom.CodeCompileUnit object that indicates the source to compile.
            Returns: The results of compilation.
        """
        pass

    def FromDomBatch(self, *args): #cannot find CLR method
        """
        FromDomBatch(self: CodeCompiler, options: CompilerParameters, ea: Array[CodeCompileUnit]) -> CompilerResults
        
            Compiles the specified compile units using the specified options, and returns the results from 
             the compilation.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.
            ea: An array of System.CodeDom.CodeCompileUnit objects that indicates the source to compile.
            Returns: The results of compilation.
        """
        pass

    def FromFile(self, *args): #cannot find CLR method
        """
        FromFile(self: CodeCompiler, options: CompilerParameters, fileName: str) -> CompilerResults
        
            Compiles the specified file using the specified options, and returns the results from the 
             compilation.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.
            fileName: The file name to compile.
            Returns: The results of compilation.
        """
        pass

    def FromFileBatch(self, *args): #cannot find CLR method
        """
        FromFileBatch(self: CodeCompiler, options: CompilerParameters, fileNames: Array[str]) -> CompilerResults
        
            Compiles the specified files using the specified options, and returns the results from the 
             compilation.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.
            fileNames: An array of strings that indicates the file names of the files to compile.
            Returns: The results of compilation.
        """
        pass

    def FromSource(self, *args): #cannot find CLR method
        """
        FromSource(self: CodeCompiler, options: CompilerParameters, source: str) -> CompilerResults
        
            Compiles the specified source code string using the specified options, and returns the results 
             from the compilation.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.
            source: The source code string to compile.
            Returns: The results of compilation.
        """
        pass

    def FromSourceBatch(self, *args): #cannot find CLR method
        """
        FromSourceBatch(self: CodeCompiler, options: CompilerParameters, sources: Array[str]) -> CompilerResults
        
            Compiles the specified source code strings using the specified options, and returns the results 
             from the compilation.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.
            sources: An array of strings containing the source code to compile.
            Returns: The results of compilation.
        """
        pass

    def GenerateArgumentReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateArgumentReferenceExpression(self: CodeGenerator, e: CodeArgumentReferenceExpression)
            Generates code for the specified argument reference expression.
        
            e: A System.CodeDom.CodeArgumentReferenceExpression that indicates the expression to generate code 
             for.
        """
        pass

    def GenerateArrayCreateExpression(self, *args): #cannot find CLR method
        """
        GenerateArrayCreateExpression(self: CodeGenerator, e: CodeArrayCreateExpression)
            Generates code for the specified array creation expression.
        
            e: A System.CodeDom.CodeArrayCreateExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateArrayIndexerExpression(self, *args): #cannot find CLR method
        """
        GenerateArrayIndexerExpression(self: CodeGenerator, e: CodeArrayIndexerExpression)
            Generates code for the specified array indexer expression.
        
            e: A System.CodeDom.CodeArrayIndexerExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateAssignStatement(self, *args): #cannot find CLR method
        """
        GenerateAssignStatement(self: CodeGenerator, e: CodeAssignStatement)
            Generates code for the specified assignment statement.
        
            e: A System.CodeDom.CodeAssignStatement that indicates the statement to generate code for.
        """
        pass

    def GenerateAttachEventStatement(self, *args): #cannot find CLR method
        """
        GenerateAttachEventStatement(self: CodeGenerator, e: CodeAttachEventStatement)
            Generates code for the specified attach event statement.
        
            e: A System.CodeDom.CodeAttachEventStatement that indicates the statement to generate code for.
        """
        pass

    def GenerateAttributeDeclarationsEnd(self, *args): #cannot find CLR method
        """
        GenerateAttributeDeclarationsEnd(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)
            Generates code for the specified attribute block end.
        
            attributes: A System.CodeDom.CodeAttributeDeclarationCollection that indicates the end of the attribute 
             block to generate code for.
        """
        pass

    def GenerateAttributeDeclarationsStart(self, *args): #cannot find CLR method
        """
        GenerateAttributeDeclarationsStart(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)
            Generates code for the specified attribute block start.
        
            attributes: A System.CodeDom.CodeAttributeDeclarationCollection that indicates the start of the attribute 
             block to generate code for.
        """
        pass

    def GenerateBaseReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateBaseReferenceExpression(self: CodeGenerator, e: CodeBaseReferenceExpression)
            Generates code for the specified base reference expression.
        
            e: A System.CodeDom.CodeBaseReferenceExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateBinaryOperatorExpression(self, *args): #cannot find CLR method
        """
        GenerateBinaryOperatorExpression(self: CodeGenerator, e: CodeBinaryOperatorExpression)
            Generates code for the specified binary operator expression.
        
            e: A System.CodeDom.CodeBinaryOperatorExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateCastExpression(self, *args): #cannot find CLR method
        """
        GenerateCastExpression(self: CodeGenerator, e: CodeCastExpression)
            Generates code for the specified cast expression.
        
            e: A System.CodeDom.CodeCastExpression that indicates the expression to generate code for.
        """
        pass

    def GenerateComment(self, *args): #cannot find CLR method
        """
        GenerateComment(self: CodeGenerator, e: CodeComment)
            Generates code for the specified comment.
        
            e: A System.CodeDom.CodeComment to generate code for.
        """
        pass

    def GenerateCommentStatement(self, *args): #cannot find CLR method
        """
        GenerateCommentStatement(self: CodeGenerator, e: CodeCommentStatement)
            Generates code for the specified comment statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateCommentStatements(self, *args): #cannot find CLR method
        """
        GenerateCommentStatements(self: CodeGenerator, e: CodeCommentStatementCollection)
            Generates code for the specified comment statements.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateCompileUnit(self, *args): #cannot find CLR method
        """
        GenerateCompileUnit(self: CodeGenerator, e: CodeCompileUnit)
            Generates code for the specified compile unit.
        
            e: The compile unit to generate code for.
        """
        pass

    def GenerateCompileUnitEnd(self, *args): #cannot find CLR method
        """
        GenerateCompileUnitEnd(self: CodeGenerator, e: CodeCompileUnit)
            Generates code for the end of a compile unit.
        
            e: The compile unit to generate code for.
        """
        pass

    def GenerateCompileUnitStart(self, *args): #cannot find CLR method
        """
        GenerateCompileUnitStart(self: CodeGenerator, e: CodeCompileUnit)
            Generates code for the start of a compile unit.
        
            e: The compile unit to generate code for.
        """
        pass

    def GenerateConditionStatement(self, *args): #cannot find CLR method
        """
        GenerateConditionStatement(self: CodeGenerator, e: CodeConditionStatement)
            Generates code for the specified conditional statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateConstructor(self, *args): #cannot find CLR method
        """
        GenerateConstructor(self: CodeGenerator, e: CodeConstructor, c: CodeTypeDeclaration)
            Generates code for the specified constructor.
        
            e: The constructor to generate code for.
            c: The type of the object that this constructor constructs.
        """
        pass

    def GenerateDecimalValue(self, *args): #cannot find CLR method
        """
        GenerateDecimalValue(self: CodeGenerator, d: Decimal)
            Generates code for the specified decimal value.
        
            d: The decimal value to generate code for.
        """
        pass

    def GenerateDefaultValueExpression(self, *args): #cannot find CLR method
        """
        GenerateDefaultValueExpression(self: CodeGenerator, e: CodeDefaultValueExpression)
            Generates code for the specified reference to a default value.
        
            e: The reference to generate code for.
        """
        pass

    def GenerateDelegateCreateExpression(self, *args): #cannot find CLR method
        """
        GenerateDelegateCreateExpression(self: CodeGenerator, e: CodeDelegateCreateExpression)
            Generates code for the specified delegate creation expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateDelegateInvokeExpression(self, *args): #cannot find CLR method
        """
        GenerateDelegateInvokeExpression(self: CodeGenerator, e: CodeDelegateInvokeExpression)
            Generates code for the specified delegate invoke expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateDirectionExpression(self, *args): #cannot find CLR method
        """
        GenerateDirectionExpression(self: CodeGenerator, e: CodeDirectionExpression)
            Generates code for the specified direction expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateDirectives(self, *args): #cannot find CLR method
        """
        GenerateDirectives(self: CodeGenerator, directives: CodeDirectiveCollection)
            Generates code for the specified code directives.
        
            directives: The code directives to generate code for.
        """
        pass

    def GenerateDoubleValue(self, *args): #cannot find CLR method
        """
        GenerateDoubleValue(self: CodeGenerator, d: float)
            Generates code for a double-precision floating point number.
        
            d: The value to generate code for.
        """
        pass

    def GenerateEntryPointMethod(self, *args): #cannot find CLR method
        """
        GenerateEntryPointMethod(self: CodeGenerator, e: CodeEntryPointMethod, c: CodeTypeDeclaration)
            Generates code for the specified entry point method.
        
            e: The entry point for the code.
            c: The code that declares the type.
        """
        pass

    def GenerateEvent(self, *args): #cannot find CLR method
        """
        GenerateEvent(self: CodeGenerator, e: CodeMemberEvent, c: CodeTypeDeclaration)
            Generates code for the specified event.
        
            e: The member event to generate code for.
            c: The type of the object that this event occurs on.
        """
        pass

    def GenerateEventReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateEventReferenceExpression(self: CodeGenerator, e: CodeEventReferenceExpression)
            Generates code for the specified event reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateExpression(self, *args): #cannot find CLR method
        """
        GenerateExpression(self: CodeGenerator, e: CodeExpression)
            Generates code for the specified code expression.
        
            e: The code expression to generate code for.
        """
        pass

    def GenerateExpressionStatement(self, *args): #cannot find CLR method
        """
        GenerateExpressionStatement(self: CodeGenerator, e: CodeExpressionStatement)
            Generates code for the specified expression statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateField(self, *args): #cannot find CLR method
        """
        GenerateField(self: CodeGenerator, e: CodeMemberField)
            Generates code for the specified member field.
        
            e: The field to generate code for.
        """
        pass

    def GenerateFieldReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateFieldReferenceExpression(self: CodeGenerator, e: CodeFieldReferenceExpression)
            Generates code for the specified field reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateGotoStatement(self, *args): #cannot find CLR method
        """
        GenerateGotoStatement(self: CodeGenerator, e: CodeGotoStatement)
            Generates code for the specified goto statement.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateIndexerExpression(self, *args): #cannot find CLR method
        """
        GenerateIndexerExpression(self: CodeGenerator, e: CodeIndexerExpression)
            Generates code for the specified indexer expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateIterationStatement(self, *args): #cannot find CLR method
        """
        GenerateIterationStatement(self: CodeGenerator, e: CodeIterationStatement)
            Generates code for the specified iteration statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateLabeledStatement(self, *args): #cannot find CLR method
        """
        GenerateLabeledStatement(self: CodeGenerator, e: CodeLabeledStatement)
            Generates code for the specified labeled statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateLinePragmaEnd(self, *args): #cannot find CLR method
        """
        GenerateLinePragmaEnd(self: CodeGenerator, e: CodeLinePragma)
            Generates code for the specified line pragma end.
        
            e: The end of the line pragma to generate code for.
        """
        pass

    def GenerateLinePragmaStart(self, *args): #cannot find CLR method
        """
        GenerateLinePragmaStart(self: CodeGenerator, e: CodeLinePragma)
            Generates code for the specified line pragma start.
        
            e: The start of the line pragma to generate code for.
        """
        pass

    def GenerateMethod(self, *args): #cannot find CLR method
        """
        GenerateMethod(self: CodeGenerator, e: CodeMemberMethod, c: CodeTypeDeclaration)
            Generates code for the specified method.
        
            e: The member method to generate code for.
            c: The type of the object that this method occurs on.
        """
        pass

    def GenerateMethodInvokeExpression(self, *args): #cannot find CLR method
        """
        GenerateMethodInvokeExpression(self: CodeGenerator, e: CodeMethodInvokeExpression)
            Generates code for the specified method invoke expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateMethodReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateMethodReferenceExpression(self: CodeGenerator, e: CodeMethodReferenceExpression)
            Generates code for the specified method reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateMethodReturnStatement(self, *args): #cannot find CLR method
        """
        GenerateMethodReturnStatement(self: CodeGenerator, e: CodeMethodReturnStatement)
            Generates code for the specified method return statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateNamespace(self, *args): #cannot find CLR method
        """
        GenerateNamespace(self: CodeGenerator, e: CodeNamespace)
            Generates code for the specified namespace.
        
            e: The namespace to generate code for.
        """
        pass

    def GenerateNamespaceEnd(self, *args): #cannot find CLR method
        """
        GenerateNamespaceEnd(self: CodeGenerator, e: CodeNamespace)
            Generates code for the end of a namespace.
        
            e: The namespace to generate code for.
        """
        pass

    def GenerateNamespaceImport(self, *args): #cannot find CLR method
        """
        GenerateNamespaceImport(self: CodeGenerator, e: CodeNamespaceImport)
            Generates code for the specified namespace import.
        
            e: The namespace import to generate code for.
        """
        pass

    def GenerateNamespaceImports(self, *args): #cannot find CLR method
        """
        GenerateNamespaceImports(self: CodeGenerator, e: CodeNamespace)
            Generates code for the specified namespace import.
        
            e: The namespace import to generate code for.
        """
        pass

    def GenerateNamespaces(self, *args): #cannot find CLR method
        """
        GenerateNamespaces(self: CodeGenerator, e: CodeCompileUnit)
            Generates code for the namespaces in the specified compile unit.
        
            e: The compile unit to generate namespaces for.
        """
        pass

    def GenerateNamespaceStart(self, *args): #cannot find CLR method
        """
        GenerateNamespaceStart(self: CodeGenerator, e: CodeNamespace)
            Generates code for the start of a namespace.
        
            e: The namespace to generate code for.
        """
        pass

    def GenerateObjectCreateExpression(self, *args): #cannot find CLR method
        """
        GenerateObjectCreateExpression(self: CodeGenerator, e: CodeObjectCreateExpression)
            Generates code for the specified object creation expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateParameterDeclarationExpression(self, *args): #cannot find CLR method
        """
        GenerateParameterDeclarationExpression(self: CodeGenerator, e: CodeParameterDeclarationExpression)
            Generates code for the specified parameter declaration expression.
        
            e: The expression to generate code for.
        """
        pass

    def GeneratePrimitiveExpression(self, *args): #cannot find CLR method
        """
        GeneratePrimitiveExpression(self: CodeGenerator, e: CodePrimitiveExpression)
            Generates code for the specified primitive expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateProperty(self, *args): #cannot find CLR method
        """
        GenerateProperty(self: CodeGenerator, e: CodeMemberProperty, c: CodeTypeDeclaration)
            Generates code for the specified property.
        
            e: The property to generate code for.
            c: The type of the object that this property occurs on.
        """
        pass

    def GeneratePropertyReferenceExpression(self, *args): #cannot find CLR method
        """
        GeneratePropertyReferenceExpression(self: CodeGenerator, e: CodePropertyReferenceExpression)
            Generates code for the specified property reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GeneratePropertySetValueReferenceExpression(self, *args): #cannot find CLR method
        """
        GeneratePropertySetValueReferenceExpression(self: CodeGenerator, e: CodePropertySetValueReferenceExpression)
            Generates code for the specified property set value reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateRemoveEventStatement(self, *args): #cannot find CLR method
        """
        GenerateRemoveEventStatement(self: CodeGenerator, e: CodeRemoveEventStatement)
            Generates code for the specified remove event statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateSingleFloatValue(self, *args): #cannot find CLR method
        """
        GenerateSingleFloatValue(self: CodeGenerator, s: Single)
            Generates code for a single-precision floating point number.
        
            s: The value to generate code for.
        """
        pass

    def GenerateSnippetCompileUnit(self, *args): #cannot find CLR method
        """
        GenerateSnippetCompileUnit(self: CodeGenerator, e: CodeSnippetCompileUnit)
            Outputs the code of the specified literal code fragment compile unit.
        
            e: The literal code fragment compile unit to generate code for.
        """
        pass

    def GenerateSnippetExpression(self, *args): #cannot find CLR method
        """
        GenerateSnippetExpression(self: CodeGenerator, e: CodeSnippetExpression)
            Outputs the code of the specified literal code fragment expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateSnippetMember(self, *args): #cannot find CLR method
        """
        GenerateSnippetMember(self: CodeGenerator, e: CodeSnippetTypeMember)
            Outputs the code of the specified literal code fragment class member.
        
            e: The member to generate code for.
        """
        pass

    def GenerateSnippetStatement(self, *args): #cannot find CLR method
        """
        GenerateSnippetStatement(self: CodeGenerator, e: CodeSnippetStatement)
            Outputs the code of the specified literal code fragment statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateStatement(self, *args): #cannot find CLR method
        """
        GenerateStatement(self: CodeGenerator, e: CodeStatement)
            Generates code for the specified statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateStatements(self, *args): #cannot find CLR method
        """
        GenerateStatements(self: CodeGenerator, stms: CodeStatementCollection)
            Generates code for the specified statement collection.
        
            stms: The statements to generate code for.
        """
        pass

    def GenerateThisReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateThisReferenceExpression(self: CodeGenerator, e: CodeThisReferenceExpression)
            Generates code for the specified this reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateThrowExceptionStatement(self, *args): #cannot find CLR method
        """
        GenerateThrowExceptionStatement(self: CodeGenerator, e: CodeThrowExceptionStatement)
            Generates code for the specified throw exception statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateTryCatchFinallyStatement(self, *args): #cannot find CLR method
        """
        GenerateTryCatchFinallyStatement(self: CodeGenerator, e: CodeTryCatchFinallyStatement)
            Generates code for the specified try...catch...finally statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateTypeConstructor(self, *args): #cannot find CLR method
        """
        GenerateTypeConstructor(self: CodeGenerator, e: CodeTypeConstructor)
            Generates code for the specified class constructor.
        
            e: The class constructor to generate code for.
        """
        pass

    def GenerateTypeEnd(self, *args): #cannot find CLR method
        """
        GenerateTypeEnd(self: CodeGenerator, e: CodeTypeDeclaration)
            Generates code for the specified end of the class.
        
            e: The end of the class to generate code for.
        """
        pass

    def GenerateTypeOfExpression(self, *args): #cannot find CLR method
        """
        GenerateTypeOfExpression(self: CodeGenerator, e: CodeTypeOfExpression)
            Generates code for the specified type of expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateTypeReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateTypeReferenceExpression(self: CodeGenerator, e: CodeTypeReferenceExpression)
            Generates code for the specified type reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GenerateTypes(self, *args): #cannot find CLR method
        """
        GenerateTypes(self: CodeGenerator, e: CodeNamespace)
            Generates code for the specified namespace and the classes it contains.
        
            e: The namespace to generate classes for.
        """
        pass

    def GenerateTypeStart(self, *args): #cannot find CLR method
        """
        GenerateTypeStart(self: CodeGenerator, e: CodeTypeDeclaration)
            Generates code for the specified start of the class.
        
            e: The start of the class to generate code for.
        """
        pass

    def GenerateVariableDeclarationStatement(self, *args): #cannot find CLR method
        """
        GenerateVariableDeclarationStatement(self: CodeGenerator, e: CodeVariableDeclarationStatement)
            Generates code for the specified variable declaration statement.
        
            e: The statement to generate code for.
        """
        pass

    def GenerateVariableReferenceExpression(self, *args): #cannot find CLR method
        """
        GenerateVariableReferenceExpression(self: CodeGenerator, e: CodeVariableReferenceExpression)
            Generates code for the specified variable reference expression.
        
            e: The expression to generate code for.
        """
        pass

    def GetResponseFileCmdArgs(self, *args): #cannot find CLR method
        """
        GetResponseFileCmdArgs(self: CodeCompiler, options: CompilerParameters, cmdArgs: str) -> str
        
            Gets the command arguments to use when invoking the compiler to generate a response file.
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler options.
            cmdArgs: A command arguments string.
            Returns: The command arguments to use to generate a response file, or null if there are no response file 
             arguments.
        """
        pass

    def GetTypeOutput(self, *args): #cannot find CLR method
        """
        GetTypeOutput(self: CodeGenerator, value: CodeTypeReference) -> str
        
            Gets the name of the specified data type.
        
            value: The type whose name will be returned.
            Returns: The name of the data type reference.
        """
        pass

    def IsValidIdentifier(self, *args): #cannot find CLR method
        """
        IsValidIdentifier(self: CodeGenerator, value: str) -> bool
        
            Gets a value indicating whether the specified value is a valid identifier.
        
            value: The value to test for conflicts with valid identifiers.
            Returns: true if the value is a valid identifier; otherwise, false.
        """
        pass

    def JoinStringArray(self, *args): #cannot find CLR method
        """
        JoinStringArray(sa: Array[str], separator: str) -> str
        
            Joins the specified string arrays.
        
            sa: The array of strings to join.
            separator: The separator to use.
            Returns: The concatenated string.
        """
        pass

    def OutputAttributeArgument(self, *args): #cannot find CLR method
        """
        OutputAttributeArgument(self: CodeGenerator, arg: CodeAttributeArgument)
            Outputs an argument in an attribute block.
        
            arg: The attribute argument to generate code for.
        """
        pass

    def OutputAttributeDeclarations(self, *args): #cannot find CLR method
        """
        OutputAttributeDeclarations(self: CodeGenerator, attributes: CodeAttributeDeclarationCollection)
            Generates code for the specified attribute declaration collection.
        
            attributes: The attributes to generate code for.
        """
        pass

    def OutputDirection(self, *args): #cannot find CLR method
        """
        OutputDirection(self: CodeGenerator, dir: FieldDirection)
            Generates code for the specified System.CodeDom.FieldDirection.
        
            dir: One of the enumeration values that indicates the attribute of the field.
        """
        pass

    def OutputExpressionList(self, *args): #cannot find CLR method
        """
        OutputExpressionList(self: CodeGenerator, expressions: CodeExpressionCollection, newlineBetweenItems: bool)
            Generates code for the specified expression list.
        
            expressions: The expressions to generate code for.
            newlineBetweenItems: true to insert a new line after each item; otherwise, false.
        OutputExpressionList(self: CodeGenerator, expressions: CodeExpressionCollection)
            Generates code for the specified expression list.
        
            expressions: The expressions to generate code for.
        """
        pass

    def OutputFieldScopeModifier(self, *args): #cannot find CLR method
        """
        OutputFieldScopeModifier(self: CodeGenerator, attributes: MemberAttributes)
            Outputs a field scope modifier that corresponds to the specified attributes.
        
            attributes: One of the enumeration values that specifies the attributes.
        """
        pass

    def OutputIdentifier(self, *args): #cannot find CLR method
        """
        OutputIdentifier(self: CodeGenerator, ident: str)
            Outputs the specified identifier.
        
            ident: The identifier to output.
        """
        pass

    def OutputMemberAccessModifier(self, *args): #cannot find CLR method
        """
        OutputMemberAccessModifier(self: CodeGenerator, attributes: MemberAttributes)
            Generates code for the specified member access modifier.
        
            attributes: One of the enumeration values that indicates the member access modifier to generate code for.
        """
        pass

    def OutputMemberScopeModifier(self, *args): #cannot find CLR method
        """
        OutputMemberScopeModifier(self: CodeGenerator, attributes: MemberAttributes)
            Generates code for the specified member scope modifier.
        
            attributes: One of the enumeration values that indicates the member scope modifier to generate code for.
        """
        pass

    def OutputOperator(self, *args): #cannot find CLR method
        """
        OutputOperator(self: CodeGenerator, op: CodeBinaryOperatorType)
            Generates code for the specified operator.
        
            op: The operator to generate code for.
        """
        pass

    def OutputParameters(self, *args): #cannot find CLR method
        """
        OutputParameters(self: CodeGenerator, parameters: CodeParameterDeclarationExpressionCollection)
            Generates code for the specified parameters.
        
            parameters: The parameter declaration expressions to generate code for.
        """
        pass

    def OutputType(self, *args): #cannot find CLR method
        """
        OutputType(self: CodeGenerator, typeRef: CodeTypeReference)
            Generates code for the specified type.
        
            typeRef: The type to generate code for.
        """
        pass

    def OutputTypeAttributes(self, *args): #cannot find CLR method
        """
        OutputTypeAttributes(self: CodeGenerator, attributes: TypeAttributes, isStruct: bool, isEnum: bool)
            Generates code for the specified type attributes.
        
            attributes: One of the enumeration values that indicates the type attributes to generate code for.
            isStruct: true if the type is a struct; otherwise, false.
            isEnum: true if the type is an enum; otherwise, false.
        """
        pass

    def OutputTypeNamePair(self, *args): #cannot find CLR method
        """
        OutputTypeNamePair(self: CodeGenerator, typeRef: CodeTypeReference, name: str)
            Generates code for the specified object type and name pair.
        
            typeRef: The type.
            name: The name for the object.
        """
        pass

    def ProcessCompilerOutputLine(self, *args): #cannot find CLR method
        """
        ProcessCompilerOutputLine(self: CodeCompiler, results: CompilerResults, line: str)
            Processes the specified line from the specified System.CodeDom.Compiler.CompilerResults.
        
            results: A System.CodeDom.Compiler.CompilerResults that indicates the results of compilation.
            line: The line to process.
        """
        pass

    def QuoteSnippetString(self, *args): #cannot find CLR method
        """
        QuoteSnippetString(self: CodeGenerator, value: str) -> str
        
            Converts the specified string by formatting it with escape codes.
        
            value: The string to convert.
            Returns: The converted string.
        """
        pass

    def Supports(self, *args): #cannot find CLR method
        """
        Supports(self: CodeGenerator, support: GeneratorSupport) -> bool
        
            Gets a value indicating whether the specified code generation support is provided.
        
            support: The type of code generation support to test for.
            Returns: true if the specified code generation support is provided; otherwise, false.
        """
        pass

    def ValidateIdentifier(self, *args): #cannot find CLR method
        """
        ValidateIdentifier(self: CodeGenerator, value: str)
            Throws an exception if the specified string is not a valid identifier.
        
            value: The identifier to test for validity as an identifier.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CompilerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the compiler executable.

"""

    CurrentClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the code type declaration for the current class.

"""

    CurrentMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current member of the class.

"""

    CurrentMemberName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current member name.

"""

    CurrentTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current class name.

"""

    FileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file name extension to use for source files.

"""

    Indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the amount of spaces to indent each indentation level.

"""

    IsCurrentClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is a class.

"""

    IsCurrentDelegate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is a delegate.

"""

    IsCurrentEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is an enumeration.

"""

    IsCurrentInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is an interface.

"""

    IsCurrentStruct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the current object being generated is a value type or struct.

"""

    NullToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the token that represents null.

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the options to be used by the code generator.

"""

    Output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text writer to use for output.

"""



class CodeDomProvider(Component, IComponent, IDisposable):
    """ Provides a base class for System.CodeDom.Compiler.CodeDomProvider implementations. This class is abstract. """
    def CompileAssemblyFromDom(self, options, compilationUnits):
        """
        CompileAssemblyFromDom(self: CodeDomProvider, options: CompilerParameters, *compilationUnits: Array[CodeCompileUnit]) -> CompilerResults
        
            Compiles an assembly based on the System.CodeDom trees contained in the specified array of 
             System.CodeDom.CodeCompileUnit objects, using the specified compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for the 
             compilation.
        
            compilationUnits: An array of type System.CodeDom.CodeCompileUnit that indicates the code to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of the compilation.
        """
        pass

    def CompileAssemblyFromFile(self, options, fileNames):
        """
        CompileAssemblyFromFile(self: CodeDomProvider, options: CompilerParameters, *fileNames: Array[str]) -> CompilerResults
        
            Compiles an assembly from the source code contained in the specified files, using the specified 
             compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the settings for the 
             compilation.
        
            fileNames: An array of the names of the files to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        pass

    def CompileAssemblyFromSource(self, options, sources):
        """
        CompileAssemblyFromSource(self: CodeDomProvider, options: CompilerParameters, *sources: Array[str]) -> CompilerResults
        
            Compiles an assembly from the specified array of strings containing source code, using the 
             specified compiler settings.
        
        
            options: A System.CodeDom.Compiler.CompilerParameters object that indicates the compiler settings for 
             this compilation.
        
            sources: An array of source code strings to compile.
            Returns: A System.CodeDom.Compiler.CompilerResults object that indicates the results of compilation.
        """
        pass

    def CreateCompiler(self):
        """
        CreateCompiler(self: CodeDomProvider) -> ICodeCompiler
        
            When overridden in a derived class, creates a new code compiler.
            Returns: An System.CodeDom.Compiler.ICodeCompiler that can be used for compilation of System.CodeDom 
             based source code representations.
        """
        pass

    def CreateEscapedIdentifier(self, value):
        """
        CreateEscapedIdentifier(self: CodeDomProvider, value: str) -> str
        
            Creates an escaped identifier for the specified value.
        
            value: The string for which to create an escaped identifier.
            Returns: The escaped identifier for the value.
        """
        pass

    def CreateGenerator(self, *__args):
        """
        CreateGenerator(self: CodeDomProvider, fileName: str) -> ICodeGenerator
        
            When overridden in a derived class, creates a new code generator using the specified file name 
             for output.
        
        
            fileName: The file name to output to.
            Returns: An System.CodeDom.Compiler.ICodeGenerator that can be used to generate System.CodeDom based 
             source code representations.
        
        CreateGenerator(self: CodeDomProvider, output: TextWriter) -> ICodeGenerator
        
            When overridden in a derived class, creates a new code generator using the specified 
             System.IO.TextWriter for output.
        
        
            output: A System.IO.TextWriter to use to output.
            Returns: An System.CodeDom.Compiler.ICodeGenerator that can be used to generate System.CodeDom based 
             source code representations.
        
        CreateGenerator(self: CodeDomProvider) -> ICodeGenerator
        
            When overridden in a derived class, creates a new code generator.
            Returns: An System.CodeDom.Compiler.ICodeGenerator that can be used to generate System.CodeDom based 
             source code representations.
        """
        pass

    def CreateParser(self):
        """
        CreateParser(self: CodeDomProvider) -> ICodeParser
        
            When overridden in a derived class, creates a new code parser.
            Returns: An System.CodeDom.Compiler.ICodeParser that can be used to parse source code. The base 
             implementation always returns null.
        """
        pass

    @staticmethod
    def CreateProvider(language, providerOptions=None):
        """
        CreateProvider(language: str) -> CodeDomProvider
        
            Gets a System.CodeDom.Compiler.CodeDomProvider instance for the specified language.
        
            language: The language name.
            Returns: A CodeDOM provider that is implemented for the specified language name.
        CreateProvider(language: str, providerOptions: IDictionary[str, str]) -> CodeDomProvider
        """
        pass

    def CreateValidIdentifier(self, value):
        """
        CreateValidIdentifier(self: CodeDomProvider, value: str) -> str
        
            Creates a valid identifier for the specified value.
        
            value: The string for which to generate a valid identifier.
            Returns: A valid identifier for the specified value.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: Component, disposing: bool)
            Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
             releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GenerateCodeFromCompileUnit(self, compileUnit, writer, options):
        """
        GenerateCodeFromCompileUnit(self: CodeDomProvider, compileUnit: CodeCompileUnit, writer: TextWriter, options: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) compilation unit and sends 
             it to the specified text writer, using the specified options.
        
        
            compileUnit: A System.CodeDom.CodeCompileUnit for which to generate code.
            writer: The System.IO.TextWriter to which the output code is sent.
            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromExpression(self, expression, writer, options):
        """
        GenerateCodeFromExpression(self: CodeDomProvider, expression: CodeExpression, writer: TextWriter, options: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) expression and sends it to 
             the specified text writer, using the specified options.
        
        
            expression: A System.CodeDom.CodeExpression object that indicates the expression for which to generate code.
            writer: The System.IO.TextWriter to which output code is sent.
            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromMember(self, member, writer, options):
        """
        GenerateCodeFromMember(self: CodeDomProvider, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) member declaration and 
             sends it to the specified text writer, using the specified options.
        
        
            member: A System.CodeDom.CodeTypeMember object that indicates the member for which to generate code.
            writer: The System.IO.TextWriter to which output code is sent.
            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromNamespace(self, codeNamespace, writer, options):
        """
        GenerateCodeFromNamespace(self: CodeDomProvider, codeNamespace: CodeNamespace, writer: TextWriter, options: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) namespace and sends it to 
             the specified text writer, using the specified options.
        
        
            codeNamespace: A System.CodeDom.CodeNamespace object that indicates the namespace for which to generate code.
            writer: The System.IO.TextWriter to which output code is sent.
            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromStatement(self, statement, writer, options):
        """
        GenerateCodeFromStatement(self: CodeDomProvider, statement: CodeStatement, writer: TextWriter, options: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) statement and sends it to 
             the specified text writer, using the specified options.
        
        
            statement: A System.CodeDom.CodeStatement containing the CodeDOM elements for which to generate code.
            writer: The System.IO.TextWriter to which output code is sent.
            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    def GenerateCodeFromType(self, codeType, writer, options):
        """
        GenerateCodeFromType(self: CodeDomProvider, codeType: CodeTypeDeclaration, writer: TextWriter, options: CodeGeneratorOptions)
            Generates code for the specified Code Document Object Model (CodeDOM) type declaration and sends 
             it to the specified text writer, using the specified options.
        
        
            codeType: A System.CodeDom.CodeTypeDeclaration object that indicates the type for which to generate code.
            writer: The System.IO.TextWriter to which output code is sent.
            options: A System.CodeDom.Compiler.CodeGeneratorOptions that indicates the options to use for generating 
             code.
        """
        pass

    @staticmethod
    def GetAllCompilerInfo():
        """
        GetAllCompilerInfo() -> Array[CompilerInfo]
        
            Returns the language provider and compiler configuration settings for this computer.
            Returns: An array of type System.CodeDom.Compiler.CompilerInfo representing the settings of all 
             configured System.CodeDom.Compiler.CodeDomProvider implementations.
        """
        pass

    @staticmethod
    def GetCompilerInfo(language):
        """
        GetCompilerInfo(language: str) -> CompilerInfo
        
            Returns the language provider and compiler configuration settings for the specified language.
        
            language: A language name.
            Returns: A System.CodeDom.Compiler.CompilerInfo object populated with settings of the configured 
             System.CodeDom.Compiler.CodeDomProvider implementation.
        """
        pass

    def GetConverter(self, type):
        """
        GetConverter(self: CodeDomProvider, type: Type) -> TypeConverter
        
            Gets a System.ComponentModel.TypeConverter for the specified data type.
        
            type: The type of object to retrieve a type converter for.
            Returns: A System.ComponentModel.TypeConverter for the specified type, or null if a 
             System.ComponentModel.TypeConverter for the specified type cannot be found.
        """
        pass

    @staticmethod
    def GetLanguageFromExtension(extension):
        """
        GetLanguageFromExtension(extension: str) -> str
        
            Returns a language name associated with the specified file name extension, as configured in the 
             System.CodeDom.Compiler.CodeDomProvider compiler configuration section.
        
        
            extension: A file name extension.
            Returns: A language name associated with the file name extension, as configured in the 
             System.CodeDom.Compiler.CodeDomProvider compiler configuration settings.
        """
        pass

    def GetService(self, *args): #cannot find CLR method
        """
        GetService(self: Component, service: Type) -> object
        
            Returns an object that represents a service provided by the System.ComponentModel.Component or 
             by its System.ComponentModel.Container.
        
        
            service: A service provided by the System.ComponentModel.Component.
            Returns: An System.Object that represents a service provided by the System.ComponentModel.Component, or 
             null if the System.ComponentModel.Component does not provide the specified service.
        """
        pass

    def GetTypeOutput(self, type):
        """
        GetTypeOutput(self: CodeDomProvider, type: CodeTypeReference) -> str
        
            Gets the type indicated by the specified System.CodeDom.CodeTypeReference.
        
            type: A System.CodeDom.CodeTypeReference that indicates the type to return.
            Returns: A text representation of the specified type, formatted for the language in which code is 
             generated by this code generator. In Visual Basic, for example, passing in a 
             System.CodeDom.CodeTypeReference for the System.Int32 type will return "Integer".
        """
        pass

    @staticmethod
    def IsDefinedExtension(extension):
        """
        IsDefinedExtension(extension: str) -> bool
        
            Tests whether a file name extension has an associated System.CodeDom.Compiler.CodeDomProvider 
             implementation configured on the computer.
        
        
            extension: A file name extension.
            Returns: true if a System.CodeDom.Compiler.CodeDomProvider implementation is configured for the specified 
             file name extension; otherwise, false.
        """
        pass

    @staticmethod
    def IsDefinedLanguage(language):
        """
        IsDefinedLanguage(language: str) -> bool
        
            Tests whether a language has a System.CodeDom.Compiler.CodeDomProvider implementation configured 
             on the computer.
        
        
            language: The language name.
            Returns: true if a System.CodeDom.Compiler.CodeDomProvider implementation is configured for the specified 
             language; otherwise, false.
        """
        pass

    def IsValidIdentifier(self, value):
        """
        IsValidIdentifier(self: CodeDomProvider, value: str) -> bool
        
            Returns a value that indicates whether the specified value is a valid identifier for the current 
             language.
        
        
            value: The value to verify as a valid identifier.
            Returns: true if the value parameter is a valid identifier; otherwise, false.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def Parse(self, codeStream):
        """
        Parse(self: CodeDomProvider, codeStream: TextReader) -> CodeCompileUnit
        
            Compiles the code read from the specified text stream into a System.CodeDom.CodeCompileUnit.
        
            codeStream: A System.IO.TextReader object that is used to read the code to be parsed.
            Returns: A System.CodeDom.CodeCompileUnit that contains a representation of the parsed code.
        """
        pass

    def Supports(self, generatorSupport):
        """
        Supports(self: CodeDomProvider, generatorSupport: GeneratorSupport) -> bool
        
            Returns a value indicating whether the specified code generation support is provided.
        
            generatorSupport: A System.CodeDom.Compiler.GeneratorSupport object that indicates the type of code generation 
             support to verify.
        
            Returns: true if the specified code generation support is provided; otherwise, false.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    FileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the default file name extension to use for source code files in the current language.

Get: FileExtension(self: CodeDomProvider) -> str

"""

    LanguageOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a language features identifier.

Get: LanguageOptions(self: CodeDomProvider) -> LanguageOptions

"""



class CodeGeneratorOptions(object):
    """
    Represents a set of options used by a code generator.
    
    CodeGeneratorOptions()
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    BlankLinesBetweenMembers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to insert blank lines between members.

Get: BlankLinesBetweenMembers(self: CodeGeneratorOptions) -> bool

Set: BlankLinesBetweenMembers(self: CodeGeneratorOptions) = value
"""

    BracingStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the style to use for bracing.

Get: BracingStyle(self: CodeGeneratorOptions) -> str

Set: BracingStyle(self: CodeGeneratorOptions) = value
"""

    ElseOnClosing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to append an else, catch, or finally block, including brackets, at the closing line of each previous if or try block.

Get: ElseOnClosing(self: CodeGeneratorOptions) -> bool

Set: ElseOnClosing(self: CodeGeneratorOptions) = value
"""

    IndentString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the string to use for indentations.

Get: IndentString(self: CodeGeneratorOptions) -> str

Set: IndentString(self: CodeGeneratorOptions) = value
"""

    VerbatimOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to generate members in the order in which they occur in member collections.

Get: VerbatimOrder(self: CodeGeneratorOptions) -> bool

Set: VerbatimOrder(self: CodeGeneratorOptions) = value
"""



class CodeParser(object, ICodeParser):
    """ Provides an empty implementation of the System.CodeDom.Compiler.ICodeParser interface. """
    def Parse(self, codeStream):
        """
        Parse(self: CodeParser, codeStream: TextReader) -> CodeCompileUnit
        
            Compiles the specified text stream into a System.CodeDom.CodeCompileUnit.
        
            codeStream: A System.IO.TextReader that is used to read the code to be parsed.
            Returns: A System.CodeDom.CodeCompileUnit containing the code model produced from parsing the code.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class CompilerError(object):
    """
    Represents a compiler error or warning.
    
    CompilerError()
    CompilerError(fileName: str, line: int, column: int, errorNumber: str, errorText: str)
    """
    def ToString(self):
        """
        ToString(self: CompilerError) -> str
        
            Provides an implementation of Object's System.Object.ToString method.
            Returns: A string representation of the compiler error.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fileName=None, line=None, column=None, errorNumber=None, errorText=None):
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str, line: int, column: int, errorNumber: str, errorText: str)
        """
        pass

    Column = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the column number where the source of the error occurs.

Get: Column(self: CompilerError) -> int

Set: Column(self: CompilerError) = value
"""

    ErrorNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the error number.

Get: ErrorNumber(self: CompilerError) -> str

Set: ErrorNumber(self: CompilerError) = value
"""

    ErrorText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text of the error message.

Get: ErrorText(self: CompilerError) -> str

Set: ErrorText(self: CompilerError) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file name of the source file that contains the code which caused the error.

Get: FileName(self: CompilerError) -> str

Set: FileName(self: CompilerError) = value
"""

    IsWarning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the error is a warning.

Get: IsWarning(self: CompilerError) -> bool

Set: IsWarning(self: CompilerError) = value
"""

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line number where the source of the error occurs.

Get: Line(self: CompilerError) -> int

Set: Line(self: CompilerError) = value
"""



class CompilerErrorCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.Compiler.CompilerError objects.
    
    CompilerErrorCollection()
    CompilerErrorCollection(value: CompilerErrorCollection)
    CompilerErrorCollection(value: Array[CompilerError])
    """
    def Add(self, value):
        """
        Add(self: CompilerErrorCollection, value: CompilerError) -> int
        
            Adds the specified System.CodeDom.Compiler.CompilerError object to the error collection.
        
            value: The System.CodeDom.Compiler.CompilerError object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CompilerErrorCollection, value: CompilerErrorCollection)
            Adds the contents of the specified compiler error collection to the end of the error collection.
        
            value: A System.CodeDom.Compiler.CompilerErrorCollection object that contains the objects to add to the 
             collection.
        
        AddRange(self: CompilerErrorCollection, value: Array[CompilerError])
            Copies the elements of an array to the end of the error collection.
        
            value: An array of type System.CodeDom.Compiler.CompilerError that contains the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CompilerErrorCollection, value: CompilerError) -> bool
        
            Gets a value that indicates whether the collection contains the specified 
             System.CodeDom.Compiler.CompilerError object.
        
        
            value: The System.CodeDom.Compiler.CompilerError to locate.
            Returns: true if the System.CodeDom.Compiler.CompilerError is contained in the collection; otherwise, 
             false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CompilerErrorCollection, array: Array[CompilerError], index: int)
            Copies the collection values to a one-dimensional System.Array instance at the specified index.
        
            array: The one-dimensional System.Array that is the destination of the values copied from 
             System.CodeDom.Compiler.CompilerErrorCollection.
        
            index: The index in the array at which to start copying.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CompilerErrorCollection, value: CompilerError) -> int
        
            Gets the index of the specified System.CodeDom.Compiler.CompilerError object in the collection, 
             if it exists in the collection.
        
        
            value: The System.CodeDom.Compiler.CompilerError to locate.
            Returns: The index of the specified System.CodeDom.Compiler.CompilerError in the 
             System.CodeDom.Compiler.CompilerErrorCollection, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CompilerErrorCollection, index: int, value: CompilerError)
            Inserts the specified System.CodeDom.Compiler.CompilerError into the collection at the specified 
             index.
        
        
            index: The zero-based index where the compiler error should be inserted.
            value: The System.CodeDom.Compiler.CompilerError to insert.
        """
        pass

    def OnClear(self, *args): #cannot find CLR method
        """
        OnClear(self: CollectionBase)
            Performs additional custom processes when clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnClearComplete(self, *args): #cannot find CLR method
        """
        OnClearComplete(self: CollectionBase)
            Performs additional custom processes after clearing the contents of the 
             System.Collections.CollectionBase instance.
        """
        pass

    def OnInsert(self, *args): #cannot find CLR method
        """
        OnInsert(self: CollectionBase, index: int, value: object)
            Performs additional custom processes before inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnInsertComplete(self, *args): #cannot find CLR method
        """
        OnInsertComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after inserting a new element into the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which to insert value.
            value: The new value of the element at index.
        """
        pass

    def OnRemove(self, *args): #cannot find CLR method
        """
        OnRemove(self: CollectionBase, index: int, value: object)
            Performs additional custom processes when removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnRemoveComplete(self, *args): #cannot find CLR method
        """
        OnRemoveComplete(self: CollectionBase, index: int, value: object)
            Performs additional custom processes after removing an element from the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which value can be found.
            value: The value of the element to remove from index.
        """
        pass

    def OnSet(self, *args): #cannot find CLR method
        """
        OnSet(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes before setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnSetComplete(self, *args): #cannot find CLR method
        """
        OnSetComplete(self: CollectionBase, index: int, oldValue: object, newValue: object)
            Performs additional custom processes after setting a value in the 
             System.Collections.CollectionBase instance.
        
        
            index: The zero-based index at which oldValue can be found.
            oldValue: The value to replace with newValue.
            newValue: The new value of the element at index.
        """
        pass

    def OnValidate(self, *args): #cannot find CLR method
        """
        OnValidate(self: CollectionBase, value: object)
            Performs additional custom processes when validating a value.
        
            value: The object to validate.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: CompilerErrorCollection, value: CompilerError)
            Removes a specific System.CodeDom.Compiler.CompilerError from the collection.
        
            value: The System.CodeDom.Compiler.CompilerError to remove from the 
             System.CodeDom.Compiler.CompilerErrorCollection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: CompilerErrorCollection)
        __new__(cls: type, value: Array[CompilerError])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    HasErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection contains errors.

Get: HasErrors(self: CompilerErrorCollection) -> bool

"""

    HasWarnings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection contains warnings.

Get: HasWarnings(self: CompilerErrorCollection) -> bool

"""

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CompilerInfo(object):
    """ Represents the configuration settings of a language provider. This class cannot be inherited. """
    def CreateDefaultCompilerParameters(self):
        """
        CreateDefaultCompilerParameters(self: CompilerInfo) -> CompilerParameters
        
            Gets the configured compiler settings for the language provider implementation.
            Returns: A read-only System.CodeDom.Compiler.CompilerParameters instance that contains the compiler 
             options and settings configured for the language provider.
        """
        pass

    def CreateProvider(self, providerOptions=None):
        """
        CreateProvider(self: CompilerInfo) -> CodeDomProvider
        
            Returns a System.CodeDom.Compiler.CodeDomProvider instance for the current language provider 
             settings.
        
            Returns: A CodeDOM provider associated with the language provider configuration.
        CreateProvider(self: CompilerInfo, providerOptions: IDictionary[str, str]) -> CodeDomProvider
        """
        pass

    def Equals(self, o):
        """
        Equals(self: CompilerInfo, o: object) -> bool
        
            Determines whether the specified object represents the same language provider and compiler 
             settings as the current System.CodeDom.Compiler.CompilerInfo.
        
        
            o: The object to compare with the current System.CodeDom.Compiler.CompilerInfo.
            Returns: true if o is a System.CodeDom.Compiler.CompilerInfo object and its value is the same as this 
             instance; otherwise, false.
        """
        pass

    def GetExtensions(self):
        """
        GetExtensions(self: CompilerInfo) -> Array[str]
        
            Returns the file name extensions supported by the language provider.
            Returns: An array of file name extensions supported by the language provider.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: CompilerInfo) -> int
        
            Returns the hash code for the current instance.
            Returns: A 32-bit signed integer hash code for the current System.CodeDom.Compiler.CompilerInfo instance, 
             suitable for use in hashing algorithms and data structures such as a hash table.
        """
        pass

    def GetLanguages(self):
        """
        GetLanguages(self: CompilerInfo) -> Array[str]
        
            Gets the language names supported by the language provider.
            Returns: An array of language names supported by the language provider.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    CodeDomProviderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the configured System.CodeDom.Compiler.CodeDomProvider implementation.

Get: CodeDomProviderType(self: CompilerInfo) -> Type

"""

    IsCodeDomProviderTypeValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a value indicating whether the language provider implementation is configured on the computer.

Get: IsCodeDomProviderTypeValid(self: CompilerInfo) -> bool

"""



class CompilerParameters(object):
    """
    Represents the parameters used to invoke a compiler.
    
    CompilerParameters(assemblyNames: Array[str], outputName: str, includeDebugInformation: bool)
    CompilerParameters()
    CompilerParameters(assemblyNames: Array[str])
    CompilerParameters(assemblyNames: Array[str], outputName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, assemblyNames=None, outputName=None, includeDebugInformation=None):
        """
        __new__(cls: type)
        __new__(cls: type, assemblyNames: Array[str])
        __new__(cls: type, assemblyNames: Array[str], outputName: str)
        __new__(cls: type, assemblyNames: Array[str], outputName: str, includeDebugInformation: bool)
        """
        pass

    CompilerOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the optional additional-command line arguments string to use when invoking the compiler.

Get: CompilerOptions(self: CompilerParameters) -> str

Set: CompilerOptions(self: CompilerParameters) = value
"""

    CoreAssemblyFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoreAssemblyFileName(self: CompilerParameters) -> str

Set: CoreAssemblyFileName(self: CompilerParameters) = value
"""

    EmbeddedResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the .NET Framework resource files to include when compiling the assembly output.

Get: EmbeddedResources(self: CompilerParameters) -> StringCollection

"""

    Evidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies an evidence object that represents the security policy permissions to grant the compiled assembly.

Get: Evidence(self: CompilerParameters) -> Evidence

Set: Evidence(self: CompilerParameters) = value
"""

    GenerateExecutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to generate an executable.

Get: GenerateExecutable(self: CompilerParameters) -> bool

Set: GenerateExecutable(self: CompilerParameters) = value
"""

    GenerateInMemory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to generate the output in memory.

Get: GenerateInMemory(self: CompilerParameters) -> bool

Set: GenerateInMemory(self: CompilerParameters) = value
"""

    IncludeDebugInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to include debug information in the compiled executable.

Get: IncludeDebugInformation(self: CompilerParameters) -> bool

Set: IncludeDebugInformation(self: CompilerParameters) = value
"""

    LinkedResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the .NET Framework resource files that are referenced in the current source.

Get: LinkedResources(self: CompilerParameters) -> StringCollection

"""

    MainClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the main class.

Get: MainClass(self: CompilerParameters) -> str

Set: MainClass(self: CompilerParameters) = value
"""

    OutputAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the output assembly.

Get: OutputAssembly(self: CompilerParameters) -> str

Set: OutputAssembly(self: CompilerParameters) = value
"""

    ReferencedAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the assemblies referenced by the current project.

Get: ReferencedAssemblies(self: CompilerParameters) -> StringCollection

"""

    TempFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the collection that contains the temporary files.

Get: TempFiles(self: CompilerParameters) -> TempFileCollection

Set: TempFiles(self: CompilerParameters) = value
"""

    TreatWarningsAsErrors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to treat warnings as errors.

Get: TreatWarningsAsErrors(self: CompilerParameters) -> bool

Set: TreatWarningsAsErrors(self: CompilerParameters) = value
"""

    UserToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the user token to use when creating the compiler process.

Get: UserToken(self: CompilerParameters) -> IntPtr

Set: UserToken(self: CompilerParameters) = value
"""

    WarningLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the warning level at which the compiler aborts compilation.

Get: WarningLevel(self: CompilerParameters) -> int

Set: WarningLevel(self: CompilerParameters) = value
"""

    Win32Resource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the file name of a Win32 resource file to link into the compiled assembly.

Get: Win32Resource(self: CompilerParameters) -> str

Set: Win32Resource(self: CompilerParameters) = value
"""



class CompilerResults(object):
    """
    Represents the results of compilation that are returned from a compiler.
    
    CompilerResults(tempFiles: TempFileCollection)
    """
    @staticmethod # known case of __new__
    def __new__(self, tempFiles):
        """ __new__(cls: type, tempFiles: TempFileCollection) """
        pass

    CompiledAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the compiled assembly.

Get: CompiledAssembly(self: CompilerResults) -> Assembly

Set: CompiledAssembly(self: CompilerResults) = value
"""

    Errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of compiler errors and warnings.

Get: Errors(self: CompilerResults) -> CompilerErrorCollection

"""

    Evidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the evidence object that represents the security policy permissions of the compiled assembly.

Get: Evidence(self: CompilerResults) -> Evidence

Set: Evidence(self: CompilerResults) = value
"""

    NativeCompilerReturnValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the compiler's return value.

Get: NativeCompilerReturnValue(self: CompilerResults) -> int

Set: NativeCompilerReturnValue(self: CompilerResults) = value
"""

    Output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the compiler output messages.

Get: Output(self: CompilerResults) -> StringCollection

"""

    PathToAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path of the compiled assembly.

Get: PathToAssembly(self: CompilerResults) -> str

Set: PathToAssembly(self: CompilerResults) = value
"""

    TempFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the temporary file collection to use.

Get: TempFiles(self: CompilerResults) -> TempFileCollection

Set: TempFiles(self: CompilerResults) = value
"""



class Executor(object):
    """ Provides command execution functions for invoking compilers. This class cannot be inherited. """
    @staticmethod
    def ExecWait(cmd, tempFiles):
        """
        ExecWait(cmd: str, tempFiles: TempFileCollection)
            Executes the command using the specified temporary files and waits for the call to return.
        
            cmd: The command to execute.
            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to 
             intermediate files generated during compilation.
        """
        pass

    @staticmethod
    def ExecWaitWithCapture(*__args):
        """
        ExecWaitWithCapture(userToken: IntPtr, cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)
        
            Executes the specified command using the specified user token and temporary files, and waits for 
             the call to return, storing output and error information from the compiler in the specified 
             strings.
        
        
            userToken: The token to start the compiler process with.
            cmd: The command to execute.
            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to 
             intermediate files generated during compilation.
        
            outputName: A reference to a string that will store the compiler's message output.
            errorName: A reference to a string that will store the name of the error or errors encountered.
            Returns: The return value from the compiler.
        ExecWaitWithCapture(userToken: IntPtr, cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)
        
            Executes the specified command using the specified user token, current directory, and temporary 
             files; then waits for the call to return, storing output and error information from the compiler 
             in the specified strings.
        
        
            userToken: The token to start the compiler process with.
            cmd: The command to execute.
            currentDir: The directory to start the process in.
            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to 
             intermediate files generated during compilation.
        
            outputName: A reference to a string that will store the compiler's message output.
            errorName: A reference to a string that will store the name of the error or errors encountered.
            Returns: The return value from the compiler.
        ExecWaitWithCapture(cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)
        
            Executes the specified command using the specified temporary files and waits for the call to 
             return, storing output and error information from the compiler in the specified strings.
        
        
            cmd: The command to execute.
            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to 
             intermediate files generated during compilation.
        
            outputName: A reference to a string that will store the compiler's message output.
            errorName: A reference to a string that will store the name of the error or errors encountered.
            Returns: The return value from the compiler.
        ExecWaitWithCapture(cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> (int, str, str)
        
            Executes the specified command using the specified current directory and temporary files, and 
             waits for the call to return, storing output and error information from the compiler in the 
             specified strings.
        
        
            cmd: The command to execute.
            currentDir: The current directory.
            tempFiles: A System.CodeDom.Compiler.TempFileCollection with which to manage and store references to 
             intermediate files generated during compilation.
        
            outputName: A reference to a string that will store the compiler's message output.
            errorName: A reference to a string that will store the name of the error or errors encountered.
            Returns: The return value from the compiler.
        """
        pass

    __all__ = [
        'ExecWait',
        'ExecWaitWithCapture',
    ]


class GeneratedCodeAttribute(Attribute, _Attribute):
    """
    Identifies code generated by a tool. This class cannot be inherited.
    
    GeneratedCodeAttribute(tool: str, version: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tool, version):
        """ __new__(cls: type, tool: str, version: str) """
        pass

    Tool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the tool that generated the code.

Get: Tool(self: GeneratedCodeAttribute) -> str

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version of the tool that generated the code.

Get: Version(self: GeneratedCodeAttribute) -> str

"""



class GeneratorSupport(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers used to determine whether a code generator supports certain types of code elements.
    
    enum (flags) GeneratorSupport, values: ArraysOfArrays (1), AssemblyAttributes (4096), ChainedConstructorArguments (32768), ComplexExpressions (524288), DeclareDelegates (512), DeclareEnums (256), DeclareEvents (2048), DeclareIndexerProperties (33554432), DeclareInterfaces (1024), DeclareValueTypes (128), EntryPointMethod (2), GenericTypeDeclaration (16777216), GenericTypeReference (8388608), GotoStatements (4), MultidimensionalArrays (8), MultipleInterfaceMembers (131072), NestedTypes (65536), ParameterAttributes (8192), PartialTypes (4194304), PublicStaticMembers (262144), ReferenceParameters (16384), Resources (2097152), ReturnTypeAttributes (64), StaticConstructors (16), TryCatchStatements (32), Win32Resources (1048576)
    """
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

    ArraysOfArrays = None
    AssemblyAttributes = None
    ChainedConstructorArguments = None
    ComplexExpressions = None
    DeclareDelegates = None
    DeclareEnums = None
    DeclareEvents = None
    DeclareIndexerProperties = None
    DeclareInterfaces = None
    DeclareValueTypes = None
    EntryPointMethod = None
    GenericTypeDeclaration = None
    GenericTypeReference = None
    GotoStatements = None
    MultidimensionalArrays = None
    MultipleInterfaceMembers = None
    NestedTypes = None
    ParameterAttributes = None
    PartialTypes = None
    PublicStaticMembers = None
    ReferenceParameters = None
    Resources = None
    ReturnTypeAttributes = None
    StaticConstructors = None
    TryCatchStatements = None
    value__ = None
    Win32Resources = None


class ICodeParser:
    """ Defines an interface for parsing code into a System.CodeDom.CodeCompileUnit. """
    def Parse(self, codeStream):
        """
        Parse(self: ICodeParser, codeStream: TextReader) -> CodeCompileUnit
        
            When implemented in a derived class, compiles the specified text stream into a 
             System.CodeDom.CodeCompileUnit.
        
        
            codeStream: A System.IO.TextReader that can be used to read the code to be compiled.
            Returns: A System.CodeDom.CodeCompileUnit that contains a representation of the parsed code.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IndentedTextWriter(TextWriter, IDisposable):
    """
    Provides a text writer that can indent new lines by a tab string token.
    
    IndentedTextWriter(writer: TextWriter, tabString: str)
    IndentedTextWriter(writer: TextWriter)
    """
    def Close(self):
        """
        Close(self: IndentedTextWriter)
            Closes the document being written to.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: TextWriter, disposing: bool)
            Releases the unmanaged resources used by the System.IO.TextWriter and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def Flush(self):
        """
        Flush(self: IndentedTextWriter)
            Flushes the stream.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def OutputTabs(self, *args): #cannot find CLR method
        """
        OutputTabs(self: IndentedTextWriter)
            Outputs the tab string once for each level of indentation according to the 
             System.CodeDom.Compiler.IndentedTextWriter.Indent property.
        """
        pass

    def Write(self, *__args):
        """
        Write(self: IndentedTextWriter, value: object)
            Writes the text representation of an object to the text stream.
        
            value: The object to write.
        Write(self: IndentedTextWriter, value: Int64)
            Writes the text representation of an 8-byte integer to the text stream.
        
            value: The 8-byte integer to write.
        Write(self: IndentedTextWriter, value: int)
            Writes the text representation of an integer to the text stream.
        
            value: The integer to write.
        Write(self: IndentedTextWriter, format: str, *arg: Array[object])
            Writes out a formatted string, using the same semantics as specified.
        
            format: The formatting string to use.
            arg: The argument array to output.
        Write(self: IndentedTextWriter, format: str, arg0: object, arg1: object)
            Writes out a formatted string, using the same semantics as specified.
        
            format: The formatting string to use.
            arg0: The first object to write into the formatted string.
            arg1: The second object to write into the formatted string.
        Write(self: IndentedTextWriter, format: str, arg0: object)
            Writes out a formatted string, using the same semantics as specified.
        
            format: The formatting string.
            arg0: The object to write into the formatted string.
        Write(self: IndentedTextWriter, value: Single)
            Writes the text representation of a Single to the text stream.
        
            value: The single to write.
        Write(self: IndentedTextWriter, value: Char)
            Writes a character to the text stream.
        
            value: The character to write.
        Write(self: IndentedTextWriter, value: bool)
            Writes the text representation of a Boolean value to the text stream.
        
            value: The Boolean value to write.
        Write(self: IndentedTextWriter, s: str)
            Writes the specified string to the text stream.
        
            s: The string to write.
        Write(self: IndentedTextWriter, value: float)
            Writes the text representation of a Double to the text stream.
        
            value: The double to write.
        Write(self: IndentedTextWriter, buffer: Array[Char], index: int, count: int)
            Writes a subarray of characters to the text stream.
        
            buffer: The character array to write data from.
            index: Starting index in the buffer.
            count: The number of characters to write.
        Write(self: IndentedTextWriter, buffer: Array[Char])
            Writes a character array to the text stream.
        
            buffer: The character array to write.
        """
        pass

    def WriteLine(self, *__args):
        """
        WriteLine(self: IndentedTextWriter, value: object)
            Writes the text representation of an object, followed by a line terminator, to the text stream.
        
            value: The object to write.
        WriteLine(self: IndentedTextWriter, value: Int64)
            Writes the text representation of an 8-byte integer, followed by a line terminator, to the text 
             stream.
        
        
            value: The 8-byte integer to write.
        WriteLine(self: IndentedTextWriter, value: int)
            Writes the text representation of an integer, followed by a line terminator, to the text stream.
        
            value: The integer to write.
        WriteLine(self: IndentedTextWriter, format: str, arg0: object)
            Writes out a formatted string, followed by a line terminator, using the same semantics as 
             specified.
        
        
            format: The formatting string.
            arg0: The object to write into the formatted string.
        WriteLine(self: IndentedTextWriter, value: UInt32)
            Writes the text representation of a UInt32, followed by a line terminator, to the text stream.
        
            value: A UInt32 to output.
        WriteLine(self: IndentedTextWriter, format: str, *arg: Array[object])
            Writes out a formatted string, followed by a line terminator, using the same semantics as 
             specified.
        
        
            format: The formatting string to use.
            arg: The argument array to output.
        WriteLine(self: IndentedTextWriter, format: str, arg0: object, arg1: object)
            Writes out a formatted string, followed by a line terminator, using the same semantics as 
             specified.
        
        
            format: The formatting string to use.
            arg0: The first object to write into the formatted string.
            arg1: The second object to write into the formatted string.
        WriteLine(self: IndentedTextWriter, value: Single)
            Writes the text representation of a Single, followed by a line terminator, to the text stream.
        
            value: The single to write.
        WriteLine(self: IndentedTextWriter, value: bool)
            Writes the text representation of a Boolean, followed by a line terminator, to the text stream.
        
            value: The Boolean to write.
        WriteLine(self: IndentedTextWriter)
            Writes a line terminator.
        WriteLine(self: IndentedTextWriter, s: str)
            Writes the specified string, followed by a line terminator, to the text stream.
        
            s: The string to write.
        WriteLine(self: IndentedTextWriter, value: Char)
            Writes a character, followed by a line terminator, to the text stream.
        
            value: The character to write.
        WriteLine(self: IndentedTextWriter, value: float)
            Writes the text representation of a Double, followed by a line terminator, to the text stream.
        
            value: The double to write.
        WriteLine(self: IndentedTextWriter, buffer: Array[Char], index: int, count: int)
            Writes a subarray of characters, followed by a line terminator, to the text stream.
        
            buffer: The character array to write data from.
            index: Starting index in the buffer.
            count: The number of characters to write.
        WriteLine(self: IndentedTextWriter, buffer: Array[Char])
            Writes a character array, followed by a line terminator, to the text stream.
        
            buffer: The character array to write.
        """
        pass

    def WriteLineNoTabs(self, s):
        """
        WriteLineNoTabs(self: IndentedTextWriter, s: str)
            Writes the specified string to a line without tabs.
        
            s: The string to write.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, writer, tabString=None):
        """
        __new__(cls: type, writer: TextWriter)
        __new__(cls: type, writer: TextWriter, tabString: str)
        """
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the encoding for the text writer to use.

Get: Encoding(self: IndentedTextWriter) -> Encoding

"""

    Indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of spaces to indent.

Get: Indent(self: IndentedTextWriter) -> int

Set: Indent(self: IndentedTextWriter) = value
"""

    InnerWriter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.IO.TextWriter to use.

Get: InnerWriter(self: IndentedTextWriter) -> TextWriter

"""

    NewLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the new line character to use.

Get: NewLine(self: IndentedTextWriter) -> str

Set: NewLine(self: IndentedTextWriter) = value
"""


    CoreNewLine = None
    DefaultTabString = '    '


class LanguageOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers that indicate special features of a language.
    
    enum (flags) LanguageOptions, values: CaseInsensitive (1), None (0)
    """
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

    CaseInsensitive = None
    None = None
    value__ = None


class TempFileCollection(object, ICollection, IEnumerable, IDisposable):
    """
    Represents a collection of temporary files.
    
    TempFileCollection(tempDir: str, keepFiles: bool)
    TempFileCollection()
    TempFileCollection(tempDir: str)
    """
    def AddExtension(self, fileExtension, keepFile=None):
        """
        AddExtension(self: TempFileCollection, fileExtension: str) -> str
        
            Adds a file name with the specified file name extension to the collection.
        
            fileExtension: The file name extension for the auto-generated temporary file name to add to the collection.
            Returns: A file name with the specified extension that was just added to the collection.
        AddExtension(self: TempFileCollection, fileExtension: str, keepFile: bool) -> str
        
            Adds a file name with the specified file name extension to the collection, using the specified 
             value indicating whether the file should be deleted or retained.
        
        
            fileExtension: The file name extension for the auto-generated temporary file name to add to the collection.
            keepFile: true if the file should be kept after use; false if the file should be deleted.
            Returns: A file name with the specified extension that was just added to the collection.
        """
        pass

    def AddFile(self, fileName, keepFile):
        """
        AddFile(self: TempFileCollection, fileName: str, keepFile: bool)
            Adds the specified file to the collection, using the specified value indicating whether to keep 
             the file after the collection is disposed or when the 
             System.CodeDom.Compiler.TempFileCollection.Delete method is called.
        
        
            fileName: The name of the file to add to the collection.
            keepFile: true if the file should be kept after use; false if the file should be deleted.
        """
        pass

    def CopyTo(self, fileNames, start):
        """
        CopyTo(self: TempFileCollection, fileNames: Array[str], start: int)
            Copies the members of the collection to the specified string, beginning at the specified index.
        
            fileNames: The array of strings to copy to.
            start: The index of the array to begin copying to.
        """
        pass

    def Delete(self):
        """
        Delete(self: TempFileCollection)
            Deletes the temporary files within this collection that were not marked to be kept.
        """
        pass

    def Dispose(self, *args): #cannot find CLR method
        """
        Dispose(self: TempFileCollection, disposing: bool)
            Releases the unmanaged resources used by the System.CodeDom.Compiler.TempFileCollection and 
             optionally releases the managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: TempFileCollection) -> IEnumerator
        
            Gets an enumerator that can enumerate the members of the collection.
            Returns: An System.Collections.IEnumerator that contains the collection's members.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tempDir=None, keepFiles=None):
        """
        __new__(cls: type)
        __new__(cls: type, tempDir: str)
        __new__(cls: type, tempDir: str, keepFiles: bool)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BasePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full path to the base file name, without a file name extension, on the temporary directory path, that is used to generate temporary file names for the collection.

Get: BasePath(self: TempFileCollection) -> str

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of files in the collection.

Get: Count(self: TempFileCollection) -> int

"""

    KeepFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether to keep the files, by default, when the System.CodeDom.Compiler.TempFileCollection.Delete method is called or the collection is disposed.

Get: KeepFiles(self: TempFileCollection) -> bool

Set: KeepFiles(self: TempFileCollection) = value
"""

    TempDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the temporary directory to store the temporary files in.

Get: TempDir(self: TempFileCollection) -> str

"""



