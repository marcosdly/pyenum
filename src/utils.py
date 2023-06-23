def is_surrounded(name: str, howmany: int, strict_check: bool = True) -> bool:
    """Returns True if the provided name is surrounded by an N amount
    of underscores, as in __name__ (for name=__name__ and N=2). Checks
    can be strict, meaning there needs to be an arbitrary, non-undercore
    character between them; or not, meaning they just need to
    start and end with the N amount of underscores."""
    if howmany <= 0: raise ValueError("Underscore amount must be positive.")
    # avoiding the user of regex to such trivial task
    try:
        if name.startswith("_"*howmany) and name.endswith("_"*howmany):
            if not strict_check:
                return True
            elif name[howmany] != "_" and name[-(howmany+1)] != "_":
                return True
        return False
    except: 
        return False
        
def is_sunder(name: str) -> bool:
    """Returns True if the provided name is a _name_"""
    return is_surrounded(name, 1)

def is_dunder(name: str) -> bool:
    """Returns True is the provided name is a __name__"""
    return is_surrounded(name, 2)