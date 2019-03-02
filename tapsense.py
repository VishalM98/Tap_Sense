import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
input_file = ""
output_file = ""
for no in range(1,55):
	input_file = "/home/luciffer/Downloads/user_data/user"
	if no<10:
		input_file += "0"+str(no)
	else:
		input_file += str(no)
	output_file = input_file+"/user"+str(no)+"_output.txt"
	input_file += "/user"+str(no)+".txt"
	print(input_file)
	f = open(output_file,"w")
	data = pd.read_csv(input_file, sep=",", header=None)
	data.columns = ["a", "b", "c", "d", "e", "f","g","h", "i"]
	dat = np.log(1+data['h'])
	dat = dat.values
	k = dat.size
	a = min(dat)
	b = max(dat)
	class1 = []
	class2 = []
	for i in range(100):
		class1.clear()
		class2.clear()
		for j in range(k):
			dis_a = abs(dat[j]-a)
			dis_b = abs(dat[j]-b)
			if(dis_a<dis_b):
				class1.append(j)
			else:
				class2.append(j)
		a = 0
		b = 0
		for e in class1:
			a += dat[e]
		a = a/(len(class1))

		for e in class2:
			b += dat[e]
		b = b/(len(class2))
	phi = 0
	if a<b:
		phi = max(dat[j] for j in class1)
	else:
		phi = max(dat[j] for j in class2)
	L = []
	l_phi = []  
	ind = []
	for i in range(1,max(data['a'])+1):
		print(i)
		dat = np.log(1+data.loc[data['a'] == i]['h'])
		dat = dat.values
		if dat.size == 0: continue
		if max(dat)<=phi:
			L.append('T')
			ind.append(i)
			l_phi.append(-1)
		elif min(dat)>=phi:
			L.append('S')
			ind.append(i)
			l_phi.append(-1)
		else:
			L.append('C')
			ind.append(i)
			k = dat.size
			x = min(dat)
			y = max(dat)
			cs1 = []
			cs2 = []
			for _ in range(100):
				cs1.clear()
				cs2.clear()
				for j in range(k):
					dis_a = abs(dat[j]-x)
					dis_b = abs(dat[j]-y)
					if(dis_a<dis_b):
						cs1.append(j)
					else:
						cs2.append(j)
				x = 0
				y = 0
				for e in cs1:
					x += dat[e]
				x = x/(len(cs1))

				for e in cs2:
					y += dat[e]
				y = y/(len(cs2))
			if x<y:
				l_phi.append(max(dat[j] for j in cs1))
			else:
				l_phi.append(max(dat[j] for j in cs2))
	for  i in range(len(L)):
		print(ind[i],L[i],l_phi[i], file=f)
