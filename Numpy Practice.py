import numpy as np
def np_op(threshold):
    array=np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]])
    first_row= array[0,:]
    array[:,-1] = 0
    print(array[1:3, 2:4])
    bool_indexing = array[array>threshold]
    print("elements greater than", threshold, ':', bool_indexing)
np_op(10)
