from networkx.utils.backends import _dispatch

@_dispatch
def rooted_tree_isomorphism(t1, root1, t2, root2): ...
@_dispatch
def tree_isomorphism(t1, t2): ...
