import numpy as np 
p_x=np.array([[3,3],[4,3],[1,1]])
y  =np.array([1,1,-1])
w=np.array([0,0])
b=0
delta=1

def gdf(p_x,y,delta,w,b):
	for x in range(5):
		for i in range(len(p_x)):
			if y[i]*(np.dot(w,p_x[i]))<=0:
				w+=delta*y[i]*p_x[i]
				b+=delta*y[i]
			
	return w,b


if __name__=='__main__':
	print(gdf(p_x,y,delta,w,b))
