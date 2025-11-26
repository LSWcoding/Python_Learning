#Strings: ordered, immutable, text representation
my_string = "Hello, World!"
print(my_string)  # Output: Hello, World!

#Accessing characters
char = my_string[7]
print(char)  # Output: W

#Slicing
substring = my_string[0:5]
print(substring)  # Output: Hello

#concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!

#iteration
for x in greeting:
    print(x)
# Output:

#Checking membership
if "World" in my_string:
    print("Found 'World' in the string!")
else:
    print("'World' not found in the string.")

#Remove whitespace
whitespace_string = "   Hello, World!   "
trimmed_string = whitespace_string.strip()#the original string remains unchanged
print(trimmed_string)  # Output: Hello, World!

#Conversion to uppercase and lowercase
upper_string = my_string.upper()
print(upper_string)  # Output: HELLO, WORLD!
lower_string = my_string.lower()
print(lower_string)  # Output: hello, world!

#Checking string start and end
starts_with_hello = my_string.startswith("Hello")
print(starts_with_hello)  # Output: True
ends_with_exclamation = my_string.endswith("!")
print(ends_with_exclamation)  # Output: True

#Finding substrings
index = my_string.find("World")
print(index)  # Output: 7 the index is where "World" starts
#-1 will be returned if the substring is not found              

#counting occurrences
count_l = my_string.count("l")
print(count_l)  # Output: 3

#Replacing substrings
new_string = my_string.replace("World", "Python"),will create a new string,the original remains unchanged
print(new_string)  # Output: Hello, Python!

#converting string to list
my_list = my_string.split(", ")#() default splits by whitespace
print(my_list)  # Output: ['Hello', 'World!']

#joining list to string
joined_string = " - ".join(my_list)
print(joined_string)  # Output: Hello - World!

#list join to empty string
no_space_string = "".join(my_list)
print(no_space_string)  # Output: HelloWorld!

#% formatting
var = "Tom"
formatted_string = "Hello, %s!" % var#s is for string
print(formatted_string)  # Output: Hello, Tom!

numbervar = 42
formatted_number_string = "The answer is %d." % numbervar#d is for integer
print(formatted_number_string)  # Output: The answer is 42.

floatvar = 3.14159
formatted_float_string = "Pi is approximately %.2f." % floatvar#f is for float, .2 for 2 decimal places
print(formatted_float_string)  # Output: Pi is approximately 3.14.

#new format() method
formatted_string2 = "Hello, {:.2f} and {}!".format(floatvar,var)#.2f for float with 2 decimal places
#{} and {} ,multiple placeholders for different variables
print(formatted_string2)  # Output: Hello, 3.14159!