# Lightricks LTX-Video 模型

[LTX-Video](https://huggingface.co/Lightricks/LTX-Video) 是 Lightricks 开发的一个非常高效的视频模型。

这个模型的重要之处在于要给它长描述性提示。

下载 [ltx-video-2b-v0.9.5.safetensors](https://huggingface.co/Lightricks/LTX-Video/blob/main/ltx-video-2b-v0.9.5.safetensors) 文件并将其放入您的 ComfyUI/models/checkpoints 文件夹。

如果您还没有下载，可以下载 [t5xxl_fp16.safetensors](https://huggingface.co/Comfy-Org/mochi_preview_repackaged/blob/main/split_files/text_encoders/t5xxl_fp16.safetensors) 文件并将其放入您的 ComfyUI/models/text_encoders/ 文件夹。

### 图像转视频

输入图像：
<img src="fox.jpg" width="256" />

#### 仅使用起始图像的简单 img2vid 工作流：

![示例](ltxv_image_to_video_simple.0.9.5.webp)

[Json 格式的工作流](ltxv_image_to_video_simple.0.9.5.json)


#### 使用多个引导图像的更复杂 img2vid 工作流：

![示例](ltxv_image_to_video.0.9.5.webp)

[Json 格式的工作流](ltxv_image_to_video.0.9.5.json)

您可以下载这个 webp 动画图像并加载它，或者将其拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 上以获取工作流。

### 文本转视频

![示例](ltxv_text_to_video_0.9.5.webp)

[Json 格式的工作流](ltxv_text_to_video_0.9.5.json)

您可以下载这个 webp 动画图像并加载它，或者将其拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 上以获取工作流。


[旧 ltxv 示例](README_old.md)


