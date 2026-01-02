# 混元图像 2.1

[混元图像 2.1](https://huggingface.co/tencent/HunyuanImage-2.1) 是一个用于图像生成的强大扩散模型。

## 基本工作流

下载以下模型并将它们放入相应的 ComfyUI 目录中：

### 文本编码器
下载并放入您的 ComfyUI/models/text_encoders 目录：
- [byt5_small_glyphxl_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/blob/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors)
- [qwen_2.5_vl_7b.safetensors](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/blob/main/split_files/text_encoders/qwen_2.5_vl_7b.safetensors)

### VAE 模型
下载并放入您的 ComfyUI/models/vae 目录：
- [hunyuan_image_2.1_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/blob/main/split_files/vae/hunyuan_image_2.1_vae_fp16.safetensors)
- **可选（用于细化器）：** [hunyuan_image_refiner_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/blob/main/split_files/vae/hunyuan_image_refiner_vae_fp16.safetensors)

### 扩散模型
下载并放入您的 ComfyUI/models/diffusion_models 目录：
- [hunyuanimage2.1_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/blob/main/split_files/diffusion_models/hunyuanimage2.1_bf16.safetensors)
- **可选（用于细化器）：** [hunyuanimage2.1_refiner_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/blob/main/split_files/diffusion_models/hunyuanimage2.1_refiner_bf16.safetensors)

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](hunyuan_image_example.png)
