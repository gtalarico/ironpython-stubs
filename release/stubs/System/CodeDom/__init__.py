# encoding: utf-8
# module System.CodeDom calls itself CodeDom
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CodeObject(object):
    """
    Provides a common base class for most Code Document Object Model (CodeDOM) objects.
    
    CodeObject()
    """
    UserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the user-definable data for the current object.

Get: UserData(self: CodeObject) -> IDictionary

"""



class CodeExpression(CodeObject):
    """
    Represents a code expression. This is a base class for other code expression objects that is never instantiated.
    
    CodeExpression()
    """

class CodeArgumentReferenceExpression(CodeExpression):
    """
    Represents a reference to the value of an argument passed to a method.
    
    CodeArgumentReferenceExpression()
    CodeArgumentReferenceExpression(parameterName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, parameterName=None):
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str)
        """
        pass

    ParameterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the parameter this expression references.

Get: ParameterName(self: CodeArgumentReferenceExpression) -> str

Set: ParameterName(self: CodeArgumentReferenceExpression) = value
"""



class CodeArrayCreateExpression(CodeExpression):
    """
    Represents an expression that creates an array.
    
    CodeArrayCreateExpression(createType: Type, size: int)
    CodeArrayCreateExpression()
    CodeArrayCreateExpression(createType: CodeTypeReference, *initializers: Array[CodeExpression])
    CodeArrayCreateExpression(createType: str, *initializers: Array[CodeExpression])
    CodeArrayCreateExpression(createType: Type, *initializers: Array[CodeExpression])
    CodeArrayCreateExpression(createType: CodeTypeReference, size: int)
    CodeArrayCreateExpression(createType: str, size: int)
    CodeArrayCreateExpression(createType: CodeTypeReference, size: CodeExpression)
    CodeArrayCreateExpression(createType: str, size: CodeExpression)
    CodeArrayCreateExpression(createType: Type, size: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, createType=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, createType: CodeTypeReference, *initializers: Array[CodeExpression])
        __new__(cls: type, createType: str, *initializers: Array[CodeExpression])
        __new__(cls: type, createType: Type, *initializers: Array[CodeExpression])
        __new__(cls: type, createType: CodeTypeReference, size: int)
        __new__(cls: type, createType: str, size: int)
        __new__(cls: type, createType: Type, size: int)
        __new__(cls: type, createType: CodeTypeReference, size: CodeExpression)
        __new__(cls: type, createType: str, size: CodeExpression)
        __new__(cls: type, createType: Type, size: CodeExpression)
        """
        pass

    CreateType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of array to create.

Get: CreateType(self: CodeArrayCreateExpression) -> CodeTypeReference

Set: CreateType(self: CodeArrayCreateExpression) = value
"""

    Initializers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the initializers with which to initialize the array.

Get: Initializers(self: CodeArrayCreateExpression) -> CodeExpressionCollection

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of indexes in the array.

Get: Size(self: CodeArrayCreateExpression) -> int

Set: Size(self: CodeArrayCreateExpression) = value
"""

    SizeExpression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the expression that indicates the size of the array.

Get: SizeExpression(self: CodeArrayCreateExpression) -> CodeExpression

Set: SizeExpression(self: CodeArrayCreateExpression) = value
"""



class CodeArrayIndexerExpression(CodeExpression):
    """
    Represents a reference to an index of an array.
    
    CodeArrayIndexerExpression()
    CodeArrayIndexerExpression(targetObject: CodeExpression, *indices: Array[CodeExpression])
    """
    @staticmethod # known case of __new__
    def __new__(self, targetObject=None, indices=None):
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, *indices: Array[CodeExpression])
        """
        pass

    Indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the index or indexes of the indexer expression.

Get: Indices(self: CodeArrayIndexerExpression) -> CodeExpressionCollection

"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target object of the array indexer.

Get: TargetObject(self: CodeArrayIndexerExpression) -> CodeExpression

Set: TargetObject(self: CodeArrayIndexerExpression) = value
"""



class CodeStatement(CodeObject):
    """
    Represents the abstract base class from which all code statements derive.
    
    CodeStatement()
    """
    EndDirectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.CodeDom.CodeDirectiveCollection object that contains end directives.

Get: EndDirectives(self: CodeStatement) -> CodeDirectiveCollection

"""

    LinePragma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line on which the code statement occurs.

Get: LinePragma(self: CodeStatement) -> CodeLinePragma

Set: LinePragma(self: CodeStatement) = value
"""

    StartDirectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.CodeDom.CodeDirectiveCollection object that contains start directives.

Get: StartDirectives(self: CodeStatement) -> CodeDirectiveCollection

"""



class CodeAssignStatement(CodeStatement):
    """
    Represents a simple assignment statement.
    
    CodeAssignStatement()
    CodeAssignStatement(left: CodeExpression, right: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, left=None, right=None):
        """
        __new__(cls: type)
        __new__(cls: type, left: CodeExpression, right: CodeExpression)
        """
        pass

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the expression representing the object or reference to assign to.

Get: Left(self: CodeAssignStatement) -> CodeExpression

Set: Left(self: CodeAssignStatement) = value
"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the expression representing the object or reference to assign.

Get: Right(self: CodeAssignStatement) -> CodeExpression

Set: Right(self: CodeAssignStatement) = value
"""



class CodeAttachEventStatement(CodeStatement):
    """
    Represents a statement that attaches an event-handler delegate to an event.
    
    CodeAttachEventStatement()
    CodeAttachEventStatement(eventRef: CodeEventReferenceExpression, listener: CodeExpression)
    CodeAttachEventStatement(targetObject: CodeExpression, eventName: str, listener: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, eventRef: CodeEventReferenceExpression, listener: CodeExpression)
        __new__(cls: type, targetObject: CodeExpression, eventName: str, listener: CodeExpression)
        """
        pass

    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event to attach an event-handler delegate to.

Get: Event(self: CodeAttachEventStatement) -> CodeEventReferenceExpression

Set: Event(self: CodeAttachEventStatement) = value
"""

    Listener = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the new event-handler delegate to attach to the event.

Get: Listener(self: CodeAttachEventStatement) -> CodeExpression

Set: Listener(self: CodeAttachEventStatement) = value
"""



class CodeAttributeArgument(object):
    """
    Represents an argument used in a metadata attribute declaration.
    
    CodeAttributeArgument()
    CodeAttributeArgument(value: CodeExpression)
    CodeAttributeArgument(name: str, value: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, value: CodeExpression)
        __new__(cls: type, name: str, value: CodeExpression)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the attribute.

Get: Name(self: CodeAttributeArgument) -> str

Set: Name(self: CodeAttributeArgument) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value for the attribute argument.

Get: Value(self: CodeAttributeArgument) -> CodeExpression

Set: Value(self: CodeAttributeArgument) = value
"""



class CodeAttributeArgumentCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeAttributeArgument objects.
    
    CodeAttributeArgumentCollection()
    CodeAttributeArgumentCollection(value: CodeAttributeArgumentCollection)
    CodeAttributeArgumentCollection(value: Array[CodeAttributeArgument])
    """
    def Add(self, value):
        """
        Add(self: CodeAttributeArgumentCollection, value: CodeAttributeArgument) -> int
        
            Adds the specified System.CodeDom.CodeAttributeArgument object to the collection.
        
            value: The System.CodeDom.CodeAttributeArgument object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeAttributeArgumentCollection, value: CodeAttributeArgumentCollection)
            Copies the contents of another System.CodeDom.CodeAttributeArgumentCollection object to the end 
             of the collection.
        
        
            value: A System.CodeDom.CodeAttributeArgumentCollection that contains the objects to add to the 
             collection.
        
        AddRange(self: CodeAttributeArgumentCollection, value: Array[CodeAttributeArgument])
            Copies the elements of the specified System.CodeDom.CodeAttributeArgument array to the end of 
             the collection.
        
        
            value: An array of type System.CodeDom.CodeAttributeArgument that contains the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeAttributeArgumentCollection, value: CodeAttributeArgument) -> bool
        
            Gets a value that indicates whether the collection contains the specified 
             System.CodeDom.CodeAttributeArgument object.
        
        
            value: The System.CodeDom.CodeAttributeArgument object to locate in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeAttributeArgumentCollection, array: Array[CodeAttributeArgument], index: int)
            Copies the collection objects to a one-dimensional System.Array instance beginning at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeAttributeArgumentCollection, value: CodeAttributeArgument) -> int
        
            Gets the index of the specified System.CodeDom.CodeAttributeArgument object in the collection, 
             if it exists in the collection.
        
        
            value: The System.CodeDom.CodeAttributeArgument object to locate in the collection.
            Returns: The index of the specified object, if found, in the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeAttributeArgumentCollection, index: int, value: CodeAttributeArgument)
            Inserts the specified System.CodeDom.CodeAttributeArgument object into the collection at the 
             specified index.
        
        
            index: The zero-based index where the specified object should be inserted.
            value: The System.CodeDom.CodeAttributeArgument object to insert.
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
        Remove(self: CodeAttributeArgumentCollection, value: CodeAttributeArgument)
            Removes the specified System.CodeDom.CodeAttributeArgument object from the collection.
        
            value: The System.CodeDom.CodeAttributeArgument object to remove from the collection.
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
        __new__(cls: type, value: CodeAttributeArgumentCollection)
        __new__(cls: type, value: Array[CodeAttributeArgument])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeAttributeDeclaration(object):
    """
    Represents an attribute declaration.
    
    CodeAttributeDeclaration(attributeType: CodeTypeReference, *arguments: Array[CodeAttributeArgument])
    CodeAttributeDeclaration()
    CodeAttributeDeclaration(name: str)
    CodeAttributeDeclaration(name: str, *arguments: Array[CodeAttributeArgument])
    CodeAttributeDeclaration(attributeType: CodeTypeReference)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, *arguments: Array[CodeAttributeArgument])
        __new__(cls: type, attributeType: CodeTypeReference)
        __new__(cls: type, attributeType: CodeTypeReference, *arguments: Array[CodeAttributeArgument])
        """
        pass

    Arguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the arguments for the attribute.

Get: Arguments(self: CodeAttributeDeclaration) -> CodeAttributeArgumentCollection

"""

    AttributeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the code type reference for the code attribute declaration.

Get: AttributeType(self: CodeAttributeDeclaration) -> CodeTypeReference

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the attribute being declared.

Get: Name(self: CodeAttributeDeclaration) -> str

Set: Name(self: CodeAttributeDeclaration) = value
"""



class CodeAttributeDeclarationCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeAttributeDeclaration objects.
    
    CodeAttributeDeclarationCollection()
    CodeAttributeDeclarationCollection(value: CodeAttributeDeclarationCollection)
    CodeAttributeDeclarationCollection(value: Array[CodeAttributeDeclaration])
    """
    def Add(self, value):
        """
        Add(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclaration) -> int
        
            Adds a System.CodeDom.CodeAttributeDeclaration object with the specified value to the collection.
        
            value: The System.CodeDom.CodeAttributeDeclaration object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclarationCollection)
            Copies the contents of another System.CodeDom.CodeAttributeDeclarationCollection object to the 
             end of the collection.
        
        
            value: A System.CodeDom.CodeAttributeDeclarationCollection that contains the objects to add to the 
             collection.
        
        AddRange(self: CodeAttributeDeclarationCollection, value: Array[CodeAttributeDeclaration])
            Copies the elements of the specified System.CodeDom.CodeAttributeDeclaration array to the end of 
             the collection.
        
        
            value: An array of type System.CodeDom.CodeAttributeDeclaration that contains the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclaration) -> bool
        
            Gets or sets a value that indicates whether the collection contains the specified 
             System.CodeDom.CodeAttributeDeclaration object.
        
        
            value: The System.CodeDom.CodeAttributeDeclaration object to locate.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeAttributeDeclarationCollection, array: Array[CodeAttributeDeclaration], index: int)
            Copies the collection objects to a one-dimensional System.Array instance beginning at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclaration) -> int
        
            Gets the index of the specified System.CodeDom.CodeAttributeDeclaration object in the 
             collection, if it exists in the collection.
        
        
            value: The System.CodeDom.CodeAttributeDeclaration object to locate in the collection.
            Returns: The index in the collection of the specified object, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeAttributeDeclarationCollection, index: int, value: CodeAttributeDeclaration)
            Inserts the specified System.CodeDom.CodeAttributeDeclaration object into the collection at the 
             specified index.
        
        
            index: The zero-based index where the specified object should be inserted.
            value: The System.CodeDom.CodeAttributeDeclaration object to insert.
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
        Remove(self: CodeAttributeDeclarationCollection, value: CodeAttributeDeclaration)
            Removes the specified System.CodeDom.CodeAttributeDeclaration object from the collection.
        
            value: The System.CodeDom.CodeAttributeDeclaration object to remove from the collection.
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
        __new__(cls: type, value: CodeAttributeDeclarationCollection)
        __new__(cls: type, value: Array[CodeAttributeDeclaration])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeBaseReferenceExpression(CodeExpression):
    """
    Represents a reference to the base class.
    
    CodeBaseReferenceExpression()
    """

class CodeBinaryOperatorExpression(CodeExpression):
    """
    Represents an expression that consists of a binary operation between two expressions.
    
    CodeBinaryOperatorExpression()
    CodeBinaryOperatorExpression(left: CodeExpression, op: CodeBinaryOperatorType, right: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, left=None, op=None, right=None):
        """
        __new__(cls: type)
        __new__(cls: type, left: CodeExpression, op: CodeBinaryOperatorType, right: CodeExpression)
        """
        pass

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the code expression on the left of the operator.

Get: Left(self: CodeBinaryOperatorExpression) -> CodeExpression

Set: Left(self: CodeBinaryOperatorExpression) = value
"""

    Operator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the operator in the binary operator expression.

Get: Operator(self: CodeBinaryOperatorExpression) -> CodeBinaryOperatorType

Set: Operator(self: CodeBinaryOperatorExpression) = value
"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the code expression on the right of the operator.

Get: Right(self: CodeBinaryOperatorExpression) -> CodeExpression

Set: Right(self: CodeBinaryOperatorExpression) = value
"""



class CodeBinaryOperatorType(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers for supported binary operators.
    
    enum CodeBinaryOperatorType, values: Add (0), Assign (5), BitwiseAnd (10), BitwiseOr (9), BooleanAnd (12), BooleanOr (11), Divide (3), GreaterThan (15), GreaterThanOrEqual (16), IdentityEquality (7), IdentityInequality (6), LessThan (13), LessThanOrEqual (14), Modulus (4), Multiply (2), Subtract (1), ValueEquality (8)
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

    Add = None
    Assign = None
    BitwiseAnd = None
    BitwiseOr = None
    BooleanAnd = None
    BooleanOr = None
    Divide = None
    GreaterThan = None
    GreaterThanOrEqual = None
    IdentityEquality = None
    IdentityInequality = None
    LessThan = None
    LessThanOrEqual = None
    Modulus = None
    Multiply = None
    Subtract = None
    ValueEquality = None
    value__ = None


class CodeCastExpression(CodeExpression):
    """
    Represents an expression cast to a data type or interface.
    
    CodeCastExpression()
    CodeCastExpression(targetType: CodeTypeReference, expression: CodeExpression)
    CodeCastExpression(targetType: str, expression: CodeExpression)
    CodeCastExpression(targetType: Type, expression: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, targetType=None, expression=None):
        """
        __new__(cls: type)
        __new__(cls: type, targetType: CodeTypeReference, expression: CodeExpression)
        __new__(cls: type, targetType: str, expression: CodeExpression)
        __new__(cls: type, targetType: Type, expression: CodeExpression)
        """
        pass

    Expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the expression to cast.

Get: Expression(self: CodeCastExpression) -> CodeExpression

Set: Expression(self: CodeCastExpression) = value
"""

    TargetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the destination type of the cast.

Get: TargetType(self: CodeCastExpression) -> CodeTypeReference

Set: TargetType(self: CodeCastExpression) = value
"""



class CodeCatchClause(object):
    """
    Represents a catch exception block of a try/catch statement.
    
    CodeCatchClause()
    CodeCatchClause(localName: str)
    CodeCatchClause(localName: str, catchExceptionType: CodeTypeReference)
    CodeCatchClause(localName: str, catchExceptionType: CodeTypeReference, *statements: Array[CodeStatement])
    """
    @staticmethod # known case of __new__
    def __new__(self, localName=None, catchExceptionType=None, statements=None):
        """
        __new__(cls: type)
        __new__(cls: type, localName: str)
        __new__(cls: type, localName: str, catchExceptionType: CodeTypeReference)
        __new__(cls: type, localName: str, catchExceptionType: CodeTypeReference, *statements: Array[CodeStatement])
        """
        pass

    CatchExceptionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the exception to handle with the catch block.

Get: CatchExceptionType(self: CodeCatchClause) -> CodeTypeReference

Set: CatchExceptionType(self: CodeCatchClause) = value
"""

    LocalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the variable name of the exception that the catch clause handles.

Get: LocalName(self: CodeCatchClause) -> str

Set: LocalName(self: CodeCatchClause) = value
"""

    Statements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the statements within the catch block.

Get: Statements(self: CodeCatchClause) -> CodeStatementCollection

"""



class CodeCatchClauseCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeCatchClause objects.
    
    CodeCatchClauseCollection()
    CodeCatchClauseCollection(value: CodeCatchClauseCollection)
    CodeCatchClauseCollection(value: Array[CodeCatchClause])
    """
    def Add(self, value):
        """
        Add(self: CodeCatchClauseCollection, value: CodeCatchClause) -> int
        
            Adds the specified System.CodeDom.CodeCatchClause object to the collection.
        
            value: The System.CodeDom.CodeCatchClause object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeCatchClauseCollection, value: CodeCatchClauseCollection)
            Copies the contents of another System.CodeDom.CodeCatchClauseCollection object to the end of the 
             collection.
        
        
            value: A System.CodeDom.CodeCatchClauseCollection that contains the objects to add to the collection.
        AddRange(self: CodeCatchClauseCollection, value: Array[CodeCatchClause])
            Copies the elements of the specified System.CodeDom.CodeCatchClause array to the end of the 
             collection.
        
        
            value: An array of type System.CodeDom.CodeCatchClause that contains the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeCatchClauseCollection, value: CodeCatchClause) -> bool
        
            Gets a value that indicates whether the collection contains the specified 
             System.CodeDom.CodeCatchClause object.
        
        
            value: The System.CodeDom.CodeCatchClause object to locate in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeCatchClauseCollection, array: Array[CodeCatchClause], index: int)
            Copies the collection objects to a one-dimensional System.Array instance beginning at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeCatchClauseCollection, value: CodeCatchClause) -> int
        
            Gets the index of the specified System.CodeDom.CodeCatchClause object in the collection, if it 
             exists in the collection.
        
        
            value: The System.CodeDom.CodeCatchClause object to locate in the collection.
            Returns: The index of the specified object, if found, in the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeCatchClauseCollection, index: int, value: CodeCatchClause)
            Inserts the specified System.CodeDom.CodeCatchClause object into the collection at the specified 
             index.
        
        
            index: The zero-based index where the specified object should be inserted.
            value: The System.CodeDom.CodeCatchClause object to insert.
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
        Remove(self: CodeCatchClauseCollection, value: CodeCatchClause)
            Removes the specified System.CodeDom.CodeCatchClause object from the collection.
        
            value: The System.CodeDom.CodeCatchClause object to remove from the collection.
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
        __new__(cls: type, value: CodeCatchClauseCollection)
        __new__(cls: type, value: Array[CodeCatchClause])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeDirective(CodeObject):
    """
    Serves as the base class for code directive classes.
    
    CodeDirective()
    """

class CodeChecksumPragma(CodeDirective):
    """
    Represents a code checksum pragma code entity.
    
    CodeChecksumPragma()
    CodeChecksumPragma(fileName: str, checksumAlgorithmId: Guid, checksumData: Array[Byte])
    """
    @staticmethod # known case of __new__
    def __new__(self, fileName=None, checksumAlgorithmId=None, checksumData=None):
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str, checksumAlgorithmId: Guid, checksumData: Array[Byte])
        """
        pass

    ChecksumAlgorithmId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a GUID that identifies the checksum algorithm to use.

Get: ChecksumAlgorithmId(self: CodeChecksumPragma) -> Guid

Set: ChecksumAlgorithmId(self: CodeChecksumPragma) = value
"""

    ChecksumData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the data for the checksum calculation.

Get: ChecksumData(self: CodeChecksumPragma) -> Array[Byte]

Set: ChecksumData(self: CodeChecksumPragma) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the path to the checksum file.

Get: FileName(self: CodeChecksumPragma) -> str

Set: FileName(self: CodeChecksumPragma) = value
"""



class CodeComment(CodeObject):
    """
    Represents a comment.
    
    CodeComment()
    CodeComment(text: str)
    CodeComment(text: str, docComment: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, text=None, docComment=None):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, docComment: bool)
        """
        pass

    DocComment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the comment is a documentation comment.

Get: DocComment(self: CodeComment) -> bool

Set: DocComment(self: CodeComment) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text of the comment.

Get: Text(self: CodeComment) -> str

Set: Text(self: CodeComment) = value
"""



class CodeCommentStatement(CodeStatement):
    """
    Represents a statement consisting of a single comment.
    
    CodeCommentStatement()
    CodeCommentStatement(comment: CodeComment)
    CodeCommentStatement(text: str)
    CodeCommentStatement(text: str, docComment: bool)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, comment: CodeComment)
        __new__(cls: type, text: str)
        __new__(cls: type, text: str, docComment: bool)
        """
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the contents of the comment.

Get: Comment(self: CodeCommentStatement) -> CodeComment

Set: Comment(self: CodeCommentStatement) = value
"""



class CodeCommentStatementCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeCommentStatement objects.
    
    CodeCommentStatementCollection()
    CodeCommentStatementCollection(value: CodeCommentStatementCollection)
    CodeCommentStatementCollection(value: Array[CodeCommentStatement])
    """
    def Add(self, value):
        """
        Add(self: CodeCommentStatementCollection, value: CodeCommentStatement) -> int
        
            Adds the specified System.CodeDom.CodeCommentStatement object to the collection.
        
            value: The System.CodeDom.CodeCommentStatement object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeCommentStatementCollection, value: CodeCommentStatementCollection)
            Copies the contents of another System.CodeDom.CodeCommentStatementCollection object to the end 
             of the collection.
        
        
            value: A System.CodeDom.CodeCommentStatementCollection that contains the objects to add to the 
             collection.
        
        AddRange(self: CodeCommentStatementCollection, value: Array[CodeCommentStatement])
            Copies the elements of the specified System.CodeDom.CodeCommentStatement array to the end of the 
             collection.
        
        
            value: An array of type System.CodeDom.CodeCommentStatement that contains the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeCommentStatementCollection, value: CodeCommentStatement) -> bool
        
            Gets a value that indicates whether the collection contains the specified 
             System.CodeDom.CodeCommentStatement object.
        
        
            value: The System.CodeDom.CodeCommentStatement to search for in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeCommentStatementCollection, array: Array[CodeCommentStatement], index: int)
            Copies the collection objects to the specified one-dimensional System.Array beginning at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeCommentStatementCollection, value: CodeCommentStatement) -> int
        
            Gets the index of the specified System.CodeDom.CodeCommentStatement object in the collection, if 
             it exists in the collection.
        
        
            value: The System.CodeDom.CodeCommentStatement object to locate.
            Returns: The index of the specified object, if found, in the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeCommentStatementCollection, index: int, value: CodeCommentStatement)
            Inserts a System.CodeDom.CodeCommentStatement object into the collection at the specified index.
        
            index: The zero-based index where the item should be inserted.
            value: The System.CodeDom.CodeCommentStatement object to insert.
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
        Remove(self: CodeCommentStatementCollection, value: CodeCommentStatement)
            Removes the specified System.CodeDom.CodeCommentStatement object from the collection.
        
            value: The System.CodeDom.CodeCommentStatement object to remove from the collection.
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
        __new__(cls: type, value: CodeCommentStatementCollection)
        __new__(cls: type, value: Array[CodeCommentStatement])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeCompileUnit(CodeObject):
    """
    Provides a container for a CodeDOM program graph.
    
    CodeCompileUnit()
    """
    AssemblyCustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of custom attributes for the generated assembly.

Get: AssemblyCustomAttributes(self: CodeCompileUnit) -> CodeAttributeDeclarationCollection

"""

    EndDirectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.CodeDom.CodeDirectiveCollection object containing end directives.

Get: EndDirectives(self: CodeCompileUnit) -> CodeDirectiveCollection

"""

    Namespaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of namespaces.

Get: Namespaces(self: CodeCompileUnit) -> CodeNamespaceCollection

"""

    ReferencedAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the referenced assemblies.

Get: ReferencedAssemblies(self: CodeCompileUnit) -> StringCollection

"""

    StartDirectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.CodeDom.CodeDirectiveCollection object containing start directives.

Get: StartDirectives(self: CodeCompileUnit) -> CodeDirectiveCollection

"""



class CodeConditionStatement(CodeStatement):
    """
    Represents a conditional branch statement, typically represented as an if statement.
    
    CodeConditionStatement()
    CodeConditionStatement(condition: CodeExpression, *trueStatements: Array[CodeStatement])
    CodeConditionStatement(condition: CodeExpression, trueStatements: Array[CodeStatement], falseStatements: Array[CodeStatement])
    """
    @staticmethod # known case of __new__
    def __new__(self, condition=None, trueStatements=None, falseStatements=None):
        """
        __new__(cls: type)
        __new__(cls: type, condition: CodeExpression, *trueStatements: Array[CodeStatement])
        __new__(cls: type, condition: CodeExpression, trueStatements: Array[CodeStatement], falseStatements: Array[CodeStatement])
        """
        pass

    Condition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the expression to evaluate true or false.

Get: Condition(self: CodeConditionStatement) -> CodeExpression

Set: Condition(self: CodeConditionStatement) = value
"""

    FalseStatements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of statements to execute if the conditional expression evaluates to false.

Get: FalseStatements(self: CodeConditionStatement) -> CodeStatementCollection

"""

    TrueStatements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of statements to execute if the conditional expression evaluates to true.

Get: TrueStatements(self: CodeConditionStatement) -> CodeStatementCollection

"""



class CodeTypeMember(CodeObject):
    """
    Provides a base class for a member of a type. Type members include fields, methods, properties, constructors and nested types.
    
    CodeTypeMember()
    """
    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the attributes of the member.

Get: Attributes(self: CodeTypeMember) -> MemberAttributes

Set: Attributes(self: CodeTypeMember) = value
"""

    Comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of comments for the type member.

Get: Comments(self: CodeTypeMember) -> CodeCommentStatementCollection

"""

    CustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the custom attributes of the member.

Get: CustomAttributes(self: CodeTypeMember) -> CodeAttributeDeclarationCollection

Set: CustomAttributes(self: CodeTypeMember) = value
"""

    EndDirectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end directives for the member.

Get: EndDirectives(self: CodeTypeMember) -> CodeDirectiveCollection

"""

    LinePragma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line on which the type member statement occurs.

Get: LinePragma(self: CodeTypeMember) -> CodeLinePragma

Set: LinePragma(self: CodeTypeMember) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the member.

Get: Name(self: CodeTypeMember) -> str

Set: Name(self: CodeTypeMember) = value
"""

    StartDirectives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the start directives for the member.

Get: StartDirectives(self: CodeTypeMember) -> CodeDirectiveCollection

"""



class CodeMemberMethod(CodeTypeMember):
    """
    Represents a declaration for a method of a type.
    
    CodeMemberMethod()
    """
    ImplementationTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the data types of the interfaces implemented by this method, unless it is a private method implementation, which is indicated by the System.CodeDom.CodeMemberMethod.PrivateImplementationType property.

Get: ImplementationTypes(self: CodeMemberMethod) -> CodeTypeReferenceCollection

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parameter declarations for the method.

Get: Parameters(self: CodeMemberMethod) -> CodeParameterDeclarationExpressionCollection

"""

    PrivateImplementationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type of the interface this method, if private, implements a method of, if any.

Get: PrivateImplementationType(self: CodeMemberMethod) -> CodeTypeReference

Set: PrivateImplementationType(self: CodeMemberMethod) = value
"""

    ReturnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type of the return value of the method.

Get: ReturnType(self: CodeMemberMethod) -> CodeTypeReference

Set: ReturnType(self: CodeMemberMethod) = value
"""

    ReturnTypeCustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the custom attributes of the return type of the method.

Get: ReturnTypeCustomAttributes(self: CodeMemberMethod) -> CodeAttributeDeclarationCollection

"""

    Statements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the statements within the method.

Get: Statements(self: CodeMemberMethod) -> CodeStatementCollection

"""

    TypeParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type parameters for the current generic method.

Get: TypeParameters(self: CodeMemberMethod) -> CodeTypeParameterCollection

"""


    PopulateImplementationTypes = None
    PopulateParameters = None
    PopulateStatements = None


class CodeConstructor(CodeMemberMethod):
    """
    Represents a declaration for an instance constructor of a type.
    
    CodeConstructor()
    """
    BaseConstructorArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of base constructor arguments.

Get: BaseConstructorArgs(self: CodeConstructor) -> CodeExpressionCollection

"""

    ChainedConstructorArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of chained constructor arguments.

Get: ChainedConstructorArgs(self: CodeConstructor) -> CodeExpressionCollection

"""



class CodeDefaultValueExpression(CodeExpression):
    """
    Represents a reference to a default value.
    
    CodeDefaultValueExpression()
    CodeDefaultValueExpression(type: CodeTypeReference)
    """
    @staticmethod # known case of __new__
    def __new__(self, type=None):
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type reference for a default value.

Get: Type(self: CodeDefaultValueExpression) -> CodeTypeReference

Set: Type(self: CodeDefaultValueExpression) = value
"""



class CodeDelegateCreateExpression(CodeExpression):
    """
    Represents an expression that creates a delegate.
    
    CodeDelegateCreateExpression()
    CodeDelegateCreateExpression(delegateType: CodeTypeReference, targetObject: CodeExpression, methodName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, delegateType=None, targetObject=None, methodName=None):
        """
        __new__(cls: type)
        __new__(cls: type, delegateType: CodeTypeReference, targetObject: CodeExpression, methodName: str)
        """
        pass

    DelegateType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type of the delegate.

Get: DelegateType(self: CodeDelegateCreateExpression) -> CodeTypeReference

Set: DelegateType(self: CodeDelegateCreateExpression) = value
"""

    MethodName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the event handler method.

Get: MethodName(self: CodeDelegateCreateExpression) -> str

Set: MethodName(self: CodeDelegateCreateExpression) = value
"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object that contains the event-handler method.

Get: TargetObject(self: CodeDelegateCreateExpression) -> CodeExpression

Set: TargetObject(self: CodeDelegateCreateExpression) = value
"""



class CodeDelegateInvokeExpression(CodeExpression):
    """
    Represents an expression that raises an event.
    
    CodeDelegateInvokeExpression()
    CodeDelegateInvokeExpression(targetObject: CodeExpression)
    CodeDelegateInvokeExpression(targetObject: CodeExpression, *parameters: Array[CodeExpression])
    """
    @staticmethod # known case of __new__
    def __new__(self, targetObject=None, parameters=None):
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression)
        __new__(cls: type, targetObject: CodeExpression, *parameters: Array[CodeExpression])
        """
        pass

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the parameters to pass to the event handling methods attached to the event.

Get: Parameters(self: CodeDelegateInvokeExpression) -> CodeExpressionCollection

"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event to invoke.

Get: TargetObject(self: CodeDelegateInvokeExpression) -> CodeExpression

Set: TargetObject(self: CodeDelegateInvokeExpression) = value
"""



class CodeDirectionExpression(CodeExpression):
    """
    Represents an expression used as a method invoke parameter along with a reference direction indicator.
    
    CodeDirectionExpression()
    CodeDirectionExpression(direction: FieldDirection, expression: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, direction=None, expression=None):
        """
        __new__(cls: type)
        __new__(cls: type, direction: FieldDirection, expression: CodeExpression)
        """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field direction for this direction expression.

Get: Direction(self: CodeDirectionExpression) -> FieldDirection

Set: Direction(self: CodeDirectionExpression) = value
"""

    Expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the code expression to represent.

Get: Expression(self: CodeDirectionExpression) -> CodeExpression

