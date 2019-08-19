class Main:
    def __init__(self):
        self.common = ["Hello"]
        self.greet = "Hey guys!"

    def display(self):
        print(self.greet)

    def changeGreeting(self):
        self.greet = "Hello guys!"

main = Main()
main2 = Main()
main.common.append("Bolo")
print(main.common)
print(main2.common)

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