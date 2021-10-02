import cv2
import numpy as np  
from matplotlib import pyplot as plt
%matplotlib inline
import mahotas
path = '<path>'


def plot_hist(img):
  plt.figure(figsize=(5, 5))  
  plt.hist(img.ravel(),256,[0,256],color = 'r') 
  plt.title('Histogram for Constrast Stretching'), plt.xlim([0,256])

def plot_img(img, title):
  plt.figure(figsize=(20, 20))  
  plt.imshow(img)
  plt.axis('off')
  plt.title(title)

def read_img():
  img = cv2.imread(path+'/ancient_painting.jpg')
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  plot_img(img, 'Original image')
  plot_hist(img)
  return img

def process_img(img):
  def sharpen():
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img_sharp = cv2.filter2D(img, -1, kernel)
    plot_img(img_sharp, 'Sharpening Filter')
    return img_sharp

  def denoise(img_cs):
    img_bi = cv2.bilateralFilter(img_cs, 1, 80, 80)
    plt.figure(figsize=(20, 20))
    plot_img(img_bi, 'Bilateral Filter')

  def trans_stretch(img_sharp):
    hist,bins = np.histogram(img_sharp.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    img_cs = cdf[img_sharp]

    plot_img(img_cs, 'Version I : Constrast Stretching with transformation function')
    plot_hist(img_cs)
    return img_cs

  def mahotas_stretch(img_sharp):
    img_cs = mahotas.stretch_rgb(img_sharp)

    plot_img(img_cs, 'Version II : Constrast Stretching with Mahotas')
    plot_hist(img_cs)
    return img_cs
  
  img_sharp = sharpen()

  img_cs = trans_stretch(img_sharp)
  denoise(img_cs)
  
  img_cs = mahotas_stretch(img_sharp)
  denoise(img_cs)


def main():
  img = read_img()
  process_img(img)
    
if __name__ == "__main__":
   main()