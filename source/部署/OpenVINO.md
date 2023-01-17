## OpenVINO 模型导出

### 环境依赖
```shell
pip install --upgrade pip
pip install openvino-dev
```

### 导出脚本
```shell
python deploy/OpenVINO/export_openvino.py --weights yolov6s.pt --img 640 --batch 1
```

### 速度测试
```shell
benchmark_app -m yolov6s_openvino/yolov6s.xml -i data/images/image1.jpg -d CPU -niter 100 -progress
```
