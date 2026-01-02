# HiDream

[HiDream I1](https://github.com/HiDream-ai/HiDream-I1) 是一个最先进的图像扩散模型。

## 需要下载的文件

下载文本编码器文件：

* [clip_l_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_l_hidream.safetensors)
* [clip_g_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_g_hidream.safetensors)
* [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors)
* [llama_3.1_8b_instruct_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors)

将这 4 个文件放入您的 ComfyUI/models/text_encoders 目录。

您可以在这里找到它们全部：[这里](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/text_encoders)。您可能已经下载了 t5xxl。

VAE 可以在[这里](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/vae/ae.safetensors)找到，应该放入您的 ComfyUI/models/vae/ 文件夹。这是 Flux VAE，所以您可能已经有了。

扩散模型可以在这个[文件夹](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/tree/main/split_files/diffusion_models)中找到

## HiDream dev 工作流

下载 [hidream_i1_dev_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/diffusion_models/hidream_i1_dev_bf16.safetensors) 并将其放入您的 ComfyUI/models/diffusion_models/ 目录。

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](hidream_dev_example.png)

## HiDream full 工作流

下载 [hidream_i1_full_fp16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/diffusion_models/hidream_i1_full_fp16.safetensors) 并将其放入您的 ComfyUI/models/diffusion_models/ 目录。

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](hidream_full_example.png)

## HiDream e1.1

这是一个编辑模型，下载 [hidream_e1_1_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/diffusion_models/hidream_e1_1_bf16.safetensors) 并将其放入您的 ComfyUI/models/diffusion_models/ 目录。

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](hidream_e1.1_example.png)


<details>
<summary>旧 hidream 1.0 编辑模型。</summary>
## HiDream e1

这是一个实验性编辑模型，下载 [hidream_e1_full_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/diffusion_models/hidream_e1_full_bf16.safetensors) 并将其放入您的 ComfyUI/models/diffusion_models/ 目录。

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](hidream_e1_example.png)
</details>
