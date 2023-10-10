import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D
import matplotlib.pyplot as plt
import imageio
import os
import imageio as io
import numpy as np
from skimage import img_as_ubyte

def read_nii(niifile):
    img = nib.load(niifile)
    img_fdata = img.get_fdata()
    return img_fdata

def save_fig(file):
    fdata = read_nii(file)
    (y,x,z) = fdata.shape
    for k in range(y):
        slice = fdata[:,:,k]
        slice = np.rot90(slice)
    

        imageio.imwrite(os.path.join(output,'{}.jpg'.format(os.path.splitext(i)[0][7]+os.path.splitext(i)[0][8]+os.path.splitext(i)[0][9]+os.path.splitext(i)[0][10]+os.path.splitext(i)[0][11]+'_'+str(k))),slice)


def findAllFile(base):
    for root,ds,fs in os.walk(base):
        for f in fs:
            yield f

base = "/Users/samanthawang/Documents//seg_vessel"

output = 'png/'

for i in findAllFile(base):
    dir = os.path.join(base,i)
    savepicdir = (os.path.join(output,i))
    print("file"+i)

    if not os.path.exists(output):
        os.mkdir(output)
        print("nononono")

    save_fig(dir)

#save_fig(file_path)
#nii_img = nib.load(file_path)
#print(nii_img)

#width,height,queue = nii_img.dataobj.shape
#OrthoSlicer3D(nii_img)

#num = 1
#for i in range(0,queue,10):
    #img_arr = nii_img.dataobj[:,:,i]
    #plt.subplot(5,4,num)
    #plt.imshow(img_arr,cmap='gray')
    #num += 1

#plt.show()



#plt.imshow(slice_data,cmap='gray')
#plt.show()