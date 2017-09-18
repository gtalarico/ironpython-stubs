# encoding: utf-8
# module System.Text.RegularExpressions calls itself RegularExpressions
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Capture(object):
    """ Represents the results from a single successful subexpression capture. """
    def ToString(self):
        """
        ToString(self: Capture) -> str
        
            Gets the captured substring from the input string.
            Returns: The actual substring that was captured by the match.
        """
        pass

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The position in the original string where the first character of the captured substring was found.

Get: Index(self: Capture) -> int

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the captured substring.

Get: Length(self: Capture) -> int

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the captured substring from the input string.

Get: Value(self: Capture) -> str

"""



class CaptureCollection(object, ICollection, IEnumerable):
    """ Represents the set of captures made by a single capturing group. """
    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: CaptureCollection, array: Array, arrayIndex: int)
            Copies all the elements of the collection to the given array beginning at the given index.
        
            array: The array the collection is to be copied into.
            arrayIndex: The position in the destination array where copying is to begin.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CaptureCollection) -> IEnumerator
        
            Provides an enumerator that iterates through the collection.
            Returns: An object that contains all System.Text.RegularExpressions.Capture objects within the 
             System.Text.RegularExpressions.CaptureCollection.
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of substrings captured by the group.

Get: Count(self: CaptureCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection is read only.

Get: IsReadOnly(self: CaptureCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to the collection is synchronized (thread-safe).

Get: IsSynchronized(self: CaptureCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the collection.

Get: SyncRoot(self: CaptureCollection) -> object

"""



class Group(Capture):
    """ Represents the results from a single capturing group. """
    @staticmethod
    def Synchronized(inner):
        """
        Synchronized(inner: Group) -> Group
        
            Returns a Group object equivalent to the one supplied that is safe to share between multiple 
             threads.
        
        
            inner: The input System.Text.RegularExpressions.Group object.
            Returns: A regular expression Group object.
        """
        pass

    Captures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all the captures matched by the capturing group, in innermost-leftmost-first order (or innermost-rightmost-first order if the regular expression is modified with the System.Text.RegularExpressions.RegexOptions.RightToLeft option). The collection may have zero or more items.

Get: Captures(self: Group) -> CaptureCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Group) -> str

"""

    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the match is successful.

Get: Success(self: Group) -> bool

"""



class GroupCollection(object, ICollection, IEnumerable):
    """ Returns the set of captured groups in a single match. """
    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: GroupCollection, array: Array, arrayIndex: int)
            Copies all the elements of the collection to the given array beginning at the given index.
        
            array: The array the collection is to be copied into.
            arrayIndex: The position in the destination array where the copying is to begin.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: GroupCollection) -> IEnumerator
        
            Provides an enumerator that iterates through the collection.
            Returns: An enumerator that contains all System.Text.RegularExpressions.Group objects in the 
             System.Text.RegularExpressions.GroupCollection.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of groups in the collection.

