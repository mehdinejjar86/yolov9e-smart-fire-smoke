# YOLOv9-E: Smart Fire and Smoke

## Getting Started
Setup a YOLOv9 [enviroment](https://github.com/WongKinYiu/yolov9).

## Download Dataset
The datasets used for this project are [Smart Fire and Smoke](https://universe.roboflow.com/mehdinejjar86-35iub/smart-fire-and-smoke).

## Available Weights
YOLOv9-E Trained on Fire, Smoke, and Pseudo classes with grayscale images (to mimic the infrared light conditions).
YOLOv9-E Trained on Fire, and Smoke classes with grayscale images (to mimic the infrared light conditions).
YOLOv9-E Trained on Fire, Smoke, and Pseudo classes without grayscale images.
YOLOv9-E Trained on Fire and Smoke classes without grayscale images.

to easily remove the pseudo class from the dataset, using the following command

`remove_pseudo_class.py train/labels valid/labels test/labels` 

Please note that the paths should be relative to the script file.





