@echo off
python train.py --dataroot datasets/multipie --name multipie --model cycle_gan --display_id -1 --gpu_ids 0 --continue_train --batch_size 4
