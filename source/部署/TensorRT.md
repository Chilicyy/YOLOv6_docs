# YOLOv6-TensorRT（C++）

## 环境依赖
- TensorRT-8.2.3.0
- OpenCV-4.1.0



## 第一步：获取onnx模型

按照指引 [ONNX README](../../tools/quantization/tensorrt/post_training/README.md) 将 pt 模型转换为 onnx 模型 `yolov6n.onnx`.

```shell
python ./deploy/ONNX/export_onnx.py \
    --weights yolov6n.pt \
    --img 640 \
    --batch 1
```

## 第二步：准备序列化引擎文件

按照指引 [post training README](../../tools/quantization/tensorrt/post_training/README.md) 转换并保存序列化引擎文件 `yolov6.engine`.

```shell
python3 onnx_to_tensorrt.py --fp16 --int8 -v \
        --max_calibration_size=${MAX_CALIBRATION_SIZE} \
        --calibration-data=${CALIBRATION_DATA} \
        --calibration-cache=${CACHE_FILENAME} \
        --preprocess_func=${PREPROCESS_FUNC} \
        --explicit-batch \
        --onnx ${ONNX_MODEL} -o ${OUTPUT}
```

## 第三步：构建 demo

按照指引[TensorRT Installation Guide](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html) 安装 TensorRT.

并且您应该在 CMakeLists.txt 中设置 TensorRT 路径和 CUDA 路径。

如果您训练自定义数据集，您可能需要修改 `num_class`、`image width`, `image height` 和 `class name` 的值。

```c++
const int num_class = 80;
static const int INPUT_W = 640;
static const int INPUT_H = 640;
static const char* class_names[] = {
        "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
        "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
        "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
        "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
        "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
        "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
        "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
        "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
        "hair drier", "toothbrush"
    };
```

构建 demo:

```shell
mkdir build
cd build
cmake ..
make
```

运行 demo:

```shell
./yolov6 ../you.engine -i image_path
```
## 测试图像
您可以使用 .trt 权重对图像进行测试，只需提供图像目录的路径及其注释路径。

```
python3 deploy/TensorRT/eval_yolo_trt.py -v -m model.trt \
--imgs-dir /workdir/datasets/coco/images/val2017 \
--annotations /workdir/datasets/coco/annotations/instances_val2017.json \
--conf-thres 0.40 --iou-thres 0.45
```
