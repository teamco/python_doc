<!-- markdownlint-disable -->

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `building.py`




**Global Variables**
---------------
- **building**
- **floor1**
- **floor2**
- **floor3**
- **room1**


---

## <kbd>class</kbd> `Crud`




<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L2"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__()
```








---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `create`

```python
create(entity_type)
```





---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `print_all`

```python
print_all()
```





---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `read`

```python
read(idx)
```





---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `remove`

```python
remove(idx)
```





---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update`

```python
update(idx, value)
```






---

## <kbd>class</kbd> `Entity`




<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(entity_type, parent)
```

This is an example of a module level function. 

Function parameters should be documented in the ``Args`` section. The name of each parameter is required. The type and description of each parameter is optional, but should be included if not obvious. 

If \*args or \*\*kwargs are accepted, they should be listed as ``*args`` and ``**kwargs``. 

The format for a parameter is:
``` 

```
name (type): description  The description may span multiple lines. Following  lines should be indented. The "(type)" is optional. 

 Multiple paragraphs are supported in parameter  descriptions. 



**Args:**
 self (Class, optional): The first parameter. entity_type (:obj:`str`): The second parameter - Entity name.  Second line of description should be indented. parent (:obj:class): The last parameter - Parent class instance. Defaults to None. *args: Variable length argument list. **kwargs: Arbitrary keyword arguments. 



**Returns:**
 bool: True if successful, False otherwise. 

The return type is optional and may be specified at the beginning of the ``Returns`` section followed by a colon. 

The ``Returns`` section may span multiple lines and paragraphs. Following lines should be indented to match the first line. 

The ``Returns`` section supports any reStructuredText formatting, including literal blocks:
``` 

     {          'param1': param1,          'param2': param2      } 

```


**Raises:**
 AttributeError: The ``Raises`` section is a list of all exceptions  that are relevant to the interface. ValueError: If `param2` is equal to `param1`. 




---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `create`

```python
create(entity_type)
```





---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `print_all`

```python
print_all()
```





---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `read`

```python
read(idx)
```





---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `remove`

```python
remove(idx)
```





---

<a href="https://github.com/teamco/python/blob/main/building-api/building.py/building.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update`

```python
update(idx, value)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
