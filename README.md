


# NYC_DOT_Neural_Network
App Dev Project Management Internship for NYC DOT.

![This is an image](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/NYCDOT.svg/1200px-NYCDOT.svg.png)




**Table of Content **
1. [Overview](https://github.com/MVVENTO/NYC_DOT/blob/main/README.md#overview)
2. [Usage](https://github.com/MVVENTO/NYC_DOT/blob/main/README.md#usage)
3. [Product Spec](https://github.com/MVVENTO/NYC_DOT/blob/main/README.md#product-spec)
4. [Schema](https://github.com/MVVENTO/NYC_DOT/blob/main/README.md#schema)
5. [Wireframes](https://github.com/MVVENTO/NYC_DOT/blob/main/README.md#wireframes)
6. [Manual](https://github.com/MVVENTO/NYC_DOT/blob/main/README.md#manual)
7. Documentation

## <Neural Network>
   Create a neural network for automation of asset collection.
  We are training the model to detect Streetlights and curbcuts. 
  Collect XYZ coordinates
  
  
   ![This is an image](https://camo.githubusercontent.com/2653cd415161265cc58a5f2f054a958bf21e97ebce636c3e49b86c82e88bf37d/68747470733a2f2f75706c6f6164732d73736c2e776562666c6f772e636f6d2f3566366263363065363635663534353435613165353261352f3631353632376535383234633963363139356162666461395f636f6d70757465722d766973696f6e2d6379636c652e706e67)
   
## Overview
   
 Description
Create an application that would capture the sentiment of customers automatically and efficiently, thus reducing the resources needed in order to complete this task. Automatically fetch text from DOT’s Twitter and Instagram. Classify the opinion(positive, negative and neutral) of the text using NLP techniques.

App Evaluation
Category: Social Networking / Neural Network / Language
Computer: This app would be primarily developed for Window devices. Functionality could be limited to Window devices.
Story: Automate feedback gathering from a social group. Users can execute scripts to optain infomartion from their particular following. Optain statistical data to further understand their sentiment. Clasify sentences on wether they are positve, negative or neutral.
Market: Limited to the social media team at the NYC DOT.

   
## Usage
   
Given login information for Twitter or Instagram, run one of the scripts to fetch data to the target account.

For more details check Manual for more details.
   
## Product Spec
   
1. Crawler Scripts
 Script naviagtes to specified account or page.
 Script can fetch comments from the specified account or page.
 Script can fetch data within a given parameter.
   
2. Neural Network Model
 Model trained.
 Model can clasify streetlights and curbcuts.
 Model can rate streetlights and curbcut.
   
3. Screen Archetypes
Creation - Select one of the scripts from a simple GUI interface to fetch and save data from your desired platform.
   
4. Navigation
Flow Navigation

Set parameter --> Set functional parameter for script.
Specific scripts -- > Specified which scrawler scripts to run.
Output --> Text and numerial data.
   
   
## Schema
   
   
## Wireframes
   
   
## Manual
   

   
###### Streetlight and Curb Cut Detection 
 Creating a custom model to detect your objects is an iterative process of collecting and organizing images, labeling your objects of interest, training a model, deploying it into the wild to make predictions, and then using that deployed model to collect examples of edge cases to repeat and improve.

1. Create Dataset
YOLOv5 models must be trained on labelled data in order to learn classes of objects in that data. There are two options for creating your dataset before you start training:

Use Roboflow to label, prepare, and host your custom data automatically in YOLO format 🚀 NEW [(click to expand)](https://app.roboflow.com/nn/streetlights-detection/images/?split=train) 
   
Or manually prepare your dataset 
   
2. Select a Model
Select a pretrained model to start training from. Here we select YOLOv5s, the smallest and fastest model available. See our README table for a full comparison of all models.
   
3. Train
Train a YOLOv5s model on COCO128 by specifying dataset, batch-size, image size and either pretrained --weights yolov5s.pt (recommended), or randomly initialized --weights '' --cfg yolov5s.yaml (not recommended). Pretrained weights are auto-downloaded from the latest YOLOv5 release.
   
 4. Visualize
Weights & Biases Logging (🚀 NEW)
Weights & Biases (W&B) is now integrated with YOLOv5 for real-time visualization and cloud logging of training runs. This allows for better run comparison and introspection, as well improved visibility and collaboration among team members. To enable W&B logging install wandb, and then train normally (you will be guided setup on first use).
   
   
   Local Logging
All results are logged by default to runs/train, with a new experiment directory created for each new training as runs/train/exp2, runs/train/exp3, etc. View train and val jpgs to see mosaics, labels, predictions and augmentation effects. Note an Ultralytics Mosaic Dataloader is used for training (shown below), which combines 4 images into 1 mosaic during training.

train_batch0.jpg shows train batch 0 mosaics and labels:
 
Training results are automatically logged to Tensorboard and CSV as results.csv, which is plotted as results.png (below) after training completes. You can also plot any results.csv file manually:
   
   
 Next Steps
Once your model is trained you can use your best checkpoint best.pt to:

Run CLI or Python inference on new images and videos
Validate accuracy on train, val and test splits
Export to TensorFlow, Keras, ONNX, TFlite, TF.js, CoreML and TensorRT formats
Evolve hyperparameters to improve performance
Improve your model by sampling real-world images and adding them to your dataset
   
 ## Documentation
   
   
  
