s:str ="   Python is fun!   "

#strip
s = "   Python is fun!   "
stripped_string = s.strip()
print(stripped_string)  

# Output: "Python is fun!"

#left justify

left_justified = stripped_string.ljust(20, '*')
print(left_justified)  

# Output: "Python is fun!*******"

#right justify

right_justified = stripped_string.rjust(20, '*')
print(right_justified)  

# Output: "*******Python is fun!"