Get: Count(self: GroupCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection is read-only.

Get: IsReadOnly(self: GroupCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to the System.Text.RegularExpressions.GroupCollection is synchronized (thread-safe).

Get: IsSynchronized(self: GroupCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the System.Text.RegularExpressions.GroupCollection.

Get: SyncRoot(self: GroupCollection) -> object

"""



class Match(Group):
    """ Represents the results from a single regular expression match. """
    def NextMatch(self):
        """
        NextMatch(self: Match) -> Match
        
            Returns a new System.Text.RegularExpressions.Match object with the results for the next match, 
             starting at the position at which the last match ended (at the character after the last matched 
             character).
        
            Returns: The next regular expression match.
        """
        pass

    def Result(self, replacement):
        """
        Result(self: Match, replacement: str) -> str
        
            Returns the expansion of the specified replacement pattern.
        
            replacement: The replacement pattern to use.
            Returns: The expanded version of the replacement parameter.
        """
        pass

    @staticmethod
    def Synchronized(inner):
        """
        Synchronized(inner: Match) -> Match
        
            Returns a System.Text.RegularExpressions.Match instance equivalent to the one supplied that is 
             suitable to share between multiple threads.
        
        
            inner: A regular expression match equivalent to the one expected.
            Returns: A regular expression match that is suitable to share between multiple threads.
        """
        pass

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of groups matched by the regular expression.

Get: Groups(self: Match) -> GroupCollection

"""


    Empty = None


class MatchCollection(object, ICollection, IEnumerable):
    """ Represents the set of successful matches found by iteratively applying a regular expression pattern to the input string. """
    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: MatchCollection, array: Array, arrayIndex: int)
            Copies all the elements of the collection to the given array starting at the given index.
        
            array: The array the collection is to be copied into.
            arrayIndex: The position in the array where copying is to begin.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MatchCollection) -> IEnumerator
        
            Provides an enumerator that iterates through the collection.
            Returns: An object that contains all System.Text.RegularExpressions.Match objects within the 
             System.Text.RegularExpressions.MatchCollection.
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of matches.

Get: Count(self: MatchCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the collection is read only.

Get: IsReadOnly(self: MatchCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether access to the collection is synchronized (thread-safe).

Get: IsSynchronized(self: MatchCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that can be used to synchronize access to the collection.

Get: SyncRoot(self: MatchCollection) -> object

"""



class MatchEvaluator(MulticastDelegate, ICloneable, ISerializable):
    """
    Represents the method that is called each time a regular expression match is found during a erload:System.Text.RegularExpressions.Regex.Replace method operation.
    
    MatchEvaluator(object: object, method: IntPtr)
    """
    def BeginInvoke(self, match, callback, object):
        """ BeginInvoke(self: MatchEvaluator, match: Match, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MatchEvaluator, result: IAsyncResult) -> str """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, match):
        """ Invoke(self: MatchEvaluator, match: Match) -> str """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class Regex(object, ISerializable):
    """
    Represents an immutable regular expression.
    
    Regex(pattern: str)
    Regex(pattern: str, options: RegexOptions)
    Regex(pattern: str, options: RegexOptions, matchTimeout: TimeSpan)
    """
    @staticmethod
    def CompileToAssembly(regexinfos, assemblyname, attributes=None, resourceFile=None):
        """
        CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName, attributes: Array[CustomAttributeBuilder], resourceFile: str)
            Compiles one or more specified System.Text.RegularExpressions.Regex objects and a specified 
             resource file to a named assembly with the specified attributes.
        
        
            regexinfos: An array that describes the regular expressions to compile.
            assemblyname: The file name of the assembly.
            attributes: An array that defines the attributes to apply to the assembly.
            resourceFile: The name of the Win32 resource file to include in the assembly.
        CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName, attributes: Array[CustomAttributeBuilder])
            Compiles one or more specified System.Text.RegularExpressions.Regex objects to a named assembly 
             with the specified attributes.
        
        
            regexinfos: An array that describes the regular expressions to compile.
            assemblyname: The file name of the assembly.
            attributes: An array that defines the attributes to apply to the assembly.
        CompileToAssembly(regexinfos: Array[RegexCompilationInfo], assemblyname: AssemblyName)
            Compiles one or more specified System.Text.RegularExpressions.Regex objects to a named assembly.
        
            regexinfos: An array that describes the regular expressions to compile.
            assemblyname: The file name of the assembly.
        """
        pass

    @staticmethod
    def Escape(str):
        """
        Escape(str: str) -> str
        
            Escapes a minimal set of characters (\, *, +, ?, |, {, [, (,), ^, $,., #, and white space) by 
             replacing them with their escape codes. This instructs the regular expression engine to 
             interpret these characters literally rather than as metacharacters.
        
        
            str: The input string that contains the text to convert.
            Returns: A string of characters with metacharacters converted to their escaped form.
        """
        pass

    def GetGroupNames(self):
        """
        GetGroupNames(self: Regex) -> Array[str]
        
            Returns an array of capturing group names for the regular expression.
            Returns: A string array of group names.
        """
        pass

    def GetGroupNumbers(self):
        """
        GetGroupNumbers(self: Regex) -> Array[int]
        
            Returns an array of capturing group numbers that correspond to group names in an array.
            Returns: An integer array of group numbers.
        """
        pass

    def GroupNameFromNumber(self, i):
        """
        GroupNameFromNumber(self: Regex, i: int) -> str
        
            Gets the group name that corresponds to the specified group number.
        
            i: The group number to convert to the corresponding group name.
            Returns: A string that contains the group name associated with the specified group number. If there is no 
             group name that corresponds to i, the method returns System.String.Empty.
        """
        pass

    def GroupNumberFromName(self, name):
        """
        GroupNumberFromName(self: Regex, name: str) -> int
        
            Returns the group number that corresponds to the specified group name.
        
            name: The group name to convert to the corresponding group number.
            Returns: The group number that corresponds to the specified group name, or -1 if name is not a valid 
             group name.
        """
        pass

    def InitializeReferences(self, *args): #cannot find CLR method
        """
        InitializeReferences(self: Regex)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    @staticmethod
    def IsMatch(input, *__args):
        """
        IsMatch(self: Regex, input: str) -> bool
        
            Indicates whether the regular expression specified in the System.Text.RegularExpressions.Regex 
             constructor finds a match in a specified input string.
        
        
            input: The string to search for a match.
            Returns: true if the regular expression finds a match; otherwise, false.
        IsMatch(self: Regex, input: str, startat: int) -> bool
        
            Indicates whether the regular expression specified in the System.Text.RegularExpressions.Regex 
             constructor finds a match in the specified input string, beginning at the specified starting 
             position in the string.
        
        
            input: The string to search for a match.
            startat: The character position at which to start the search.
            Returns: true if the regular expression finds a match; otherwise, false.
        IsMatch(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> bool
        IsMatch(input: str, pattern: str) -> bool
        
            Indicates whether the specified regular expression finds a match in the specified input string.
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            Returns: true if the regular expression finds a match; otherwise, false.
        IsMatch(input: str, pattern: str, options: RegexOptions) -> bool
        
            Indicates whether the specified regular expression finds a match in the specified input string, 
             using the specified matching options.
        
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            options: A bitwise combination of the enumeration values that provide options for matching.
            Returns: true if the regular expression finds a match; otherwise, false.
        """
        pass

    @staticmethod
    def Match(input, *__args):
        """
        Match(self: Regex, input: str) -> Match
        
            Searches the specified input string for the first occurrence of the regular expression specified 
             in the System.Text.RegularExpressions.Regex constructor.
        
        
            input: The string to search for a match.
            Returns: An object that contains information about the match.
        Match(self: Regex, input: str, startat: int) -> Match
        
            Searches the input string for the first occurrence of a regular expression, beginning at the 
             specified starting position in the string.
        
        
            input: The string to search for a match.
            startat: The zero-based character position at which to start the search.
            Returns: An object that contains information about the match.
        Match(self: Regex, input: str, beginning: int, length: int) -> Match
        
            Searches the input string for the first occurrence of a regular expression, beginning at the 
             specified starting position and searching only the specified number of characters.
        
        
            input: The string to search for a match.
            beginning: The zero-based character position in the input string that defines the leftmost position to be 
             searched.
        
            length: The number of characters in the substring to include in the search.
            Returns: An object that contains information about the match.
        Match(input: str, pattern: str) -> Match
        
            Searches the specified input string for the first occurrence of the specified regular expression.
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            Returns: An object that contains information about the match.
        Match(input: str, pattern: str, options: RegexOptions) -> Match
        
            Searches the input string for the first occurrence of the specified regular expression, using 
             the specified matching options.
        
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            options: A bitwise combination of the enumeration values that provide options for matching.
            Returns: An object that contains information about the match.
        Match(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> Match
        """
        pass

    @staticmethod
    def Matches(input, *__args):
        """
        Matches(self: Regex, input: str) -> MatchCollection
        
            Searches the specified input string for all occurrences of a regular expression.
        
            input: The string to search for a match.
            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no 
             matches are found, the method returns an empty collection object.
        
        Matches(self: Regex, input: str, startat: int) -> MatchCollection
        
            Searches the specified input string for all occurrences of a regular expression, beginning at 
             the specified starting position in the string.
        
        
            input: The string to search for a match.
            startat: The character position in the input string at which to start the search.
            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no 
             matches are found, the method returns an empty collection object.
        
        Matches(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> MatchCollection
        Matches(input: str, pattern: str) -> MatchCollection
        
            Searches the specified input string for all occurrences of a specified regular expression.
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no 
             matches are found, the method returns an empty collection object.
        
        Matches(input: str, pattern: str, options: RegexOptions) -> MatchCollection
        
            Searches the specified input string for all occurrences of a specified regular expression, using 
             the specified matching options.
        
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            options: A bitwise combination of the enumeration values that specify options for matching.
            Returns: A collection of the System.Text.RegularExpressions.Match objects found by the search. If no 
             matches are found, the method returns an empty collection object.
        """
        pass

    @staticmethod
    def Replace(input, *__args):
        """
        Replace(input: str, pattern: str, evaluator: MatchEvaluator, options: RegexOptions, matchTimeout: TimeSpan) -> str
        Replace(input: str, pattern: str, evaluator: MatchEvaluator, options: RegexOptions) -> str
        
            Within a specified input string, replaces all strings that match a specified regular expression 
             with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate. Specified 
             options modify the matching operation.
        
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            evaluator: A custom method that examines each match and returns either the original matched string or a 
             replacement string.
        
            options: A bitwise combination of the enumeration values that provide options for matching.
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(input: str, pattern: str, evaluator: MatchEvaluator) -> str
        
            Within a specified input string, replaces all strings that match a specified regular expression 
             with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate.
        
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            evaluator: A custom method that examines each match and returns either the original matched string or a 
             replacement string.
        
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(self: Regex, input: str, evaluator: MatchEvaluator, count: int, startat: int) -> str
        
            Within a specified input substring, replaces a specified maximum number of strings that match a 
             regular expression pattern with a string returned by a 
             System.Text.RegularExpressions.MatchEvaluator delegate.
        
        
            input: The string to search for a match.
            evaluator: A custom method that examines each match and returns either the original matched string or a 
             replacement string.
        
            count: The maximum number of times the replacement will occur.
            startat: The character position in the input string where the search begins.
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(self: Regex, input: str, evaluator: MatchEvaluator, count: int) -> str
        
            Within a specified input string, replaces a specified maximum number of strings that match a 
             regular expression pattern with a string returned by a 
             System.Text.RegularExpressions.MatchEvaluator delegate.
        
        
            input: The string to search for a match.
            evaluator: A custom method that examines each match and returns either the original matched string or a 
             replacement string.
        
            count: The maximum number of times the replacement will occur.
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(self: Regex, input: str, evaluator: MatchEvaluator) -> str
        
            Within a specified input string, replaces all strings that match a specified regular expression 
             with a string returned by a System.Text.RegularExpressions.MatchEvaluator delegate.
        
        
            input: The string to search for a match.
            evaluator: A custom method that examines each match and returns either the original matched string or a 
             replacement string.
        
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(input: str, pattern: str, replacement: str, options: RegexOptions, matchTimeout: TimeSpan) -> str
        Replace(input: str, pattern: str, replacement: str, options: RegexOptions) -> str
        
            Within a specified input string, replaces all strings that match a specified regular expression 
             with a specified replacement string. Specified options modify the matching operation.
        
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            replacement: The replacement string.
            options: A bitwise combination of the enumeration values that provide options for matching.
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(input: str, pattern: str, replacement: str) -> str
        
            Within a specified input string, replaces all strings that match a specified regular expression 
             with a specified replacement string.
        
        
            input: The string to search for a match.
            pattern: The regular expression pattern to match.
            replacement: The replacement string.
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(self: Regex, input: str, replacement: str, count: int, startat: int) -> str
        
            Within a specified input substring, replaces a specified maximum number of strings that match a 
             regular expression pattern with a specified replacement string.
        
        
            input: The string to search for a match.
            replacement: The replacement string.
            count: Maximum number of times the replacement can occur.
            startat: The character position in the input string where the search begins.
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(self: Regex, input: str, replacement: str, count: int) -> str
        
            Within a specified input string, replaces a specified maximum number of strings that match a 
             regular expression pattern with a specified replacement string.
        
        
            input: The string to search for a match.
            replacement: The replacement string.
            count: The maximum number of times the replacement can occur.
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        
        Replace(self: Regex, input: str, replacement: str) -> str
        
            Within a specified input string, replaces all strings that match a regular expression pattern 
             with a specified replacement string.
        
        
            input: The string to search for a match.
            replacement: The replacement string.
            Returns: A new string that is identical to the input string, except that a replacement string takes the 
             place of each matched string.
        """
        pass

    @staticmethod
    def Split(input, *__args):
        """
        Split(self: Regex, input: str) -> Array[str]
        
            Splits the specified input string at the positions defined by a regular expression pattern 
             specified in the System.Text.RegularExpressions.Regex constructor.
        
        
            input: The string to split.
            Returns: An array of strings.
        Split(self: Regex, input: str, count: int) -> Array[str]
        
            Splits the specified input string a specified maximum number of times at the positions defined 
             by a regular expression specified in the System.Text.RegularExpressions.Regex constructor.
        
        
            input: The string to be split.
            count: The maximum number of times the split can occur.
            Returns: An array of strings.
        Split(self: Regex, input: str, count: int, startat: int) -> Array[str]
        
            Splits the specified input string a specified maximum number of times at the positions defined 
             by a regular expression specified in the System.Text.RegularExpressions.Regex constructor. The 
             search for the regular expression pattern starts at a specified character position in the input 
             string.
        
        
            input: The string to be split.
            count: The maximum number of times the split can occur.
            startat: The character position in the input string where the search will begin.
            Returns: An array of strings.
        Split(input: str, pattern: str) -> Array[str]
        
            Splits the input string at the positions defined by a regular expression pattern.
        
            input: The string to split.
            pattern: The regular expression pattern to match.
            Returns: An array of strings.
        Split(input: str, pattern: str, options: RegexOptions) -> Array[str]
        
            Splits the input string at the positions defined by a specified regular expression pattern. 
             Specified options modify the matching operation.
        
        
            input: The string to split.
            pattern: The regular expression pattern to match.
            options: A bitwise combination of the enumeration values that provide options for matching.
            Returns: An array of strings.
        Split(input: str, pattern: str, options: RegexOptions, matchTimeout: TimeSpan) -> Array[str]
        """
        pass

    def ToString(self):
        """
        ToString(self: Regex) -> str
        
            Returns the regular expression pattern that was passed into the Regex constructor.
            Returns: The pattern parameter that was passed into the Regex constructor.
        """
        pass

    @staticmethod
    def Unescape(str):
        """
        Unescape(str: str) -> str
        
            Converts any escaped characters in the input string.
        
            str: The input string containing the text to convert.
            Returns: A string of characters with any escaped characters converted to their unescaped form.
        """
        pass

    def UseOptionC(self, *args): #cannot find CLR method
        """
        UseOptionC(self: Regex) -> bool
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        
            Returns: true if the System.Text.RegularExpressions.Regex.Options property contains the 
             System.Text.RegularExpressions.RegexOptions.Compiled option; otherwise, false.
        """
        pass

    def UseOptionR(self, *args): #cannot find CLR method
        """
        UseOptionR(self: Regex) -> bool
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        
            Returns: true if the System.Text.RegularExpressions.Regex.Options property contains the 
             System.Text.RegularExpressions.RegexOptions.RightToLeft option; otherwise, false.
        """
        pass

    def ValidateMatchTimeout(self, *args): #cannot find CLR method
        """ ValidateMatchTimeout(matchTimeout: TimeSpan) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pattern, options=None, matchTimeout=None):
        """
        __new__(cls: type)
        __new__(cls: type, pattern: str)
        __new__(cls: type, pattern: str, options: RegexOptions)
        __new__(cls: type, pattern: str, options: RegexOptions, matchTimeout: TimeSpan)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MatchTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchTimeout(self: Regex) -> TimeSpan

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the options passed into the System.Text.RegularExpressions.Regex constructor.

Get: Options(self: Regex) -> RegexOptions

"""

    RightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the regular expression searches from right to left.

Get: RightToLeft(self: Regex) -> bool

"""


    CacheSize = 15
    capnames = None
    caps = None
    capsize = None
    capslist = None
    factory = None
    InfiniteMatchTimeout = None
    internalMatchTimeout = None
    pattern = None
    roptions = None


class RegexCompilationInfo(object):
    """
    Provides information about a regular expression that is used to compile a regular expression to a stand-alone assembly.
    
    RegexCompilationInfo(pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool)
    RegexCompilationInfo(pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool, matchTimeout: TimeSpan)
    """
    @staticmethod # known case of __new__
    def __new__(self, pattern, options, name, fullnamespace, ispublic, matchTimeout=None):
        """
        __new__(cls: type, pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool)
        __new__(cls: type, pattern: str, options: RegexOptions, name: str, fullnamespace: str, ispublic: bool, matchTimeout: TimeSpan)
        """
        pass

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the compiled regular expression has public visibility.

Get: IsPublic(self: RegexCompilationInfo) -> bool

Set: IsPublic(self: RegexCompilationInfo) = value
"""

    MatchTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchTimeout(self: RegexCompilationInfo) -> TimeSpan

Set: MatchTimeout(self: RegexCompilationInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the type that represents the compiled regular expression.

Get: Name(self: RegexCompilationInfo) -> str

Set: Name(self: RegexCompilationInfo) = value
"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the namespace to which the new type belongs.

Get: Namespace(self: RegexCompilationInfo) -> str

Set: Namespace(self: RegexCompilationInfo) = value
"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the options to use when compiling the regular expression.

Get: Options(self: RegexCompilationInfo) -> RegexOptions

Set: Options(self: RegexCompilationInfo) = value
"""

    Pattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the regular expression to compile.

Get: Pattern(self: RegexCompilationInfo) -> str

Set: Pattern(self: RegexCompilationInfo) = value
"""



class RegexMatchTimeoutException(TimeoutException, ISerializable, _Exception):
    """
    RegexMatchTimeoutException(regexInput: str, regexPattern: str, matchTimeout: TimeSpan)
    RegexMatchTimeoutException()
    RegexMatchTimeoutException(message: str)
    RegexMatchTimeoutException(message: str, inner: Exception)
    """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, regexInput: str, regexPattern: str, matchTimeout: TimeSpan)
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Input(self: RegexMatchTimeoutException) -> str

"""

    MatchTimeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchTimeout(self: RegexMatchTimeoutException) -> TimeSpan

"""

    Pattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pattern(self: RegexMatchTimeoutException) -> str

"""



class RegexOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides enumerated values to use to set regular expression options.
    
    enum (flags) RegexOptions, values: Compiled (8), CultureInvariant (512), ECMAScript (256), ExplicitCapture (4), IgnoreCase (1), IgnorePatternWhitespace (32), Multiline (2), None (0), RightToLeft (64), Singleline (16)
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

    Compiled = None
    CultureInvariant = None
    ECMAScript = None
    ExplicitCapture = None
    IgnoreCase = None
    IgnorePatternWhitespace = None
    Multiline = None
    None = None
    RightToLeft = None
    Singleline = None
    value__ = None


class RegexRunner(object):
    """ The System.Text.RegularExpressions.RegexRunner class is the base class for compiled regular expressions. """
    def Capture(self, *args): #cannot find CLR method
        """
        Capture(self: RegexRunner, capnum: int, start: int, end: int)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def CharInClass(self, *args): #cannot find CLR method
        """
        CharInClass(ch: Char, charClass: str) -> bool
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method. Determines whether a 
             character is in a character class.
        
        
            ch: A character to test.
            charClass: The internal name of a character class.
            Returns: true if the ch parameter is in the character class specified by the charClass parameter.
        """
        pass

    def CharInSet(self, *args): #cannot find CLR method
        """
        CharInSet(ch: Char, set: str, category: str) -> bool
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def CheckTimeout(self, *args): #cannot find CLR method
        """ CheckTimeout(self: RegexRunner) """
        pass

    def Crawl(self, *args): #cannot find CLR method
        """
        Crawl(self: RegexRunner, i: int)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def Crawlpos(self, *args): #cannot find CLR method
        """
        Crawlpos(self: RegexRunner) -> int
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def DoubleCrawl(self, *args): #cannot find CLR method
        """
        DoubleCrawl(self: RegexRunner)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def DoubleStack(self, *args): #cannot find CLR method
        """
        DoubleStack(self: RegexRunner)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def DoubleTrack(self, *args): #cannot find CLR method
        """
        DoubleTrack(self: RegexRunner)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def EnsureStorage(self, *args): #cannot find CLR method
        """
        EnsureStorage(self: RegexRunner)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def FindFirstChar(self, *args): #cannot find CLR method
        """
        FindFirstChar(self: RegexRunner) -> bool
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def Go(self, *args): #cannot find CLR method
        """
        Go(self: RegexRunner)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def InitTrackCount(self, *args): #cannot find CLR method
        """
        InitTrackCount(self: RegexRunner)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def IsBoundary(self, *args): #cannot find CLR method
        """
        IsBoundary(self: RegexRunner, index: int, startpos: int, endpos: int) -> bool
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def IsECMABoundary(self, *args): #cannot find CLR method
        """
        IsECMABoundary(self: RegexRunner, index: int, startpos: int, endpos: int) -> bool
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def IsMatched(self, *args): #cannot find CLR method
        """
        IsMatched(self: RegexRunner, cap: int) -> bool
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def MatchIndex(self, *args): #cannot find CLR method
        """
        MatchIndex(self: RegexRunner, cap: int) -> int
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def MatchLength(self, *args): #cannot find CLR method
        """
        MatchLength(self: RegexRunner, cap: int) -> int
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def Popcrawl(self, *args): #cannot find CLR method
        """
        Popcrawl(self: RegexRunner) -> int
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def Scan(self, *args): #cannot find CLR method
        """
        Scan(self: RegexRunner, regex: Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool, timeout: TimeSpan) -> Match
        Scan(self: RegexRunner, regex: Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool) -> Match
        
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def TransferCapture(self, *args): #cannot find CLR method
        """
        TransferCapture(self: RegexRunner, capnum: int, uncapnum: int, start: int, end: int)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    def Uncapture(self, *args): #cannot find CLR method
        """
        Uncapture(self: RegexRunner)
            Used by a System.Text.RegularExpressions.Regex object generated by the 
             erload:System.Text.RegularExpressions.Regex.CompileToAssembly method.
        """
        pass

    runcrawl = None
    runcrawlpos = None
    runmatch = None
    runregex = None
    runstack = None
    runstackpos = None
    runtext = None
    runtextbeg = None
    runtextend = None
    runtextpos = None
    runtextstart = None
    runtrack = None
    runtrackcount = None
    runtrackpos = None


class RegexRunnerFactory(object):
    """ Creates a System.Text.RegularExpressions.RegexRunner class for a compiled regular expression. """
    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: RegexRunnerFactory) -> RegexRunner
        
            When overridden in a derived class, creates a System.Text.RegularExpressions.RegexRunner object 
             for a specific compiled regular expression.
        
            Returns: A System.Text.RegularExpressions.RegexRunner object designed to execute a specific compiled 
             regular expression.
        """
        pass


