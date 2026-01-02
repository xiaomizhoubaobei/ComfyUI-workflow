# 原始 Nvidia Cosmos 模型

对于较新的 Cosmos 模型，请参阅 [Cosmos Predict2](../cosmos_predict2)

[Nvidia Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) 是一系列"世界模型"。ComfyUI 目前特别支持 7B 和 14B 文本转视频扩散模型以及 7B 和 14B 图像转视频扩散模型。

## 需要下载的文件

您首先需要：

#### 文本编码器和 VAE：

[oldt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/cosmos_1.0_text_encoder_and_VAE_ComfyUI/tree/main/text_encoders) 放入：ComfyUI/models/text_encoders/

[cosmos_cv8x8x8_1.0.safetensors](https://huggingface.co/comfyanonymous/cosmos_1.0_text_encoder_and_VAE_ComfyUI/blob/main/vae/cosmos_cv8x8x8_1.0.safetensors) 放入：ComfyUI/models/vae/

注意：oldt5_xxl 与 flux 和其他模型中使用的 t5xxl 不同。
oldt5_xxl 是 t5xxl 1.0，而 flux 和其他模型中使用的是 t5xxl 1.1

#### 视频模型

视频模型可以在[这里找到 safetensors 格式](https://huggingface.co/mcmonkey/cosmos-1.0/tree/main)

此页面上的工作流使用 [Cosmos-1_0-Diffusion-7B-Text2World.safetensors](https://huggingface.co/mcmonkey/cosmos-1.0/blob/main/Cosmos-1_0-Diffusion-7B-Text2World.safetensors) 和 [Cosmos-1_0-Diffusion-7B-Video2World.safetensors](https://huggingface.co/mcmonkey/cosmos-1.0/blob/main/Cosmos-1_0-Diffusion-7B-Video2World.safetensors)

这些文件放入：ComfyUI/models/diffusion_models

注意："Text to World" 意味着文本转视频，"Video to World" 意味着图像/视频转视频。

如果您想要原始的 .pt 格式扩散模型而不是重新打包的 safetensors，官方链接是：[7B-Text2World](https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-7B-Text2World) [7B-Video2World](https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-7B-Video2World) [14B-Text2World](https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-14B-Text2World) [14B-Video2World](https://huggingface.co/nvidia/Cosmos-1.0-Diffusion-14B-Video2World)

## 工作流

### 文本转视频

此工作流需要您可以下载的 7B 文本转视频模型。

![示例](text_to_video_cosmos_7B.webp)

[Json 格式的工作流](text_to_video_cosmos_7B.json)

### 图像转视频

此模型支持从 1 个或多个图像生成视频。如果输入多个图像，它将把它们全部作为指南并继续运动。您还可以通过设置一个或多个 start_image 和 end_image 来进行基本插值，如果这些图像彼此相似，效果最好。

此工作流需要您可以下载的 7B 图像转视频模型。

此模型主要在真实视频上训练，但在此示例中，您可以看到它在动漫上也相当有效。

![示例](image_to_video_cosmos_7B.webp)

[Json 格式的工作流](image_to_video_cosmos_7B.json)
