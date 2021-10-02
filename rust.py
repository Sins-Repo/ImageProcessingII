import numpy as np
import cv2
import matplotlib.pyplot as plt
path = '<path>'
inputs = [] 
rusts = []  
and_ops = [] 
close_ops = [] 
messages = []

def read_images():
  for i in range(1,5):
    img = cv2.imread(path + '/rust_' + str(i) + ".png")
    rust = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    inputs.append(img)
    rusts.append(rust)

def segment_rust(image):
  hsv_rust = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv_rust, np.array([120, 80, 0],dtype="uint8"), np.array([255, 255, 80],dtype="uint8"))
  and_ops.append(cv2.bitwise_and(image,image, mask=mask))

  close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20)))
  close_ops.append(close)

  def find_contours(mask):
    contours, hierarchy = cv2.findContours(mask,
                          cv2.RETR_LIST,
                          cv2.CHAIN_APPROX_SIMPLE)

    message = 'No rust' # assume no rust initially

    for c in contours:
      area = cv2.contourArea(c)

      # ignore all small contours 
      if area < 500:
          cv2.fillPoly(mask, pts=[c], color=0)
          continue

      message = 'Alert: Rust detected' # warning message 
      rect = cv2.minAreaRect(c)
      box = cv2.boxPoints(rect)

      # convert all coordinates floating point values to int
      box = np.int0(box)
      cv2.drawContours(image, [box], 0, (255, 0, 0),2)
    
    return message

  messages.append(find_contours(close))
  
def plot_output():
  for x in rusts:
    segment_rust(x)
  for i in range(0, 4):
    plt.figure(figsize=(8,8))
    plt.subplot(1, 2, 1)
    plt.title('Input image', fontsize=15)
    plt.imshow(cv2.cvtColor(inputs[i], cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title(messages[i], fontsize=15)
    plt.imshow(rusts[i])
    plt.show()
 
def plot_process():
  for i in range(0, 4):
    plt.figure(figsize=(8,8))
    plt.subplot(1, 2, 1)
    plt.title('AND Operation', fontsize=15)
    plt.imshow(and_ops[i])
    plt.subplot(1, 2, 2)
    plt.title('Closing Operation', fontsize=15)
    plt.imshow(close_ops[i])
    plt.show()
 
def main():
  read_images()
  plot_output()
  plot_process()
    
if __name__ == "__main__":
   main()