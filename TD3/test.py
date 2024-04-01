import unittest
from tree2 import Tree

#### class:

class TestTree(unittest.TestCase):

    def test_getLabel(self):
        arbre = Tree("+",Tree("1"),Tree("X"))
        self.assertEqual(arbre.getLabel(),"+")

    def test_getchildren(self):
        arbre = Tree("z",Tree("X"),Tree("9"),Tree("A"))
        etiquette = arbre.getchildren()
        self.assertEqual(etiquette[0].getLabel(),"X")
        self.assertEqual(etiquette[1].getLabel(),"9")
        self.assertEqual(etiquette[2].getLabel(),"A")
    
    def test_nb_children(self):
        arbre = Tree("z",Tree("X"),Tree("9"),Tree("A"))
        self.assertEqual(arbre.nb_children(),3)
    
    def test_child(self):
        arbre = Tree("z",Tree("X"),Tree("9"),Tree("A"))
        self.assertEqual(arbre.child(0).getLabel(),"X")
        self.assertEqual(arbre.child(1).getLabel(),"9")
        self.assertEqual(arbre.child(2).getLabel(),"A")

    def test_is_leaf(self):
        arbre=Tree("a")
        self.assertTrue(arbre.is_leaf())

    def test_str(self):
        arbre = Tree("z",Tree("X"),Tree("9"),Tree("A"))
        self.assertEqual(arbre.__str__(),"z(X,9,A,)")

    def test_depth(self):
        arbre = Tree("a")
        brbre = Tree("b",arbre,arbre)
        self.assertEqual(arbre.depth(),0)
        self.assertEqual(brbre.depth(),1)
    
    def test_eq(self):
        arbre = Tree("z",Tree("X"),Tree("9"),Tree("A"))
        brbre = Tree("z",Tree("X"),Tree("9"),Tree("A"))
        crbre = Tree("z",Tree("X"),Tree("9"))
        self.assertTrue(arbre == brbre)
        self.assertFalse(arbre == crbre)
    
    
    
#### Script/Main
        
if __name__ == "__main__":    
    unittest.main()