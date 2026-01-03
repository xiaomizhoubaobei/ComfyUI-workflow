# ComfyUI Workflows ZHO

我的 ComfyUI 工作流合集 | My ComfyUI workflows collection

## 简介

这是一个包含各种 ComfyUI 工作流的项目仓库，涵盖了 AI 图像生成、视频制作、3D 生成等多个领域。所有工作流均经过优化，适合不同水平的用户使用。

## 工作流列表

### 🎨 图像生成工作流

#### Stable Cascade 系列
- [Stable Cascade Canny ControlNet【Zho】.json](Stable%20Cascade%20Canny%20ControlNet%E3%80%90Zho%E3%80%91.json) - 使用 Canny 边缘检测的 Stable Cascade 工作流
- [Stable Cascade Img2Img【Zho】.json](Stable%20Cascade%20Img2Img%E3%80%90Zho%E3%80%91.json) - Stable Cascade 图像到图像生成
- [Stable Cascade Inpainting ControlNet【Zho】.json](Stable%20Cascade%20Inpainting%20ControlNet%E3%80%90Zho%E3%80%91.json) - Stable Cascade 图像重绘
- [Stable Cascade ImagePrompt Mix【Zho】.json](Stable%20Cascade%20ImagePrompt%20Mix%E3%80%90Zho%E3%80%91.json) - Stable Cascade 图像提示混合
- [Stable Cascade ImagePrompt Standard【Zho】.json](Stable%20Cascade%20ImagePrompt%20Standard%E3%80%90Zho%E3%80%91.json) - Stable Cascade 图像提示标准版

#### FLUX 系列
- [FLUX.1 DEV 1.0【Zho】.json](FLUX.1%20DEV%201.0%E3%80%90Zho%E3%80%91.json) - FLUX.1 DEV 工作流
- [FLUX.1 SCHNELL 1.0【Zho】.json](FLUX.1%20SCHNELL%201.0%E3%80%90Zho%E3%80%91.json) - FLUX.1 SCHNELL 快速工作流

#### SD3 系列
- [SD3 BASE 1.0【Zho】.json](SD3%20BASE%201.0%E3%80%90Zho%E3%80%91.json) - Stable Diffusion 3 Base 工作流
- [SD3 Medium + Qwen2 【Zho】.json](SD3%20Medium%20%2B%20Qwen2%20%E3%80%90Zho%E3%80%91.json) - SD3 Medium 结合 Qwen2 文本模型
- [SD3 Medium + 肖像大师（中文版）【Zho】.json](SD3%20Medium%20%2B%20%E8%82%96%E5%83%8F%E5%A4%A7%E5%B8%88%EF%BC%88%E4%B8%AD%E6%96%87%E7%89%88%EF%BC%89%E3%80%90Zho%E3%80%91.json) - SD3 Medium 结合中文肖像大师
- [SD3是否内置文本编码器的对比【Zho】.json](SD3%E6%98%AF%E5%90%A6%E5%86%85%E7%BD%AE%E6%96%87%E6%9C%AC%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%AF%B9%E6%AF%94%E3%80%90Zho%E3%80%91.json) - SD3 文本编码器对比工作流

#### 其他模型
- [SDXS-512-0.9【Zho】.json](SDXS-512-0.9%E3%80%90Zho%E3%80%91.json) - SDXS 快速生成模型工作流
- [CosXL Edit + ArtGallery 1.0【Zho】.json](CosXL%20Edit%20%2B%20ArtGallery%201.0%E3%80%90Zho%E3%80%91.json) - CosXL 编辑结合 ArtGallery

### 🎬 视频生成工作流

- [HUNYUAN VIDEO 1.0 【Zho】.json](HUNYUAN%20VIDEO%201.0%20%E3%80%90Zho%E3%80%91.json) - 混元视频生成工作流
- [LivePortrait Animals 1.0【Zho】.json](LivePortrait%20Animals%201.0%E3%80%90Zho%E3%80%91.json) - 动物肖像动画工作流

### 🎭 3D 生成工作流

- [CRM Comfy 3D【Zho】.json](CRM%20Comfy%203D%E3%80%90Zho%E3%80%91.json) - CRM 3D 生成工作流
- [Sketch to 3D【Zho】.json](Sketch%20to%203D%E3%80%90Zho%E3%80%91.json) - 草图转 3D 工作流

## 使用方法

### 前置要求

- 安装 [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- 安装所需的自定义节点（根据具体工作流需求）
- 下载所需的模型文件

### 使用步骤

1. 启动 ComfyUI
2. 点击 "Load" 按钮
3. 选择本仓库中的 `.json` 工作流文件
4. 根据需要配置参数
5. 点击 "Queue Prompt" 开始生成

## 工作流分类

- **图像生成**: Stable Cascade, FLUX, SD3, SDXS, CosXL
- **视频生成**: Hunyuan Video, LivePortrait
- **3D 生成**: CRM 3D, Sketch to 3D
- **图像编辑**: Img2Img, Inpainting, ImagePrompt
---

**最后更新**: 2026-01-03