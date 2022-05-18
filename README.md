# NYC_DOT_Neural_Network
App Dev Project Management Internship for NYC DOT.


**Table of Content **
1. Overview
2. Usage
3. Product Spec
4. Schema
5. Wireframes
6. Manual
7. Documentation

<Neural Network>
   Create a neural network for automation of asset collection.
  We are training the model to detect Streetlights and curbcuts. 
  Collect XYZ coordinates
  
  https://github.com/kylehslee/DOTNN 
  
  
  Overview
  Description
  
   App Evaluation
Category: Social Networking / Neural Network / Language
Computer: This app would be primarily developed for Window devices. Functionality could be limited to Window devices.
Story: Automate feedback gathering from a social group. Users can execute scripts to optain infomartion from their particular following. Optain statistical data to further understand their sentiment. Clasify sentences on wether they are positve, negative or neutral.
Market: Limited to the social media team at the NYC DOT.
   
   
 Creating a custom model to detect your objects is an iterative process of collecting and organizing images, labeling your objects of interest, training a model, deploying it into the wild to make predictions, and then using that deployed model to collect examples of edge cases to repeat and improve.

1. Create Dataset
YOLOv5 models must be trained on labelled data in order to learn classes of objects in that data. There are two options for creating your dataset before you start training:

Use Roboflow to label, prepare, and host your custom data automatically in YOLO format 🚀 NEW (click to expand)
Or manually prepare your dataset (click to expand)
   
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
  
