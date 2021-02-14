


def calcLetters(stringIn, letter):
    for i in range(len(stringIn)):
        if(stringIn[i] == letter):
            count[letter] = count[letter] +1
count = {'a': 0, 'e': 0, 'i':0 , 'o': 0, 'u':0}
stringIn = input('Enter a sentence: ')
calcLetters(stringIn, 'a')
calcLetters(stringIn, 'e')
calcLetters(stringIn, 'i')
calcLetters(stringIn, 'o')
calcLetters(stringIn, 'u')

for keys,values in count.items():
    print(keys, values)
    
x = str(sum(count.values()))
print("There are" + x + "vowels in this string")

