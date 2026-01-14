<!-- TOC -->

- [图像到图像条件](#图像到图像条件)
    - [简单 Img2Img](#简单-img2img)
    - [unCLIP 模型](#unclip-模型)
    - [风格模型](#风格模型)
    - [IPAdapter 图像 + 文本](#ipadapter-图像--文本)
    - [SDXL Revision](#sdxl-revision)
- [实验](#实验)
    - [unCLIP 多图像](#unclip-多图像)
    - [unCLIP 与 SDXL refiner 增强](#unclip-与-sdxl-refiner-增强)
    - [IPAdapter 图像变体](#ipadapter-图像变体)
    - [IPAdapter + Canny control net](#ipadapter--canny-control-net)
    - [风格模型的时间步进](#风格模型的时间步进)

<!-- /TOC -->

# 图像到图像条件

一图胜千言，有时从参考图像开始比尝试简单的[文本到图像](../text2img/README.md)更有效。

在本节中，我们将探索各种图像到图像技术。

如果您想遵循以下示例，请确保下载此存储库的 [input](../input/) 目录的内容并将其放在 `ComfyUI/input/` 中。

## [简单 Img2Img](./img2img_SDXL.json)

最简单的图像到图像工作流是通过在采样器中使用*小于 1* 的去噪值在现有图像上"绘制"。

去噪值越低，构图越接近原始图像。

我们当然可以通过适当的提示词来增强生成。在这个工作流中，我们使用女性肖像的基础图像来创建类似的男性图像。

<img src="./images/img2img.png" width="512" height="256" alt="img to img" />

:point_right: **注意：** 我们在这个示例中使用 SDXL。潜空间大小为 `1024x1024`，但条件图像仅为 `512x512`。始终使用相同大小的图像是一个好主意。这就是为什么在这个示例中我们将原始图像缩放以匹配潜空间。**这通常适用于每个图像到图像工作流**，包括 ControlNets，特别是如果宽高比不同。

## [unCLIP 模型](./conditioning_unclip.json)

有时您想根据参考图片的风格创建图像。您不是在绘制，而是从源中获取灵感。

这可以通过 [unCLIP 模型](https://huggingface.co/stabilityai/stable-diffusion-2-1-unclip/tree/main) 完成。在这个示例中，我们使用 `sd21-unclip-h.ckpt` 检查点。

<img src="images/unclip.png" width="100%" alt="unclip" />

1. 我们使用 `unCLIPCheckpointLoader` 节点加载检查点。请注意，它基于 SD2.1，所以我们使用 `768x768` 潜空间大小，这是模型训练的分辨率。

2. 我们使用 `CLIP Vision Encode` 节点为模型编码参考图片。

3. 条件化发生在 `unCLIPConditioning` 节点上。`noise_augmentation` 定义新图像与原始图像的接近程度，`0` 表示最忠实。通常将此值设置为 `0.1-0.3` 是一个好主意，只是为了给采样器一些回旋余地。`strength` 是相对于其他条件（在此示例中为文本 clip）的条件强度。这就像在提示词中设置文本的权重，例如：`(red hat:1.2)`。

:bulb: **提示：** 您会注意到有两个 unCLIP 模型可用：`sd21-unclip-l.ckpt` 和 `sd21-unclip-h.ckpt`。通常对于单个图像，您想使用更准确的 `-h` 变体。`-l` 模型是在资源稀缺或需要极端速度时创建的。

## [风格模型](./conditioning_style.json)

风格模型的工作方式类似于 unCLIP，但它是 CLIP Vision 条件，可以与任何 SD1.5 模型一起使用。

要使其工作，您需要 `ComfyUI/models/clip_vision` 目录中的 [CLIP Vision 模型](https://huggingface.co/openai/clip-vit-large-patch14/resolve/main/pytorch_model.bin) 和 `ComfyUI/models/style_models` 中的 [风格模型](https://huggingface.co/TencentARC/T2I-Adapter/blob/main/models/coadapter-style-sd15v1.pth) 本身。

<img src="images/style.png" width="100%" alt="style model" />

1. 加载 CLIP Vision 模型。

2. 对源图像进行编码以供模型使用。

3. 加载风格模型

4. 将您的提示词连接到 `Apply style model` 节点，然后连接到 KSampler 正面。请注意，虽然该节点不提供 `strength` 选项，但您技术上可以通过 [时间步进](../text2img/README.md#timestepping) 微调效果。查看 [实验](#experiments) 以获取一些示例。

:point_right: **注意：** 风格模型——像许多"以...风格"的 img2img 一样——无法应用它不理解的东西的风格。著名绘画或人物的照片很容易处理，但更异国情调、抽象或难以理解的东西可能会导致令人失望的结果。

## [IPAdapter 图像 + 文本](./IPAdapter_basic_SDXL.json)

[IPAdapter](https://github.com/tencent-ailab/IP-Adapter) 是一系列非常有效的图像条件模型。它们可以单独使用，也可以与文本和 ControlNets 结合使用。

在这个工作流中，我们提供了一个简单的图像+文本条件示例。还要查看 [实验](#experiments) 以获取更多用例。我们使用 SDXL，但 SD1.5 的模型也可用。

您需要在 huggingface 上下载 [这些预训练模型](https://huggingface.co/h94/IP-Adapter/tree/main) 并安装 [ComgyUI 扩展](https://github.com/cubiq/ComfyUI_IPAdapter_plus)（来自我本人）。请注意，**您既需要模型也需要图像编码器**。按照扩展页面上的安装说明进行操作。

工作流本身非常简单，类似于风格模型。

:bulb: **提示**：您可以使用 `ImageBatch` 节点使用多个参考图像。

<img src="./images/ipadapter-img-txt.jpg" height="256" alt="IPAdapter" />

## [SDXL Revision](./revision_SDXL.json)

Stability AI 发布了 [Revision 模型](https://huggingface.co/stabilityai/control-lora#revision)，它类似于我们在本节中探索的其他方法，但专门用于 SDXL。

Revision 用于图像（包括多个图像）和图像+文本条件，它也是创建图像变体的相当有效的工具。

下载 [clip vision 模型](https://huggingface.co/stabilityai/control-lora/resolve/main/revision/clip_vision_g.safetensors) 并将其放在 `ComfyUI/models/clip_vision` 目录中。

工作流类似于 [unCLIP](#unclip-model)，但检查点是 SDXL base。在这个示例中，我们合并两个图像的风格。

<img src="./images/revision.jpg" width="768" alt="revision" >

与 unCLIP 一样，`noise_augmentation` 决定与参考图像的接近程度（`0` 表示最接近），`strength` 决定条件的权重。

:point_right: **注意：** 为了消除文本 clip 的任何干扰，我们还使用 `ConditioningZeroOut`，这是可选的，仅用于此示例的目的，该示例旨在作为没有任何其他外部影响的纯图像+图像条件。您可以通过消除零输出节点并添加自定义提示词来进一步改变图像生成。

# 实验

## [unCLIP 多图像](./experiments/conditioning_unclip_multiple_imgs.json)

使用 unCLIP 模型合并两个图像的风格。

## [unCLIP 与 SDXL refiner 增强](./experiments/unclip_SDXL_refiner.json)

这是一个有趣的实验。我们使用 unclip 融合两个图像，然后使用 SDXL refiner 增强分辨率。

## [IPAdapter 图像变体](./experiments/IPAdapter_img_variations.json)

在这个 SD1.5 工作流中，我们首先使用 [dreamshaper](https://civitai.com/models/4384/dreamshaper) 创建图像，然后使用 IPAdapter 创建该图像的 4 个变体，并带有额外的文本条件。

## [IPAdapter + Canny control net](./experiments/IPAdapter_canny.json)

此工作流使用 IPAdapter 的条件图像并添加 Canny control net 以进一步增强构图。

对于此示例，您需要下载 [canny controlnet](https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny.pth) 并将其放在 `ComfyUI/models/controlnet` 下。或者，您可以使用 [Controlnet 扩展](https://github.com/Fannovel16/comfyui_controlnet_aux)，它应该负责下载所有缺失的模型。

## [风格模型的时间步进](./experiments/timestepping_style_model.json)

有时似乎无法微调某些条件节点，例如我们之前看到的风格模型。

通过一点技巧和时间步进，实际上可以微调任何条件节点。

<img src="./images/timestepping_style_model.png" width="100%" alt="timestepping the style model" />

在这个实验中，我们使用一个提示词作为文本条件，然后将一个零输出的空提示词连接到风格模型。现在我们可以对两个条件进行时间步进，以轻松校准最终结果。