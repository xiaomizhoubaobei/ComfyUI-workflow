# BrushNet + PowerPaint 工作流集

本目录包含基于 BrushNet 和 PowerPaint 模型的高级图像修复、重绘、扩图和擦除工作流。这些工作流提供了强大的图像编辑功能，能够处理复杂的修复任务。

## 📁 工作流文件

### BrushNet 系列

#### BrushNet1.json
- **功能**: BrushNet 基础重绘工作流
- **特点**:
  - 支持手动遮罩绘制
  - 基于文本提示词进行重绘
  - 适合局部区域修复和重绘
- **适用场景**: 
  - 局部图像修复
  - 物体替换
  - 细节增强

#### BrushNet1a-segrand.json
- **功能**: BrushNet 随机遮罩重绘
- **特点**:
  - 自动生成随机遮罩
  - 支持遮罩密度调整
  - 测试和实验用途
- **适用场景**:
  - 模型效果测试
  - 批量处理
  - 遮罩效果对比

#### BrushNet2.json
- **功能**: BrushNet 进阶重绘工作流
- **特点**:
  - 更高级的重绘控制
  - 支持多区域处理
  - 更好的细节保留
- **适用场景**:
  - 复杂场景重绘
  - 大面积修复
  - 艺术风格转换

#### BrushNet3.json
- **功能**: BrushNet 高级重绘工作流
- **特点**:
  - 优化的重绘算法
  - 支持高分辨率处理
  - 更快的生成速度
- **适用场景**:
  - 高质量图像修复
  - 专业级图像编辑
  - 商业用途

### PowerPaint V2 系列

#### PowerPaintV2-1.json
- **功能**: PowerPaint V2 基础版本
- **特点**:
  - 基于文本的智能填充
  - 支持多种修复模式
  - 结合 GroundingDINO 和 SAM 进行自动分割
- **适用场景**:
  - 智能对象移除
  - 文本引导的图像修复
  - 自动遮罩生成

#### PowerPaintV2-2.json
- **功能**: PowerPaint V2 扩展版本
- **特点**:
  - 支持更多修复模式
  - 更好的上下文理解
  - 支持对象级编辑
- **适用场景**:
  - 复杂对象编辑
  - 场景重构
  - 内容生成

#### PowerPaintV2-3.json
- **功能**: PowerPaint V2 高级版本
- **特点**:
  - 最新的 PowerPaint 功能
  - 支持多种编辑任务
  - 最佳的生成质量
- **适用场景**:
  - 专业图像编辑
  - 商业项目
  - 创意设计

## 🚀 快速开始

### 1. 安装依赖

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/nullquant/ComfyUI-BrushNet
```

### 2. 下载模型

#### BrushNet 模型
从 HuggingFace 下载 BrushNet 模型：

```bash
mkdir -p ComfyUI/models/inpaint

# SD 1.5 版本
wget https://huggingface.co/Sanster/BrushNet/resolve/main/diffusion_pytorch_model.safetensors

# SDXL 版本
wget https://huggingface.co/Sanster/BrushNet/resolve/main/diffusion_pytorch_model_sdxl_v0.safetensors
```

#### PowerPaint 模型
下载 PowerPaint 所需模型：

```bash
# PowerPaint 主模型
wget https://huggingface.co/open-mmlab/PowerPaint/resolve/main/diffusion_pytorch_model.safetensors

# 文本编码器模型
wget https://huggingface.co/open-mmlab/PowerPaint/resolve/main/model.safetensors
```

将模型文件放置在 `ComfyUI/models/inpaint/` 目录下。

#### SAM 和 GroundingDINO 模型（PowerPaint 需要）
```bash
mkdir -p ComfyUI/models/sam
mkdir -p ComfyUI/models/grounding-dino

# SAM 模型
wget https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth

