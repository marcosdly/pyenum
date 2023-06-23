# PyEnum

## Roadmap

- [ ] Each member is of its own type [^1]
- [ ] Member must be handled at least once inside match context [^1]
  - [ ] Loose handling (just accessing the member is enough)
  - [ ] Strict handling (must be explicitly signalized in some way)
- [ ] Enum object cannot be instantiated or subclassed, but can be implemented (`impl`)
  - [ ] Implementation cannot be instantiated or subclassed [^DEBATABLE]
- [ ] Allowed types can be constrained [^1]
- [ ] Member creation mechanism
  - [ ] Protocolled [^1]
  - [ ] Can be wrapped to return processed values
- [ ] Member values can be automatically generated
  - [ ] Primitive types (int, float, str, etc) [^1]
  - [ ] Built-in objects (dict, set, list, etc) [^DEBATABLE]
  - [ ] User-defined objects [^DEBATABLE]
- [ ] Members can be assigned mannualy:
  - [ ] Imperativelly [^1]
  - [ ] Declarativelly
  - [ ] Functionally
- [ ] Members can be assigned automatically:
  - [ ] Imperativelly [^1]
  - [ ] Declarativelly
  - [ ] Functionally

---

[^1]: Must be present in the first official release (`0.1.0`).
[^DEBATABLE]: Uncertain. Can be modified or deleted later, unless end up being implemented.
