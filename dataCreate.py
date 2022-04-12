import random
import configparser
config=configparser.ConfigParser()
list1=range(0,50)
random.SystemRandom(random.random())
for n in list1:
	config[str(n)]={"value:" : str(random.randrange(1,50))}

db=open("data.ini","w+")
config.write(db)