Set: Expression(self: CodeDirectionExpression) = value
"""



class CodeDirectiveCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeDirective objects.
    
    CodeDirectiveCollection()
    CodeDirectiveCollection(value: CodeDirectiveCollection)
    CodeDirectiveCollection(value: Array[CodeDirective])
    """
    def Add(self, value):
        """
        Add(self: CodeDirectiveCollection, value: CodeDirective) -> int
        
            Adds the specified System.CodeDom.CodeDirective object to the collection.
        
            value: The System.CodeDom.CodeDirective object to add.
            Returns: The index position at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeDirectiveCollection, value: CodeDirectiveCollection)
            Adds the contents of the specified System.CodeDom.CodeDirectiveCollection object to the end of 
             the collection.
        
        
            value: A System.CodeDom.CodeDirectiveCollection object containing the System.CodeDom.CodeDirective 
             objects to add to the collection.
        
        AddRange(self: CodeDirectiveCollection, value: Array[CodeDirective])
            Adds an array of System.CodeDom.CodeDirective objects to the end of the collection.
        
            value: An array of System.CodeDom.CodeDirective objects to add to the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeDirectiveCollection, value: CodeDirective) -> bool
        
            Gets a value indicating whether the collection contains the specified 
             System.CodeDom.CodeDirective object.
        
        
            value: The System.CodeDom.CodeDirective object to search for in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeDirectiveCollection, array: Array[CodeDirective], index: int)
            Copies the contents of the collection to a one-dimensional array beginning at the specified 
             index.
        
        
            array: An array of type System.CodeDom.CodeDirective that is the destination of the values copied from 
             the collection.
        
            index: The index in the array at which to begin inserting collection objects.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeDirectiveCollection, value: CodeDirective) -> int
        
            Gets the index in the collection of the specified System.CodeDom.CodeDirective object, if it 
             exists in the collection.
        
        
            value: The System.CodeDom.CodeDirective object to locate in the collection.
            Returns: The index position in the collection of the specified object, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeDirectiveCollection, index: int, value: CodeDirective)
            Inserts the specified System.CodeDom.CodeDirective object into the collection at the specified 
             index.
        
        
            index: The zero-based index position where the specified object should be inserted.
            value: The System.CodeDom.CodeDirective object to insert.
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
        Remove(self: CodeDirectiveCollection, value: CodeDirective)
            Removes the specified System.CodeDom.CodeDirective object from the collection.
        
            value: The System.CodeDom.CodeDirective object to remove from the collection.
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
        __new__(cls: type, value: CodeDirectiveCollection)
        __new__(cls: type, value: Array[CodeDirective])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeEntryPointMethod(CodeMemberMethod):
    """
    Represents the entry point method of an executable.
    
    CodeEntryPointMethod()
    """

class CodeEventReferenceExpression(CodeExpression):
    """
    Represents a reference to an event.
    
    CodeEventReferenceExpression()
    CodeEventReferenceExpression(targetObject: CodeExpression, eventName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, targetObject=None, eventName=None):
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, eventName: str)
        """
        pass

    EventName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the event.

Get: EventName(self: CodeEventReferenceExpression) -> str

Set: EventName(self: CodeEventReferenceExpression) = value
"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object that contains the event.

Get: TargetObject(self: CodeEventReferenceExpression) -> CodeExpression

Set: TargetObject(self: CodeEventReferenceExpression) = value
"""



class CodeExpressionCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeExpression objects.
    
    CodeExpressionCollection()
    CodeExpressionCollection(value: CodeExpressionCollection)
    CodeExpressionCollection(value: Array[CodeExpression])
    """
    def Add(self, value):
        """
        Add(self: CodeExpressionCollection, value: CodeExpression) -> int
        
            Adds the specified System.CodeDom.CodeExpression object to the collection.
        
            value: The System.CodeDom.CodeExpression object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeExpressionCollection, value: CodeExpressionCollection)
            Copies the contents of another System.CodeDom.CodeExpressionCollection object to the end of the 
             collection.
        
        
            value: A System.CodeDom.CodeExpressionCollection that contains the objects to add to the collection.
        AddRange(self: CodeExpressionCollection, value: Array[CodeExpression])
            Copies the elements of the specified array to the end of the collection.
        
            value: An array of type System.CodeDom.CodeExpression that contains the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeExpressionCollection, value: CodeExpression) -> bool
        
            Gets a value that indicates whether the collection contains the specified 
             System.CodeDom.CodeExpression object.
        
        
            value: The System.CodeDom.CodeExpression object to locate in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeExpressionCollection, array: Array[CodeExpression], index: int)
            Copies the collection objects to a one-dimensional System.Array instance beginning at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeExpressionCollection, value: CodeExpression) -> int
        
            Gets the index of the specified System.CodeDom.CodeExpression object in the collection, if it 
             exists in the collection.
        
        
            value: The System.CodeDom.CodeExpression object to locate in the collection.
            Returns: The index of the specified object, if found, in the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeExpressionCollection, index: int, value: CodeExpression)
            Inserts the specified System.CodeDom.CodeExpression object into the collection at the specified 
             index.
        
        
            index: The zero-based index where the specified object should be inserted.
            value: The System.CodeDom.CodeExpression object to insert.
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
        Remove(self: CodeExpressionCollection, value: CodeExpression)
            Removes the specified System.CodeDom.CodeExpression object from the collection.
        
            value: The System.CodeDom.CodeExpression object to remove from the collection.
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
        __new__(cls: type, value: CodeExpressionCollection)
        __new__(cls: type, value: Array[CodeExpression])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeExpressionStatement(CodeStatement):
    """
    Represents a statement that consists of a single expression.
    
    CodeExpressionStatement()
    CodeExpressionStatement(expression: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, expression=None):
        """
        __new__(cls: type)
        __new__(cls: type, expression: CodeExpression)
        """
        pass

    Expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the expression for the statement.

Get: Expression(self: CodeExpressionStatement) -> CodeExpression

Set: Expression(self: CodeExpressionStatement) = value
"""



class CodeFieldReferenceExpression(CodeExpression):
    """
    Represents a reference to a field.
    
    CodeFieldReferenceExpression()
    CodeFieldReferenceExpression(targetObject: CodeExpression, fieldName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, targetObject=None, fieldName=None):
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, fieldName: str)
        """
        pass

    FieldName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the field to reference.

Get: FieldName(self: CodeFieldReferenceExpression) -> str

Set: FieldName(self: CodeFieldReferenceExpression) = value
"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object that contains the field to reference.

Get: TargetObject(self: CodeFieldReferenceExpression) -> CodeExpression

Set: TargetObject(self: CodeFieldReferenceExpression) = value
"""



class CodeGotoStatement(CodeStatement):
    """
    Represents a goto statement.
    
    CodeGotoStatement()
    CodeGotoStatement(label: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, label=None):
        """
        __new__(cls: type)
        __new__(cls: type, label: str)
        """
        pass

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the label at which to continue program execution.

Get: Label(self: CodeGotoStatement) -> str

Set: Label(self: CodeGotoStatement) = value
"""



class CodeIndexerExpression(CodeExpression):
    """
    Represents a reference to an indexer property of an object.
    
    CodeIndexerExpression()
    CodeIndexerExpression(targetObject: CodeExpression, *indices: Array[CodeExpression])
    """
    @staticmethod # known case of __new__
    def __new__(self, targetObject=None, indices=None):
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, *indices: Array[CodeExpression])
        """
        pass

    Indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of indexes of the indexer expression.

Get: Indices(self: CodeIndexerExpression) -> CodeExpressionCollection

"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the target object that can be indexed.

Get: TargetObject(self: CodeIndexerExpression) -> CodeExpression

Set: TargetObject(self: CodeIndexerExpression) = value
"""



class CodeIterationStatement(CodeStatement):
    """
    Represents a for statement, or a loop through a block of statements, using a test expression as a condition for continuing to loop.
    
    CodeIterationStatement()
    CodeIterationStatement(initStatement: CodeStatement, testExpression: CodeExpression, incrementStatement: CodeStatement, *statements: Array[CodeStatement])
    """
    @staticmethod # known case of __new__
    def __new__(self, initStatement=None, testExpression=None, incrementStatement=None, statements=None):
        """
        __new__(cls: type)
        __new__(cls: type, initStatement: CodeStatement, testExpression: CodeExpression, incrementStatement: CodeStatement, *statements: Array[CodeStatement])
        """
        pass

    IncrementStatement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the statement that is called after each loop cycle.

Get: IncrementStatement(self: CodeIterationStatement) -> CodeStatement

Set: IncrementStatement(self: CodeIterationStatement) = value
"""

    InitStatement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the loop initialization statement.

Get: InitStatement(self: CodeIterationStatement) -> CodeStatement

Set: InitStatement(self: CodeIterationStatement) = value
"""

    Statements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of statements to be executed within the loop.

Get: Statements(self: CodeIterationStatement) -> CodeStatementCollection

"""

    TestExpression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the expression to test as the condition that continues the loop.

Get: TestExpression(self: CodeIterationStatement) -> CodeExpression

Set: TestExpression(self: CodeIterationStatement) = value
"""



class CodeLabeledStatement(CodeStatement):
    """
    Represents a labeled statement or a stand-alone label.
    
    CodeLabeledStatement()
    CodeLabeledStatement(label: str)
    CodeLabeledStatement(label: str, statement: CodeStatement)
    """
    @staticmethod # known case of __new__
    def __new__(self, label=None, statement=None):
        """
        __new__(cls: type)
        __new__(cls: type, label: str)
        __new__(cls: type, label: str, statement: CodeStatement)
        """
        pass

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the label.

Get: Label(self: CodeLabeledStatement) -> str

Set: Label(self: CodeLabeledStatement) = value
"""

    Statement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the optional associated statement.

Get: Statement(self: CodeLabeledStatement) -> CodeStatement

Set: Statement(self: CodeLabeledStatement) = value
"""



class CodeLinePragma(object):
    """
    Represents a specific location within a specific file.
    
    CodeLinePragma()
    CodeLinePragma(fileName: str, lineNumber: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, fileName=None, lineNumber=None):
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str, lineNumber: int)
        """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the associated file.

Get: FileName(self: CodeLinePragma) -> str

Set: FileName(self: CodeLinePragma) = value
"""

    LineNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line number of the associated reference.

Get: LineNumber(self: CodeLinePragma) -> int

Set: LineNumber(self: CodeLinePragma) = value
"""



class CodeMemberEvent(CodeTypeMember):
    """
    Represents a declaration for an event of a type.
    
    CodeMemberEvent()
    """
    ImplementationTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type that the member event implements.

Get: ImplementationTypes(self: CodeMemberEvent) -> CodeTypeReferenceCollection

"""

    PrivateImplementationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the privately implemented data type, if any.

Get: PrivateImplementationType(self: CodeMemberEvent) -> CodeTypeReference

Set: PrivateImplementationType(self: CodeMemberEvent) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type of the delegate type that handles the event.

Get: Type(self: CodeMemberEvent) -> CodeTypeReference

Set: Type(self: CodeMemberEvent) = value
"""



class CodeMemberField(CodeTypeMember):
    """
    Represents a declaration for a field of a type.
    
    CodeMemberField()
    CodeMemberField(type: CodeTypeReference, name: str)
    CodeMemberField(type: str, name: str)
    CodeMemberField(type: Type, name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, type=None, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference, name: str)
        __new__(cls: type, type: str, name: str)
        __new__(cls: type, type: Type, name: str)
        """
        pass

    InitExpression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initialization expression for the field.

Get: InitExpression(self: CodeMemberField) -> CodeExpression

Set: InitExpression(self: CodeMemberField) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the field.

Get: Type(self: CodeMemberField) -> CodeTypeReference

Set: Type(self: CodeMemberField) = value
"""



class CodeMemberProperty(CodeTypeMember):
    """
    Represents a declaration for a property of a type.
    
    CodeMemberProperty()
    """
    GetStatements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of get statements for the property.

