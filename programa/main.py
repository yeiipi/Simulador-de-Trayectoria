from fun import *



def main():
    p1 = Proyectil(2.2,15,'r')
    p2 = Proyectil(2.2,30,'g')
    p3 = Proyectil(2.2,45,'b')
    p4 = Proyectil(2.2,60,'c')
    p5 = Proyectil(2.2,90,'m')

    proyectiles = [p1,p2,p3,p4,p5]
    MAX_T,MAX_Y,MAX_X = MAXMAXMAX(proyectiles)

    fig, ax, t = HelloWorld(MAX_T,MAX_Y,MAX_X)


    for i in proyectiles:
        i.set_t(t)
        i.update_x()
        i.update_y()
        i.make_path(ax)


    anim = animation.FuncAnimation(fig,el_alma_de_la_fiesta,frames=len(t),fargs=proyectiles)
    plt.show()



if __name__ == '__main__':
    main()
