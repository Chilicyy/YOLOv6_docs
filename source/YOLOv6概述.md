# YOLOv6 概述
<p align="center">
  <img src="https://raw.githubusercontent.com/meituan/YOLOv6/main/assets/banner-YOLO.png" align="middle" width = "1000" />
</p>

本文向您介绍 YOLOv6 的整体框架，并提供详细的教程链接。

官方论文 ☞ [YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications](https://arxiv.org/abs/2209.02976)

v3.0版本论文更新 ☞ [YOLOv6 v3.0: A Full-Scale Reloading](https://arxiv.org/abs/2301.05586) 🔥

<p align="center">
  <img src="https://raw.githubusercontent.com/meituan/YOLOv6/main/assets/speed_comparision_v3.png" align="middle" width = "1000" />
</p>

YOLOv6 是一款面向工业应用研发的目标检测框架，致力于提供极致的检测精度和推理效率。其包括丰富的目标检测算法以及相关的组件模块，下面是整体代码框架的介绍：

```
├── configs        #配置文件目录，用于指定网络结构，优化器，数据增强等超参
│   ├── experiment #存放非发版模型的实验配置
│   ├── repopt     #存放repopt训练相关的配置
│   ├── base       #存放基础版模型的配置(PTQ量化友好)
│   ├── *.py       #常规模型的配置（RepVGG进阶版）
├── data           #数据集路径配置文件
├── tools          #启动训练、评估、推理、量化等任务
│   ├── train.py   #训练启动脚本
│   ├── eval.py    #评估启动脚本
│   └── infer.py   #推理启动脚本
│   ├── qat        #qat量化相关脚本
│   ├── partial_quantization   #ptq量化相关脚本
|── yolov6         #检测算法核心部分，包含运行组件、网络定义、数据处理、标签分配及损失计算等核心模块
|    ├── assigners #标签分配算法，包括ATSS和TAL分配算法及相关工具脚本
|    ├── core      #模型训练、评估和推理等组件的核心运行逻辑
|    ├── data      #数据预处理，包括数据加载，各种数据增强变换和数据格式转换等脚本
|    ├── layers    #定义卷积，RepVGG block，SPPF 等基础算子和模块
|    ├── models    #网络结构定义（包括 Backbone, Neck, Head）以及loss计算等脚本
|    ├── solver    #优化器构建组件
|    └── utils     #模型保存加载、指标计算，NMS后处理等工具脚本
├── deploy         #模型部署目录
│   ├── ONNX       #导出 ONNX 模型
│   ├── OpenVINO   #导出 OpenVINO 模型
│   └── TensorRT   #转换 TRT 模型以及验证可视化
├── docs           #相关教程文档
│   ├── Test_speed.md           #复现测速指标的相关命令教程
│   ├── Train_coco_data.md      #复现 COCO 精度指标的命令
│   ├── Train_custom_data.md    #训练自定义数据集的教程指引
│   ├── Tutorial of Quantization.md #量化相关的教程和指引
│   └── tutorial_voc.ipynb      #训练 VOC 数据集的教程指引
```

以下是关于 YOLOv6 的详细使用指南：

1. [环境安装](全流程使用指南/环境安装.md)
2. [选型指导](选型指导.md)
3. [配置文件学习](全流程使用指南/配置文件学习.md)
4. [模型训练、评估和推理流程](全流程使用指南/训练评估推理流程.md)
5. [模型量化](量化/量化.md)
6. [模型部署](部署/ONNX.md)





