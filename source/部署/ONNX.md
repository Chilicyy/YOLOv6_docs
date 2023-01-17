# ONNX 模型导出

## 环境依赖
```shell
pip install onnx>=1.10.0
```

## 导出脚本
```shell
python ./deploy/ONNX/export_onnx.py \
    --weights yolov6s.pt \
    --img 640 \
    --batch 1 \
    --simplify
```



#### Description of all arguments

- `--weights` : yolov6 模型权重路径
- `--img` : 模型输入图片尺寸，默认640
- `--batch` : 模型输入的批大小
- `--half` : 是否导出半精度(fp16)模型
- `--inplace` : 是否需要设置Detect()类inplace为True
- `--simplify` : 是否采用onnx-sim简化模型，端到端导出模型不支持简化
- `--end2end` : 是否需要导出端到端的onnx模型，仅支持 onnxruntime 和 TensorRT >= 8.0.0
- `--trt-version` :  TensorRT 版本，支持7或8
- `--ort` : 是否为 onnxruntime 后端导出模型
- `--with-preprocess` : 是否需要预处理操作(bgr2rgb和归一化)
- `--topk-all` : 保留每张图像的topK个目标
- `--iou-thres` : NMS算法使用的IOU阈值
- `--conf-thres` : NMS算法使用的置信度阈值
- `--device` : 导出时用的环境设备，如显卡0或CPU

## 下载

* [YOLOv6-N](https://github.com/meituan/YOLOv6/releases/download/0.3.0/yolov6n.onnx)
* [YOLOv6-S](https://github.com/meituan/YOLOv6/releases/download/0.3.0/yolov6s.onnx)
* [YOLOv6-M](https://github.com/meituan/YOLOv6/releases/download/0.3.0/yolov6m.onnx)
* [YOLOv6-L](https://github.com/meituan/YOLOv6/releases/download/0.3.0/yolov6l.onnx)


## 端到端导出模型

现在 YOLOv6 支持 onnxruntime 和 TensorRT 的端到端检测！

如果你想在 TensorRT 中部署，请确保你已经安装了 TensorRT！

### onnxruntime 后端
#### 使用方式

```bash
python ./deploy/ONNX/export_onnx.py \
    --weights yolov6s.pt \
    --img 640 \
    --batch 1 \
    --end2end \
    --ort
```
您将获得带有 NMS 操作的 onnx 模型。

### TensorRT 后端 (TensorRT version == 7.2.3.4)
#### 使用方式

```bash
python ./deploy/ONNX/export_onnx.py \
    --weights yolov6s.pt \
    --img 640 \
    --batch 1 \
    --end2end \
    --trt-version 7
```
您将获得带有 BatchedNMSDynamic_TRT 插件的 onnx 模型。


### TensorRT 后端 (TensorRT version>= 8.0.0)

#### 使用方式

```bash
python ./deploy/ONNX/export_onnx.py \
    --weights yolov6s.pt \
    --img 640 \
    --batch 1 \
    --end2end \
    --trt-version 8
```

您将获得带有 BatchedNMSDynamic_TRT 插件的 onnx 模型。

### 输出描述

onnx 输出如图所示：

<img src="https://user-images.githubusercontent.com/92794867/176650971-a4fa3d65-10d4-4b65-b8ef-00a2ff13406c.png" height="300px" />

```num_dets``` 表示其批次中每个图像中的目标数

```det_boxes``` 表示 topk(100) 目标的坐标信息 [`x0`,`y0`,`x1`,`y1`] .

```det_scores``` 表示每个 topk(100) 个对象的置信度分数

```det_classes``` 表示每个 topk(100) 个对象的类别

您可以使用 [trtexec](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#trtexec-ovr) 工具导出 TensorRT 引擎。

#### 使用方式

``` shell
trtexec --onnx=yolov6s.onnx \
        --saveEngine=yolov6s.engine \
        --workspace=8192 # 8GB
        --fp16 # if export TensorRT fp16 model
```

## 评估 TensorRT 模型性能

当我们得到 TensorRT 模型后，我们可以通过以下方式评估其性能：
```
python deploy/ONNX/eval_trt.py --weights yolov6s.engine --batch-size=1 --data data/coco.yaml
```

## 动态批量推理

YOLOv6支持动态批量导出和推理，请参考以下教程：

[export ONNX model with dynamic batch ](YOLOv6-Dynamic-Batch-onnxruntime.ipynb)

[export TensorRT model with dynamic batch](YOLOv6-Dynamic-Batch-tensorrt.ipynb)
