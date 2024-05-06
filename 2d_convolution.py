import numpy as np
def conv2d(im, kernel, stride):
    # reverse the convolution core
    ker_f = np.flipud(np.fliplr(kernel))
    
    # calculate the size of image and kernel
    im_height, im_width = len(im), len(im[0])
    ker_f_height, ker_f_width = len(ker_f), len(ker_f[0])

    # calculate the size of output matrix
    o_height = (im_height - ker_f_height) // stride + 1
    o_width = (im_width - ker_f_width) // stride + 1
    im_out = [[0 for _ in range(o_width)]for _ in range(o_height)]
    
    # convolution
    for i in range(0, im_height-ker_f_height+1, stride):
        for j in range(0, im_height-ker_f_height+1, stride):
            value = 0
            for u in range(ker_f_height):
                for v in range(ker_f_width):
                    value += im[i+u][j+v] * ker_f[u][v]
            im_out[i//stride][j//stride] = value

    return im_out
        
im = [[ 8, -1, -8,  2,  3, -9, -2,  5,  5,  5, -8],
       [ 8,  2, -8, -4,  1,  7,  6, -7,  8, -4, -6],
       [ 5,  7, -1,  2,  1, -7, -4,  1, -1,  1,  0],
       [-3,  0, -2, -2, -5, -4, -7,  5,  0, -3, -1],
       [-5,  0,  3,  1, -1,  4,  8, -2, -3, -8,  5],
       [-2, -7, -6, -3, -3, -3,  2,  5, -7,  7,  3],
       [ 8, -9, -3,  3,  0, -4, -6, -8,  6, -8, -7],
       [-6,  0,  0,  8,  3, -6,  1,  8, -2,  2,  7],
       [-4, -8,  6, -3, -9,  2, -5, -4, -9,  0, -5],
       [-6,  4, -1,  0, -4,  7,  4,  5,  0, -4, -6],
       [ 6,  4,  2, -4,  7,  4,  8, -5, -1, -7, -5]]

K = [[ 5, -3,  3,  5,  7],
       [ 0, -9,  8, -8, -8],
       [ 6,  6,  1, -5,  3],
       [-3, -9,  5,  0,  1],
       [ 1, -9, -6,  0,  8]]

stride = 2

print(conv2d(im, K, stride))
    
