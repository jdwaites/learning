print "Try to guess a number in my list"
print "If you win you are smart, but not smarter then me :) "

number1 = raw_input( "Please enter your guess " )
number1 = int(number1)

mynumber = 10

def compareThem(number1, mynumber):
    if number1 == mynumber:
        script = "%d is my number...Good Job!!" % (number1)
	
    if number1 != mynumber:
        script =  "%d is not my number loser" % (number1)
	    
    return script

print compareThem(number1, mynumber)
