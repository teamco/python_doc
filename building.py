class Crud:
    def __init__(self):
        self.index = None
        self.entity_type = None
        self.remove_items = None
        self.items = None

    def create(self, entity_type):
        _entity = self.__class__(entity_type, self)  # Entity(entity_type)
        self.items.append(_entity)
        self.remove_items = []

    def read(self, idx):
        return self.items[idx]

    def update(self, idx, value):
        if len(self.items) == 0:
            self.items.append(value)
        else:
            self.items[idx] = value

    def remove(self, idx):
        print('Start removing', self.entity_type, 'item', self.index, idx)
        items = self.items[idx].items
        while len(items) > 0:
            items[0].parent.remove(0)

        return self.items.pop(idx)

    def print_all(self):
        for i, element in enumerate(self.items):
            if len(element.items) > 0:
                print(element.entity_type, i)
                element.print_all()
            else:
                print(element.entity_type, i)


class Entity(Crud):
    def __init__(self, entity_type, parent):
        """This is an example of a module level function.

Function parameters should be documented in the ``Args`` section. The name
of each parameter is required. The type and description of each parameter
is optional, but should be included if not obvious.

If \*args or \*\*kwargs are accepted,
they should be listed as ``*args`` and ``**kwargs``.

The format for a parameter is::

name (type): description
    The description may span multiple lines. Following
    lines should be indented. The "(type)" is optional.

    Multiple paragraphs are supported in parameter
    descriptions.

Args:
self (Class, optional): The first parameter.
entity_type (:obj:`str`): The second parameter - Entity name.
    Second line of description should be indented.
parent (:obj:class): The last parameter - Parent class instance. Defaults to None.
*args: Variable length argument list.
**kwargs: Arbitrary keyword arguments.

Returns:
bool: True if successful, False otherwise.

The return type is optional and may be specified at the beginning of
the ``Returns`` section followed by a colon.

The ``Returns`` section may span multiple lines and paragraphs.
Following lines should be indented to match the first line.

The ``Returns`` section supports any reStructuredText formatting,
including literal blocks::

    {
        'param1': param1,
        'param2': param2
    }

Raises:
AttributeError: The ``Raises`` section is a list of all exceptions
    that are relevant to the interface.
ValueError: If `param2` is equal to `param1`.

"""
        super().__init__()
        self.entity_type = entity_type
        self.parent = parent
        self.index = 0
        if parent is not None:
            self.index = len(parent.items)
        self.items = []


# Hierarchy = ["Building", "floor", "room", "table"]
building = Entity('Building', None)

# print(building)
# print(building.entity_type)

building.create('floor-1')
building.create('floor-2')
building.create('floor-3')

floor1 = building.read(0)
floor1.create('room-1.1')
# floor1.create('room')

floor2 = building.read(1)
floor2.create('room-2.1')
floor2.create('room-2.2')

floor3 = building.read(2)
floor3.create('room-3.1')

room1 = floor2.read(0)
room1.create('table-2.1.1')
room1.create('trash-2.1.2')

building.print_all()
print("************")
floor2.remove(0)
print("************")
building.print_all()

# building.create('floor')
# print('floors', building.items)

# floor2 = building.read(2)
# print('rooms', floor2.items)
# floor2.update(0, room1)
# floor2.update(0, room1)
# print('rooms', floor2.items)
# print(floor2.items)

# building.remove(1)

# print(building.items)
