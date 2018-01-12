
class Animal:
    body = ""
    head = ""

    meal = ""
    looking = ""
    lookk = ""
    loo = ""

    def look(self):
        self.looking = self.body + "-" + self.head
        return self.looking

    def __init__(self):
        self.body = "[****]"
        self.head = "(-:"
        pass

    def eat(self, some):
        self.meal = some
        self.body=self.body + "-" + some
        pass

    def shit(self):
        self.body = self.body.replace(self.meal, "")
        pass