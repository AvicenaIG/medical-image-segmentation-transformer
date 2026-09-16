# Medical Image Segmentation Transformer
Medical AI for Image Analysis of Tumors and Lesions
=============================================

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-0.1.0-red.svg)](https://shields.io/)
[![Python](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/)

## One-liner
A medical image segmentation transformer for accurate tumor and lesion detection.

## Table of Contents
[Installation](#installation)
[Features](#features)
[Quick Start](#quick-start)
[Usage](#usage)
[Configuration](#configuration)
[Contributing](#contributing)
[License](#license)

## Features
- **Augment Medical Images**: Apply random rotations and flips to enhance dataset.
- **Load Medical Datasets**: Utilize Synapse dataset for training and testing purposes.
- **Create Medical Models**: Design and train Vision Transformer models for segmentation tasks.
- **Evaluate Model Performance**: Assess model accuracy using Dice Loss and other metrics.
- **Infer on Medical Images**: Use trained models to segment tumors and lesions in new images.
- **Visualize Segmentation Results**: Display output of segmentation models for interpretation.

## Installation
```bash
git clone https://github.com/medical-image-segmentation-transformer
cd medical-image-segmentation-transformer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start
```bash
python train.py --dataset Synapse --vit_name R50-ViT-B_16
python test.py --dataset Synapse --vit_name R50-ViT-B_16
```

## Usage
### Training a Model
To train a Vision Transformer model on the Synapse dataset:

```bash
python train.py --dataset Synapse --vit_name R50-ViT-B_16
```

### Testing a Model
To test a trained Vision Transformer model on the Synapse dataset:

```bash
python test.py --dataset Synapse --vit_name R50-ViT-B_16
```

## Configuration
| Option | Type | Default | Description |
| --- | --- | --- | --- |
| dataset | str | Synapse | Selects the dataset to use for training and testing. |
| vit_name | str | R50-ViT-B_16 | Specifies the Vision Transformer model architecture. |

## Contributing
Contributions to this project are welcome. Please submit a pull request with your changes.

## License
Copyright 2026 medical-image-segmentation-transformer contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.