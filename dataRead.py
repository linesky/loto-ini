import configparser
config=configparser.ConfigParser()
config.read("data.ini")
list1=range(0,50)
for n in list1:
	print (str(n)+"\t"+config[str(n)]["value"])

