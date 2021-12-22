init python:
    class Ability:
        def __init__(self, name, description, cost):
            self._name = name
            self._description = description
            self._cost = cost

        # Getters
        @property
        def name(self):
            return self._name
        
        @property 
        def description(self):
            return self._description
        
        @property
        def cost(self):
            return self._cost

        # Setters
        @name.setter
        def name(self, name):
            self._name = name

        @description.setter
        def description(self, description):
            self._description = description

        @cost.setter
        def cost(self, cost):
            self._cost = cost

        # Deleters
        @name.deleter
        def name(self):
            del self._name

        @description.deleter
        def description(self):
            del self._description

        @cost.deleter
        def cost(self):
            del self._cost