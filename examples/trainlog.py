#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : CTRZOO.
# @File         : trainlog
# @Time         : 2021/1/5 8:10 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import wandb

# 1. Start a W&B run
wandb.init(project='gpt3')

# 2. Save model inputs and hyperparameters
config = wandb.config
config.learning_rate = 0.01
# wandb.init()
# wandb.config.epochs = 4
# wandb.config.batch_size = 32
# wandb.config.learning_rate = 0.001
# wandb.config.architecture = "resnet"

# Model training code here ...

# 3. Log metrics over time to visualize performance
for i in range (10):
    wandb.log({"loss": 1})