# Flux 2

[Flux 2](https://github.com/black-forest-labs/flux2) 是一个最先进的图像扩散模型。

## 需要下载的文件

文本编码器文件：[mistral_3_small_flux2_fp8.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/text_encoders/mistral_3_small_flux2_fp8.safetensors)（放入 ComfyUI/models/text_encoders/）。


Fp8 扩散模型文件：[flux2_dev_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors)（放入 ComfyUI/models/diffusion_models/）。如果您想要完整大小的扩散模型，可以在官方仓库[这里](https://huggingface.co/black-forest-labs/FLUX.2-dev)找到 flux2-dev.safetensors

VAE：[flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/blob/main/split_files/vae/flux2-vae.safetensors)（放入 ComfyUI/models/vae/）

## 基本示例工作流

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](flux2_example.png)

此模型支持多个参考图像作为可选输入。此示例工作流中有两个被绕过，但您可以添加更多。
