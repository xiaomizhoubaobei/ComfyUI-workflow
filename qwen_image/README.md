# Qwen Image

[Qwen Image](https://github.com/QwenLM/Qwen-Image) 是一个 20B 扩散模型。

## 基本工作流

下载 [qwen_image_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) 并将其放入您的 ComfyUI/models/diffusion_models 目录。

[qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) 并将其放入您的 ComfyUI/models/text_encoders 目录。

[qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors) 并将其放入您的 ComfyUI/models/vae/ 目录

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](qwen_image_basic_example.png)

## 编辑模型 v2509

确保您已下载上述基本工作流的文本编码器和 vae 文件。此模型支持最多 3 个不同的图像输入。

下载 [qwen_image_edit_2509_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors) 并将其放入您的 ComfyUI/models/diffusion_models 目录。


然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](qwen_image_edit_2509_basic_example.png)

您可以在[这里](../images/fennec_girl_sing.png)找到输入图像


## 编辑模型（旧的第一版本）

确保您已下载上述基本工作流的文本编码器和 vae 文件。

下载 [qwen_image_edit_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_edit_fp8_e4m3fn.safetensors) 并将其放入您的 ComfyUI/models/diffusion_models 目录。


然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](qwen_image_edit_basic_example.png)

您可以在[这里](../images/fennec_girl_sing.png)找到输入图像
