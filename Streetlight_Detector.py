# @author Melissa Ann Vento (Melissa.vento52@myhunter.cuny.edu >> Mvvento@gmail.com)
# @brief Train a custom object detection model using Custom data (streetlights & curbcuts)
# @version 0.1
# @date 2022-4-19
#
# @copyright Copyright (c) 2022


####### Install pytorch
################################

 # pip3 install torch torchvision


########  Download Data Set
#####################################

# Terminal dataset
# curl -L "https://app.roboflow.com/ds/8HkeXVxUQm?key=sI684lts8p" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip

######################################

# JUPYTER dataset
# !pip install roboflow

# from roboflow import Roboflow
# rf = Roboflow(api_key="RVS1EdNU2QXYrUNJFqRw")
# project = rf.workspace("nn").project("streetlights-detection")
# dataset = project.version(2).download("yolov5")

# SETUP & INSTALL
######################################

#clone YOLOv5 and add to same folder 
!git clone https://github.com/ultralytics/yolov5 3 clone repo
%cd yolov5
%pip install -qr requirements.txt #insstall dependencies
%pip install -q roboflow

import torch
import os
from IPython.display import Image, clear_output # to display images

# mount goggle drive
from google.colab import drive
drive.mount('/content/drive')

from roboflow import Roboflow
rf = Roboflow(model_format="yolov5", notebook="ultralytics")

# download YOLOv5 dataset and add it to the Neural Network folder to test and run code


# set up environment
os.environ["DATASET_DIRECTORY"] = "/content/datasets"

# Get Dataset from Roboflow

!pip3 install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="RVS1EdNU2QXYrUNJFqRw")
project = rf.workspace("nn").project("streetlights-detection")
dataset = project.version(2).download("yolov5")

# Train the YOLO Model

!python train.py --img 416 --batch 16 --epochs 100 --data {dataset.location}/data.yaml --weights yolov5s.pt --cache

# show Training results

# Start tensorboard 
# Launch after you have started training 
# logs save in the folder "runs
%load_ext tensorboard
%tensorboard --logdir runs 


#PREDICTION 

!python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source {dataset.location}/valid/images 



#Display interface images

# display interface on ALL test images

import glob
from IPython.display import Image, display

i = 0
# Choose the correct exp folder - see prev output block
for imageName in glob.glob('/content/yolov5/runs/detect/exp/*.jpg'): # assuming JPG
  i += 1 

  if i < 10:
    display(Image(filename=imageName))
    print("\n")


