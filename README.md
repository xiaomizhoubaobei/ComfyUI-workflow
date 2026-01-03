# ComfyUI 工作流集合

这是一个包含各种 ComfyUI 工作流的项目仓库，涵盖了 AI 图像生成、视频制作、3D 生成、音频处理等多个领域。所有工作流均经过优化，适合不同水平的用户使用。

## 📑 目录

- [项目简介](#项目简介)
- [项目结构](#-项目结构)
- [快速开始](#-快速开始)
- [主要模型](#-主要模型)
- [文档](#-文档)
- [硬件要求](#-硬件要求)
- [使用技巧](#-使用技巧)
- [常见问题](#-常见问题)
- [相关资源](#-相关资源)
- [许可证](#-许可证)

## 📁 项目结构

### 主要工作流目录

#### 🇨🇳 中文工作流 (`workflows_chinese/`)
包含大量中文优化的 ComfyUI 工作流，适合中文用户使用。

**主要分类**:
- 图像生成 (Stable Cascade, PixArt-sigma, 混元 DiT)
- 图像放大与增强 (SUPIR)
- 局部重绘与修复 (BrushNet, PowerPaint)
- 扩图与背景处理
- 人像处理与换脸 (InstantID, IPAdapter)
- 风格转换
- 视频处理
- 证件照制作
- ControlNet 与线稿控制
- 智能检测与分割
- Flux 模型系列

**子目录**:
- `hunyuandit/` - 混元 DiT 工作流集（详细文档）
- `重绘、扩图、擦除BrushNet+PowerPaint给你完美解决/` - BrushNet + PowerPaint 工作流集（详细文档）
- `凡人-视频转绘/` - 凡人视频转绘工作流集（详细文档）

#### 📚 ComfyUI Wiki (`ComfyUI-wiki/`)
ComfyUI 相关文档和资源集合。

#### 🎨 图像生成工作流

- `2_pass_txt2img/` - 两阶段文本生成图像
- `3d/` - 3D 图像生成
- `area_composition/` - 区域合成
- `flux/` - Flux 模型工作流
- `flux2/` - Flux 2.0 工作流
- `hidream/` - HiDream 模型工作流
- `hunyuan_dit/` - 混元 DiT 图像生成
- `hunyuan_image/` - 混元图像生成
- `lumina2/` - Lumina 2 模型
- `omnigen/` - OmniGen 模型
- `sd3/` - Stable Diffusion 3
- `sdxl/` - Stable Diffusion XL
- `stable_cascade/` - Stable Cascade
- `unclip/` - UnCLIP 模型
- `z_image/` - Z 图像生成

#### 🎬 视频工作流

- `video/` - 视频生成和处理
- `ltxv/` - LTXV 视频生成
- `mochi/` - Mochi 视频生成
- `wan/` - Wan 视频生成
- `wan22/` - Wan 2.2 视频生成
- `hunyuan_video/` - 混元视频生成
- `cosmos/` - Cosmos 视频生成
- `cosmos_predict2/` - Cosmos Predict 2

#### 🖌️ 图像编辑工作流

- `inpaint/` - 图像重绘和修复
- `img2img/` - 图像到图像转换
- `edit_models/` - 编辑模型
- `hypernetworks/` - 超网络
- `lora/` - LoRA 模型
- `model_merging/` - 模型合并
- `noisy_latent_composition/` - 噪声潜在组合

#### 🎯 控制与增强

- `controlnet/` - ControlNet 工作流
- `lcm/` - LCM (Latent Consistency Models)
- `audio/` - 音频处理
- `images/` - 图像示例
- `faq/` - 常见问题

## 🚀 快速开始

### 前置要求

- Python 3.8+
- Git
- NVIDIA GPU（推荐 8GB+ VRAM）
- CUDA 11.8+ 或 12.x

### 安装 ComfyUI

#### 方法一：使用 Git 克隆

```bash
# 克隆 ComfyUI 仓库
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 启动 ComfyUI
python main.py --listen 0.0.0.0 --port 8188
```

#### 方法二：使用 ComfyUI Manager（推荐）

1. 下载 ComfyUI-Manager
2. 在 ComfyUI 中安装管理器
3. 通过管理器安装节点和模型

### 使用工作流

1. 启动 ComfyUI
2. 在浏览器中打开 `http://127.0.0.1:8188`
3. 点击右上角 "Load" 按钮
4. 浏览并选择本仓库中的 `.json` 工作流文件
5. 根据需要配置参数（提示词、分辨率等）
6. 点击 "Queue Prompt" 开始生成
7. 等待生成完成，查看输出结果

### 安装自定义节点

```bash
cd ComfyUI/custom_nodes

# 常用节点
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus
git clone https://github.com/cubiq/ComfyUI_InstantID
git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM
git clone https://github.com/nullquant/ComfyUI-BrushNet
git clone https://github.com/kijai/ComfyUI-IC-Light
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite
git clone https://github.com/maepopi/Diffusers-in-ComfyUI
```

## 📦 主要模型

### 图像生成模型

| 模型 | 用途 | 显存需求 | 推荐场景 |
|------|------|----------|----------|
| Stable Diffusion 1.5 | 基础图像生成 | 4GB+ | 日常使用，快速生成 |
| Stable Diffusion 2.1 | 改进版 SD | 6GB+ | 高质量图像生成 |
| Stable Diffusion XL (SDXL) | 高分辨率生成 | 8GB+ | 专业图像创作 |
| Stable Diffusion 3 (SD3) | 最新 SD 系列 | 12GB+ | 高质量图像生成 |
| Stable Cascade | 高效生成 | 6GB+ | 快速高质量生成 |
| Flux | 新一代模型 | 12GB+ | 现代风格生成 |
| 混元 DiT (HunyuanDiT) | 中文优化 | 8GB+ | 中文提示词生成 |
| PixArt-sigma | 高质量生成 | 8GB+ | 艺术创作 |

### 视频生成模型

| 模型 | 用途 | 显存需求 | 特点 |
|------|------|----------|------|
| LTXV | 快速视频生成 | 8GB+ | 实时生成 |
| Mochi | 高质量视频 | 12GB+ | 细节丰富 |
| Wan | 通用视频生成 | 16GB+ | 多样化风格 |
| Cosmos | NVIDIA 视频 | 12GB+ | 高性能 |
| 混元视频 (HunyuanVideo) | 中文视频 | 12GB+ | 中文优化 |

### 专用模型

| 模型 | 用途 | 安装位置 |
|------|------|----------|
| InstantID | 人脸身份保持 | `models/instantid/` |
| IPAdapter | 图像提示适配器 | `models/ipadapter/` |
| ControlNet | 结构控制 | `models/controlnet/` |
| BrushNet | 图像修复 | `models/inpaint/brushnet_sd1.5/` |
| PowerPaint | 智能修复 | `models/inpaint/` |
| SUPIR | 图像放大 | `models/supir/` |
| 混元 DiT | 中文生成 | `models/hunyuan/ckpts/` |

## 📖 文档

### 中文工作流文档
- [workflows_chinese/README.md](workflows_chinese/README.md) - 中文工作流总览
- [workflows_chinese/hunyuandit/README.md](workflows_chinese/hunyuandit/README.md) - 混元 DiT 工作流
- [workflows_chinese/重绘、扩图、擦除BrushNet+PowerPaint给你完美解决/README.md](workflows_chinese/重绘、扩图、擦除BrushNet+PowerPaint给你完美解决/README.md) - BrushNet + PowerPaint 工作流
- [workflows_chinese/凡人-视频转绘/README.md](workflows_chinese/凡人-视频转绘/README.md) - 凡人视频转绘工作流

### 其他资源
- [ComfyUI 官方文档](https://github.com/comfyanonymous/ComfyUI)
- [ComfyUI Wiki](ComfyUI-wiki/)
- [FAQ](faq/)

## 🔧 常用自定义节点

### 核心节点

**InstantID** - 人脸换脸和身份保持
```bash
git clone https://github.com/cubiq/ComfyUI_InstantID
```

**IPAdapter** - 图像风格和构图迁移
```bash
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus
```

**ControlNet** - 结构控制和引导
- 已内置在 ComfyUI 中

**BrushNet** - 高级图像修复
```bash
git clone https://github.com/nullquant/ComfyUI-BrushNet
```

**PowerPaint** - 智能图像编辑
- 包含在 BrushNet 中

**IC-Light** - 光照处理
```bash
git clone https://github.com/kijai/ComfyUI-IC-Light
```

### 视频处理

**ComfyUI-VideoHelperSuite** - 视频加载和保存
```bash
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite
```

**AnimateDiff** - 动画生成
```bash
git clone https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved
```

### 检测与分割

**YoloWorld-EfficientSAM** - 目标检测和分割
```bash
git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM
```

**GroundingDINO** - 文本引导目标检测
```bash
git clone https://github.com/IDEA-Research/GroundingDINO
```

### Diffusers 支持

**Diffusers-in-ComfyUI** - Diffusers 管道支持
```bash
git clone https://github.com/maepopi/Diffusers-in-ComfyUI
```

## 💻 硬件要求

### 最低配置
- **GPU**: NVIDIA GTX 1060 6GB 或同等性能
- **RAM**: 16GB
- **存储**: 50GB 可用空间
- **系统**: Windows 10/11, Linux, macOS

### 推荐配置
- **GPU**: NVIDIA RTX 3060 12GB 或更高
- **RAM**: 32GB
- **存储**: 100GB SSD
- **系统**: Windows 10/11, Linux

### 高性能配置
- **GPU**: NVIDIA RTX 4090 24GB
- **RAM**: 64GB
- **存储**: 200GB NVMe SSD
- **系统**: Windows 10/11, Linux

### 不同任务的显存需求

| 任务 | 最低显存 | 推荐显存 |
|------|----------|----------|
| SD 1.5 生成 | 4GB | 8GB |
| SDXL 生成 | 8GB | 12GB |
| SD3 生成 | 12GB | 16GB |
| Flux 生成 | 12GB | 24GB |
| 视频生成 | 12GB | 24GB |
| 高分辨率放大 | 8GB | 16GB |

## 📝 使用技巧

### 提示词编写

**基本规则**:
- 使用清晰、具体的描述
- 用逗号分隔不同的描述元素
- 使用权重调整：`(keyword:1.2)` 增强强度，`(keyword:0.8)` 降低强度

**正面提示词示例**:
```
美丽的风景画，山脉和湖泊，日落时分，高清，细节丰富，电影级光照
```

**负面提示词示例**:
```
模糊，低质量，变形，丑陋，多余的手指，水印，文字
```

**权重调整**:
```
(keyword:1.5)  - 大幅增强
(keyword:1.2)  - 轻微增强
(keyword:0.8)  - 轻微减弱
(keyword:0.5)  - 大幅减弱
```

### 参数优化

**采样步数**:
- 20-30 步：快速生成，质量尚可
- 30-50 步：平衡质量和速度
- 50+ 步：最高质量，但速度较慢

**CFG (Classifier Free Guidance)**:
- 5-7：适合大多数情况
- 7-9：更强的提示词遵循
- 9+：可能导致图像失真

**分辨率**:
- 512x512：快速生成，适合测试
- 768x768：平衡质量和速度
- 1024x1024：高质量生成
- 更高分辨率：需要更多显存

**批次大小**:
- 1：单张生成，显存占用最小
- 2-4：批量生成，提高效率
- 4+：需要更多显存

### 性能优化

**降低显存占用**:
- 使用 FP16 精度
- 降低分辨率
- 减少批次大小
- 使用 tiled sampling
- 启用 xformers 优化

**提高生成速度**:
- 使用更快的采样器（DPM++ 2M）
- 减少采样步数
- 使用 LCM 模型
- 启用 GPU 加速

**提高生成质量**:
- 增加采样步数
- 使用高质量采样器（DPM++ SDE）
- 使用 Refiner 模型
- 调整 CFG 值
- 使用更好的提示词

## ❓ 常见问题

### Q1: 如何安装自定义节点？
A: 在 ComfyUI 的 `custom_nodes` 目录下运行：
```bash
git clone <节点仓库地址>
```
然后重启 ComfyUI。或者使用 ComfyUI Manager 自动安装。

### Q2: 模型文件应该放在哪里？
A: 不同类型的模型需要放在不同目录：
- Checkpoints: `models/checkpoints/`
- VAE: `models/vae/`
- LoRA: `models/loras/`
- ControlNet: `models/controlnet/`
- IPAdapter: `models/ipadapter/`
- InstantID: `models/instantid/`
- BrushNet: `models/inpaint/brushnet_sd1.5/`

### Q3: 显存不足怎么办？
A: 可以尝试以下方法：
- 降低生成分辨率
- 减少批次大小
- 使用 FP16 精度
- 使用 tiled sampling
- 选择更小的模型

### Q4: 工作流加载后显示错误？
A: 检查以下几点：
- 确认所有必需的节点已安装
- 检查模型文件是否存在
- 查看 ComfyUI 控制台的错误信息
- 尝试更新 ComfyUI 和相关节点

### Q5: 如何获取更好的生成效果？
A: 建议尝试：
- 使用高质量的提示词
- 调整采样步数和 CFG 值
- 使用合适的采样器
- 使用 Refiner 模型
- 参考工作流中的默认参数

### Q6: 如何备份和分享工作流？
A: 
- 点击 "Save" 按钮保存工作流为 .json 文件
- 可以将 .json 文件分享给其他人
- 加载时点击 "Load" 按钮选择 .json 文件

### Q7: 支持哪些图像格式？
A: 
- 输入：PNG, JPG, WEBP, BMP 等
- 输出：PNG, JPG, WEBP 等
- 视频：MP4, WEBM, GIF 等

### Q8: 如何使用中文提示词？
A: 
- 使用混元 DiT 等中文优化的模型
- 或使用翻译工具将中文提示词翻译为英文
- 部分模型对中文支持有限

## 🔗 相关资源

### 官方资源
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [ComfyUI 官方文档](https://docs.comfy.org/)
- [HuggingFace](https://huggingface.co/)
- [Stability AI](https://stability.ai/)

### 模型下载
- [Civitai](https://civitai.com/) - SD 模型下载
- [HuggingFace Models](https://huggingface.co/models) - 各类模型
- [LiblibAI](https://www.liblib.art/) - 中文模型平台
- [ModelScope](https://modelscope.cn/) - 阿里模型平台

### 社区资源
- [ComfyUI Reddit](https://www.reddit.com/r/comfyui/)
- [ComfyUI Discord](https://discord.gg/comfyui)
- [GitHub Discussions](https://github.com/comfyanonymous/ComfyUI/discussions)
- [Bilibili 教程](https://www.bilibili.com/) - 中文教程

### 学习资源
- [ComfyUI 教程合集](https://www.youtube.com/)
- [AI 绘画论坛](https://www.liblib.art/forum)
- [Stable Diffusion 论坛](https://civitai.com/)

## 📄 许可证

本项目遵循原 ComfyUI 和相关模型的许可证协议。请确保在使用时遵守相关条款。

主要许可证：
- ComfyUI: GPL-3.0
- Stable Diffusion 系列: CreativeML Open RAIL-M
- 其他模型：请参考各自模型的许可证

## 🤝 贡献

欢迎提交问题报告和改进建议！

### 贡献方式
- 提交 Issue 报告问题
- 发送 Pull Request 贡献代码
- 分享你的工作流
- 改进文档

### 贡献指南
1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## ⚠️ 免责声明

本仓库中的工作流和模型仅供学习和研究使用。使用时请遵守相关法律法规和模型许可证。作者不对使用本仓库内容产生的任何后果负责。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- 提交 [Issue](https://github.com/yourusername/ComfyUI-workflows/issues)
- 发送 [Pull Request](https://github.com/yourusername/ComfyUI-workflows/pulls)
- 参与 [Discussions](https://github.com/yourusername/ComfyUI-workflows/discussions)

## 🌟 致谢

感谢所有为 ComfyUI 和相关模型做出贡献的开发者和社区成员！

---

**最后更新**: 2026-01-03  
**版本**: 1.0.0