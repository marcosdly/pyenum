import random
import pytest
from faker import Faker
from src import Enum, Member
from exceptions import UnhandledEnumCasesError

fake = Faker()

def gen_enum() -> Enum:
    m = 10 # number of members
    members = {name: Member for name in
               [fake.pystr(max_chars=10, prefix="", suffix="") for _ in range(m)]}
    enum = type("MyEnum", (Enum,), members)
    return enum

class TestLooseHandling:
    def test_all_handled(self):
        try:
            for _ in range(50):
                enum = gen_enum()
                with enum.match() as enum_match:
                    for name in enum_match.meta.members.keys():
                        enum_match[name]
        except UnhandledEnumCasesError:
            pytest.fail("Error occurred even when all cases were handled.")

    def test_none_handled(self):
        for _ in range(50):
            with pytest.raises(UnhandledEnumCasesError):
                enum = gen_enum()
                with enum.match(): pass

    def test_almost_all_handled(self):
        for _ in range(50):
            with pytest.raises(UnhandledEnumCasesError):
                enum = gen_enum()
                handle_num = random.randint(1, len(enum.meta.members.keys())-1)
                with enum.match() as enum_match:
                    for i, name in enumerate(enum_match.meta.members.keys()):
                        if i+1 >= handle_num: break
                        _ = enum_match[name]