import time
start_time = time.time()
time.time() - start_time
int(time.time() - start_time)

print("What is your name?")
myName = input()
print("Hello, " + myName + ". That is a good name. How old are you?")
myAge = int(input())
programAge = int(time.time() - start_time)
print("%s? Thats funny, Im only a few seconds old." % (myAge, programAge))
print("I wish I was %s years old" % (myAge * 2 ))

time.sleep(3)
print("I'm tired. I go sleep sleep now.")