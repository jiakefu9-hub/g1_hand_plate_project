#!/bin/bash
# 将 RL 仓库加入环境变量，解决 legged_gym 模块找不到的问题
export PYTHONPATH=/home/fjk/g1_ws/unitree_rl_gym:$PYTHONPATH
python main_sim.py g1.yaml
