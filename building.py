class Crud:
    """
    A class to represent a person.

    ...

    Methods
    -------
    create(entity_type):
        Creates entity.

    read(idx):
        Get entity by index.

    update(idx, value):
        Update entity value by index.

    remove(idx):
        Get entity by index.

    print_all():
        Print all collected entities.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the entity object.

        Parameters
        ----------
            index : int
                Item index.
            entity_type : str
                Parent class instance.
            remove_items : list
                Items to remove collector.
            items : list
                Items collector.
        """
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
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    entity_type : str
        Abstract entity name.
    parent : object
        Parent class instance.
    """

    def __init__(self, entity_type, parent):
        """
        Init abstract entity.
            Parameters:
                entity_type (str): Abstract entity name.
                parent (object): Parent class instance. Default is None.
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
