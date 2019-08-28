# Let's use some methods to manipulate the string stored in name.

name = "John Jacob Jingleheimer Schmidt"

# 1. Use print and a built-in method to print out the string "jOHN jACOB jINGLEHEIMER sCHMIDT"

print(name.swapcase())

# 2. Use print and a built-in method to print out the string "JOHN JACOB JINGELHEIMER SCHMIDT"

print(name.upper())

# 3. Use print and a built-in method to count how many times the letter i is in Mr. Schmidt's name.
 
count = name.count('i')
print(count)

# 4. Use print and a built-in method to print out Mr. Schmidt's name, but with all the instances of the letter i removed or deleted.

print (name.replace('i', ""))

# 5. Use print and a built-in function to find out how many characters are in Mr. Schmidt's name.
## NOTE that since this is a funciton and not a method, the best solution won't be on the string methods page - you'll need to Google this one. 

print(str(len(name) - name.count(' ')))

# 6. Use a built-in method to replace every letter J with the letter G instead. Bonus point if you can say the result out loud without laughing.

print (name.replace('J', 'G'))

# 7. Chain a few methods together to print out the string with all the vowels removed. 

def remove_vowels(name): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in name.lower(): 
        if x in vowels: 
            name = name.replace(x, "") 
    print(name) 

# 8. Try to print the name as four separate strings by using a function that will split it up like this: ["John", "Jacob", "Jingleheimer", "Schmidt"]

print (name.replace(" ", ", "))

# 9. Print out only the first four letters of the string.

firstFourLetters = name[:4]
print (firstFourLetters)

# 10. Print out only the first ten letters of the string but make them all uppercase.

firstTenLetters = name[:12]
print(firstTenLetters.upper())

# 11. CHALLENGE: Try to print out the string "tdimhcS remiehelgniJ bocaJ nhoJ" (which is the name backwards)

def reverse(name):
    str = ""
    for i in name:
        str = i + str
    return str
print (reverse(name))
    

# 12. CHALLENGE: Chain two methods together to print out the string "TDIMHCS REMIEHELGNIJ BOCAJ NHOJ", (which is the name in uppercase and backwards).

print (reverse(name).upper())