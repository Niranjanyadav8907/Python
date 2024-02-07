
# raise errors example 1
# NotImplemented error
#abstract method

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        #return 'this is animal sound' # raise error pass krane pr
        raise NotImplemented('you have to define this method in subclass')
    

class Dog(Animal):
    def __init__(self, name, breed):
        super(). __init__(name)
        self.breed = breed

    def sound(self): # method difine 
        return'bhow bhow'


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self): # method difine
        return 'meao meao'


doggy = Dog('boony', 'pug')
print(doggy.sound())