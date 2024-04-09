import matplotlib.pyplot as plt

path = "frenchssaccent.dic"

#### Class:

class Hashtable:

    def __init__(self,H,n) -> None:
        self.capacity = n
        self.hashFunc = H
        self.table=[None for i in range (n)]
    
    def put(self, key, value):
        """Insert (key,value) in the table using the hash function"""
        indice = self.hashFunc(key) % self.capacity
        if self.table[indice] is None:
            self.table[indice] = [[key, value]]
        else:
            for pair in self.table[indice]:
                if pair[0] == key:
                    pair[1] = value # modifier la valeur associée à key dans la table
                else:
                    self.table[indice].append((key, value))
        return self.table
    
    def get(self, key):
        indice = self.hashFunc(key) % self.capacity
        if indice < len(self.table) and self.table[indice] is not None:            
            for pair in self.table[indice]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def repartition(self):
        x= [i for i in range (self.capacity)]
        y= [len(self.table[i]) for i in range (self.capacity)]
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()

    def resize(self):
        new_capacity = 2 * self.capacity
        new_table = [None] * new_capacity
        for chain in self.table:
            if chain is not None:
                for key, value in chain:
                    new_index = self.hashFunc(key) % new_capacity
                    if new_table[new_index] is None:
                        new_table[new_index] = [[key, value]]
                    else:
                        new_table[new_index].append([key, value])
        self.capacity = new_capacity
        self.table = new_table
    
#### Fonction:

def hashage_naive(key):
    h = 0
    for c in key:
        h += ord(c)
    return h

# charger les données dans mots_possibles depuis frenchssacent.dic
def read_file(path):
    # charge les données de path dans une liste et retourne la liste
    output = list()
    file = open(path,'r')
    for line in file:
        mot = line[0:len(line)-1]
        if len(mot) <=8:
            output.append(mot) # éliminer les mots de taille >= 8
        # output.append(line[0:len(line)-1])
        # output.append(line.replace("\n",""))
    file.close()        
    return output

#### Script/Main:

if __name__ == "__main__":
    my_table = Hashtable(10,3)
    print(my_table)


        