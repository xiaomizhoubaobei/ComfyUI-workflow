# 2 遍 Txt2Img（Hires fix）示例

这些示例演示了如何实现"Hires fix"功能。

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载这些图像以获取完整的工作流。

Hires fix 只是以较低分辨率创建图像，对其进行上采样，然后通过 img2img 发送它。请注意，在 ComfyUI 中，txt2img 和 img2img 是同一个节点。Txt2Img 是通过向采样器节点传递空图像并使用最大去噪来实现的。

这是 ComfyUI 中使用基本潜在上采样执行此操作的简单工作流：

![示例](hiresfix_latent_workflow.png)

## 非潜在上采样

这是一个如何使用 [esrgan 上采样器](../upscale_models) 进行上采样步骤的示例。由于 ESRGAN 在像素空间中操作，因此图像必须在被上采样后转换为像素空间并返回潜在空间。

![示例](hiresfix_esrgan_workflow.png)


## 更多示例

这是一个更复杂的 2 遍工作流的示例，此图像首先使用 WD1.5 beta 3 illusion 模型生成，潜在上采样，然后使用 cardosAnime_v10 进行第二遍：

![示例](latent_upscale_different_prompt_model.png)


