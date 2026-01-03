# ComfyUI + IPAdapter 线稿上色系列工作流

本目录包含使用 ComfyUI 和 IPAdapter 技术实现的线稿上色和图像风格转换工作流。

## 📁 工作流列表

### 1. 线稿上色1.json
**基础线稿上色工作流**

- **功能**: 使用 IPAdapter 和 T2I-Adapter 为黑白线稿进行上色
- **主要技术**:
  - IPAdapter Advanced (风格迁移)
  - T2I-Adapter Lineart (线条控制)
  - ImageInvert (图像反转)
- **模型要求**:
  - 主模型: `sdxl/ProteusV0.3.safetensors`
  - ControlNet: `T2I-Adapter/adapter-xl-lineart-fp16.safetensors`
  - IPAdapter: PLUS (high strength)
- **输入**:
  - 线稿图像 (黑白)
  - 参考风格图像 (用于 IPAdapter)
- **提示词示例**:
  - 正向: `illustration of a beautiful blond woman with leaves on the hair, closed eyes, peaceful, detailed, high quality`
  - 负向: `blurry, noisy, messy, glitch, distorted, malformed, ill, horror, naked`
- **采样参数**:
  - Steps: 30
  - CFG: 6
  - Sampler: dpmpp_2m
  - Seed: 4

### 2. 线稿上色2.json
**进阶线稿上色工作流**

- **功能**: 类似线稿上色1，但增加了图像预处理节点
- **主要技术**:
  - IPAdapter Advanced (风格迁移)
  - T2I-Adapter Lineart (线条控制)
  - PrepImageForClipVision (图像预处理)
  - ImageInvert (图像反转)
- **模型要求**:
  - 主模型: `sdxl/ProteusV0.3.safetensors`
  - ControlNet: `T2I-Adapter/adapter-xl-lineart-fp16.safetensors`
  - IPAdapter: PLUS (high strength)
- **输入**:
  - 线稿图像 (黑白)
  - 参考风格图像 (用于 IPAdapter)
- **提示词示例**:
  - 正向: `illustration of a tiny castle with high towers in a peaceful spring morning, detailed, high quality`
  - 负向: `blurry, noisy, messy, glitch, distorted, malformed, ill, horror, naked`
- **采样参数**:
  - Steps: 30
  - CFG: 6
  - Sampler: dpmpp_2m
  - Seed: 8

### 3. 美女变画作.json
**照片转绘画风格工作流**

- **功能**: 将人物照片转换为动漫/绘画风格
- **主要技术**:
  - IPAdapterStyleComposition (风格与构图分离)
  - Canny ControlNet (边缘控制)
  - Depth ControlNet (深度控制)
  - DepthAnythingPreprocessor (深度预处理)
- **模型要求**:
  - 主模型: `sdxl/juggernautXL_version8Rundiffusion.safetensors`
  - ControlNet 1: `diffusers/controlnet-canny-sdxl-1.0-mid.safetensors`
  - ControlNet 2: `control-lora/control-lora-depth-rank256.safetensors`
  - IPAdapter: PLUS (high strength)
- **输入**:
  - 原始照片 (人物)
  - 参考风格图像 (动漫/绘画)
- **提示词示例**:
  - 正向: `photo of a woman smiling open mouth closed eyes, serene bright atmosphere\n\ndetailed, high quality`
  - 负向: `blurry, noisy, messy, glitch, distorted, malformed, ill, horror, naked, nipples`
- **采样参数**:
  - Steps: 25
  - CFG: 6
  - Sampler: dpmpp_2m
  - Scheduler: karras
  - Seed: 19

### 4. 老虎变冰雕.json
**材质转换工作流**

- **功能**: 将图像中的物体转换为不同材质（如冰雕）
- **主要技术**:
  - IPAdapterAdvanced (材质风格迁移)
  - Depth ControlNet (深度控制)
  - RemBG (背景移除)
  - InpaintModelConditioning (重绘模型条件)
  - DifferentialDiffusion (差分扩散)
  - GrowMask (遮罩扩展)
