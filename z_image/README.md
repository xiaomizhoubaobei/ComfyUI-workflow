# Z Image

[Z Image Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) 是一个快速的蒸馏扩散模型。

## 需要下载的文件

文本编码器文件：[qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/blob/main/split_files/text_encoders/qwen_3_4b.safetensors)（放置于 ComfyUI/models/text_encoders/）。

扩散模型文件：[z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/blob/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors)（放置于 ComfyUI/models/diffusion_models/）。

VAE：[ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/blob/main/split_files/vae/ae.safetensors) Flux 1 VAE（如果您还没有的话）（放置于 ComfyUI/models/vae/）

## 基本示例工作流

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](z_image_turbo_example.png)