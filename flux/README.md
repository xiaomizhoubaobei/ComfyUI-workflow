# Flux 示例

Flux 是 [Black Forest Labs](https://blackforestlabs.ai/announcing-black-forest-labs/) 开发的一系列扩散模型。

关于可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中轻松使用的单文件版本，请参见下方：[FP8 检查点版本](#简单易用的-fp8-检查点版本)

## 常规完整版本

### 常规版本需要下载的文件

如果您的 ComfyUI/models/text_encoders/ 目录中还没有 t5xxl_fp16.safetensors 或 clip_l.safetensors，您可以在 [此链接](https://huggingface.co/comfyanonymous/flux_text_encoders/tree/main)找到它们。如果内存有限，可以使用 t5xxl_fp8_e4m3fn_scaled.safetensors 来降低内存使用，但如果您有超过 32GB 内存，推荐使用 fp16 版本。

VAE 可以在[这里](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/blob/main/split_files/vae/ae.safetensors)找到，应该放入您的 ComfyUI/models/vae/ 文件夹中。

### 内存不足的提示：

使用单文件 fp8 版本，您可以[在下方](#简单易用的-fp8-检查点版本)找到它

您可以在"加载扩散模型"节点中设置 weight_dtype 为 fp8，这将使内存使用量减半，但可能会稍微降低质量。您也可以下载示例。

### Flux Dev

您可以在[这里](https://huggingface.co/black-forest-labs/FLUX.1-dev)找到 Flux Dev 扩散模型权重。将 flux1-dev.safetensors 文件放入您的：ComfyUI/models/diffusion_models/ 文件夹中。

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](flux_dev_example.png)

### Flux Schnell

Flux Schnell 是一个蒸馏的 4 步模型。

您可以在[这里](https://huggingface.co/black-forest-labs/FLUX.1-schnell)找到 Flux Schnell 扩散模型权重，flux1-schnell.safetensors 文件应该放入您的：ComfyUI/models/unet/ 文件夹中。


然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](flux_schnell_example.png)


## 简单易用的 FP8 检查点版本

### Flux Dev

您可以在[这里](https://huggingface.co/Comfy-Org/flux1-dev/blob/main/flux1-dev-fp8.safetensors)找到易于使用的 Flux dev 检查点，可以放入您的：ComfyUI/models/checkpoints/ 目录中。

此文件可以使用常规的"加载检查点"节点加载。使用时请确保将 CFG 设置为 1.0。

请注意 fp8 会稍微降低质量，如果您有资源，推荐使用官方的完整 16 位版本。

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](flux_dev_checkpoint_example.png)

### Flux Schnell

对于 Flux schnell，您可以在[这里](https://huggingface.co/Comfy-Org/flux1-schnell/blob/main/flux1-schnell-fp8.safetensors)获取检查点，可以放入您的：ComfyUI/models/checkpoints/ 目录中。

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](flux_schnell_checkpoint_example.png)

## Flux 扩展功能

以下示例可能需要您拥有一些可以在本页面顶部找到链接的常规 flux 文件。

### Flux Kontext（图像编辑）模型

下载 [flux1-kontext-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev) 模型文件并将其放入您的 ComfyUI/models/diffusion_models/ 文件夹中。如果另一个对您来说太大，这里有一个替代的 fp8 模型：[flux1-dev-kontext_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/flux1-kontext-dev_ComfyUI/blob/main/split_files/diffusion_models/flux1-dev-kontext_fp8_scaled.safetensors)。

这是一个简单的示例。您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](flux_kontext_example.png)


您可以在[这里](../images/fennec_girl_sing.png)找到上述工作流的输入图像

这是另一个更复杂的示例，从上述输入图像生成漫画：

![示例](flux_kontext_example_comic.webp)

### Fill（修复）模型

下载 [flux1-fill-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev) 模型文件并将其放入您的 ComfyUI/models/diffusion_models/ 文件夹中。

这是一个您可以拖入 ComfyUI 进行修复的示例，提醒您可以在"加载图像"节点中右键单击图像并"在 MaskEditor 中打开"。

![示例](flux_fill_inpaint_example.png)

这是一个外扩的示例：

![示例](flux_fill_outpaint_example.png)


### Redux

Redux 模型是一个可以使用一张或多张图像来提示 flux dev 或 flux schnell 的模型。

下载 [sigclip_vision_patch14_384.safetensors](https://huggingface.co/Comfy-Org/sigclip_vision_384/blob/main/sigclip_vision_patch14_384.safetensors) 模型并将其放入您的 ComfyUI/models/clip_vision 文件夹，并下载 [flux1-redux-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev) 并将其放入您的 ComfyUI/models/style_models 文件夹。

然后您可以在 ComfyUI 中加载或拖动以下图像以获取工作流：

![示例](flux_redux_model_example.png)

### Canny 和 Depth

它们以两种版本发布，完整模型格式：[flux1-canny-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev) 和 [flux1-depth-dev.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev)，将它们放入您的 ComfyUI/models/diffusion_models/ 文件夹中

这是完整 canny 模型的示例：

![示例](flux_canny_model_example.png)

它们也以 lora 格式发布，可以应用于 flux dev 模型：[flux1-canny-dev-lora.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Canny-dev-lora) 和 [flux1-depth-dev-lora.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-Depth-dev-lora)，将它们放入您的 ComfyUI/models/loras/ 文件夹中

这是 depth lora 的示例。

![示例](flux_depth_lora_example.png)


### 社区 Flux Controlnets

XLab 和 InstantX + Shakker Labs 已经为 Flux 发布了 Controlnets。您可以在[这里](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny/blob/main/diffusion_pytorch_model.safetensors)找到 InstantX Canny 模型文件（重命名为 instantx_flux_canny.safetensors 以用于下面的示例），[这里](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Depth/blob/main/diffusion_pytorch_model.safetensors)的 Depth controlnet，以及[这里](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/blob/main/diffusion_pytorch_model.safetensors)的 Union Controlnet。

XLab controlnets 可以在[这里](https://huggingface.co/XLabs-AI/flux-controlnet-collections)找到。

将这些文件放入 `ComfyUI/models/controlnet` 目录下。

通过将此图像拖入 ComfyUI 来尝试一个 Canny Controlnet 工作流示例。

![示例](flux_controlnet_example.png)

如果您需要 canny 的示例输入图像，请使用[这个](girl_in_field.png)。将其放入 `ComfyUI/input` 下。