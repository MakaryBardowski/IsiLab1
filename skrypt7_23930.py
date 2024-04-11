import utils.obliczenia as obl
def task7a(floored):
    return obl.floor(float(floored))

def task7b(ceiled):
    return obl.ceil(float(ceiled))

def task7c(deg):
    return obl.degToRad(float(deg))

def task7d(rad):
    return obl.radToDeg(float(rad))

if __name__ == "__main__":
    radToDeg = input("podaj kat w radianach do zamiany na stopnie: ")
    degToRad = input("podaj kat w stopniach do zamiany na radiany: ")
    ceilFloor = input("podaj liczbe do sufitu/podlogi: ")
    print("podloga: " + (str( task7a(ceilFloor) )))
    print("sufit: " + (str( task7b(ceilFloor) )))

    print(task7c(degToRad))
    print(task7d(radToDeg))

