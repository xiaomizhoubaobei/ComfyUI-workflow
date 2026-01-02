# Wan 2.2 模型

[Wan 2.2](https://github.com/Wan-Video/Wan2.2) 是一系列视频模型，是 [Wan 2.1](../wan) 的后续版本

Wan2.2 最初发布了 3 个不同的模型：一个可以同时进行文本到视频和图像到视频的 5B 模型，以及两个 14B 模型，一个用于文本到视频，另一个用于视频到视频。

另请参阅 [Comfy Docs Wan 2.2 页面以获取更多工作流示例。](https://docs.comfy.org/tutorials/video/wan/wan2_2)

## 需要下载的文件

您首先需要：

#### 文本编码器和 VAE：

[umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/text_encoders) 放置于：ComfyUI/models/text_encoders/

14B 模型需要：[wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/vae/wan_2.1_vae.safetensors) 放置于：ComfyUI/models/vae/

5B 模型需要（新增）：[wan2.2_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/vae/wan2.2_vae.safetensors) 放置于：ComfyUI/models/vae/

#### 视频模型

扩散模型可以在[这里](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models)找到

这些文件放置于：ComfyUI/models/diffusion_models/

## 工作流

### 5B 模型

此工作流需要 [wan2.2_ti2v_5B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors) 文件（放置于：ComfyUI/models/diffusion_models/）。

确保您有 [wan2.2 VAE](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/vae/wan2.2_vae.safetensors)（放置于：ComfyUI/models/vae/）

#### 文本到视频

![示例](text_to_video_wan22_5B.webp)

[Json 格式的工作流](text_to_video_wan22_5B.json)


#### 图像到视频

![示例](image_to_video_wan22_5B.webp)

[Json 格式的工作流](image_to_video_wan22_5B.json)

您可以在[这里](../images/fennec_girl_hug.png)找到输入图像

### 14B 模型

确保您有 [wan2.1 VAE](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/vae/wan_2.1_vae.safetensors)（放置于：ComfyUI/models/vae/）

#### 文本到视频

此工作流需要 [wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors) 和 [wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors) 两个文件（放置于：ComfyUI/models/diffusion_models/）。

![示例](text_to_video_wan22_14B.webp)

[Json 格式的工作流](text_to_video_wan22_14B.json)

#### 图像到视频

此工作流需要 [wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors) 和 [wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors) 两个文件（放置于：ComfyUI/models/diffusion_models/）。

![示例](image_to_video_wan22_14B.webp)

[Json 格式的工作流](image_to_video_wan22_14B.json)

您可以在[这里](../images/fennec_girl_flowers.png)找到输入图像