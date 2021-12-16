## COMSE 6998 Practical Deep Learning Systems Performance Final Project

# Human Activity Recognition Using Tactile Patterns
## Zijia Chen (zc2521), Bowen Chen (bc2916)

# Project Description:
- Using densely deployed flexible pressure sensors to estimate precise human movements.
- Built customized data pipeline and multiple lightweight ML/DL models to classify human actions given inputs from our flexible pressure sensors.
- Our pressure sensors can be deployed in large scale with relatively low cost.
- Our models are computational friendly to edge computing devices.
- Human movements that can be recognized:
  1. Good Posture
  2. Cross-Legged(Right)
  3. Cross-Legged(Left)
  4. Leaning Right
  5. Leaning Left
  6. Slouch

# About this repository
- ./data: folder containing collected data for training, testing and validation
- ./vis: some visualization result for inputs from pressure sensors
- bc2916_6998_project_binary.ipynb: 
  - deep learning models training, testing and validation pipline for binary classification
- bc2916_6998_project_multi_class.ipynb: 
  - deep learning models training, testing and validation pipline for multiclass classification
- data_collection_with_model_finetuning.py:
  - script for data collection and XGBoost model finetuning
- final_XGB.ipynb:
  - XGBoost model training, testing and validation pipeline
- pose_prediction.py:
  - script running on MCU using exported XGBoost model for final pose prediction
- realtime_line_graph.py:
  - script for visualizing XGBoost prediction confidence at runtime
- sensor_visualization.py:
  - script for visualizing pressure map directly from connected pressure sensors

For notebook files, simply following code blocks should work. 

Other python scripts can be run directly without input arguments.

However, some of them requires connecting to our custom hardwares including MCU or pressure sensors.

# Results

