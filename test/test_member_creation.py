import pytest
from src import Enum, Member
from faker import Faker
import random as rand

fake = Faker()

def test_surrounded_above_permitted():
    # max permitted number of underscores to have on each side
    max_unders: int = 2
    for i in [x+1+max_unders for x in range(10)]:
        with pytest.raises(ValueError):
            name = f"{'_'*i}name{'_'*i}"
            _ = type("MyEnum", (Enum,), {name: Member(1)})

def test_key_member_access():
    """Passes if trying to access a non-member throws."""
    for _ in range(50):
        with pytest.raises(ValueError):
            name = fake.word()
            enum = type("MyEnum", (Enum,), {name: Member(1)})
            enum[f"_{name}_"]

# TODO remove whitelisting sunder and dunder methods because they are private in some level
# single underscore for inheritable, and double for private. Custom behaviour must only
# be possible through enum.implement

def test_illegal_mechanisms():
    """Tests if the enum member was created using a
    class/function that IS NOT permitted."""
    for value in fake.pylist(50):
        with pytest.raises(TypeError):
            _ = type("MyEnum", (Enum,), {"MEMBER": value})

def test_legal_mechanisms():
    """Tests if the enum member was created using a
    class/function that IS permitted."""
    for value in fake.pylist(50):
        try:
            _ = type("MyEnum", (Enum,), {"MEMBER": Member(value)})
        except TypeError:
            pytest.fail("Exception was not supposed to be thrown.")

class TestTyping:
    possible_types = [int, float, dict, set, list, str, bool]

    def run(self, types: tuple, enum_types: tuple = None, cases: int = 50) -> None:
        for value in fake.pylist(cases, allowed_types=types):
            _ = type("MyEnum", (Enum,), {"MEMBER": Member(value)},
                     types=(types if enum_types == None else enum_types))

    def gen_type_list(self, possible_types: list) -> set:
        possible_types = list(set(possible_types)) # remove duplicates and keep it a list
        amount = rand.randint(1, len(possible_types)-2) # never takes the whole list
        type_list = set([])
        while len(type_list) < amount:
            type_list.add(rand.choice(possible_types))
        return type_list
        
    def test_legal_types(self):
        """Passes if the member types ARE among the defined legal types."""
        for _ in range(20): 
            try:
                self.run(tuple(self.gen_type_list(self.possible_types)))
            except TypeError:
                pytest.fail("A value wasn't an instance of one of the passed classes.")

    def test_illegal_types(self):
        """Passes if the member types ARE NOT among the defined legal types."""
        for _ in range(20):
            with pytest.raises(TypeError):
                allowed_types = self.gen_type_list(self.possible_types)
                unallowed_types = tuple(allowed_types ^ set(self.possible_types))
                self.run(types=tuple(allowed_types), enum_types=unallowed_types)
