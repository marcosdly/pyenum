from typing import Any, Callable, Self
import utils
from member import Member, ImplicitValue
from dataclasses import dataclass, field
from enum import auto
from type_hints import BaseEnumTyping, MetaInfo, MatchInfo

class EnumMeta(type, BaseEnumTyping):
    _ignored_names: set = set()
    _reserved_class_names: set = set(["match"])
    _prohibited_class_names: set = set(["meta", "already", "not_yet", "all"])

    # TODO make namespace a ordered dict and assign automatically for implicit values

    def __new__(metacls, cls_name: str, bases: tuple, namespace: dict,
                types: tuple = (object,)):
        if len(metacls._ignored_names
               & metacls._reserved_class_names
               & metacls._prohibited_class_names) > 0:
            raise ValueError("Names can only be reserved in one caregory.")
        
        # TODO implement class names and member names in implements

        members = {name: value for name, value in namespace.items()
                   if not (utils.is_sunder(name) or utils.is_dunder(name))}

        for k, v in members.items():
            if k in metacls._ignored_names:
                del namespace[k]
                continue
            elif k in metacls._reserved_class_names: continue
            elif k in metacls._prohibited_class_names:
                raise ValueError(f"'{k}' is among the names that cannot be used as members: {metacls._prohibited_class_names}")
            elif utils.is_surrounded(name=k, howmany=1, strict_check=False):
                # is surrounded by more than 2 underscores
                raise ValueError("_names_ and __names__ are reserved, while ___names___ and so on are prohibited.")
            elif v is Member:
                # implicit value is defined as default value for MEMBER.value, no need for checking
                pass
            elif not v.__class__ is Member: # very strict
                raise TypeError(f"Enum members must be defined using the provided mechanisms. Attribute '{k}' is invalid.")
            elif not isinstance(v.value, types):
                raise TypeError(f"Values for enum members must be instances of the allowed types. Allowed types: {'all' if object in types else types}")
            
            # is a permitted name, created with a permited method, and the value is of correct type
            namespace[k] = type(f"{cls_name}.{k}", (), {"name": k,"value": v.value})

            # TODO add member and class method/attribute system

        namespace["meta"] = MetaInfo(members=members, match=MatchInfo())
        print(cls_name, bases)
        print(namespace)
        enum_class = super().__new__(metacls, cls_name, bases, namespace)
        return enum_class
    
    def __getattr__(self, name: str):
        if name in self.meta.members and self.meta.match.active:
            self.meta.match.already.add(name)
        return super().__getattribute__(name)
    
    def __getitem__(self, name: str):
        if not name in self.meta.members:
            raise ValueError(f"Key access to an Enum is only possible if you're trying to access a member. '{name}' is not a member.")
        if self.meta.match.active:
            self.meta.match.already.add(name)
        return self.meta.members[name]

class MatchMeta(EnumMeta):
    def __new__(metacls, cls_name: str, bases: tuple, namespace: dict, types: tuple = (object, )):
        match_reserved_names: set = set(["already", "not_yet", "all"])
        metacls._prohibited_class_names = match_reserved_names ^ metacls._prohibited_class_names
        metacls._reserved_class_names   = match_reserved_names | metacls._reserved_class_names
        enum = super().__new__(metacls, cls_name, bases, namespace, types)
        enum.meta.match.active = True
        return enum

    def already(self) -> set:
        return self.meta.match.already
    
    def not_yet(self) -> set:
        return set(self.meta.members.keys()) ^ self.meta.match.already
        
    def all(self) -> set:
        return self.already() & self.not_yet() == set(self.meta.members.keys())
