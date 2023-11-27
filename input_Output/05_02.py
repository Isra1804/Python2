valeurFile = open("valeur.txt")
outputFile = open("outputs.txt", "wt")
phrase = " "

for index, line in enumerate(valeurFile):
     if index == 0:
        phrase += " " + line.strip()
     elif index == 2:
        phrase += " " + line.strip()
     else:
        phrase += " " + line.strip().lower()
print(phrase)

   
print(phrase, file=outputFile)
outputFile.close()




