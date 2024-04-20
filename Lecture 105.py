class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")


class Car(Vehicle):

    def sayHello(self):
        print("Hello World")



class PickUp(Vehicle):
    licenseCode = "1111"
    serialCode = ""
    Color = ""
    def Blue(self):
        print("Blue")
class Van(Vehicle):
    licenseCode = ""
    serialCode = ""
    Color = ""

    def red(self):
        print("Red")
class EsateCar(Vehicle):
    licenseCode = ""
    serialCode = ""
    Color = ""

    def Gray(self):
        print("Gray")

say1 = Car
say1.turnOnAirConditioner(Vehicle)
say1.sayHello(self=Car)


van1 = Van
van1.turnOnAirConditioner(Vehicle)
van1.red(self=Van)


pickUp1 = PickUp
pickUp1.turnOnAirConditioner(Vehicle)
pickUp1.Blue(self=PickUp)

EsateCar1 = EsateCar
EsateCar1.turnOnAirConditioner(Vehicle)
EsateCar1.Gray(self=EsateCar)

