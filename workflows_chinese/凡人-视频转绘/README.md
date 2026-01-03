# 凡人视频转绘工作流集

本目录包含基于 ComfyUI 的视频转绘工作流，由"凡人"制作，专注于将视频转换为绘画风格的动画效果。这些工作流提供了从基础到高级的视频处理功能。

## 📁 工作流文件

### 凡人-动画平滑-超简易版.json
- **功能**: 视频动画平滑处理
- **特点**:
  - 超简易操作流程
  - 自动帧插值和平滑
  - 支持视频输出
  - 使用 SmoothVideo 节点
- **适用场景**:
  - 视频帧率提升
  - 动画流畅度优化
  - 视频后期处理
- **主要参数**:
  - 帧率: 30 fps
  - 输出格式: MP4 (H.264)
  - CRF: 20 (高质量)

### 凡人-视频转换IPA参考图绘制.json
- **功能**: 使用 IPAdapter 进行视频转绘
- **特点**:
  - 基于 IPAdapter 的风格迁移
  - 支持参考图风格
  - 保持视频连贯性
  - 高质量风格转换
- **适用场景**:
  - 视频风格化
  - 艺术风格迁移
  - 参考图风格应用
- **技术特点**:
  - 使用 IPAdapter V2
  - 支持多种风格
  - 保持原视频内容

### 凡人-视频转绘画SDXL加速版.json
- **功能**: 基于 SDXL 的视频转绘
- **特点**:
  - 使用 SDXL 模型
  - 加速处理流程
  - 支持批量帧处理
  - 高质量绘画效果
- **适用场景**:
  - 视频转绘画
  - 批量视频处理
  - 高质量艺术转换
- **主要参数**:
  - 模型: SDXL
  - 支持跳帧处理
  - 批量生成优化

## 🚀 快速开始

### 1. 安装依赖

#### ComfyUI-VideoHelperSuite (VHS)
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite
```

#### IPAdapter
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus
```

#### 其他必需节点
- Anything Everywhere3
- SmoothVideo (如需要)
- rgthree-comfy (SetNode 等)

### 2. 下载模型

#### SDXL 模型
```bash
mkdir -p ComfyUI/models/checkpoints

# 下载 SDXL 基础模型
wget https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors

# 或使用 SDXL Refiner
wget https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors
```

#### IPAdapter 模型
```bash
mkdir -p ComfyUI/models/ipadapter

# 下载 IPAdapter SDXL 模型
wget https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter_sdxl.safetensors
```

### 3. 加载工作流

1. 启动 ComfyUI
2. 点击 "Load" 按钮
3. 选择本目录中的 .json 文件
4. 上传输入视频或参考图
5. 调整提示词和参数
6. 点击 "Queue Prompt" 开始处理

## 💡 使用技巧

### 凡人-动画平滑-超简易版

1. **视频准备**
   - 支持常见视频格式（MP4, AVI, MOV 等）
   - 建议使用较短的视频进行测试
   - 确保视频帧率一致

2. **参数调整**
   - `strength`: 平滑强度（0-2）
   - `window_size`: 窗口大小（15-30）
   - `padding`: 填充大小（0-20）

3. **输出设置**
   - 帧率: 建议 30-60 fps
   - CRF: 18-23 (数值越小质量越高)
   - 格式: MP4 (H.264)

### 凡人-视频转换IPA参考图绘制

1. **参考图选择**
   - 选择与目标风格匹配的参考图
   - 参考图应清晰且风格明显
   - 建议使用高分辨率参考图

2. **IPAdapter 参数**
   - `weight`: 风格迁移权重（0.5-1.5）
   - `start/end`: 应用范围（0-1）
   - `mix_ratio`: 混合比例

3. **提示词编写**
   - 正面提示词：描述目标风格
   - 负面提示词：避免不需要的元素
   - 示例：
     ```
     正面: 油画风格，笔触明显，色彩丰富
     负面: 模糊，失真，噪点
     ```

### 凡人-视频转绘画SDXL加速版

