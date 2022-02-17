import os
def cls():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])
cls()
banner = '\n ##################################\n'
banner += ' # Zip Password Breaker (BruteZip) #\n'
banner += ' ###################################\n'
banner += ' # Coded By MnQazi                 #\n'
banner += ' ###################################\n'
banner += ' # HackingOnItsPeak                #\n'
banner += ' ###################################\n'
banner += ' GitHub: https://github.com/mnqazi/BruteZip\n\n\n'
banner += ' [1] Start BruteZip\n'
banner += ' [0] Exit\n'
print banner

a=input(" [?] Enter 1 to Start : ")
if a==0:
 import os
 cls()
 print " [!] Good Bye :)"
 quit()
elif a==1:
 #!/usr/bin/python

 import zipfile
 import os
 from time import time
 
 cls()
 textzippass = '''
 #########################################
 # Zip Password Breaker    (BruteZip)    #
 #########################################
 #  Coded By MnQazi                      #
 #  HackingOnItsPeak                     #
 #########################################
 '''
 print textzippass
 file_path = raw_input (" [+] Please Enter Your ZIP File Path: ")
 print ""
 word_list = raw_input (" [+] Please Enter your wordlist path(TXT file): ")
 def main(file_path, word_list):
	try:
		zip_ = zipfile.ZipFile(file_path)
	except zipfile.BadZipfile:
		print " [!] ZIP File is Not Valid. Please Enter correct path or valid file."
		quit()

	password = None 
	i = 0 
	c_t = time()
        print " Please wait..! Cracking Begins.! "
	with open(word_list, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			i += 1
			password = x.split("\n")[0]  
			try:
				zip_.extractall(pwd=password)
				t_t = time() - c_t 
				print "\n Congrats.! We Got it. \n Password: "+password+"\n" 
				print " Just in %f seconds. We Tried, %i attempts per second." % (t_t,i/t_t)
				quit()
			except Exception:
				pass
		print " [X] Not found.! Really Sorry, Please Try with another wordlist"
		quit()
 main(file_path, word_list)