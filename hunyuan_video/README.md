# 混元视频模型

[混元视频](https://huggingface.co/tencent/HunyuanVideo) 是一个文本转视频模型。


从[这里](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files/text_encoders)下载 clip_l.safetensors 和 llava_llama3_fp8_scaled.safetensors 文件，并将它们放入您的 ComfyUI/models/text_encoders 目录。

下载 [hunyuan_video_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files/vae) 文件并将其放入您的 ComfyUI/models/vae 文件夹。

### 文本转视频

下载 [hunyuan_video_t2v_720p_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files/diffusion_models) 文件并将其放入您的 ComfyUI/models/diffusion_models 文件夹。

此模型还可以通过将视频长度设置为 1 来生成静态图像。

![示例](hunyuan_video_text_to_video.webp)

[Json 格式的工作流](hunyuan_video_text_to_video.json)

您可以下载这个 webp 动画图像并加载它，或者将其拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 上以获取工作流。

### 图像转视频

下载 [llava_llama3_vision.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/blob/main/split_files/clip_vision/llava_llama3_vision.safetensors) 文件并将其放入您的 ComfyUI/models/clip_vision/ 文件夹。

您可以选择两个不同的模型，它们会产生不同的结果。

#### v1 "concat"

第一个模型比另一个模型更少地遵循引导图像，但可能会提供更好的运动效果。

下载 [hunyuan_video_image_to_video_720p_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files/diffusion_models) 文件并将其放入您的 ComfyUI/models/diffusion_models/ 文件夹。

![示例](hunyuan_video_image_to_video.webp)

[Json 格式的工作流](hunyuan_video_image_to_video.json)

您可以下载这个 webp 动画图像并加载它，或者将其拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 上以获取工作流。输入图像可以在 [flux](../flux) 页面上找到。

#### v2 "replace"

第二个模型非常紧密地遵循引导图像，但似乎比第一个模型稍微不那么动态。

下载 [hunyuan_video_v2_replace_image_to_video_720p_bf16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files/diffusion_models) 文件并将其放入您的 ComfyUI/models/diffusion_models/ 文件夹。

![示例](hunyuan_video_image_to_video_v2.webp)

[Json 格式的工作流](hunyuan_video_image_to_video_v2.json)

您可以下载这个 webp 动画图像并加载它，或者将其拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 上以获取工作流。输入图像可以在 [flux](../flux) 页面上找到。
