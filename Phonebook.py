class Phonebook :
    def __init__(self):
        self.__enteries = {}

    def adder(self,*args):
        m = [*args]
        listestr = []
        listeint = []
        for n in m:
            if type (n) == str:
                listestr.append (n)
            if type (n) == int:
                listeint.append (n)
            self.__enteries = dict (zip (listestr, listeint))
        return self.__enteries

    def searcher(self, search_name):
        if search_name in self.__enteries:
            return self.__enteries[search_name]
        else:
            return 'not found'
    def __str__(self) :
        return  'Phonebook' + str(self.__enteries) + '!'
    def __repr__(self) :
        return  self.__str__ ()
    def len (self) :
        return len(self.__enteries)
   

