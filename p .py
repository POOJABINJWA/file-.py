# a=open("nikita .txt","w")
# a.write("nikita verma")
# print(a)

# a=open("nikita .txt","r")
# s=a.read()
# print(s)

# a=open("pooja.txt","x")

# a=open("shubham love","x")

# import os
# os.remove("shubham love") 

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 