Get: GetStatements(self: CodeMemberProperty) -> CodeStatementCollection

"""

    HasGet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the property has a get method accessor.

Get: HasGet(self: CodeMemberProperty) -> bool

Set: HasGet(self: CodeMemberProperty) = value
"""

    HasSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the property has a set method accessor.

Get: HasSet(self: CodeMemberProperty) -> bool

Set: HasSet(self: CodeMemberProperty) = value
"""

    ImplementationTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the data types of any interfaces that the property implements.

Get: ImplementationTypes(self: CodeMemberProperty) -> CodeTypeReferenceCollection

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of declaration expressions for the property.

Get: Parameters(self: CodeMemberProperty) -> CodeParameterDeclarationExpressionCollection

"""

    PrivateImplementationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type of the interface, if any, this property, if private, implements.

Get: PrivateImplementationType(self: CodeMemberProperty) -> CodeTypeReference

Set: PrivateImplementationType(self: CodeMemberProperty) = value
"""

    SetStatements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of set statements for the property.

Get: SetStatements(self: CodeMemberProperty) -> CodeStatementCollection

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type of the property.

Get: Type(self: CodeMemberProperty) -> CodeTypeReference

Set: Type(self: CodeMemberProperty) = value
"""



class CodeMethodInvokeExpression(CodeExpression):
    """
    Represents an expression that invokes a method.
    
    CodeMethodInvokeExpression()
    CodeMethodInvokeExpression(targetObject: CodeExpression, methodName: str, *parameters: Array[CodeExpression])
    CodeMethodInvokeExpression(method: CodeMethodReferenceExpression, *parameters: Array[CodeExpression])
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, method: CodeMethodReferenceExpression, *parameters: Array[CodeExpression])
        __new__(cls: type, targetObject: CodeExpression, methodName: str, *parameters: Array[CodeExpression])
        """
        pass

    Method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the method to invoke.

Get: Method(self: CodeMethodInvokeExpression) -> CodeMethodReferenceExpression

Set: Method(self: CodeMethodInvokeExpression) = value
"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parameters to invoke the method with.

Get: Parameters(self: CodeMethodInvokeExpression) -> CodeExpressionCollection

"""



class CodeMethodReferenceExpression(CodeExpression):
    """
    Represents a reference to a method.
    
    CodeMethodReferenceExpression()
    CodeMethodReferenceExpression(targetObject: CodeExpression, methodName: str)
    CodeMethodReferenceExpression(targetObject: CodeExpression, methodName: str, *typeParameters: Array[CodeTypeReference])
    """
    @staticmethod # known case of __new__
    def __new__(self, targetObject=None, methodName=None, typeParameters=None):
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, methodName: str)
        __new__(cls: type, targetObject: CodeExpression, methodName: str, *typeParameters: Array[CodeTypeReference])
        """
        pass

    MethodName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the method to reference.

Get: MethodName(self: CodeMethodReferenceExpression) -> str

Set: MethodName(self: CodeMethodReferenceExpression) = value
"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the expression that indicates the method to reference.

Get: TargetObject(self: CodeMethodReferenceExpression) -> CodeExpression

Set: TargetObject(self: CodeMethodReferenceExpression) = value
"""

    TypeArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type arguments for the current generic method reference expression.

Get: TypeArguments(self: CodeMethodReferenceExpression) -> CodeTypeReferenceCollection

"""



class CodeMethodReturnStatement(CodeStatement):
    """
    Represents a return value statement.
    
    CodeMethodReturnStatement()
    CodeMethodReturnStatement(expression: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, expression=None):
        """
        __new__(cls: type)
        __new__(cls: type, expression: CodeExpression)
        """
        pass

    Expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the return value.

Get: Expression(self: CodeMethodReturnStatement) -> CodeExpression

Set: Expression(self: CodeMethodReturnStatement) = value
"""



class CodeNamespace(CodeObject):
    """
    Represents a namespace declaration.
    
    CodeNamespace(name: str)
    CodeNamespace()
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    Comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the comments for the namespace.

Get: Comments(self: CodeNamespace) -> CodeCommentStatementCollection

"""

    Imports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of namespace import directives used by the namespace.

Get: Imports(self: CodeNamespace) -> CodeNamespaceImportCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the namespace.

Get: Name(self: CodeNamespace) -> str

Set: Name(self: CodeNamespace) = value
"""

    Types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of types that the namespace contains.

Get: Types(self: CodeNamespace) -> CodeTypeDeclarationCollection

"""


    PopulateComments = None
    PopulateImports = None
    PopulateTypes = None


class CodeNamespaceCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeNamespace objects.
    
    CodeNamespaceCollection()
    CodeNamespaceCollection(value: CodeNamespaceCollection)
    CodeNamespaceCollection(value: Array[CodeNamespace])
    """
    def Add(self, value):
        """
        Add(self: CodeNamespaceCollection, value: CodeNamespace) -> int
        
            Adds the specified System.CodeDom.CodeNamespace object to the collection.
        
            value: The System.CodeDom.CodeNamespace to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeNamespaceCollection, value: CodeNamespaceCollection)
            Adds the contents of the specified System.CodeDom.CodeNamespaceCollection object to the end of 
             the collection.
        
        
            value: A System.CodeDom.CodeNamespaceCollection that contains the objects to add to the collection.
        AddRange(self: CodeNamespaceCollection, value: Array[CodeNamespace])
            Copies the elements of the specified System.CodeDom.CodeNamespace array to the end of the 
             collection.
        
        
            value: An array of type System.CodeDom.CodeNamespace that contains the objects to add to the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeNamespaceCollection, value: CodeNamespace) -> bool
        
            Gets a value that indicates whether the collection contains the specified 
             System.CodeDom.CodeNamespace object.
        
        
            value: The System.CodeDom.CodeNamespace to search for in the collection.
            Returns: true if the System.CodeDom.CodeNamespace is contained in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeNamespaceCollection, array: Array[CodeNamespace], index: int)
            Copies the collection objects to a one-dimensional System.Array instance, starting at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeNamespaceCollection, value: CodeNamespace) -> int
        
            Gets the index of the specified System.CodeDom.CodeNamespace object in the 
             System.CodeDom.CodeNamespaceCollection, if it exists in the collection.
        
        
            value: The System.CodeDom.CodeNamespace to locate.
            Returns: The index of the specified System.CodeDom.CodeNamespace, if it is found, in the collection; 
             otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeNamespaceCollection, index: int, value: CodeNamespace)
            Inserts the specified System.CodeDom.CodeNamespace object into the collection at the specified 
             index.
        
        
            index: The zero-based index where the new item should be inserted.
            value: The System.CodeDom.CodeNamespace to insert.
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
        Remove(self: CodeNamespaceCollection, value: CodeNamespace)
            Removes the specified System.CodeDom.CodeNamespace object from the collection.
        
            value: The System.CodeDom.CodeNamespace to remove from the collection.
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
        __new__(cls: type, value: CodeNamespaceCollection)
        __new__(cls: type, value: Array[CodeNamespace])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeNamespaceImport(CodeObject):
    """
    Represents a namespace import directive that indicates a namespace to use.
    
    CodeNamespaceImport(nameSpace: str)
    CodeNamespaceImport()
    """
    @staticmethod # known case of __new__
    def __new__(self, nameSpace=None):
        """
        __new__(cls: type)
        __new__(cls: type, nameSpace: str)
        """
        pass

    LinePragma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line and file the statement occurs on.

Get: LinePragma(self: CodeNamespaceImport) -> CodeLinePragma

Set: LinePragma(self: CodeNamespaceImport) = value
"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the namespace to import.

Get: Namespace(self: CodeNamespaceImport) -> str

Set: Namespace(self: CodeNamespaceImport) = value
"""



class CodeNamespaceImportCollection(object, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeNamespaceImport objects.
    
    CodeNamespaceImportCollection()
    """
    def Add(self, value):
        """
        Add(self: CodeNamespaceImportCollection, value: CodeNamespaceImport)
            Adds a System.CodeDom.CodeNamespaceImport object to the collection.
        
            value: The System.CodeDom.CodeNamespaceImport object to add to the collection.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeNamespaceImportCollection, value: Array[CodeNamespaceImport])
            Adds a set of System.CodeDom.CodeNamespaceImport objects to the collection.
        
            value: An array of type System.CodeDom.CodeNamespaceImport that contains the objects to add to the 
             collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: CodeNamespaceImportCollection)
            Clears the collection of members.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CodeNamespaceImportCollection) -> IEnumerator
        
            Gets an enumerator that enumerates the collection members.
            Returns: An System.Collections.IEnumerator that indicates the collection members.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IList, value: object) -> bool
        
            Determines whether the System.Collections.IList contains a specific value.
        
            value: The object to locate in the System.Collections.IList.
            Returns: true if the System.Object is found in the System.Collections.IList; otherwise, false.
        """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of namespaces in the collection.

Get: Count(self: CodeNamespaceImportCollection) -> int

"""



class CodeObjectCreateExpression(CodeExpression):
    """
    Represents an expression that creates a new instance of a type.
    
    CodeObjectCreateExpression(createType: str, *parameters: Array[CodeExpression])
    CodeObjectCreateExpression()
    CodeObjectCreateExpression(createType: CodeTypeReference, *parameters: Array[CodeExpression])
    CodeObjectCreateExpression(createType: Type, *parameters: Array[CodeExpression])
    """
    @staticmethod # known case of __new__
    def __new__(self, createType=None, parameters=None):
        """
        __new__(cls: type)
        __new__(cls: type, createType: CodeTypeReference, *parameters: Array[CodeExpression])
        __new__(cls: type, createType: str, *parameters: Array[CodeExpression])
        __new__(cls: type, createType: Type, *parameters: Array[CodeExpression])
        """
        pass

    CreateType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type of the object to create.

Get: CreateType(self: CodeObjectCreateExpression) -> CodeTypeReference

Set: CreateType(self: CodeObjectCreateExpression) = value
"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the parameters to use in creating the object.

Get: Parameters(self: CodeObjectCreateExpression) -> CodeExpressionCollection

"""



class CodeParameterDeclarationExpression(CodeExpression):
    """
    Represents a parameter declaration for a method, property, or constructor.
    
    CodeParameterDeclarationExpression()
    CodeParameterDeclarationExpression(type: CodeTypeReference, name: str)
    CodeParameterDeclarationExpression(type: str, name: str)
    CodeParameterDeclarationExpression(type: Type, name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, type=None, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference, name: str)
        __new__(cls: type, type: str, name: str)
        __new__(cls: type, type: Type, name: str)
        """
        pass

    CustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the custom attributes for the parameter declaration.

Get: CustomAttributes(self: CodeParameterDeclarationExpression) -> CodeAttributeDeclarationCollection

Set: CustomAttributes(self: CodeParameterDeclarationExpression) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the direction of the field.

Get: Direction(self: CodeParameterDeclarationExpression) -> FieldDirection

Set: Direction(self: CodeParameterDeclarationExpression) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the parameter.

Get: Name(self: CodeParameterDeclarationExpression) -> str

Set: Name(self: CodeParameterDeclarationExpression) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the parameter.

Get: Type(self: CodeParameterDeclarationExpression) -> CodeTypeReference

