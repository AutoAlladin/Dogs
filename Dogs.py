from Animal import Animal


class Dog(Animal):
    paws =""
    tail = ""
    wool = ""
    mustache = ""

    def look(self):
        self.looking = self.tail+self.body[0]+self.wool+self.body[1]+"-" + self.head+ self.mustache+"\n"+\
                       "   "+self.paws[0]+ self.paws[1]+self.paws[2]+self.paws[3]
        print()
        print(self.looking)

    def __init__(self,
                 h="[[-",
                 p=["| ", "| ", "| ", "| "],
                 t="---",
                 w="******",
                 b="()",
                 m="<"):
        self.body = b
        self.head = h

        self.paws = p
        self.tail = t
        self.wool = w
        self.mustache=m
        pass




    def gav_gav(self):
        return "gav-gav-gav"

    def start_wag_tail(self):

        self.tail= "|_|"
        pass

    def finish_wag_tail(self):

        self.tail= "---"
        pass


