
"""
LinkedNode:
    value: T
    next: LinkedNode

that forms this structure

      > 2 -> 3
    /         \
   1          5
    \         /
     7 <- 6 <

---

FOR LATER:
What I want is a function that will transform any arbitrary datum into this form.
- get_value(LinkedNode): T
- get_next(LinkedNode): LinkedNode

"""

def check_cycle(some_node):
    """
    Arguments:
    ----
    some_node - A node in the self-referential linked list, that therefore has
                a "last" node that points to the "head" node.
    """
    pass
