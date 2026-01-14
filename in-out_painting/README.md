<!-- TOC -->

- [内/外绘](#内外绘)
    - [内绘](#内绘)
    - [外绘](#外绘)
    - [使用 SD1.5 进行 SDXL 内绘](#使用-sd15-进行-sdxl-内绘)
- [实验](#实验)
    - [多次外绘](#多次外绘)
    - [外绘接缝修复](#外绘接缝修复)

<!-- /TOC -->

# 内/外绘

有时候您需要更改图像上的细节，或者您想要扩展到一侧。内绘在 Stable Diffusion 中非常有效，ComfyUI 中的工作流也非常简单。

请注意，在内绘时，最好使用为此目的训练的检查点。它们通常以基础模型名称加上 `inpainting` 来命名。虽然普通检查点可以用于内绘，但使用特定模型通常会产生更好的结果。对于这些工作流，我们主要使用 [DreamShaper Inpainting](https://civitai.com/models/4384?modelVersionId=131004)。

:bulb: **提示：** 大多数图像节点都集成了蒙版编辑器。右键单击任何图像并选择 `Open in Mask Editor`（在蒙版编辑器中打开）。或者，您可以在任何照片编辑软件上创建 alpha 蒙版。[GIMP](https://www.gimp.org/) 是一个免费的软件，对于大多数任务来说已经足够了。

标题直接链接到相关的工作流。

## [内绘](./inpaint.json)

工作流非常简单，唯一需要注意的是，为了对图像进行内绘编码，我们使用 `VAE Encode (for Inpainting)` 节点，并将 `grow_mask_by` 设置为 8 像素。稍微扩大蒙版通常是一个好主意，这样模型可以"看到"周围区域。

<img src="./images/inpainting.png" width="100%" alt="inpainting" />

在内绘区域周围出现接缝线并不罕见，在这种情况下，我们可以进行低去噪的第二遍（如示例工作流所示），或者您可以简单地在上放过程中修复它。

下面您可以看到原始图像、蒙版和通过添加"红发"文本提示词进行内绘的结果。

<img src="./images/inpainting_result.jpg" width="100%" alt="inpainting example" />

## [外绘](./outpaint.json)

外绘类似于内绘，我们仍然使用内绘模型以获得最佳结果，工作流完全相同，除了 `Pad Image for Outpainting` 节点。

<img src="./images/outpaint.png" width="100%" alt="inpainting" />

该节点允许我们在图像的侧面添加空白空间，以便进行外绘魔法。它提供了一个羽化选项，但通常不需要，实际上可以通过简单地增加 `VAE Encode (for Inpainting)` 节点中的 `grow_mask_by` 来获得更好的结果。

## [使用 SD1.5 进行 SDXL 内绘](./SDXL_inpaint_SD15.json)

在撰写本文时，SDXL 只有一个 beta [内绘模型](https://huggingface.co/diffusers/stable-diffusion-xl-1.0-inpainting-0.1)，但没有什么能阻止我们使用 SD1.x/2.x 进行内绘。此工作流向您展示如何操作，它还添加了使用 SDXL refiner 的最后一遍，以修复内绘过程可能产生的任何接缝线。

# 实验

## [多次外绘](./experiments/multiple_outpaints.json)

当然可以链接多次外绘。这样我们能够为每一遍自定义提示词。效果非常好。

<img src="./images/multiple_outpaints.jpg" width="100%" alt="Multiple outpaints" />

## [外绘接缝修复](./experiments/outpaint_seam_fix_SDXL.json)

在这个示例中，我们使用 SDXL 进行外绘。在外绘开始的地方会出现接缝，为了修复这个问题，我们应用了蒙版第二遍，这将使任何不一致的地方变得平滑。

在下图中，您可以看到工作流如何修复接缝。之前/之后。

![seam fix](./images/seam_detail.jpg)

唯一有趣的一点是我们如何为重叠区域创建蒙版。您当然可以使用 *Mask Editor*（蒙版编辑器）粗略地手动绘制它，但更好的方法是使用一系列蒙版相关节点，如图所示。

<img src="./images/seam_mask.png" width="100%" alt="seam mask" />