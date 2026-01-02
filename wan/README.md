# Wan 2.1 模型

[Wan 2.1](https://github.com/Wan-Video/Wan2.1) 是一系列视频模型。

关于 Wan 2.2，请参阅：[Wan 2.2](../wan22)

## 需要下载的文件

您首先需要：

#### 文本编码器和 VAE：

[umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/text_encoders) 放置于：ComfyUI/models/text_encoders/

[wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/vae/wan_2.1_vae.safetensors) 放置于：ComfyUI/models/vae/


#### 视频模型

扩散模型可以在[这里](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models)找到

注意：推荐使用 fp16 版本而不是 bf16 版本，因为它们会提供更好的结果。

质量排名（从高到低）：fp16 > bf16 > fp8_scaled > fp8_e4m3fn

这些文件放置于：ComfyUI/models/diffusion_models/

这些示例使用 16 位文件，但如果您的内存不足，可以使用 fp8 版本。

## 工作流

### 文本到视频

此工作流需要 [wan2.1_t2v_1.3B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_t2v_1.3B_fp16.safetensors) 文件（放置于：ComfyUI/models/diffusion_models/）。您也可以将其与 14B 模型一起使用。

![示例](text_to_video_wan.webp)

[Json 格式的工作流](text_to_video_wan.json)

### 图像到视频

此工作流需要 [wan2.1_i2v_480p_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_i2v_480p_14B_fp16.safetensors) 文件（放置于：ComfyUI/models/diffusion_models/）和
[clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/clip_vision/clip_vision_h.safetensors)，放置于：ComfyUI/models/clip_vision/

注意：此示例仅生成 33 帧 512x512 的视频，因为我希望它易于访问，该模型可以做得更多。如果您有硬件/耐心来运行它，720p 模型相当不错。

<img src="image_to_video_wan_example.webp" width="512" />

[Json 格式的工作流](image_to_video_wan_example.json)

输入图像可以在 [flux](../flux) 页面找到。

以下是使用 [720p](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_i2v_720p_14B_fp16.safetensors) 模型的相同示例：

<img src="image_to_video_wan_720p_example.webp" width="768" />


### VACE 参考图像到视频

此工作流需要 [wan2.1_vace_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) 文件（放置于：ComfyUI/models/diffusion_models/）

此示例从参考图像生成视频，这与从起始图像生成视频不同。您会注意到视频实际上不包含参考图像，但显然是源自它的。

<img src="vace_reference_to_video.webp" width="768" />

[Json 格式的工作流](vace_reference_to_video.json)

您可以在[这里](../images/fennec_girl_sing.png)找到输入图像，该图像包含一个 [Chroma](../chroma) 工作流，如果您对它是如何生成的感兴趣。

### 图像相机到视频

此工作流需要 [wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/diffusion_models/wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors) 文件（放置于：ComfyUI/models/diffusion_models/）和
[clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/clip_vision/clip_vision_h.safetensors)，放置于：ComfyUI/models/clip_vision/（如果您还没有的话）。


<img src="camera_image_to_video_wan_example.webp" width="512" />

[Json 格式的工作流](camera_image_to_video_wan_example.json)

输入图像可以在 [flux](../flux) 页面找到。