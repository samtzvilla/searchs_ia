import numpy as np
import matplotlib.pyplot as plt


def dibuja_frontera_2D(clf,X,yp):
  x=np.linspace(X[:,0].min()-0.5,X[:,0].max()+0.5, 200)
  y=np.linspace(X[:,1].min()-0.5,X[:,1].max()+0.5, 200)
  XX,YY=np.meshgrid(x,y)
  xx,yy=XX.flatten(), YY.flatten()
  xx,yy=xx.reshape((len(xx),1)),yy.reshape((len(yy),1))
  B=np.hstack((xx,yy))
  print(B.shape, XX.shape)
  Bo=clf.predict(B).reshape(XX.shape)
  plt.contourf(XX,YY,Bo, alpha=0.2)
  plt.scatter(X[:,0],X[:,1], c=yp)
  
