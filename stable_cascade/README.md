# Stable Cascade 示例

首先下载 [stable_cascade_stage_c.safetensors 和 stable_cascade_stage_b.safetensors 检查点](https://huggingface.co/stabilityai/stable-cascade/tree/main/comfyui_checkpoints) 并将它们放入 ComfyUI/models/checkpoints 文件夹中。

Stable Cascade 是一个 3 阶段过程，首先使用 Stage C 扩散模型生成低分辨率潜在图像。然后使用 Stage B 扩散模型对该潜在图像进行上采样。这个上采样后的潜在图像再由 Stage A VAE 进行上采样并转换为像素空间。

请注意，您可以下载此页面中的所有图像，然后将它们拖动或加载到 ComfyUI 上以获取嵌入在图像中的工作流。

## 文本转图像

这是一个基本的文本转图像工作流：

![示例](stable_cascade__text_to_image.png)


## 图像转图像

这是一个如何通过编码图像并将其传递给 Stage C 来进行基本图像转图像的示例：

![示例](stable_cascade__image_to_image.png)

## 图像变体

Stable Cascade 支持使用 CLIP vision 的输出来创建图像的变体。请参阅以下工作流以获取示例：

![示例](stable_cascade__image_remixing.png)

请参阅下一个工作流以了解如何将多个图像混合在一起：

![示例](stable_cascade__image_remixing_multiple.png)

您可以在 [unCLIP 示例页面](../unclip)上找到上述工作流的输入图像


## ControlNet

您可以从[这里](https://huggingface.co/stabilityai/stable-cascade/tree/main/controlnet)下载 stable cascade controlnets。对于这些示例，我通过在文件名前面添加 stable_cascade_ 来重命名文件，例如：[stable_cascade_canny.safetensors](https://huggingface.co/stabilityai/stable-cascade/blob/main/controlnet/canny.safetensors)，[stable_cascade_inpainting.safetensors](https://huggingface.co/stabilityai/stable-cascade/blob/main/controlnet/inpainting.safetensors)

这是一个如何使用 Canny Controlnet 的示例：

![示例](stable_cascade__canny_controlnet.png)


这是一个如何使用 Inpaint Controlnet 的示例，示例输入图像可以在[这里](../inpaint/yosemite_inpaint_example.png)找到。提醒您可以在 LoadImage 节点中右键单击图像并使用 mask editor 编辑它们。

![示例](stable_cascade__inpaint_controlnet.png)

