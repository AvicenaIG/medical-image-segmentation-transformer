import argparse
import logging
import os
import random
import numpy as np
import torch
import torch.backends.cudnn as cudnn
from networks.vit_seg_modeling import VisionTransformer as ViT_seg
from networks.vit_seg_modeling import CONFIGS as CONFIGS_ViT_seg
from trainer import trainer_synapse

parser = argparse.ArgumentParser()
parser.add_argument('--root_path', type=str,
parser.add_argument('--dataset', type=str,
parser.add_argument('--list_dir', type=str,
parser.add_argument('--num_classes', type=int,
parser.add_argument('--max_iterations', type=int,
parser.add_argument('--max_epochs', type=int,
parser.add_argument('--batch_size', type=int,
parser.add_argument('--n_gpu', type=int, default=1, help='total gpu')
parser.add_argument('--deterministic', type=int,  default=1,
parser.add_argument('--base_lr', type=float,  default=0.01,
parser.add_argument('--img_size', type=int,
parser.add_argument('--seed', type=int,
parser.add_argument('--n_skip', type=int,
parser.add_argument('--vit_name', type=str,
parser.add_argument('--vit_patches_size', type=int,
args = parser.parse_args()


if __name__ == "__main__":