# GroundingDINO 模型
wget https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
```

### 3. 加载工作流

1. 启动 ComfyUI
2. 点击 "Load" 按钮
3. 选择本目录中的 .json 文件
4. 上传输入图像和遮罩（如需要）
5. 调整提示词和参数
6. 点击 "Queue Prompt" 生成结果

## 💡 使用技巧

### BrushNet 使用技巧

1. **遮罩准备**
   - 使用红色通道作为遮罩
   - 确保遮罩边缘清晰
   - 可以使用 Photoshop 或其他工具绘制遮罩

2. **提示词编写**
   - 正面提示词：描述你想要的内容
   - 负面提示词：描述你不想要的内容
   - 示例：
     ```
     正面: 一只可爱的小猫，毛茸茸的，坐在草地上
     负面: 模糊，变形，多余的手指
     ```

3. **参数调整**
   - `denoise`: 控制重绘强度（0.5-1.0）
   - `steps`: 采样步数（20-40）
   - `cfg`: 提示词引导强度（5-8）

### PowerPaint 使用技巧

1. **修复模式选择**
   - **文本引导修复**: 使用文本描述修复内容
   - **对象移除**: 自动移除指定对象
   - **形状填充**: 保持形状进行内容填充

2. **自动分割**
   - 使用 GroundingDINO 检测对象
   - 使用 SAM 进行精确分割
   - 支持文本提示自动生成遮罩

3. **混合使用**
   - 可以结合 BrushNet 和 PowerPaint
   - 先用 PowerPaint 自动生成遮罩
   - 再用 BrushNet 进行精细调整

## 🔧 技术细节

### BrushNet 特点

- **双分支架构**: 分离遮罩图像和噪声潜在
- **即插即用**: 可以与任何预训练扩散模型配合使用
- **高质量修复**: 保持图像质量和语义一致性
- **支持多种模型**: SD 1.5 和 SDXL

### PowerPaint 特点

- **多任务学习**: 支持多种图像编辑任务
- **文本引导**: 强大的文本理解能力
- **自动分割**: 集成 SAM 和 GroundingDINO
- **V2 改进**: 更好的生成质量和速度

## 📊 性能要求

- **显存**: 建议 8GB+ VRAM
- **分辨率**: 支持最高 2048x2048
- **生成时间**: 
  - BrushNet: 10-30 秒
  - PowerPaint: 15-40 秒
  - 取决于图像大小和硬件配置

## 📝 注意事项

1. **模型文件较大**: 确保有足够的存储空间
2. **遮罩质量**: 遮罩质量直接影响修复效果
3. **提示词重要性**: 准确的提示词能获得更好的结果
4. **分辨率限制**: 过高的分辨率可能导致显存不足
5. **首次使用**: 建议先使用小图像测试效果

## 🎯 应用场景

### 图像修复
- 修复老照片
- 去除水印
- 修复划痕和污渍

### 内容编辑
- 移除不需要的对象
- 替换背景
- 添加新元素

### 艺术创作
- 风格转换
- 创意重绘
- 艺术效果增强

### 商业应用
- 产品图片编辑
- 广告素材制作
- 电商图片优化

## 🔗 相关资源

- [BrushNet 论文](https://arxiv.org/abs/2403.06976)
- [BrushNet GitHub](https://github.com/Sanster/BrushNet)
- [PowerPaint GitHub](https://github.com/open-mmlab/PowerPaint)
- [ComfyUI-BrushNet 节点](https://github.com/nullquant/ComfyUI-BrushNet)
- [ComfyUI 官方文档](https://github.com/comfyanonymous/ComfyUI)

## 📄 许可证

BrushNet 和 PowerPaint 模型遵循其原始许可证协议。请确保在使用时遵守相关条款。

## 🤝 常见问题

### Q1: BrushNet 和 PowerPaint 有什么区别？
A: BrushNet 专注于高质量图像重绘，需要手动或自动提供遮罩；PowerPaint 支持多种编辑任务，包括自动对象检测和分割。

### Q2: 如何选择合适的工作流？
A: 
- 简单重绘：使用 BrushNet1.json
- 自动对象移除：使用 PowerPaintV2-1.json
- 复杂编辑：使用 BrushNet3.json 或 PowerPaintV2-3.json

### Q3: 显存不足怎么办？
A: 
- 降低图像分辨率
- 减少批次大小
- 使用 FP16 精度
- 选择更小的模型版本

### Q4: 如何获得最佳效果？
A: 
- 使用高质量的输入图像
- 准确绘制遮罩
- 编写详细的提示词
- 调整合适的参数

### Q5: 支持哪些模型？
A: 
- BrushNet: 支持 SD 1.5 和 SDXL
- PowerPaint: 主要支持 SD 1.5
- 需要相应的基础模型文件