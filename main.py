with open ('file.txt',"w") as f:
    f.write("WOW!OK!COOL!SUPER!")
print(f)

with open ('file.txt',"r") as file:
  data=file.readlines()
  for lines in data:
    word=lines.split()
    print(word)