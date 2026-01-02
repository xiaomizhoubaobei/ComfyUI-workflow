# Img2Img 示例

这些示例演示了如何进行 img2img。

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载这些图像以获取完整的工作流。

Img2Img 的工作原理是加载像这个[示例图像](https://github.com/comfyanonymous/ComfyUI/blob/master/input/example.png)这样的图像，使用 VAE 将其转换为潜在空间，然后使用低于 1.0 的去噪值对其进行采样。去噪控制添加到图像中的噪声量。去噪值越低，添加的噪声越少，图像的变化也越小。

输入图像应放入 input 文件夹。

这是一个简单的 img2img 工作流的样子，它与默认的 txt2img 工作流相同，但去噪设置为 0.87，并且将加载的图像传递给采样器而不是空图像。

![示例](img2img_workflow.png)
