import calc
class Main:
    def __init__(self,a,b):
        self.common = ["Hello"]
        self.greet = "Hey guys!"
        self.a = a
        self.b = b
        # self.res = 0

    def display(self):
        print(self.greet)

    def changeGreeting(self):
        self.greet = "Hello guys!"

    def calculation(self,a,b):
        cal = calc.Calculate
        self.res = cal.addition(a,b)
        # print(res)

    def getResult(self):
        return self.res

main = Main(1,2)
main2 = Main(1,2)
Main.calculation(main,3,4)
Main.calculation(main2,5,4)
# print(main.__dict__)
# print(main2.__dict__)
# main2 = Main()
# main.common.append("Bolo")
# print(main.common)
# print(main2.common)

# main.common = "Hi"
# print(main.common)
# print(main2.common)
# print(Main.common)
# Main.common = "Hola Amigos!"
# print(main.common)
# print(main2.common)
# print(Main.common)
# main.display()
# main2.changeGreeting()
# main2.display()
# main.display()

# Main.display()