- **模型要求**:
  - 主模型: `sd15/Deliberate_v4-inpainting.safetensors`
  - ControlNet: `control_v11f1p_sd15_depth_fp16.safetensors`
  - IPAdapter: PLUS (high strength)
  - RemBG: u2net (general purpose)
- **输入**:
  - 原始图像 (如老虎)
  - 参考材质图像 (如冰山)
- **提示词示例**:
  - 正向: `a (tiger:0.7) made of ice, high quality, highly detailed, 4k`
  - 负向: `blurry, noisy, messy, glitch, distorted, malformed, ill, horror, naked`
- **采样参数**:
  - Steps: 35
  - CFG: 6
  - Sampler: dpmpp_2m
  - Scheduler: karras
  - Seed: 7

## 🛠️ 依赖节点

使用这些工作流需要安装以下 ComfyUI 自定义节点：

1. **IPAdapter**
   - `ComfyUI_IPAdapter_plus`
   - 提供 IPAdapter 相关节点

2. **ControlNet**
   - `ComfyUI_ControlNet_aux`
   - 提供各种 ControlNet 预处理器

3. **图像处理**
   - `ComfyUI-WD14-Tagger` (可选)
   - `ComfyUI-Impact-Pack` (用于 RemBG 等功能)

4. **其他工具**
   - `ComfyUI-GGUF` (可选)
   - `ComfyUI-Inpaint-Crop` (可选)

## 📝 使用说明

### 基本步骤

1. **加载工作流**: 在 ComfyUI 中拖入对应的 `.json` 文件
2. **准备输入图像**:
   - 线稿上色: 准备黑白线稿和参考风格图
   - 照片转绘画: 准备人物照片和目标风格图
   - 材质转换: 准备原始图像和参考材质图
3. **调整参数**: 根据需要调整提示词、采样参数等
4. **运行工作流**: 点击 Queue Prompt 开始生成

### 参数调整建议

**IPAdapter 权重**:
- 风格迁移: 0.8-1.0 (高权重)
- 材质转换: 1.0 (完全迁移)
- 构图保留: 0.5-0.7 (中等权重)

**ControlNet 权重**:
- 线条控制: 0.6-0.8
- 深度控制: 0.3-1.0
- Canny 边缘: 0.75-1.0

**采样参数**:
- Steps: 20-40 (根据效果调整)
- CFG: 6-9 (过高可能导致过饱和)
- Sampler: 推荐使用 `dpmpp_2m` 或 `euler_a`

## 🎯 应用场景

1. **线稿上色**: 为黑白漫画、插画自动上色
2. **照片艺术化**: 将照片转换为绘画风格
3. **材质转换**: 改变物体的材质属性（如金属、冰、木等）
4. **风格迁移: 将一张图像的风格应用到另一张图像
5. **创意设计**: 快速生成多种风格变体

## ⚠️ 注意事项

1. **模型下载**: 确保所有必需的模型都已下载并放置在正确的目录
2. **显存要求**: SDXL 模型需要至少 12GB 显存，SD1.5 模型需要 8GB
3. **图像尺寸**: 输入图像建议使用 512x512 或 1024x1024 分辨率
4. **参考图像**: 选择与目标风格匹配的参考图像可以获得更好的效果
5. **多次尝试**: 生成效果可能需要多次尝试不同参数才能达到理想效果

## 📚 参考资源

- [ComfyUI 官方文档](https://github.com/comfyanonymous/ComfyUI)
- [IPAdapter 项目](https://github.com/tencent-ailab/IP-Adapter)
- [ControlNet 文档](https://github.com/lllyasviel/ControlNet)
- [ComfyUI 社区](https://reddit.com/r/comfyui)

## 📄 许可证

本工作流遵循原项目的许可证。使用时请遵守相关模型的许可证要求。

---

**最后更新**: 2026-01-03