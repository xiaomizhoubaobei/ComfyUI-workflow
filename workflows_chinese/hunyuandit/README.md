# 混元 DiT 工作流

本目录包含腾讯混元 DiT (Diffusion Transformer) 模型的 ComfyUI 工作流文件。混元 DiT 是腾讯开发的中文原生文生图模型，在中文提示词理解和图像生成质量方面表现优异。

## 📁 工作流文件

### 基础工作流

#### Huyuan-dit--v0-rodent.json
- **版本**: 混元 DiT v0
- **功能**: 基础文生图工作流
- **特点**:
  - 支持中文提示词
  - 使用 KSampler 采样器
  - 分辨率: 1024x1024
  - 采样步数: 30
  - CFG: 6
- **适用场景**: 日常图像生成，中文提示词测试

#### Huyuan-dit--v1-compare.json
- **版本**: 混元 DiT v1
- **功能**: 混元 DiT 与 SDXL 模型对比工作流
- **特点**:
  - 双模型并行生成对比
  - 同时使用混元 DiT 和 SDXL 模型
  - 相同提示词生成对比效果
  - 支持向量艺术风格
- **适用场景**: 模型效果对比，选择最佳模型

### 采样器对比工作流

#### Huyuan-dit-Diffusers-Vs-KSampler.json
- **功能**: Diffusers 与 KSampler 采样器对比
- **特点**:
  - 左侧使用 Diffusers 原生采样器
  - 右侧使用 KSampler 采样器
  - 相同参数设置，对比生成效果
  - 支持中文和英文提示词
- **适用场景**: 采样器效果对比，选择最佳采样方式

### API 格式工作流

#### hunyuan_diffusers_api.json
- **格式**: Diffusers API
- **功能**: 使用 Diffusers 后端的混元 DiT 工作流
- **特点**:
  - 原生 Diffusers 管道
  - 更好的中文理解能力
  - 支持写实风格生成
  - 示例提示词: "描绘的风格是写实，画面主要描述一双泥泞的靴子在雨天里..."
- **适用场景**: API 调用，批量生成

#### hunyuan_ksampler_api.json
- **格式**: KSampler API
- **功能**: 使用 KSampler 后端的混元 DiT 工作流
- **特点**:
  - 标准 ComfyUI KSampler 工作流
  - 兼容性更好
  - 支持中文提示词
  - 示例提示词: "描绘的风格是写实，画面主要描述一双泥泞的靴子在雨天里..."
- **适用场景**: 标准工作流使用，与其他节点兼容

## 🚀 快速开始

### 1. 下载模型

从 HuggingFace 下载混元 DiT 模型：

```bash
# 创建模型目录
mkdir -p ComfyUI/models/hunyuan

# 下载模型
wget https://huggingface.co/Tencent-Hunyuan/HunyuanDiT-v1.1-Diffusers/resolve/main/pytorch_model_ema.pt
```

将模型文件放置在 `ComfyUI/models/hunyuan/` 目录下。

### 2. 安装依赖

确保已安装 Diffusers-in-ComfyUI 自定义节点：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/maepopi/Diffusers-in-ComfyUI
```

或者使用 ComfyUI Manager 安装：
1. 打开 ComfyUI Manager
2. 搜索 "Diffusers in Comfy UI"
3. 点击安装

### 3. 加载工作流

1. 启动 ComfyUI
2. 点击 "Load" 按钮
3. 选择本目录中的 .json 文件
4. 根据需要调整提示词和参数
5. 点击 "Queue Prompt" 生成图像

## 💡 使用技巧

### 提示词编写

混元 DiT 对中文提示词理解优秀，建议使用中文描述：

**正面提示词示例**:
```
描绘的风格是写实，画面主要描述一双泥泞的靴子在雨天里，靴子颜色是棕色，泥沙溅在 Boot 的表面，背景是湿漉漉的地板，泥泞的环境，天气是阴沉的雨天，镜头是近景
```

**负面提示词**:
```
错误的眼睛，糟糕的人脸，毁容，糟糕的艺术，变形，多余的肢体，模糊的颜色，模糊，重复，病态，残缺
```

### 参数调整

- **分辨率**: 建议 1024x1024，非正方形分辨率可能失败
- **采样步数**: 30-50 步可获得较好效果
- **CFG**: 6-8，过高的 CFG 可能导致图像失真
- **采样器**: 推荐 DDIM 或 DPM++ 2M

## 🔧 技术细节

### Diffusers vs KSampler

- **Diffusers**: 原生 Diffusers 管道，更好的模型兼容性，中文理解更准确
- **KSampler**: 标准 ComfyUI 采样器，与其他节点兼容性更好

### 版本差异

- **v0**: 早期版本，基础功能
- **v1**: 改进版本，图像质量更好，中文理解更强

## 📊 性能要求

- **显存**: 建议 8GB+ VRAM
- **分辨率**: 1024x1024
- **生成时间**: 约 30-50 秒（取决于硬件配置）

## 📝 注意事项

1. 混元 DiT 模型文件较大，确保有足够的存储空间
2. 首次使用需要下载模型，可能需要较长时间
3. 非正方形分辨率当前可能失败
4. 建议使用中文提示词以获得最佳效果
5. 确保已安装 ComfyUI-Diffusers 自定义节点

## 🔗 相关资源

- [混元 DiT 官方仓库](https://huggingface.co/Tencent-Hunyuan/HunyuanDiT-v1.1-Diffusers)
- [混元 DiT 论文](https://arxiv.org/abs/2312.06697)
- [ComfyUI 官方文档](https://github.com/comfyanonymous/ComfyUI)

## 📄 许可证

混元 DiT 模型遵循其原始许可证协议。请确保在使用时遵守相关条款。