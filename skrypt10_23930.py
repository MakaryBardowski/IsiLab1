def task10():
    empty = ""
    writeAccess = "w"
    asciiStart = 97
    asciiEnd = 123
    abSeq = [chr(index) for index in range(asciiStart, asciiEnd)] # od 97 do 122 lista charow(index)
    with open("alfabet1-23930.txt", writeAccess) as file: # parametr "w" otwiera plik do zapisu albo go tworzy jesli nie istnieje
        file.write(empty.join(abSeq))
        
    with open("alfabet2-23930.txt", writeAccess) as file:
        for c in abSeq:
            file.write(c+"\n")
    
if __name__ == "__main__":
    task10() #bedzie w folderze usera
