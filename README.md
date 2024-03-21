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
remove_pseudo_class.py train/labels valid/labels test/labels
```
Please note that the paths should be relative to the script file.


```math
\begin{table*}[thb] \centering
\caption{Detection outcome on different datasets}\label{table_metricsvalues}%
\begin{center}
\begin{tabular}{c p{15mm} c c c}
\hline
    \multicolumn{2}{c}{}&\multicolumn{3}{c}{Metrics}\\
  & & Precision (\%) & Recall (\%)& mAP50 (\%)\\
  \hline
  \hline
  \multirow{4}{*}{\textbf{FSO}} & Fire & 62.2 & 61.7 & 65.8 \\
  & Smoke & 67.7 & 57.4 & 64.5 \\
  & Other & 52.5 & 38.7 & 42.3 \\
  & \textbf{Overall} & \textbf{60.8} & \textbf{52.6} & \textbf{57.5} \\
  \hline
  %\multirow{3}{*}{\textbf{CARPA}} & 0-2 & 6& 0& 0\\
  %& 3-5 & 0 & 0& 0\\
  %&6-10 & 0 & 5 & 3 \\
  %\hline
\multirow{3}{*}{\textbf{FS}} & Fire & 66.3 & 59.7 & 66.2\\
  & Smoke & 72.2 & 55.7 & 65.2\\
  & \textbf{Overall} & \textbf{69.3} & \textbf{57.7} & \textbf{65.7}\\
  \hline
  %\multirow{2}{*}{\begin{tabular}{c}
  %\textbf{Pathologic lymph} \\
  %\textbf{node invasion}
  %\end{tabular}} & Yes & 0& 0& 1\\
  %& No & 5 & 6& 2\\
  %\hline
  \multirow{4}{*}{\textbf{FSO$w/o$}} & Fire & 64.6 & 60.5 & 66.1\\
  & Smoke & 69.0 & 56.9 & 64.5\\
  & Other & 55.3 & 39.8 & 42.0 \\
  & \textbf{Overall} & \textbf{63.0} & \textbf{52.4} & \textbf{57.6} \\
  \hline
  \multirow{3}{*}{\textbf{FS$w/o$}} & Fire & 70.0 & 60.1 & 65.8\\
  & Smoke & 72.6 & 56.2 & 64.8 \\
  & \textbf{Overall} & \textbf{71.3} & \textbf{58.1} & \textbf{65.3} \\
  \hline
\end{tabular}
\end{center}
\end{table*}
```
