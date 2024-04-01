#### Class:

class Tree:

    def __init__(self, label, *children):
        self.__label = label
        self.__children = children

    def getLabel(self):
        return self.__label
    
    def getchildren(self):
        return self.__children
    
    def nb_children(self):
        return len(self.__children)

    def child(self,i):
        if i>=self.nb_children():
            raise IndexError
        return self.__children[i]

    def is_leaf(self):
        return self.nb_children() ==0
    
    def depth(self):
        if self.is_leaf():
            return 0
        return 1+max([child.depth() for child in self.getchildren()])
    
    def __str__(self):
        out = "{}".format(self.__label)
        if self.is_leaf():
            return out
        out +="("
        for child in (self.__children):
            out+=child.__str__() + ","
            # out+="{},".format(child)
        out += ")"
        return out
    
    def __eq__(self,tree):
        #python compare les éléments un par un des tuples en utilisant notre méthode __eq__
        return self.__label == tree.__label and self.__children == tree.__children 

    def deriv(self, variable):
        if self.is_leaf():
            if self.__label == variable:
                return Tree("1")
            return Tree("0")
        # cas où on a un seul enfant
        elif self.nb_children() == 1:
            return self.__children[0].deriv(variable)
        # cas de l'addition
        elif self.__label == '+':
            left_deriv = self.__children[0].deriv(variable)
            right_deriv = self.__children[1].deriv(variable)
            return Tree('+', left_deriv, right_deriv)
         # cas de la multiplication
        elif self.__label == '*':
            left = self.__children[0]
            right = self.__children[1]
            left_deriv = Tree('*', left.deriv(variable), right)
            right_deriv = Tree('*', left, right.deriv(variable))
           
            return Tree('+', left_deriv, right_deriv)
        else:
            # Gérer d'autres types d'opérateurs ici si nécessaire
            return None





#### Fonction:

#### Script/Main:
        
if __name__ == "__main__":
    arbre=Tree("a")
    brbre=Tree("b",arbre)
    print(brbre.nb_children())
    print(brbre.child(0))
    cbre=Tree("*",Tree("X"),Tree("X"))
    dbre=Tree("*",Tree("3"),cbre)
    ebre=Tree("*",Tree("X"),Tree("5"))
    fbre=Tree("+",Tree("7"))
    gbre=Tree("+",dbre,ebre)
    print("Arbre à dériver")
    hbre=Tree("+",gbre,fbre)
    print(hbre.__str__())
    print("Réseultat")
    print((hbre.deriv("X")).__str__())
