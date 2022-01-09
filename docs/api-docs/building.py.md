<!-- markdownlint-disable -->

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
A class to represent a person. 

... 

Methods 
------- create(entity_type):  Creates entity. 

read(idx):  Get entity by index. 

update(idx, value):  Update entity value by index. 

remove(idx):  Get entity by index. 

print_all():  Print all collected entities. 

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__()
```

Constructs all the necessary attributes for the entity object. 

Parameters 
----------  index : int  Item index.  entity_type : str  Parent class instance.  remove_items : list  Items to remove collector.  items : list  Items collector. 




---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `create`

```python
create(entity_type)
```





---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `print_all`

```python
print_all()
```





---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `read`

```python
read(idx)
```





---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `remove`

```python
remove(idx)
```





---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update`

```python
update(idx, value)
```






---

## <kbd>class</kbd> `Entity`
A class to represent a person. 

... Attributes 
---------- entity_type : str  Abstract entity name. parent : object  Parent class instance. 

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(entity_type, parent)
```

Init abstract entity. 

**Parameters:**
 
     - <b>`entity_type`</b> (str):  Abstract entity name. 
     - <b>`parent`</b> (object):  Parent class instance. Default is None. 




---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `create`

```python
create(entity_type)
```





---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `print_all`

```python
print_all()
```





---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `read`

```python
read(idx)
```





---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `remove`

```python
remove(idx)
```





---

<a href="https://github.com/teamco/python_doc/blob/main/building.py/building.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `update`

```python
update(idx, value)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
