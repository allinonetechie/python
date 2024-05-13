import os

#read
f = open("/Users/waqasahmed/Github Repo/python/python/file/testcontent.txt", "r")

print(f.read())
f.close()
print('\n')

# write text to file
f = open("/Users/waqasahmed/Github Repo/python/python/file/testcontent.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("/Users/waqasahmed/Github Repo/python/python/file/testcontent.txt", "r")
print(f.read())

print('\n')

# create new file

f = open("/Users/waqasahmed/Github Repo/python/python/file/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("/Users/waqasahmed/Github Repo/python/python/file/demofile3.txt", "r")
print(f.read())

print('\n')

os.remove("/Users/waqasahmed/Github Repo/python/python/file/demofile3.txt")