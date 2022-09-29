import numpy as np
initialpos = [0,0,10]
zsubsections = 10
zIncrements = 100
edgetohole = 50
holetohole = 100
hole = 100
nholes = 5
xmat = np.array([[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]])
ymat  = [[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]]
def printmat(path,matrix,size1,size2):
	xtempstr = ""
	ytempstr = ""
	ztempstr = ""
	x = open("x"+path,"w")
	y = open("y"+path,"w")
	z = open("z"+path,"w")

	for i in range(0,size1):
		for j in range(0,size2):
			if j < size2-1:
				xtempstr = xtempstr+str(xmat[i,j,0]) +","
				ytempstr = ytempstr+str(xmat[i,j,1]) +","
				ztempstr = ztempstr+str(xmat[i,j,2]) +","
			else:
				xtempstr = xtempstr+str(xmat[i,j,0]) +""
				ytempstr = ytempstr+str(xmat[i,j,1]) +""
				ztempstr = ztempstr+str(xmat[i,j,2]) +""

			
		x.write(xtempstr+"\n")
		y.write(ytempstr+"\n")
		z.write(ztempstr+"\n")
		xtempstr = ""
		ytempstr = ""
		ztempstr = ""
	x.close()
	y.close()
	z.close()
	
for z in range(1,zsubsections+1):
	for y in range(1,nholes+1):
		for x in range(1,nholes+1):
			xmat[y-1,x-1] = [edgetohole*2+(x-1)*2*holetohole,edgetohole*2+(y-1)*2*holetohole,z*zIncrements-90]

	printmat("correctMat"+str(z)+".txt",xmat,nholes,nholes)