Set: Type(self: CodeParameterDeclarationExpression) = value
"""



class CodeParameterDeclarationExpressionCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeParameterDeclarationExpression objects.
    
    CodeParameterDeclarationExpressionCollection()
    CodeParameterDeclarationExpressionCollection(value: CodeParameterDeclarationExpressionCollection)
    CodeParameterDeclarationExpressionCollection(value: Array[CodeParameterDeclarationExpression])
    """
    def Add(self, value):
        """
        Add(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpression) -> int
        
            Adds the specified System.CodeDom.CodeParameterDeclarationExpression to the collection.
        
            value: The System.CodeDom.CodeParameterDeclarationExpression to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpressionCollection)
            Adds the contents of another System.CodeDom.CodeParameterDeclarationExpressionCollection to the 
             end of the collection.
        
        
            value: A System.CodeDom.CodeParameterDeclarationExpressionCollection containing the objects to add to 
             the collection.
        
        AddRange(self: CodeParameterDeclarationExpressionCollection, value: Array[CodeParameterDeclarationExpression])
            Copies the elements of the specified array to the end of the collection.
        
            value: An array of type System.CodeDom.CodeParameterDeclarationExpression containing the objects to add 
             to the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpression) -> bool
        
            Gets a value indicating whether the collection contains the specified 
             System.CodeDom.CodeParameterDeclarationExpression.
        
        
            value: A System.CodeDom.CodeParameterDeclarationExpression to search for in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeParameterDeclarationExpressionCollection, array: Array[CodeParameterDeclarationExpression], index: int)
            Copies the collection objects to a one-dimensional System.Array instance beginning at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpression) -> int
        
            Gets the index in the collection of the specified 
             System.CodeDom.CodeParameterDeclarationExpression, if it exists in the collection.
        
        
            value: The System.CodeDom.CodeParameterDeclarationExpression to locate in the collection.
            Returns: The index in the collection of the specified object, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeParameterDeclarationExpressionCollection, index: int, value: CodeParameterDeclarationExpression)
            Inserts the specified System.CodeDom.CodeParameterDeclarationExpression into the collection at 
             the specified index.
        
        
            index: The zero-based index where the specified object should be inserted.
            value: The System.CodeDom.CodeParameterDeclarationExpression to insert.
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
        Remove(self: CodeParameterDeclarationExpressionCollection, value: CodeParameterDeclarationExpression)
            Removes the specified System.CodeDom.CodeParameterDeclarationExpression from the collection.
        
            value: The System.CodeDom.CodeParameterDeclarationExpression to remove from the collection.
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
        __new__(cls: type, value: CodeParameterDeclarationExpressionCollection)
        __new__(cls: type, value: Array[CodeParameterDeclarationExpression])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodePrimitiveExpression(CodeExpression):
    """
    Represents a primitive data type value.
    
    CodePrimitiveExpression()
    CodePrimitiveExpression(value: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: object)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the primitive data type to represent.

Get: Value(self: CodePrimitiveExpression) -> object

Set: Value(self: CodePrimitiveExpression) = value
"""



class CodePropertyReferenceExpression(CodeExpression):
    """
    Represents a reference to the value of a property.
    
    CodePropertyReferenceExpression(targetObject: CodeExpression, propertyName: str)
    CodePropertyReferenceExpression()
    """
    @staticmethod # known case of __new__
    def __new__(self, targetObject=None, propertyName=None):
        """
        __new__(cls: type)
        __new__(cls: type, targetObject: CodeExpression, propertyName: str)
        """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the property to reference.

Get: PropertyName(self: CodePropertyReferenceExpression) -> str

Set: PropertyName(self: CodePropertyReferenceExpression) = value
"""

    TargetObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object that contains the property to reference.

Get: TargetObject(self: CodePropertyReferenceExpression) -> CodeExpression

Set: TargetObject(self: CodePropertyReferenceExpression) = value
"""



class CodePropertySetValueReferenceExpression(CodeExpression):
    """
    Represents the value argument of a property set method call within a property set method.
    
    CodePropertySetValueReferenceExpression()
    """

class CodeRegionDirective(CodeDirective):
    """
    Specifies the name and mode for a code region.
    
    CodeRegionDirective()
    CodeRegionDirective(regionMode: CodeRegionMode, regionText: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, regionMode=None, regionText=None):
        """
        __new__(cls: type)
        __new__(cls: type, regionMode: CodeRegionMode, regionText: str)
        """
        pass

    RegionMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the mode for the region directive.

Get: RegionMode(self: CodeRegionDirective) -> CodeRegionMode

Set: RegionMode(self: CodeRegionDirective) = value
"""

    RegionText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the region.

Get: RegionText(self: CodeRegionDirective) -> str

Set: RegionText(self: CodeRegionDirective) = value
"""



class CodeRegionMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the start or end of a code region.
    
    enum CodeRegionMode, values: End (2), None (0), Start (1)
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

    End = None
    None = None
    Start = None
    value__ = None


class CodeRemoveEventStatement(CodeStatement):
    """
    Represents a statement that removes an event handler.
    
    CodeRemoveEventStatement()
    CodeRemoveEventStatement(eventRef: CodeEventReferenceExpression, listener: CodeExpression)
    CodeRemoveEventStatement(targetObject: CodeExpression, eventName: str, listener: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, eventRef: CodeEventReferenceExpression, listener: CodeExpression)
        __new__(cls: type, targetObject: CodeExpression, eventName: str, listener: CodeExpression)
        """
        pass

    Event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event to remove a listener from.

Get: Event(self: CodeRemoveEventStatement) -> CodeEventReferenceExpression

Set: Event(self: CodeRemoveEventStatement) = value
"""

    Listener = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the event handler to remove.

Get: Listener(self: CodeRemoveEventStatement) -> CodeExpression

Set: Listener(self: CodeRemoveEventStatement) = value
"""



class CodeSnippetCompileUnit(CodeCompileUnit):
    """
    Represents a literal code fragment that can be compiled.
    
    CodeSnippetCompileUnit()
    CodeSnippetCompileUnit(value: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: str)
        """
        pass

    LinePragma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the line and file information about where the code is located in a source code document.

Get: LinePragma(self: CodeSnippetCompileUnit) -> CodeLinePragma

Set: LinePragma(self: CodeSnippetCompileUnit) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the literal code fragment to represent.

Get: Value(self: CodeSnippetCompileUnit) -> str

Set: Value(self: CodeSnippetCompileUnit) = value
"""



class CodeSnippetExpression(CodeExpression):
    """
    Represents a literal expression.
    
    CodeSnippetExpression()
    CodeSnippetExpression(value: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: str)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the literal string of code.

Get: Value(self: CodeSnippetExpression) -> str

Set: Value(self: CodeSnippetExpression) = value
"""



class CodeSnippetStatement(CodeStatement):
    """
    Represents a statement using a literal code fragment.
    
    CodeSnippetStatement()
    CodeSnippetStatement(value: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, value=None):
        """
        __new__(cls: type)
        __new__(cls: type, value: str)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the literal code fragment statement.

Get: Value(self: CodeSnippetStatement) -> str

Set: Value(self: CodeSnippetStatement) = value
"""



class CodeSnippetTypeMember(CodeTypeMember):
    """
    Represents a member of a type using a literal code fragment.
    
    CodeSnippetTypeMember()
    CodeSnippetTypeMember(text: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, text=None):
        """
        __new__(cls: type)
        __new__(cls: type, text: str)
        """
        pass

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the literal code fragment for the type member.

Get: Text(self: CodeSnippetTypeMember) -> str

Set: Text(self: CodeSnippetTypeMember) = value
"""



class CodeStatementCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeStatement objects.
    
    CodeStatementCollection()
    CodeStatementCollection(value: CodeStatementCollection)
    CodeStatementCollection(value: Array[CodeStatement])
    """
    def Add(self, value):
        """
        Add(self: CodeStatementCollection, value: CodeExpression) -> int
        
            Adds the specified System.CodeDom.CodeExpression object to the collection.
        
            value: The System.CodeDom.CodeExpression object to add.
            Returns: The index at which the new element was inserted.
        Add(self: CodeStatementCollection, value: CodeStatement) -> int
        
            Adds the specified System.CodeDom.CodeStatement object to the collection.
        
            value: The System.CodeDom.CodeStatement object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeStatementCollection, value: CodeStatementCollection)
            Adds the contents of another System.CodeDom.CodeStatementCollection object to the end of the 
             collection.
        
        
            value: A System.CodeDom.CodeStatementCollection object that contains the objects to add to the 
             collection.
        
        AddRange(self: CodeStatementCollection, value: Array[CodeStatement])
            Adds a set of System.CodeDom.CodeStatement objects to the collection.
        
            value: An array of System.CodeDom.CodeStatement objects to add to the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeStatementCollection, value: CodeStatement) -> bool
        
            Gets a value that indicates whether the collection contains the specified 
             System.CodeDom.CodeStatement object.
        
        
            value: The System.CodeDom.CodeStatement object to search for in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeStatementCollection, array: Array[CodeStatement], index: int)
            Copies the elements of the System.CodeDom.CodeStatementCollection object to a one-dimensional 
             System.Array instance, starting at the specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeStatementCollection, value: CodeStatement) -> int
        
            Gets the index of the specified System.CodeDom.CodeStatement object in the 
             System.CodeDom.CodeStatementCollection, if it exists in the collection.
        
        
            value: The System.CodeDom.CodeStatement to locate in the collection.
            Returns: The index of the specified object, if it is found, in the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeStatementCollection, index: int, value: CodeStatement)
            Inserts the specified System.CodeDom.CodeStatement object into the collection at the specified 
             index.
        
        
            index: The zero-based index where the specified object should be inserted.
            value: The System.CodeDom.CodeStatement object to insert.
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
        Remove(self: CodeStatementCollection, value: CodeStatement)
            Removes the specified System.CodeDom.CodeStatement object from the collection.
        
            value: The System.CodeDom.CodeStatement to remove from the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
        __new__(cls: type, value: CodeStatementCollection)
        __new__(cls: type, value: Array[CodeStatement])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeThisReferenceExpression(CodeExpression):
    """
    Represents a reference to the current local class instance.
    
    CodeThisReferenceExpression()
    """

class CodeThrowExceptionStatement(CodeStatement):
    """
    Represents a statement that throws an exception.
    
    CodeThrowExceptionStatement()
    CodeThrowExceptionStatement(toThrow: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, toThrow=None):
        """
        __new__(cls: type)
        __new__(cls: type, toThrow: CodeExpression)
        """
        pass

    ToThrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the exception to throw.

Get: ToThrow(self: CodeThrowExceptionStatement) -> CodeExpression

Set: ToThrow(self: CodeThrowExceptionStatement) = value
"""



class CodeTryCatchFinallyStatement(CodeStatement):
    """
    Represents a try block with any number of catch clauses and, optionally, a finally block.
    
    CodeTryCatchFinallyStatement()
    CodeTryCatchFinallyStatement(tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause])
    CodeTryCatchFinallyStatement(tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause], finallyStatements: Array[CodeStatement])
    """
    @staticmethod # known case of __new__
    def __new__(self, tryStatements=None, catchClauses=None, finallyStatements=None):
        """
        __new__(cls: type)
        __new__(cls: type, tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause])
        __new__(cls: type, tryStatements: Array[CodeStatement], catchClauses: Array[CodeCatchClause], finallyStatements: Array[CodeStatement])
        """
        pass

    CatchClauses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the catch clauses to use.

