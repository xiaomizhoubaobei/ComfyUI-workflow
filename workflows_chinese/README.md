# ComfyUI 中文工作流集

这个目录包含了各种预配置的 **ComfyUI 中文工作流**，涵盖 AI 图像生成、处理、修复、视频制作等多个领域。所有工作流均经过优化，适合中文用户使用。

## 📑 目录

- [工作流分类](#-工作流分类)
- [🚀 快速开始](#-快速开始)
- [📦 依赖与安装](#-依赖与安装)
- [💻 硬件要求](#-硬件要求)
- [📝 注意事项](#-注意事项)
- [🔧 技术支持](#-技术支持)
- [❓ 常见问题](️-常见问题)

## 📁 工作流分类

### 🎨 图像生成

#### Stable Cascade 系列
- `1.0Cascade_Standard.json` - Cascade 模型标准工作流
- `1.1cascade-inpainting.json` - Cascade 模型重绘工作流
- `1.2cosXL编辑版.json` - Cascade XL 编辑版工作流

#### 其他生成模型
- `12-PixArt-sigma.json` - PixArt-sigma 模型工作流
- `hunyuandit/` - 混元 DiT 模型工作流目录

### 🔍 图像放大与增强
- `2.0放大supir.json` - SUPIR 模型图像放大，支持高质量超分辨率

### 🖌️ 局部重绘与修复
- `10局部重绘-进阶版.json` - 高级局部重绘，支持复杂场景
- `4.0修复手部.json` - AI 手部修复，解决常见的手部绘制问题
- `小小局部重绘Inpaint_Anything.json` - Inpaint Anything 局部重绘
- `重绘、扩图、擦除BrushNet+PowerPaint给你完美解决/` - BrushNet+PowerPaint 修复组合目录
- `comfyui-flux局部重绘（升级版）修脸、修手、修一切2024-8-13.json` - Flux 模型局部重绘升级版

### 🖼️ 扩图与背景处理
- `5.0扩图.json` - 智能扩图，扩展图像边界
- `6.0移除背景3件套.json` - 综合背景移除方案
- `6.0移除背景BiRefNet-ZHO.json` - BiRefNet 模型背景移除
- `6.0移除背景BRIA.json` - BRIA 模型背景移除
- `IC-Light产品换背景2024-7-27.json` - IC-Light 产品背景替换

### 👤 人像处理与换脸
- `100%还原参考人脸.json` - 人脸风格迁移，高度还原参考人脸
- `9.0InstantID-换脸到任何风格图上.json` - InstantID 换脸到任意风格
- `reface-变脸到动漫.json` - Reface 变脸到动漫风格
- `reface-变脸到真人.json` - Reface 变脸到真人风格

### 🎭 风格转换
- `9.1IPAdapter-V2.0风格转换.json` - IPAdapter V2.0 风格转换
- `9.2IPAdapter-V2.0构图转换.json` - IPAdapter V2.0 构图转换
- `9.3IPAdapter-V2.0构图+风格转换.json` - IPAdapter V2.0 构图与风格双重转换

### 🎬 视频处理
- `2025-7-1转绘全自动SegaAttention.json` - 视频转绘，使用 SegaAttention 技术
- `凡人-视频转绘/` - 凡人视频转绘工作流目录
- `送给小白的傻瓜动画工作流.json` - 简单易用的动画制作工作流

### 📄 证件照与实用工具
- `2024-9-9一键制作证件照（HivisionIDPhotos）.json` - 一键制作证件照，使用 HivisionIDPhotos
- `anytext-一键12套.json` - AnyText 文本生成，12套预设方案

### 🎯 ControlNet 与线稿控制
- `MistoLine一个足矣.json` - MistoLine 线稿控制（基础版）
- `MistoLine（+Anyline）一个足矣【第二版】.json` - MistoLine + Anyline 线稿控制（增强版）
- `SD3_ControNet_Canny一键克隆midjouney橱窗图片.json` - SD3 ControlNet Canny 边缘检测，克隆 Midjourney 图片

### 🤖 智能检测与分割
- `3.0检测（简单）YoloWorld-EfficientSAM.json` - YoloWorld + EfficientSAM 简单检测
- `3.1检测+重绘YoloWorld-EfficientSAM.json` - YoloWorld + EfficientSAM 检测与重绘

### 🌟 Flux 模型系列
- `ComfyUI-结合FLUX写汉字、做海报、做封面2024-8-19.json` - Flux 模型生成汉字、海报和封面
- `fluxDev-LLM+图生图无限可能2024-8-9.json` - Flux Dev 结合 LLM 的图生图
- `fluxDev-图生图&切换文生图.json` - Flux Dev 图生图与文生图切换

### 🧠 高级功能
- `11ELLA-复杂提示词理解.json` - ELLA 复杂提示词理解，提升提示词效果

## 🚀 快速开始

### 基础使用
1. **启动 ComfyUI**
   ```bash
   cd ComfyUI
   python main.py --listen 0.0.0.0 --port 8188
   ```

2. **加载工作流**
   - 在浏览器中打开 `http://127.0.0.1:8188`
   - 点击右上角 "Load" 按钮
   - 浏览并选择本目录中的 .json 文件

3. **配置参数**
   - 上传输入图像（如需要）
   - 调整文本提示词（支持中文）
   - 检查模型路径是否正确
   - 设置生成参数（步数、CFG、分辨率等）

4. **运行工作流**
   - 点击 "Queue Prompt" 按钮开始生成
   - 等待生成完成，查看输出结果

### 子目录使用
- 部分工作流位于子目录中（如 `hunyuandit/`、`凡人-视频转绘/`、`重绘、扩图、擦除BrushNet+PowerPaint给你完美解决/` 等）
- 进入相应子目录查看详细工作流文件
- 子目录中的工作流可能包含多个相关配置文件

### 提示词编写技巧
- **正面提示词**: 描述你想要的内容
  - 示例: "一张美丽的风景画，山脉和湖泊，日落时分，高清，细节丰富"
- **负面提示词**: 描述你不想要的内容
  - 示例: "模糊，低质量，变形，丑陋，多余的手指"
- **使用标点**: 用逗号分隔不同的描述元素
- **调整权重**: 使用 `(keyword:1.2)` 增加强度，`(keyword:0.8)` 降低强度

## 📦 依赖与安装

### 必需组件
- ComfyUI 主程序
- 相应的模型文件（SDXL、Flux、Cascade 等）
- 自定义节点（根据具体工作流需求）

### 安装步骤

#### 1. 安装 ComfyUI
```bash
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install -r requirements.txt
```

#### 2. 安装自定义节点
在 ComfyUI 目录的 `custom_nodes` 文件夹中安装所需节点：

```bash
cd custom_nodes
# InstantID - 人脸身份保持与换脸技术，支持将人脸特征迁移到不同风格
git clone https://github.com/cubiq/ComfyUI_InstantID

# IPAdapter - 图像提示适配器，实现图像风格和构图迁移
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus

# YoloWorld-EfficientSAM - 目标检测与图像分割，支持文本提示检测和精确分割
git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM

# BrushNet - 高级图像修复与重绘，包含 PowerPaint 功能，支持复杂场景修复
git clone https://github.com/nullquant/ComfyUI-BrushNet

# IC-Light - 智能光照处理，实现产品背景替换和光照一致性调整
git clone https://github.com/kijai/ComfyUI-IC-Light
```

#### 3. 下载模型文件

**基础模型**:
- SDXL: [下载链接](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- Flux: [下载链接](https://huggingface.co/black-forest-labs/FLUX.1-dev)
- Stable Cascade: [下载链接](https://huggingface.co/stabilityai/stable-cascade)

**专用模型**:
- InstantID: [下载链接](https://huggingface.co/InstantX/InstantID)
- IPAdapter: [下载链接](https://huggingface.co/h94/IP-Adapter)
- ControlNet: [下载链接](https://huggingface.co/lllyasviel/ControlNet-v1-1)
- 混元 DiT: 使用 `huggingface-cli download Tencent-Hunyuan/HunyuanDiT --local-dir ./ckpts` 下载

### 常见自定义节点
- **ComfyUI_InstantID** - InstantID 换脸功能
- **ComfyUI_IPAdapter_plus** - IPAdapter 风格转换
- **ComfyUI-YoloWorld-EfficientSAM** - YoloWorld 目标检测 + EfficientSAM 分割
- **ComfyUI-BrushNet** - BrushNet 重绘（包含 PowerPaint 功能）
- **ComfyUI-IC-Light** - IC-Light 光照处理
- **Diffusers-in-ComfyUI** - Diffusers 管道支持，用于混元 DiT 等模型

## 💻 硬件要求

### 最低配置
- **显卡**: NVIDIA GTX 1060 6GB 或同等性能
- **内存**: 16GB RAM
- **存储**: 50GB 可用空间
- **系统**: Windows 10/11, Linux, macOS

### 推荐配置
- **显卡**: NVIDIA RTX 3060 12GB 或更高
- **内存**: 32GB RAM
- **存储**: 100GB SSD
- **系统**: Windows 10/11, Linux

### 不同工作流的显存需求
- **轻量级** (4-6GB VRAM): `1.0Cascade_Standard.json`, `小小局部重绘Inpaint_Anything.json`, `anytext-一键12套.json`
- **中等** (8-12GB VRAM): `10局部重绘-进阶版.json`, `9.0InstantID-换脸到任何风格图上.json`, `fluxDev-图生图&切换文生图.json`, `hunyuandit/Huyuan-dit--v0-rodent.json`
- **高需求** (16GB+ VRAM): `2.0放大supir.json`, `comfyui-flux局部重绘（升级版）修脸、修手、修一切2024-8-13.json`, `2025-7-1转绘全自动SegaAttention.json`, `hunyuandit/Huyuan-dit--v1-compare.json`

## 📝 注意事项

- 部分工作流可能需要额外安装扩展或模型，请根据工作流内的提示进行配置
- 所有工作流均为中文配置，适合中文用户使用
- 建议根据硬件配置选择合适的工作流（显存需求不同）
- 首次使用建议从编号较小的工作流开始（如 1.0、2.0 等）
- 生成大尺寸图像时建议使用高分辨率工作流或分步生成

## 🔧 技术支持

如遇到问题，请检查：
1. 模型文件是否正确下载并放置在对应目录
2. 所需自定义节点是否已安装
3. ComfyUI 版本是否兼容
4. 硬件配置是否满足要求

## ❓ 常见问题

### Q1: 如何安装自定义节点？
A: 在 ComfyUI 目录下运行以下命令：
```bash
cd custom_nodes
git clone <节点仓库地址>
```
然后重启 ComfyUI 即可。

### Q2: 模型文件应该放在哪里？
A: 不同类型的模型需要放在不同目录：
- Checkpoints: `models/checkpoints/`
- VAE: `models/vae/`
- LoRA: `models/loras/`
- ControlNet: `models/controlnet/`
- IPAdapter: `models/ipadapter/`
- InstantID: `models/instantid/`

### Q3: 显存不足怎么办？
A: 可以尝试以下方法：
- 降低生成分辨率
- 减少批次大小（batch size）
- 使用显存优化选项（如 FP16）
- 选择更小的模型

### Q4: 工作流加载后显示错误？
A: 检查以下几点：
- 确认所有必需的节点已安装
- 检查模型文件是否存在
- 查看 ComfyUI 控制台的错误信息
- 尝试更新 ComfyUI 和相关节点到最新版本

### Q5: 如何获取更好的生成效果？
A: 建议尝试：
- 使用高质量的提示词
- 调整采样步数和 CFG 值
- 使用合适的种子值
- 参考工作流中的默认参数设置

## 📚 相关资源

- [ComfyUI 官方文档](https://github.com/comfyanonymous/ComfyUI)
- [模型下载推荐](https://civitai.com/)
- [社区教程](https://www.reddit.com/r/comfyui/)

## 📄 许可证

本工作流集遵循原 ComfyUI 的许可证协议。请确保在使用时遵守相关模型的许可证要求。

## 🤝 贡献

欢迎提交问题报告和改进建议！
