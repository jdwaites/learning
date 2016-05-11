'''
f = open("test.txt","r") #opens file with name of "test.txt"
print(f.read(3))
print(f.read())

'''


f = open("test2.txt","w") #opens file with name of "test.txt"
f.write("I am a test file.")
f.write("Maybe someday, he will promote me to a real file.")
f.write("Man, I long to be a real file")
f.write("and hang out with all my new real file friends.") 
f.close()
 
