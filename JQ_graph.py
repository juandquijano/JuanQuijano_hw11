import numpy as np 
import matplotlib.pyplot as plt 

##cargar los datos
data = np.loadtxt("tray.txt")
tiempo=data[:,2]
pos=data[:,0]
vel=data[:,1]

##grafica de x vs T  t en el x 
plt.figure()
plt.plot(tiempo,pos)
plt.xlabel("tiempo")
plt.ylabel("posicion")
plt.title("X vs T") 
plt.savefig("pos.png")
plt.show()

##grafica de x vs T
plt.figure()
plt.plot(tiempo,vel)
plt.xlabel("tiempo")
plt.ylabel("velocidad")
plt.title("V vs T") 
plt.savefig("vel.png")
plt.show()


##grafica de x vs T
plt.figure()
plt.plot(pos,vel)
plt.xlabel("tiempo")
plt.xlabel("fase")
plt.title("fase vs T") 
plt.savefig("phase.png")
plt.show()
