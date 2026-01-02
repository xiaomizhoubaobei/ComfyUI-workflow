# SDXL 示例

SDXL 基础检查点可以像 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中的任何常规检查点一样使用。唯一重要的是，为了获得最佳性能，分辨率应设置为 1024x1024 或具有相同像素数量但不同纵横比的其他分辨率。
例如：896x1152 或 1536x640 是很好的分辨率。

对于使用基础检查点和细化器（refiner），您可以使用此工作流。您可以下载此图像并将其加载或拖动到 ComfyUI 上以获取它。

![示例](sdxl_simple_example.png)

您也可以像在这个工作流中一样为基础检查点和细化器提供不同的提示。

![示例](sdxl_refiner_prompt_example.png)


### ReVision

ReVision 与 [unCLIP](../unclip) 非常相似，但在概念层面上表现得更深。您可以向它传递一个或多个图像，它将从图像中提取概念，并使用它们作为灵感创建新图像。

首先下载 [CLIP-G Vision](https://huggingface.co/comfyanonymous/clip_vision_g/blob/main/clip_vision_g.safetensors) 并将其放入您的 ComfyUI/models/clip_vision/ 目录中。


这是一个可以拖动或加载到 ComfyUI 中的示例工作流。在以下示例中，正向文本提示被清零，以便最终输出更紧密地遵循输入图像。

![示例](sdxl_revision_zero_positive.png)


如果您想使用文本提示，可以使用此示例：

![示例](sdxl_revision_text_prompts.png)

请注意，strength 选项可用于增加每个输入图像对最终输出的影响。它还可以通过使用单个 unCLIPConditioning 或像上述示例那样将多个链接在一起来处理任意数量的图像。

如果您需要上述工作流的输入图像，它们在这里：

<img src="../unclip/mountains.png" width="256" /><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><img src="../unclip/sunset.png" width="256" />
