#Written by James Dorgan 20000040
#Date: 2020/03/12
#Program to count the number of each vowel in a sence


vowelCount = {'a': 0, 'e': 0, 'i':0 , 'o': 0, 'u':0}

def count(input_string, vowel):
    for i in range(len(input_string)):
        if(input_string[i] == vowel):
            vowelCount[vowel] = vowelCount[vowel] +1

input_string = input('Enter a sentence: ')



count(input_string, 'a')
count(input_string, 'e')
count(input_string, 'i')
count(input_string, 'o')
count(input_string, 'u')

for keys,values in vowelCount.items():
    print(keys, values)
    
x = sum(vowelCount.values())
print("There are {} vowels in this sentence.".format(x))

