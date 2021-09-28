# 清明上河圖 (Along the River During the Qing Ming Festival)
A famous painting which belongs to Dynasty Song. The challenge here is to restore the blurry ancient painting. <br/><br/>

#### To enhance the image quality
* Brightness of the image
* Bring out the details


<br/>

#### Original image 
<img src="img/ancient_painting.jpg">

<br/>

#### Restored image 
<img src="img/restored_painting.png">

<br/>

#### Implementation
The notebook can be found [here](https://github.com/Sins-Repo/ImageProcessingII/blob/main/QingMing.ipynb) <br/><br/>

#### Techniques:
* Sharpening filter
* Contrast stretching
* Denoising

<br/>
<br/>

# Industrial Inspection
Detect rustic region and output a warning message

<br/>

#### Sample output
<img src="img/rust_detection.png" height=800>

<br/>

#### Sample masks
<img src="img/rust_mask.png" height=800>

<br/>

#### Techniques:
* Segment rustic region using color space (concept of thresholding)
* Morphological processing
* Contour
