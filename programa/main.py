from fun import *


def main():

    col1 = [ '#e76f51', '#f4a261', '#e9c46a', '#2a9d8f', '#264653']
    col2 = [ '#0f4c5c', '#e36414', '#fb8b24', '#9a031e', '#5f0f40']
    col3 = [ '#ff9b85', '#ffd97d', '#aaf683', '#60d394', '#ee6055']

    p1 = Proyectil(22,15,col2[0])
    p2 = Proyectil(22,30,col2[1])
    p3 = Proyectil(22,45,col2[2])
    p4 = Proyectil(22,60,col2[3])
    p5 = Proyectil(22,90,col2[4])

    proyectiles = [p1,p2,p3,p4,p5]
    MAX_T,MAX_Y,MAX_X = MAXMAXMAX(proyectiles)

    fig, ax, t = HelloWorld(MAX_T,MAX_Y,MAX_X)


    for i in proyectiles:
        i.set_t(t)
        i.update_x()
        i.update_y()
        i.make_path(ax)


    anim = animation.FuncAnimation(fig,el_alma_de_la_fiesta,frames=len(t),interval=len(t)/24,fargs=proyectiles)
    plt.legend()
    plt.show()



if __name__ == '__main__':
    main()
