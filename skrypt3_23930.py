def task3(string1, string2):
    return string2.find(string1)

if __name__ == "__main__":
    found = input("podaj string ktorego index trzeba znalezc: ")
    target = input("podaj string, w ktorm ten index ma wystapic: ")
    print( task3(found,target) )