Get: CatchClauses(self: CodeTryCatchFinallyStatement) -> CodeCatchClauseCollection

"""

    FinallyStatements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the finally statements to use.

Get: FinallyStatements(self: CodeTryCatchFinallyStatement) -> CodeStatementCollection

"""

    TryStatements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the statements to try.

Get: TryStatements(self: CodeTryCatchFinallyStatement) -> CodeStatementCollection

"""



class CodeTypeConstructor(CodeMemberMethod):
    """
    Represents a static constructor for a class.
    
    CodeTypeConstructor()
    """

class CodeTypeDeclaration(CodeTypeMember):
    """
    Represents a type declaration for a class, structure, interface, or enumeration.
    
    CodeTypeDeclaration(name: str)
    CodeTypeDeclaration()
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    BaseTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the base types of the type.

Get: BaseTypes(self: CodeTypeDeclaration) -> CodeTypeReferenceCollection

"""

    IsClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the type is a class or reference type.

Get: IsClass(self: CodeTypeDeclaration) -> bool

Set: IsClass(self: CodeTypeDeclaration) = value
"""

    IsEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the type is an enumeration.

Get: IsEnum(self: CodeTypeDeclaration) -> bool

Set: IsEnum(self: CodeTypeDeclaration) = value
"""

    IsInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the type is an interface.

Get: IsInterface(self: CodeTypeDeclaration) -> bool

Set: IsInterface(self: CodeTypeDeclaration) = value
"""

    IsPartial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the type declaration is complete or partial.

Get: IsPartial(self: CodeTypeDeclaration) -> bool

Set: IsPartial(self: CodeTypeDeclaration) = value
"""

    IsStruct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the type is a value type (struct).

Get: IsStruct(self: CodeTypeDeclaration) -> bool

Set: IsStruct(self: CodeTypeDeclaration) = value
"""

    Members = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of class members for the represented type.

Get: Members(self: CodeTypeDeclaration) -> CodeTypeMemberCollection

"""

    TypeAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the attributes of the type.

Get: TypeAttributes(self: CodeTypeDeclaration) -> TypeAttributes

Set: TypeAttributes(self: CodeTypeDeclaration) = value
"""

    TypeParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type parameters for the type declaration.

Get: TypeParameters(self: CodeTypeDeclaration) -> CodeTypeParameterCollection

"""


    PopulateBaseTypes = None
    PopulateMembers = None


class CodeTypeDeclarationCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeTypeDeclaration objects.
    
    CodeTypeDeclarationCollection()
    CodeTypeDeclarationCollection(value: CodeTypeDeclarationCollection)
    CodeTypeDeclarationCollection(value: Array[CodeTypeDeclaration])
    """
    def Add(self, value):
        """
        Add(self: CodeTypeDeclarationCollection, value: CodeTypeDeclaration) -> int
        
            Adds the specified System.CodeDom.CodeTypeDeclaration object to the collection.
        
            value: The System.CodeDom.CodeTypeDeclaration object to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeTypeDeclarationCollection, value: CodeTypeDeclarationCollection)
            Adds the contents of another System.CodeDom.CodeTypeDeclarationCollection object to the end of 
             the collection.
        
        
            value: A System.CodeDom.CodeTypeDeclarationCollection object that contains the objects to add to the 
             collection.
        
        AddRange(self: CodeTypeDeclarationCollection, value: Array[CodeTypeDeclaration])
            Copies the elements of the specified array to the end of the collection.
        
            value: An array of type System.CodeDom.CodeTypeDeclaration that contains the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeTypeDeclarationCollection, value: CodeTypeDeclaration) -> bool
        
            Gets a value that indicates whether the collection contains the specified 
             System.CodeDom.CodeTypeDeclaration object.
        
        
            value: The System.CodeDom.CodeTypeDeclaration object to search for in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeTypeDeclarationCollection, array: Array[CodeTypeDeclaration], index: int)
            Copies the elements in the System.CodeDom.CodeTypeDeclarationCollection object to a 
             one-dimensional System.Array instance, starting at the specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeTypeDeclarationCollection, value: CodeTypeDeclaration) -> int
        
            Gets the index of the specified System.CodeDom.CodeTypeDeclaration object in the 
             System.CodeDom.CodeTypeDeclarationCollection, if it exists in the collection.
        
        
            value: The System.CodeDom.CodeTypeDeclaration to locate in the collection.
            Returns: The index of the specified object, if it is found, in the collection; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeTypeDeclarationCollection, index: int, value: CodeTypeDeclaration)
            Inserts the specified System.CodeDom.CodeTypeDeclaration object into the collection at the 
             specified index.
        
        
            index: The zero-based index where the specified object should be inserted.
            value: The System.CodeDom.CodeTypeDeclaration object to insert.
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
        Remove(self: CodeTypeDeclarationCollection, value: CodeTypeDeclaration)
            Removes the specified System.CodeDom.CodeTypeDeclaration object from the collection.
        
            value: The System.CodeDom.CodeTypeDeclaration to remove from the collection.
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
        __new__(cls: type, value: CodeTypeDeclarationCollection)
        __new__(cls: type, value: Array[CodeTypeDeclaration])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeTypeDelegate(CodeTypeDeclaration):
    """
    Represents a delegate declaration.
    
    CodeTypeDelegate()
    CodeTypeDelegate(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parameters of the delegate.

Get: Parameters(self: CodeTypeDelegate) -> CodeParameterDeclarationExpressionCollection

"""

    ReturnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the return type of the delegate.

Get: ReturnType(self: CodeTypeDelegate) -> CodeTypeReference

Set: ReturnType(self: CodeTypeDelegate) = value
"""



class CodeTypeMemberCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeTypeMember objects.
    
    CodeTypeMemberCollection()
    CodeTypeMemberCollection(value: CodeTypeMemberCollection)
    CodeTypeMemberCollection(value: Array[CodeTypeMember])
    """
    def Add(self, value):
        """
        Add(self: CodeTypeMemberCollection, value: CodeTypeMember) -> int
        
            Adds a System.CodeDom.CodeTypeMember with the specified value to the collection.
        
            value: The System.CodeDom.CodeTypeMember to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeTypeMemberCollection, value: CodeTypeMemberCollection)
            Adds the contents of another System.CodeDom.CodeTypeMemberCollection to the end of the 
             collection.
        
        
            value: A System.CodeDom.CodeTypeMemberCollection containing the objects to add to the collection.
        AddRange(self: CodeTypeMemberCollection, value: Array[CodeTypeMember])
            Copies the elements of the specified System.CodeDom.CodeTypeMember array to the end of the 
             collection.
        
        
            value: An array of type System.CodeDom.CodeTypeMember containing the objects to add to the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeTypeMemberCollection, value: CodeTypeMember) -> bool
        
            Gets a value indicating whether the collection contains the specified 
             System.CodeDom.CodeTypeMember.
        
        
            value: The System.CodeDom.CodeTypeMember to search for in the collection.
            Returns: true if the collection contains the specified object; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeTypeMemberCollection, array: Array[CodeTypeMember], index: int)
            Copies the collection objects to a one-dimensional System.Array instance, beginning at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeTypeMemberCollection, value: CodeTypeMember) -> int
        
            Gets the index in the collection of the specified System.CodeDom.CodeTypeMember, if it exists in 
             the collection.
        
        
            value: The System.CodeDom.CodeTypeMember to locate in the collection.
            Returns: The index in the collection of the specified object, if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeTypeMemberCollection, index: int, value: CodeTypeMember)
            Inserts the specified System.CodeDom.CodeTypeMember into the collection at the specified index.
        
            index: The zero-based index where the specified object should be inserted.
            value: The System.CodeDom.CodeTypeMember to insert.
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
        Remove(self: CodeTypeMemberCollection, value: CodeTypeMember)
            Removes a specific System.CodeDom.CodeTypeMember from the collection.
        
            value: The System.CodeDom.CodeTypeMember to remove from the collection.
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
        __new__(cls: type, value: CodeTypeMemberCollection)
        __new__(cls: type, value: Array[CodeTypeMember])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeTypeOfExpression(CodeExpression):
    """
    Represents a typeof expression, an expression that returns a System.Type for a specified type name.
    
    CodeTypeOfExpression()
    CodeTypeOfExpression(type: CodeTypeReference)
    CodeTypeOfExpression(type: str)
    CodeTypeOfExpression(type: Type)
    """
    @staticmethod # known case of __new__
    def __new__(self, type=None):
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference)
        __new__(cls: type, type: str)
        __new__(cls: type, type: Type)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type referenced by the typeof expression.

Get: Type(self: CodeTypeOfExpression) -> CodeTypeReference

