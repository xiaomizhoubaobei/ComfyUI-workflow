# SD3 示例

## SD3.5

第一步是下载文本编码器文件，如果您还没有从 SD3、Flux 或其他模型获得它们：([clip_l.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/blob/main/text_encoders/clip_l.safetensors), [clip_g.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/blob/main/text_encoders/clip_g.safetensors) 和 t5xxl)，如果您的 ComfyUI/models/text_encoders/ 文件夹中还没有它们的话。对于 t5xxl，如果您有超过 32GB 内存，我推荐 [t5xxl_fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/blob/main/text_encoders/t5xxl_fp16.safetensors)，如果没有，则推荐 [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/blob/main/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors)。

SD3.5 模型系列包含一个大型 8B 模型和一个中型 2.5B 模型。中型模型会更快并占用更少内存，但对某些概念的理解可能不够复杂。我建议下载两者并尝试它们如何响应您的提示。

[sd3.5_large.safetensors](https://huggingface.co/stabilityai/stable-diffusion-3.5-large/tree/main) 和 [sd3.5_medium.safetensors](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium/tree/main) 文件（选择您想要的并将其放入您的 ComfyUI/models/checkpoints/ 目录）不包含文本编码器/CLIP 权重，因此您必须单独加载它们才能使用该文件，就像以下示例一样：

![示例](sd3.5_text_encoders_example.png)

要使用 [sd3.5_large_turbo.safetensors](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-turbo/tree/main) 文件（将其放入您的 ComfyUI/models/checkpoints/ 目录），您可以使用上面的示例并将 steps 设置为 4，cfg 设置为 1.2。

为了方便，有一个易于使用的一体化检查点文件 [sd3.5_large_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/blob/main/sd3.5_large_fp8_scaled.safetensors)（将其放入您的 ComfyUI/models/checkpoints/ 目录），可以在默认工作流中像其他检查点文件一样使用。还有一个用于 SD3.5 medium 的：[sd3.5_medium_incl_clips_t5xxlfp8scaled.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/blob/main/sd3.5_medium_incl_clips_t5xxlfp8scaled.safetensors)

请参阅此工作流以获取示例。

![示例](sd3.5_simple_example.png)

提醒您，您可以保存这些图像文件并将它们拖动或加载到 ComfyUI 中以获取工作流。

### SD3.5 Controlnets

Stability 发布了一些官方 SD3.5 controlnets，您可以在[这里](https://huggingface.co/stabilityai/stable-diffusion-3.5-controlnets)找到它们，这些文件（sd3.5_large_controlnet_canny.safetensors, sd3.5_large_controlnet_depth.safetensors, sd3.5_large_controlnet_blur.safetensors）放入您的 ComfyUI/models/controlnet 目录，旨在与 SD3.5 large 一起使用。

请参阅此工作流以获取使用 canny ([sd3.5_large_controlnet_canny.safetensors](https://huggingface.co/stabilityai/stable-diffusion-3.5-controlnets/tree/main)) controlnet 的示例：

![示例](sd3.5_large_canny_controlnet_example.png)