# YOLOv9-E: Smart Fire and Smoke

## Getting Started
Setup a YOLOv9 [enviroment](https://github.com/WongKinYiu/yolov9).

## Download Dataset
The datasets used for this project are [Smart Fire and Smoke](https://universe.roboflow.com/mehdinejjar86-35iub/smart-fire-and-smoke).

## Available Weights

YOLOv9-E Trained on Fire, Smoke, and Pseudo classes with grayscale images (to mimic the infrared light conditions). (FSO)

YOLOv9-E Trained on Fire, and Smoke classes with grayscale images (to mimic the infrared light conditions). (FS)

YOLOv9-E Trained on Fire, Smoke, and Pseudo classes without grayscale images. (FSO$`w/o`$)

YOLOv9-E Trained on Fire and Smoke classes without grayscale images. (FS$`w/o`$)


To easily remove the Pseudo class from the dataset, use the following command
```bash
python remove_pseudo_class.py train/labels valid/labels test/labels
```
Please note that the paths should be relative to the script file.

## Inference Using Weight

We should clone [YOLOv9 repository]([enviroment](https://github.com/WongKinYiu/yolov9)).

```bash
git clone https://github.com/WongKinYiu/yolov9.git
```

After that, we should specify the weight (one of the provided weights or a fine-tuned one) and the path of the desired images

```bash
# inference yolov9 models
# python detect_dual.py --source 'path_to_images' --img 640 --device 0 --weights 'path_to_weight' --name specify_name_of_detection
```
