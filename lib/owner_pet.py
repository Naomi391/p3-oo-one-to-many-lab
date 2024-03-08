class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added as pets.")
        pet.owner = self

    def get_sorted_pets(self):
        owned_pets = self.pets()
        return sorted(owned_pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Allowed types: {}".format(", ".join(self.PET_TYPES)))
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all.append(self)

