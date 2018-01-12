from Animal import Animal


class Dog(Animal):
    paws =[]
    tail = ""
    wool = ""
    mustache = ""

    def look(self):
        self.looking = "\033[31m"+self.tail+self.body[0]+"\033[5m"+"\033[96m"+self.wool+"\033[25m"+"\033[0m"+"\033[31m"+self.body[1]+"-" + self.head+ self.mustache+"\n"+\
                       "   "+"\033[32m"+self.paws[0]+ self.paws[1]+self.paws[2]+self.paws[3]+"\033[0m"
        print()
        print(self.looking)

    def look_dog(self):
        self.loo = self.str_1+"\n"+self.str_2+"\n"+self.str_3+"\n"+self.str_4
        print()
        print(self.loo)



    def __init__(self,
                 h="[[-",
                 p=["| ", "| ", "| ", "| "],
                 t="---",
                 w="******",
                 b="()",
                 m="<",
                 str1 = "            __",
                 str2 = "(\,--------_()'--o",
                 str3 = " (_    ___    /~\"",
                 str4 = "  (_)_)  (_)_)",

                 str_1 = "  __    __",
                 str_2 = "o-''))_____\\",
                 str_3 = "\"--__/ * * * )",
                 str_4 = "c_c__/-c____/"
                 ):
        self.body = b
        self.head = h
        self.paws = p
        self.tail = t
        self.wool = w
        self.mustache=m
        self.str1 = str1
        self.str2 = str2
        self.str3 = str3
        self.str4 = str4
        self.str_1 = str_1
        self.str_2 = str_2
        self.str_3 = str_3
        self.str_4 = str_4



    def look_dog2(self):
        self.lookk = self.str1 +"\n"+self.str2 +"\n" +self.str3 +"\n" +self.str4
        print()
        print(self.lookk)


    def gav_gav(self):
        return "gav-gav-gav"

    def start_wag_tail(self):

        self.tail= "|_|"
        return self.tail

    def finish_wag_tail(self):

        self.tail= "---"
        pass


