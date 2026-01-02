# unCLIP 模型示例

unCLIP 模型是 SD 模型的特殊版本，专门调优以接收图像概念作为输入，除了您的文本提示之外。图像使用这些模型附带的 CLIPVision 进行编码，然后提取的概念在采样时传递给主模型。

它基本上让您可以在提示中使用图像。

这是在 ComfyUI 中使用它的方法（您可以将此图像拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中以获取工作流）：

![示例](unclip_example.png)

noise_augmentation 控制模型尝试遵循图像概念的紧密程度。值越低，它就越会遵循该概念。

strength 是它对图像的影响强度。

可以像这样使用多个图像：

![示例](unclip_example_multiple.png)

您会注意到它不会以传统意义混合图像，而是实际上从两者中选择一些概念并制作一个连贯的图像。

输入图像：

<img src="mountains.png" width="256" /><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><img src="sunset.png" width="256" />

您可以在[这里](https://huggingface.co/stabilityai/stable-diffusion-2-1-unclip/tree/main)找到官方 unCLIP 检查点

您可以在[这里（基于 WD1.5 beta 2）](https://huggingface.co/comfyanonymous/wd-1.5-beta2_unCLIP/tree/main)和[这里（基于 illuminati Diffusion）](https://huggingface.co/comfyanonymous/illuminatiDiffusionV1_v11_unCLIP/tree/main)找到我通过一些巧妙的合并从现有 768-v 检查点制作的一些 unCLIP 检查点

### 更高级的工作流

使用 unCLIP 检查点的一个好方法是将它们用于两遍工作流的第一遍，然后在第二遍切换到 1.x 模型。这就是生成以下图像的方法。（您可以将其加载到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中以获取工作流）：

![示例](unclip_2pass.png)
