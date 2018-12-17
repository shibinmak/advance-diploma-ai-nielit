#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,6),facecolor='#00FF00')
fobj.canvas.set_window_title("Test")
spobj=fobj.add_subplot(1,1,1)
yn=np.random.randint(1,100,10)
xn=np.arange(2,21,2)
yn.sort()
yn1=yn[yn<50]
yn2=yn[yn>=50]
yn2=np.insert(yn2,0,yn1[yn1.size-1])
spobj.plot(xn[:yn1.size],yn1,linestyle='solid',marker='o',color='b',markerfacecolor='w',markeredgecolor='r')
spobj.plot(xn[yn1.size-1:],yn2,linestyle='solid',marker='o',color='y',markerfacecolor='w',markeredgecolor='r')
print 'xn=',xn
print 'yn=',yn
plt.show()