Set: Type(self: CodeTypeOfExpression) = value
"""



class CodeTypeParameter(CodeObject):
    """
    Represents a type parameter of a generic type or method.
    
    CodeTypeParameter()
    CodeTypeParameter(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    Constraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the constraints for the type parameter.

Get: Constraints(self: CodeTypeParameter) -> CodeTypeReferenceCollection

"""

    CustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the custom attributes of the type parameter.

Get: CustomAttributes(self: CodeTypeParameter) -> CodeAttributeDeclarationCollection

"""

    HasConstructorConstraint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating whether the type parameter has a constructor constraint.

Get: HasConstructorConstraint(self: CodeTypeParameter) -> bool

Set: HasConstructorConstraint(self: CodeTypeParameter) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the type parameter.

Get: Name(self: CodeTypeParameter) -> str

Set: Name(self: CodeTypeParameter) = value
"""



class CodeTypeParameterCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeTypeParameter objects.
    
    CodeTypeParameterCollection()
    CodeTypeParameterCollection(value: CodeTypeParameterCollection)
    CodeTypeParameterCollection(value: Array[CodeTypeParameter])
    """
    def Add(self, value):
        """
        Add(self: CodeTypeParameterCollection, value: str)
            Adds the specified System.CodeDom.CodeTypeParameter object to the collection using the specified 
             data type name.
        
        
            value: The name of a data type for which to add the System.CodeDom.CodeTypeParameter object to the 
             collection.
        
        Add(self: CodeTypeParameterCollection, value: CodeTypeParameter) -> int
        
            Adds the specified System.CodeDom.CodeTypeParameter object to the collection.
        
            value: The System.CodeDom.CodeTypeParameter to add.
            Returns: The zero-based index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeTypeParameterCollection, value: CodeTypeParameterCollection)
            Copies the elements of the specified System.CodeDom.CodeTypeParameterCollection to the end of 
             the collection.
        
        
            value: A System.CodeDom.CodeTypeParameterCollection containing the System.CodeDom.CodeTypeParameter 
             objects to add to the collection.
        
        AddRange(self: CodeTypeParameterCollection, value: Array[CodeTypeParameter])
            Copies the elements of the specified System.CodeDom.CodeTypeParameter array to the end of the 
             collection.
        
        
            value: An array of type System.CodeDom.CodeTypeParameter containing the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeTypeParameterCollection, value: CodeTypeParameter) -> bool
        
            Determines whether the collection contains the specified System.CodeDom.CodeTypeParameter object.
        
            value: The System.CodeDom.CodeTypeParameter object to search for in the collection.
            Returns: true if the System.CodeDom.CodeTypeParameter object is contained in the collection; otherwise, 
             false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeTypeParameterCollection, array: Array[CodeTypeParameter], index: int)
            Copies the items in the collection to the specified one-dimensional System.Array at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeTypeParameterCollection, value: CodeTypeParameter) -> int
        
            Gets the index in the collection of the specified System.CodeDom.CodeTypeParameter object, if it 
             exists in the collection.
        
        
            value: The System.CodeDom.CodeTypeParameter object to locate in the collection.
            Returns: The zero-based index of the specified System.CodeDom.CodeTypeParameter object in the collection 
             if found; otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeTypeParameterCollection, index: int, value: CodeTypeParameter)
            Inserts the specified System.CodeDom.CodeTypeParameter object into the collection at the 
             specified index.
        
        
            index: The zero-based index at which to insert the item.
            value: The System.CodeDom.CodeTypeParameter object to insert.
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
        Remove(self: CodeTypeParameterCollection, value: CodeTypeParameter)
            Removes the specified System.CodeDom.CodeTypeParameter object from the collection.
        
            value: The System.CodeDom.CodeTypeParameter object to remove from the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
        __new__(cls: type, value: CodeTypeParameterCollection)
        __new__(cls: type, value: Array[CodeTypeParameter])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeTypeReference(CodeObject):
    """
    Represents a reference to a type.
    
    CodeTypeReference(type: Type)
    CodeTypeReference()
    CodeTypeReference(type: Type, codeTypeReferenceOption: CodeTypeReferenceOptions)
    CodeTypeReference(typeName: str, codeTypeReferenceOption: CodeTypeReferenceOptions)
    CodeTypeReference(typeName: str)
    CodeTypeReference(typeName: str, *typeArguments: Array[CodeTypeReference])
    CodeTypeReference(typeParameter: CodeTypeParameter)
    CodeTypeReference(baseType: str, rank: int)
    CodeTypeReference(arrayType: CodeTypeReference, rank: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        __new__(cls: type, type: Type, codeTypeReferenceOption: CodeTypeReferenceOptions)
        __new__(cls: type, typeName: str, codeTypeReferenceOption: CodeTypeReferenceOptions)
        __new__(cls: type, typeName: str)
        __new__(cls: type, typeName: str, *typeArguments: Array[CodeTypeReference])
        __new__(cls: type, typeParameter: CodeTypeParameter)
        __new__(cls: type, baseType: str, rank: int)
        __new__(cls: type, arrayType: CodeTypeReference, rank: int)
        """
        pass

    ArrayElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the elements in the array.

Get: ArrayElementType(self: CodeTypeReference) -> CodeTypeReference

Set: ArrayElementType(self: CodeTypeReference) = value
"""

    ArrayRank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the array rank of the array.

Get: ArrayRank(self: CodeTypeReference) -> int

Set: ArrayRank(self: CodeTypeReference) = value
"""

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the type being referenced.

Get: BaseType(self: CodeTypeReference) -> str

Set: BaseType(self: CodeTypeReference) = value
"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the code type reference option.

Get: Options(self: CodeTypeReference) -> CodeTypeReferenceOptions

Set: Options(self: CodeTypeReference) = value
"""

    TypeArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type arguments for the current generic type reference.

Get: TypeArguments(self: CodeTypeReference) -> CodeTypeReferenceCollection

"""



class CodeTypeReferenceCollection(CollectionBase, IList, ICollection, IEnumerable):
    """
    Represents a collection of System.CodeDom.CodeTypeReference objects.
    
    CodeTypeReferenceCollection()
    CodeTypeReferenceCollection(value: CodeTypeReferenceCollection)
    CodeTypeReferenceCollection(value: Array[CodeTypeReference])
    """
    def Add(self, value):
        """
        Add(self: CodeTypeReferenceCollection, value: Type)
            Adds a System.CodeDom.CodeTypeReference to the collection using the specified data type.
        
            value: The data type for which to add a System.CodeDom.CodeTypeReference to the collection.
        Add(self: CodeTypeReferenceCollection, value: str)
            Adds a System.CodeDom.CodeTypeReference to the collection using the specified data type name.
        
            value: The name of a data type for which to add a System.CodeDom.CodeTypeReference to the collection.
        Add(self: CodeTypeReferenceCollection, value: CodeTypeReference) -> int
        
            Adds the specified System.CodeDom.CodeTypeReference to the collection.
        
            value: The System.CodeDom.CodeTypeReference to add.
            Returns: The index at which the new element was inserted.
        """
        pass

    def AddRange(self, value):
        """
        AddRange(self: CodeTypeReferenceCollection, value: CodeTypeReferenceCollection)
            Adds the contents of the specified System.CodeDom.CodeTypeReferenceCollection to the end of the 
             collection.
        
        
            value: A System.CodeDom.CodeTypeReferenceCollection containing the objects to add to the collection.
        AddRange(self: CodeTypeReferenceCollection, value: Array[CodeTypeReference])
            Copies the elements of the specified System.CodeDom.CodeTypeReference array to the end of the 
             collection.
        
        
            value: An array of type System.CodeDom.CodeTypeReference containing the objects to add to the 
             collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: CodeTypeReferenceCollection, value: CodeTypeReference) -> bool
        
            Gets a value indicating whether the collection contains the specified 
             System.CodeDom.CodeTypeReference.
        
        
            value: The System.CodeDom.CodeTypeReference to search for in the collection.
            Returns: true if the System.CodeDom.CodeTypeReference is contained in the collection; otherwise, false.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CodeTypeReferenceCollection, array: Array[CodeTypeReference], index: int)
            Copies the items in the collection to the specified one-dimensional System.Array at the 
             specified index.
        
        
            array: The one-dimensional System.Array that is the destination of the values copied from the 
             collection.
        
            index: The index of the array at which to begin inserting.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: CodeTypeReferenceCollection, value: CodeTypeReference) -> int
        
            Gets the index in the collection of the specified System.CodeDom.CodeTypeReference, if it exists 
             in the collection.
        
        
            value: The System.CodeDom.CodeTypeReference to locate in the collection.
            Returns: The index of the specified System.CodeDom.CodeTypeReference in the collection if found; 
             otherwise, -1.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: CodeTypeReferenceCollection, index: int, value: CodeTypeReference)
            Inserts a System.CodeDom.CodeTypeReference into the collection at the specified index.
        
            index: The zero-based index where the item should be inserted.
            value: The System.CodeDom.CodeTypeReference to insert.
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
        Remove(self: CodeTypeReferenceCollection, value: CodeTypeReference)
            Removes the specified System.CodeDom.CodeTypeReference from the collection.
        
            value: The System.CodeDom.CodeTypeReference to remove from the collection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
        __new__(cls: type, value: CodeTypeReferenceCollection)
        __new__(cls: type, value: Array[CodeTypeReference])
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    InnerList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

    List = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""



class CodeTypeReferenceExpression(CodeExpression):
    """
    Represents a reference to a data type.
    
    CodeTypeReferenceExpression()
    CodeTypeReferenceExpression(type: CodeTypeReference)
    CodeTypeReferenceExpression(type: str)
    CodeTypeReferenceExpression(type: Type)
    """
    @staticmethod # known case of __new__
    def __new__(self, type=None):
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference)
        __new__(cls: type, type: str)
        __new__(cls: type, type: Type)
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type to reference.

Get: Type(self: CodeTypeReferenceExpression) -> CodeTypeReference

Set: Type(self: CodeTypeReferenceExpression) = value
"""



class CodeTypeReferenceOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how the code type reference is to be resolved.
    
    enum (flags) CodeTypeReferenceOptions, values: GenericTypeParameter (2), GlobalReference (1)
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

    GenericTypeParameter = None
    GlobalReference = None
    value__ = None


class CodeVariableDeclarationStatement(CodeStatement):
    """
    Represents a variable declaration.
    
    CodeVariableDeclarationStatement()
    CodeVariableDeclarationStatement(type: CodeTypeReference, name: str)
    CodeVariableDeclarationStatement(type: str, name: str)
    CodeVariableDeclarationStatement(type: Type, name: str)
    CodeVariableDeclarationStatement(type: CodeTypeReference, name: str, initExpression: CodeExpression)
    CodeVariableDeclarationStatement(type: str, name: str, initExpression: CodeExpression)
    CodeVariableDeclarationStatement(type: Type, name: str, initExpression: CodeExpression)
    """
    @staticmethod # known case of __new__
    def __new__(self, type=None, name=None, initExpression=None):
        """
        __new__(cls: type)
        __new__(cls: type, type: CodeTypeReference, name: str)
        __new__(cls: type, type: str, name: str)
        __new__(cls: type, type: Type, name: str)
        __new__(cls: type, type: CodeTypeReference, name: str, initExpression: CodeExpression)
        __new__(cls: type, type: str, name: str, initExpression: CodeExpression)
        __new__(cls: type, type: Type, name: str, initExpression: CodeExpression)
        """
        pass

    InitExpression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the initialization expression for the variable.

Get: InitExpression(self: CodeVariableDeclarationStatement) -> CodeExpression

Set: InitExpression(self: CodeVariableDeclarationStatement) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the variable.

Get: Name(self: CodeVariableDeclarationStatement) -> str

Set: Name(self: CodeVariableDeclarationStatement) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type of the variable.

Get: Type(self: CodeVariableDeclarationStatement) -> CodeTypeReference

Set: Type(self: CodeVariableDeclarationStatement) = value
"""



class CodeVariableReferenceExpression(CodeExpression):
    """
    Represents a reference to a local variable.
    
    CodeVariableReferenceExpression()
    CodeVariableReferenceExpression(variableName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, variableName=None):
        """
        __new__(cls: type)
        __new__(cls: type, variableName: str)
        """
        pass

    VariableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the local variable to reference.

Get: VariableName(self: CodeVariableReferenceExpression) -> str

Set: VariableName(self: CodeVariableReferenceExpression) = value
"""



class FieldDirection(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines identifiers used to indicate the direction of parameter and argument declarations.
    
    enum FieldDirection, values: In (0), Out (1), Ref (2)
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

    In = None
    Out = None
    Ref = None
    value__ = None


class MemberAttributes(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines member attribute identifiers for class members.
    
    enum MemberAttributes, values: Abstract (1), AccessMask (61440), Assembly (4096), Const (5), Family (12288), FamilyAndAssembly (8192), FamilyOrAssembly (16384), Final (2), New (16), Overloaded (256), Override (4), Private (20480), Public (24576), ScopeMask (15), Static (3), VTableMask (240)
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

    Abstract = None
    AccessMask = None
    Assembly = None
    Const = None
    Family = None
    FamilyAndAssembly = None
    FamilyOrAssembly = None
    Final = None
    New = None
    Overloaded = None
    Override = None
    Private = None
    Public = None
    ScopeMask = None
    Static = None
    value__ = None
    VTableMask = None


# variables with complex values