1. **视频处理**
   - 支持长视频处理
   - 可设置跳帧减少处理时间
   - 建议分批处理长视频

2. **SDXL 优化**
   - 使用 SDXL Base + Refiner 组合
   - 调整采样步数（20-40）
   - CFG 建议 5-8

3. **批量处理**
   - 设置合理的批次大小
   - 监控显存使用
   - 保存中间结果

## 🔧 技术细节

### 视频处理流程

1. **视频加载**: 使用 VHS_LoadVideoPath 加载视频
2. **帧提取**: 将视频分解为帧序列
3. **帧处理**: 对每帧应用 AI 模型
4. **帧组合**: 使用 VHS_VideoCombine 组合为视频

### IPAdapter 工作原理

- 提取参考图像的特征
- 将特征注入到扩散过程中
- 保持视频内容的连贯性
- 实现风格迁移

### SDXL 优势

- 更高的分辨率支持
- 更好的图像质量
- 更强的文本理解能力
- 更快的处理速度

## 📊 性能要求

- **显存**: 建议 12GB+ VRAM（SDXL）
- **内存**: 建议 32GB+ RAM
- **存储**: 视频文件的 3-5 倍空间
- **处理时间**:
  - 动画平滑: 快速（实时处理）
  - IPA 转绘: 中等（取决于视频长度）
  - SDXL 转绘: 较慢（取决于分辨率和帧数）

## 📝 注意事项

1. **视频格式**: 确保视频格式兼容
2. **显存管理**: 长视频可能导致显存不足
3. **处理时间**: 高质量处理需要较长时间
4. **输出质量**: 平衡质量和速度
5. **备份原视频**: 处理前备份原始视频

## 🎯 应用场景

### 动画制作
- 视频帧率提升
- 动画平滑处理
- 风格统一

### 艺术创作
- 视频艺术化
- 风格迁移
- 创意视频制作

### 内容创作
- 短视频制作
- 社交媒体内容
- 广告视频

### 教育培训
- 视频美化
- 教学视频制作
- 演示视频优化

## 🔗 相关资源

- [ComfyUI 官方文档](https://github.com/comfyanonymous/ComfyUI)
- [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)
- [IPAdapter GitHub](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
- [SDXL 模型](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- [凡人工作流教程](https://www.bilibili.com/video/BV1...)

## 📄 许可证

本工作流集遵循原 ComfyUI 和相关模型的许可证协议。请确保在使用时遵守相关条款。

## 🤝 常见问题

### Q1: 三个工作流有什么区别？
A: 
- 动画平滑: 专注于视频流畅度提升
- IPA 参考图: 专注于风格迁移
- SDXL 转绘: 专注于高质量绘画转换

### Q2: 如何选择合适的工作流？
A: 
- 需要提升流畅度: 使用动画平滑
- 需要风格迁移: 使用 IPA 参考图
- 需要高质量转绘: 使用 SDXL 转绘

### Q3: 显存不足怎么办？
A: 
- 降低视频分辨率
- 减少批次大小
- 使用跳帧功能
- 分段处理视频

### Q4: 如何提高处理速度？
A: 
- 使用较小的分辨率
- 减少采样步数
- 使用跳帧处理
- 使用更快的硬件

### Q5: 输出视频质量如何优化？
A: 
- 使用更高的 CRF 值
- 调整采样参数
- 使用 Refiner 模型
- 增加处理步数

### Q6: 支持哪些视频格式？
A: 
- 输入: MP4, AVI, MOV, MKV 等
- 输出: MP4 (H.264), WebM 等
- 具体取决于 VHS 插件支持

### Q7: 如何保持视频连贯性？
A: 
- 使用合适的 IPAdapter 权重
- 调整采样参数
- 使用帧间一致性技术
- 避免过强的风格迁移

## 💡 进阶技巧

1. **组合使用**: 可以先使用动画平滑，再使用 IPA 转绘
2. **批量处理**: 使用脚本批量处理多个视频
3. **参数预设**: 保存常用参数为预设
4. **质量监控**: 定期检查中间结果
5. **硬件优化**: 使用 GPU 加速和多线程处理