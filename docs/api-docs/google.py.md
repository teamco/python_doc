<!-- markdownlint-disable -->

<a href="https://github.com/teamco/python_doc/blob/main/google.py/google.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `google.py`
Example Google style docstrings. 

This module demonstrates documentation as specified by the `Google Python Style Guide`_. Docstrings may extend over multiple lines. Sections are created with a section header and a colon followed by a block of indented text. 



**Example:**
  Examples can be given using either the ``Example`` or ``Examples``  sections. Sections support any reStructuredText formatting, including literal blocks:
``` 

         $ python example_google.py 

```
Section breaks are created by resuming unindented text. Section breaks are also implicitly created anytime a new section starts. 



**Attributes:**
 
 - <b>`module_level_variable1`</b> (int):  Module level variables may be documented in  either the ``Attributes`` section of the module docstring, or in an  inline docstring immediately following the variable. 

 Either form is acceptable, but the two should not be mixed. Choose  one convention to document module level variables and be consistent  with it. 



**Todo:**
 * For module TODOs * You have to also use ``sphinx.ext.todo`` extension 

.. _Google Python Style Guide: http://google.github.io/styleguide/pyguide.html 

**Global Variables**
---------------
- **module_level_variable1**
- **module_level_variable2**

---

<a href="https://github.com/teamco/python_doc/blob/main/google.py/google.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `function_with_types_in_docstring`

```python
function_with_types_in_docstring(param1, param2)
```

Example function with types documented in the docstring. 

`PEP 484`_ type annotations are supported. If attribute, parameter, and return types are annotated according to `PEP 484`_, they do not need to be included in the docstring: 



**Args:**
 
 - <b>`param1`</b> (int):  The first parameter. 
 - <b>`param2`</b> (str):  The second parameter. 



**Returns:**
 
 - <b>`bool`</b>:  The return value. True for success, False otherwise. 

.. _PEP 484: 
 - <b>`https`</b>: //www.python.org/dev/peps/pep-0484/ 


---

<a href="https://github.com/teamco/python_doc/blob/main/google.py/google.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `function_with_pep484_type_annotations`

```python
function_with_pep484_type_annotations(param1: int, param2: str) → bool
```

Example function with PEP 484 type annotations. 



**Args:**
 
 - <b>`param1`</b>:  The first parameter. 
 - <b>`param2`</b>:  The second parameter. 



**Returns:**
 The return value. True for success, False otherwise. 


---

<a href="https://github.com/teamco/python_doc/blob/main/google.py/google.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `module_level_function`

```python
module_level_function(param1, param2=None, *args, **kwargs)
```

This is an example of a module level function. 

Function parameters should be documented in the ``Args`` section. The name of each parameter is required. The type and description of each parameter is optional, but should be included if not obvious. 

If \*args or \*\*kwargs are accepted, they should be listed as ``*args`` and ``**kwargs``. 

The format for a parameter is:
``` 

     name (type): description          The description may span multiple lines. Following          lines should be indented. The "(type)" is optional. 

         Multiple paragraphs are supported in parameter          descriptions. 

```


**Args:**
 
 - <b>`param1`</b> (int):  The first parameter. 
 - <b>`param2`</b> (:obj:`str`, optional):  The second parameter. Defaults to None.  Second line of description should be indented. 
 - <b>`*args`</b>:  Variable length argument list. 
 - <b>`**kwargs`</b>:  Arbitrary keyword arguments. 



**Returns:**
 
 - <b>`bool`</b>:  True if successful, False otherwise. 

The return type is optional and may be specified at the beginning of the ``Returns`` section followed by a colon. 

The ``Returns`` section may span multiple lines and paragraphs. Following lines should be indented to match the first line. 

The ``Returns`` section supports any reStructuredText formatting, including literal blocks:
``` 

         {              'param1': param1,              'param2': param2          } 

```


**Raises:**
 
 - <b>`AttributeError`</b>:  The ``Raises`` section is a list of all exceptions  that are relevant to the interface. 
 - <b>`ValueError`</b>:  If `param2` is equal to `param1`. 


---

<a href="https://github.com/teamco/python_doc/blob/main/google.py/google.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `example_generator`

```python
example_generator(n)
```

Generators have a ``Yields`` section instead of a ``Returns`` section. 



**Args:**
 
 - <b>`n`</b> (int):  The upper limit of the range to generate, from 0 to `n` - 1. 



**Yields:**
 
 - <b>`int`</b>:  The next number in the range of 0 to `n` - 1. 



**Examples:**
 Examples should be written in doctest format, and should illustrate how to use the function. 

``` print([i for i in example_generator(4)])```
    [0, 1, 2, 3]



---

## <kbd>class</kbd> `ExampleClass`
The summary line for a class docstring should fit on one line. 

If the class has public attributes, they may be documented here in an ``Attributes`` section and follow the same formatting as a function's ``Args`` section. Alternatively, attributes may be documented inline with the attribute's declaration (see __init__ method below). 

Properties created with the ``@property`` decorator should be documented in the property's getter method. 



**Attributes:**
 
 - <b>`attr1`</b> (str):  Description of `attr1`. 
 - <b>`attr2`</b> (:obj:`int`, optional):  Description of `attr2`. 

<a href="https://github.com/teamco/python_doc/blob/main/google.py/google.py#L203"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(param1, param2, param3)
```

Example of docstring on the __init__ method. 

The __init__ method may be documented in either the class level docstring, or as a docstring on the __init__ method itself. 

Either form is acceptable, but the two should not be mixed. Choose one convention to document the __init__ method and be consistent with it. 



**Note:**

> Do not include the `self` parameter in the ``Args`` section. 
>

**Args:**
 
 - <b>`param1`</b> (str):  Description of `param1`. 
 - <b>`param2`</b> (:obj:`int`, optional):  Description of `param2`. Multiple  lines are supported. 
 - <b>`param3`</b> (:obj:`list` of :obj:`str`):  Description of `param3`. 


---

#### <kbd>property</kbd> readonly_property

str: Properties should be documented in their getter method. 

---

#### <kbd>property</kbd> readwrite_property

:obj:`list` of :obj:`str`: Properties with both a getter and setter should only be documented in their getter method. 

If the setter method contains notable behavior, it should be mentioned here. 



---

<a href="https://github.com/teamco/python_doc/blob/main/google.py/google.py#L251"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `example_method`

```python
example_method(param1, param2)
```

Class methods are similar to regular functions. 



**Note:**

> Do not include the `self` parameter in the ``Args`` section. 
>

**Args:**
 
 - <b>`param1`</b>:  The first parameter. 
 - <b>`param2`</b>:  The second parameter. 



**Returns:**
 True if successful, False otherwise. 


---

## <kbd>class</kbd> `ExampleError`
Exceptions are documented in the same way as classes. 

The __init__ method may be documented in either the class level docstring, or as a docstring on the __init__ method itself. 

Either form is acceptable, but the two should not be mixed. Choose one convention to document the __init__ method and be consistent with it. 



**Note:**

> Do not include the `self` parameter in the ``Args`` section. 
>

**Args:**
 
 - <b>`msg`</b> (str):  Human readable string describing the exception. 
 - <b>`code`</b> (:obj:`int`, optional):  Error code. 



**Attributes:**
 
 - <b>`msg`</b> (str):  Human readable string describing the exception. 
 - <b>`code`</b> (int):  Exception error code. 

<a href="https://github.com/teamco/python_doc/blob/main/google.py/google.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(msg, code)
```

:param msg: :param code: 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
