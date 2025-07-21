# Weed Detection System

This project implements a weed detection system using YOLOv8 that can:
1. Detect weeds in images and video feeds
2. Highlight detected weeds in red
3. Suggest appropriate pesticides based on the detected weed type

## Setup

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
├── data/
│   ├── images/         # Training and testing images
│   ├── labels/         # YOLO format annotations
│   └── dataset.yaml    # Dataset configuration
├── models/             # Trained model weights
├── src/
│   ├── train.py       # Training script
│   ├── detect.py      # Detection script
│   ├── utils.py       # Utility functions
│   └── pesticides.py  # Pesticide recommendation system
└── requirements.txt    # Project dependencies
```

## Usage

1. To train the model:
```bash
python src/train.py
```

2. To detect weeds in images:
```bash
python src/detect.py --source path/to/image
```

## Dataset

The dataset consists of various weed species commonly found in agricultural fields. Each image is annotated with bounding boxes around weeds, and the corresponding pesticide recommendations are provided in the database. 