def task4(string1, string2):
    indices = []
    start_index = 0
    
    while True:
        index = string2.find(string1, start_index)
        if index == -1:
            break
        indices.append(index)
        start_index = index+1

    if indices:
        return indices
   
    return -1

if __name__ == "__main__":
    found = input("podaj string ktorego indexy trzeba znalezc: ")
    target = input("podaj string, w ktorm te stringi maja wystapic: ")
    print( task4(found,target) )

