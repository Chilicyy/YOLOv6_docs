# YOLOv6 概述
<p align="center">
  <img src="https://raw.githubusercontent.com/meituan/YOLOv6/main/assets/banner-YOLO.png" align="middle" width = "1000" />
</p>

本文向您介绍 YOLOv6 的整体框架，并提供详细的教程链接。

[demo]或[pics]

官方论文 ☞ [YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications](https://arxiv.org/abs/2209.02976)

YOLOv6 是一款致力于工业应用的目标检测框架，其包括丰富的目标检测算法以及相关的组件模块，下面是整体代码框架的介绍：

```
├── configs        #配置文件目录，用于指定网络结构，优化器，数据增强等超参
│   ├── experiment #存放非发版模型的实验配置
│   ├── repopt     #存放repopt训练相关的配置
│   ├── simplify   #存放简易版模型的配置
│   ├── advance    #存放进阶版模型的配置
├── data           #数据集路径配置文件
├── tools          #启动训练、评估、推理、量化等任务
│   ├── train.py   #训练启动脚本
│   ├── eval.py    #评估启动脚本
│   └── infer.py   #推理启动脚本
│   ├── qat        #qat量化相关脚本
│   ├── partial_quantization   #ptq量化相关脚本
|── yolov6    #检测算法核心部分，包含运行组件、网络定义、数据处理、标签分配及损失计算等核心模块
|    ├── assigners #标签分配算法，包括ATSS和TAL分配算法
|    ├── core      #模型训练、评估和推理等组件的核心运行逻辑
|    ├── data      #数据预处理，包括数据加载和各种数据增强变换
|    ├── layers    #定义卷积、RepVGG block等算子
|    ├── models    #网络结构定义以及损失计算脚本
|    ├── solver    #优化器构建组件
|    └── utils     #模型保存加载、指标计算等工具型脚本
├── deploy         #模型部署目录
│   ├── ONNX 
│   ├── OpenVINO
│   └── TensorRT
├── docs           #相关教程文档

```

以下是关于 YOLOv6 的详细使用指南：

1. [环境安装](全流程使用指南/install.md)
2. 配置文件学习
3. 模型训练、评估和推理流程
4. 模型量化
5. 模型部署











