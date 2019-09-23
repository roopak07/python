name = raw_input('Enter name with numbers followed by letters:'); # we use "raw_input" for string input ,for interger just use "input"
print("name before modifying:") 
print(name)
mname=name.translate(None,"0123456789") 
print("after modifying:")
print(mname)
