from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from math import cos, sin, radians

g = 9.80665

class Proyectil:
    def __init__(self,v0:float,theta:float,color:str):
        self.x = 0
        self.y = 0
        self.ax = 0
        self.ay = -g
        self.v0 = v0
        self.theta = theta
        self.color = color
        self.vx = v0 * cos(radians(theta))
        self.vy = v0 * sin(radians(theta))

    def __repr__(self):
        return f'({self.x,self.y})'

    def make_path(self,ax):
        self.path, = ax.plot(self.x,self.y,'ro-',color=f'{self.color}')


    def update_x(self,frame):
        self.x = self.x + self.vx*(frame/len(self.t)) + 0.5*self.ax*((frame/len(self.t))**2)

    def set_xy(self,nx,ny):
        self.x = nx
        self.y = ny

    def set_t(self,t):
        self.t = t

    def update_y(self,frame):
        self.y = self.y + self.vy*(frame/len(self.t)) + 0.5*self.ay*((frame/len(self.t))**2)

    def update_pos(self,frame):
        if ( frame == 0 ):
            self.set_xy(0,0)
        else:
            self.update_x(frame)
            self.update_y(frame)

        self.path.set_data((self.x,self.y))

    def make_some_limits(self):
        t_max = 2*self.v0*sin(radians(self.theta))/g
        y_max = (self.v0*sin(radians(self.theta)))**2 / (2*g)
        x_max = self.v0**2 * sin(2*radians(self.theta))/g

        return t_max,y_max,x_max



def HelloWorld(t_max:float,y_max:float,x_max:float):
    """Puede que sea un entorno para simular tiro parabólico y que no
    tengasentimientos (por lo mismo), pero es de buena costumbre saludar. Por
    cierto, está función es donde se configura todo lo relacionado con el plot de
    la animación.
    ====================
        > t_max (float): es el tiempo máximo que dura el proyectil en el aire
        > x_max (float): es la distancia máxima que recorre el proyectil con
            respecto al eje x.
        > y_max (float): es la distancia máxima que recorre el proyectil con
            respecto al eje y.
    ====================
    """
    fig, ax = plt.subplots()
    ax = plt.axes(autoscale_on=True, xlim=(0,x_max*25.5), ylim=(0,y_max*25.5))
    ax.set_xlabel('distancia en x')
    ax.set_ylabel('distancia en y')
    ax.grid()

    t = np.linspace(0,t_max)
    return fig, ax, t

def el_alma_de_la_fiesta(frame,*args):
    print(frame)
    for i in args:
        i.update_pos(frame)
    return args




