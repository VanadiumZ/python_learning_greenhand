import numpy as np
def conv2d(im, kernel, stride):
    im = np.array(im)
    # reverse the convolution core
    ker_f = np.flipud(np.fliplr(kernel))
    
    # calculate the size of image and kernel
    im_height, im_width = len(im), len(im[0])
    ker_f_height, ker_f_width = len(ker_f), len(ker_f[0])

    # calculate the size of output matrix
    o_height = (im_height - ker_f_height) // stride + 1
    o_width = (im_width - ker_f_width) // stride + 1             #output shape没问题


    # 问题出在了卷积上！！！


    im_out = [[0 for _ in range(o_width)]for _ in range(o_height)]
    
    # convolution
    for i in range(0, im_height-ker_f_height+1, stride):
        for j in range(0, im_width-ker_f_width+1, stride):
            #注意i和j的range是不一样的
            #图像有一半黑，说明那一半没有附上值，同时前面的赋值程序完全正常，应该意识到是range有问题！！！
            value = 0
            for u in range(ker_f_height):
                for v in range(ker_f_width):
                    value += im[i+u][j+v] * ker_f[u][v]
            im_out[i//stride][j//stride] = value

    return im_out

    # convolution = []
    # # convolution 
    # for i in range(0, im_height-ker_f_height+1, stride):
    #     for j in range (0, im_width-ker_f_width, stride):
    #         conv = im[i:i+ker_f_height, j:j+ker_f_width] * ker_f
    #         value = conv.sum()
    #         convolution.append(value)
    # im_out = np.array(convolution).reshape(o_height, o_width)
    # return im_out









from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# input image
im = np.array(Image.open('D:\\JupyterSpace\\AI&python\\大作业\\ruc.jpg').convert('L'))
plt.imshow(im)
plt.show()
# im is a list transferred from image-input
im = im.tolist()

ker = np.array([[1,1,1,-1,-1],
               [1,0,0,0,-1],
               [1,0,0,0,-1],
               [1,0,0,0,-1],
               [1,1,1,-1,-1]])
ker = ker.tolist()

print(conv2d(im, ker, 1))