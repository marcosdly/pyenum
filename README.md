# PyEnum

## Roadmap

- [ ] Each member is of its own type
- [ ] Member must be handled at least once inside match context
  - [ ] Loose handling (just accessing the member is enough)
  - [ ] Strict handling (must be explicitly signalized in some way)
- [ ] Enum object cannot be instantiated or subclassed, but can be implemented (`impl`)
  - [ ] Implementation cannot be instantiated or subclassed (_Debatable_)
- [ ] Allowed types can be contrained
- [ ] Member creation API is standardized
  - [ ] Can be wrapped to return processed values
- [ ] Member values can be automtically generated
  - [ ] Primitive types (int, float, str, etc)
  - [ ] Built-in objects (dict, set, list, etc) (_Debatable_)
  - [ ] User-defined objects (_Debatable_)
- [ ] Members can be assigned mannualy:
  - [ ] Imperativelly
  - [ ] Declarativelly
  - [ ] Functionally
- [ ] Members can be assigned automatically:
  - [ ] Imperativelly
  - [ ] Declarativelly
  - [ ] Functionally
