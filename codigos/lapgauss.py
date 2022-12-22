import cv2
import numpy as np

def menu():
    print("\nPressione a tecla para ativar o filtro:"
          "\na - calcular modulo"
          "\nm - media"
          "\ng - gauss"
          "\nv - vertical"
          "\nh - horizontal"
          "\nl - laplaciano"
          "\nx - laplaciano do gaussiano"
          "\nesc - sair\n")

media = np.ones([3,3],dtype=np.float32)
gauss = np.array([[1,2,1],
                 [2,4,2],
                 [1,2,1]],dtype=np.float32)
horizontal = np.array([[-1,0,1],
                 [-2,0,2],
                 [-1,0,1]],dtype=np.float32)
vertical = np.array([[-1,-2,-1],
                 [0,0,0],
                 [1,2,1]],dtype=np.float32)
laplacian = np.array([[0,-1,0],
                 [-1,4,-1],
                 [0,-1,0]],dtype=np.float32)
lapgauss = np.array([[0,0,1,0,0],
                     [0,1,2,1,0],
                     [1,2,-16,2,1],
                     [0,1,2,1,0],
                     [0,0,1,0,0]],dtype=np.float32)
mask = media.copy()
img = cv2.imread("biel.png",0)
rows,cols = img.shape
mask = cv2.scaleAdd(mask,1/9.0,np.zeros([3,3],dtype=np.float32))
absolute = True

menu()
case = -1
while True:
    nova = img.copy()
    cv2.flip(nova,1,nova)
    cv2.imshow("entrada", nova)
    nova32 = np.array(nova,dtype=np.float32)
    frameFiltered = cv2.filter2D(nova32,-1,mask,anchor=(1,1))
    if absolute:
        frameFiltered = abs(frameFiltered)
    result = np.array(frameFiltered,dtype=np.uint8)
    cv2.imshow("saida",result)
    case = cv2.waitKey(10)
    if case == ord('a'):
        menu()
        absolute = not absolute
    elif case == ord('m'):
        menu()
        mask = media.copy()
        mask = cv2.scaleAdd(mask,1/9.0,np.zeros([3,3],dtype=np.float32))
    elif case == ord('g'):
        menu()
        mask = gauss.copy()
        mask = cv2.scaleAdd(mask, 1/16.0, np.zeros([3, 3],dtype=np.float32))
    elif case == ord('h'):
        menu()
        mask = horizontal.copy()
    elif case == ord('v'):
        menu()
        mask = vertical.copy()
    elif case == ord('l'):
        menu()
        mask = laplacian.copy()
    elif case == ord('x'):
        menu()
        mask = lapgauss.copy()
    elif case == 27:
        break
    else:
        pass

cv2.destroyAllWindows()