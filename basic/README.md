<!-- TOC -->

- [基础](#基础)
    - [基础 SD1.x 工作流](#基础-sd1x-工作流)
    - [使用外部 VAE 的基础 SD1.x](#使用外部-vae-的基础-sd1x)
    - [批量处理图像](#批量处理图像)
    - [参数化节点选项](#参数化节点选项)
    - [应用 LoRA](#应用-lora)
    - [应用多个 LoRA](#应用多个-lora)
    - [CLIP skip（设置 CLIP 最后一层）](#clip-skip设置-clip-最后一层)
    - [SDXL 简单版](#sdxl-简单版)
    - [SDXL 高级版](#sdxl-高级版)
    - [SDXL Text_G + Text_L](#sdxl-text_g--text_l)
    - [SDXL 仅使用 Base 模型](#sdxl-仅使用-base-模型)
- [实验](#实验)
    - [比较采样器](#比较采样器)
    - [比较检查点](#比较检查点)
    - [保存每个去噪步骤](#保存每个去噪步骤)

<!-- /TOC -->

# 基础

本节包含 ComfyUI 中基础文本到图像生成的工作流。这些是您未来所有节点设计的脚手架。

标题链接直接指向 JSON 工作流。

## [基础 SD1.x 工作流](./basic_workflow.json)

最简单的图像生成工作流。我们将详细检查这个第一个工作流的各个方面，因为它将帮助您更好地理解 Stable Diffusion 的工作原理，但我们不会对每个工作流都这样做，因为我们主要通过示例学习。

<img src="images/wf_sd1x_basic.png" alt="cat" width="100%" />

1. 首先加载检查点，这是生成的大脑。对于本教程，请确保至少在 `ComfyUI/models/checkpoints` 目录中安装了 [v1-5-pruned-emaonly.safetensors](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors) 文件，但您可以使用任何想要的 SD1.5 模型。

2. 接下来我们设置 **Latent**（潜空间）大小。理解 *潜空间和像素空间* 之间的区别很重要。图像实际上是在一个特殊的环境中处理的，该环境包含对模型有用但对我们不太有用的信息。这个环境就是 **Latent**。一旦计算完成，数据就可以转换成我们可以看到的东西，即：**像素**。这个阶段发生在上图中的步骤 #5 "Vae Decode"。

3. 是时候添加正面和负面提示词了。文本必须被解释成机器可以理解的语言。这个翻译由 CLIP 模型执行（因此节点名称为 "CLIP Text Encode"）。

4. 如果检查点是大脑，那么 **KSampler** 就是心脏。现在我们拥有所有需要的数据来进行数字计算。我们需要设置的主要参数如下：
    - **Seed（种子）**：这是用于种子随机数生成的数字。不同的种子 = 不同的图像。
    - **Steps（步数）**：用于达到最终图像的步数。更多步数需要更多计算时间，但可能会提供更好的构图。这很大程度上取决于提示词、采样器和检查点。如果不确定，从 15-20 的值开始。
    - **CFG**：*无分类器指导*（Classifier-free Guidance）比例定义了图像与提示词的接近程度。数字越低，模型越接近您的指示（即它在概念上的迭代时间越少）。如果您尝试创建模型没有直接训练过的复杂图像，更高的 CFG 可能有助于构图。通常 4 到 9 之间的值应该涵盖所有用例，但这取决于许多因素，包括您使用的检查点。
    - **Sampler（采样器）** 和 **Scheduler（调度器）** 共同负责在潜空间中携带噪声，直到在定义的步数内达到最终图像。一些采样器可能在更少的步数内达到良好结果，但可能更慢。一般来说，没有"最佳"采样器，但总体上不错的选择是 "euler ancestral" 和 "dpmpp_2m karras"，但一定要尝试所有采样器。

5. 最后，由于 VAEDecode 节点，潜空间被转换成我们可以看到的图像。请注意，转换是有损的且计算量大，因此在您的实验中，在潜空间内工作越多越好。

:warning: **重要：** 在 ComfyUI 中，随机数生成与其他 UI 不同，这使得很难重现生成的相同图像——例如——在 A1111 上。

:bulb: **提示：** 每个节点上的连接"点"都有颜色，该颜色帮助您理解节点应该连接到哪里/从哪里连接。

:bulb: **提示：** 如果图像看起来过度饱和或对比度过高，请尝试降低 CFG 比例。

:bulb: **提示：** 记住您始终可以将图像拖放到 ComfyUI 工作空间，整个节点布局将出现。这对于您在此存储库中看到的所有工作流的屏幕截图也是如此！

## [使用外部 VAE 的基础 SD1.x](./basic_workflow_ext_vae.json)

此工作流与前一个基本相同，除了我们现在使用外部 VAE 模型而不是原始检查点中内置的模型。这非常重要，因为 VAE 是 SD 图像创建的关键元素。

StabilityAI 提供了一个总体上非常好的外部 VAE，称为 [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/blob/main/vae-ft-mse-840000-ema-pruned.safetensors)。请确保下载它并将其放在 `ComfyUI/models/vae` 目录中。

如果检查点不包含适当的 VAE 或不确定，上述文件是一个很好的通用选项。在下图中，您可以看到 VAE 可以产生的差异。在右侧，眼睛和牙齿更加清晰。

<img src="images/vae_comparison.jpg" alt="vae comparison" width="512" height="256" />

## [批量处理图像](./basic_latent_batch.json)

一个非常常见的做法是生成一批 4 张图像并选择最好的一张进行放大，也许还可以对其进行一些重绘。ComfyUI 通过 "Latent From Batch" 节点提供此选项。

<img src="images/latent_batch.png" alt="latent batch" width="100%" />

工作流与基础工作流类似，但是：

1. 当我们定义潜空间大小时，我们还可以告诉我们要创建的图片数量；在这种情况下，我们将 **batch_size** 设置为 4。

2. 当 KSampler 完成后，我们可以像以前一样正常显示四张图像，并仅提取我们喜欢的那张。这可以通过 **LatentFromBatch** 节点完成。在这种情况下，我们要第三张图像（**batch index=2**，因为我们从 0 开始计数）。**Length** 是我们要提取的图片数量，因为可以过滤多张图片以对其进行额外计算。

**注意：** 您可以通过选择节点并按 <kbd>CTRL</kbd> + <kbd>M</kbd> 来启用/禁用节点。在上面的示例中，您可以禁用 LatentFromBatch 和连接的 VAEDecode 以及 SaveImage，并仅在找到您感兴趣的图像时重新启用它们。

:bulb: **提示：** 如果您双击工作区域的空白空间，您将能够通过按名称搜索来添加节点。

## [参数化节点选项](./basic_parametrized.json)

简单示例工作流，展示大多数节点参数可以转换为输入，您可以将其连接到外部值。

这在处理复杂工作流时非常有用，因为它允许您为多个节点重用相同的选项。可以在下面的 [实验部分](#Experiments) 中找到更有趣的用例。

要将参数转换为输入，请右键单击节点并选择 `convert [parm name] to input`。然后您可以创建一个 **PrimitiveNode** 并将其连接到新创建的输入。

要将输入转换回输入框，请再次右键单击并选择 `convert [parm name] to widget`。

<img src="images/widget_to_input.gif" alt="widget convert to input" width="640" height="480" />

## [应用 LoRA](./basic_lora.json)

在 ComfyUI 中，LoRA 也是节点。

<img src="images/lora.png" alt="lora node" width="50%" />

您可以使用 `strength_model` 和 `strength_clip` 参数增加/减少 lora 的效果。通常您希望它们是相同的值，但您可以尝试使用它们以获得不同的结果。查看 [这篇有趣的文章](https://github.com/cloneofsimo/lora#what-happens-to-text-encoder-lora-and-unet-lora) 了解更多信息。

**注意：** 对于此工作流，我们使用 [Studio Ghibli Lora](https://civitai.com/models/6526/studio-ghibli-style-lora)。

## [应用多个 LoRA](./multiple_loras.json)

您当然可以使用不同的权重应用多个 LoRA。此工作流向您展示如何操作。

我们将 [More Details Lora](https://civitai.com/models/82098/add-more-details-detail-enhancer-tweaker-lora) 添加到 *Studio Ghibli* 中。

## [CLIP skip（设置 CLIP 最后一层）](./clip_skip.json)

一个常见的做法是在其他 UI 中有时被称为 "clip skip" 的操作。在 ComfyUI 中，您可以使用 **CLIP Set Last Layer** 节点实现相同的结果。它用负值表示，其中 -1 表示没有 "CLIP skip"。

<img src="images/clip_skip.png" alt="clip skip" width="512" height="256" />

您可以将 CLIP 想象为一系列层，它们逐渐越来越精确地描述您的提示词。假设您有一个像 "A young woman standing in a grass field"（一个年轻女子站在草地上）这样的提示词。第一层可能是 "a woman"（一个女子），在第二层中我们添加她是 "young"（年轻）的，在第三层中她 "standing in a grass field"（站在草地上），以此类推。这并不那么简单，但只是为了给您一个想法。

通过设置最后一层，您主动限制了 CLIP 在描述您的图像时可以多深入。有时——还取决于检查点——跳过最后一层（-2）可能会导致更好的结果。

## [SDXL 简单版](./SDXL_simple.json)

在深入研究 SDXL 工作流之前的一个快速说明。您会注意到有许多使用 SDXL 的方法，我们将只探索其中几种。这正是我们在 [介绍](../README.md) 中谈到的 ComfyUI 的优势和灵活性。您可以自由地探索和尝试不同的工作流，找到最适合您需求的工作流。

**注意：** 对于 SDXL 示例，我们使用 [sd_xl_base_1.0.safetensors](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors) 和 [sd_xl_refiner_1.0.safetensors](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors) 文件，请确保下载它们并将它们放入 `ComfyUI/models/checkpoints` 目录中。

您还会发现以 `_0.9vae` 结尾的相同文件，这些文件已经内置了更好的 VAE，或者您可以像使用 SD1.x 模型一样使用 [外部 VAE](https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors)。

简单的工作流类似于 [官方存储库](https://comfyanonymous.github.io/ComfyUI_examples/sdxl/) 中建议的工作流。SDXL 由两个模型组成，即使您可以只使用 Base 模型，refiner 也可能会给您的图像带来额外的清晰细节。

布局看起来像这样：

<img src="images/SDXL_simple.png" alt="clip skip" width="100%" />

1. 我们加载 **base 模型**

2. 设置 **latent size**（潜空间大小）。记住 SDXL 是用 1024x1024 的图片训练的，所以这是一个很好的起始分辨率。在本节的末尾，您会发现一个参考，其中包含 SDXL 可以工作的所有分辨率（具有不同程度的成功）。

3. **总步数**。注意我们对一些值进行了参数化，以便我们可以轻松重用它们（参见 [上面的部分](#Parametrize-node-options)）。

4. 图像创建分为两个阶段：Base 和 Refiner。此参数定义在 Base 模型上花费多少步数，在 refiner 上花费多少步。**在总共 25 步中，我们决定在 Base 上花费 19 步**，因此在 Refiner 上花费 6 步。一个好的经验法则是让 base 模型完成 80% 的工作，但一如既往：实验。

5. 这次我们使用 **Advanced KSampler**，它是一个非常重要的节点，让我们更精确地使用采样器。我们将总步数设置为 25，但指示采样器在第 19 步停止。注意我们需要将 `return_with_leftover_noise` 设置为 `enable`，以便 refiner 可以在 base 停止的地方继续工作。

6. 我们加载 refiner 模型。

7. 我们从 base ksampler 获取剩余的潜空间并将其直接传递给 refiner。我们仍然将总步数设置为 25，但告诉采样器从第 19 步开始，这是我们离开 base 的地方。注意我们使用的是在 base KSampler 节点中使用的采样器和调度器。一些采样器彼此兼容，但最好使用相同的。

剩下的就是解码 VAE 并保存图像。您可以使用 Base 或 Refiner 中内置的 VAE，或使用外部 VAE。

<details>
<summary>SDXL 分辨率</summary>

| 比例 | 分辨率
| ----- | ----------
| 0.5   | 704×1408
| 0.52  | 704×1344
| 0.57  | 768×1344
| 0.6   | 768×1280
| 0.68  | 832×1216
| 0.72  | 832×1152
| 0.78  | 896×1152
| 0.82  | 896×1088
| 0.88  | 960×1088
| 0.94  | 960×1024
| 1.0   | 1024×1024
| 1.07  | 1024×960
| 1.13  | 1088×960
| 1.21  | 1088×896
| 1.29  | 1152×896
| 1.38  | 1152×832
| 1.46  | 1216×832
| 1.67  | 1280×768
| 1.75  | 1344×768
| 1.91  | 1344×704
| 2.0   | 1408×704
| 2.09  | 1472×704
| 2.4   | 1536×640
| 2.5   | 1600×640
| 2.89  | 1664×576
| 3.0   | 1728×576

</details>

## [SDXL 高级版](./SDXL_advanced.json)

SDXL 引入了两个新的 **CLIP Text Encode 节点**，一个用于 base，一个用于 refiner。它们添加 `text_g` 和 `text_l` 提示词以及宽度/高度条件。

**Text G** 是 *自然语言* 提示词，您只需通过描述您想要的内容来与模型交谈，就像您对一个人所做的那样。**Text L** 接受概念和单词，就像我们在 SD1.x/2.x 中习惯的那样。各种实验让我们相信，为 G 和 L 设置相同的值通常效果更好，或者无论如何模型似乎更能理解我们想要什么。当然，尝试所有选项，下面我们还提供了一个拆分两个提示词的工作流。

目前还不完全清楚维度条件如何影响构图。通过初步测试，似乎将 `width/height` 和 `target_width/height` 设置为 4096 倾向于生成稍微更清晰的细节。为了在更极端的图像分辨率下保持正确的宽高比，将 CLIP 宽度和高度设置为 Latent 大小的 4 倍可能是一个好主意。

## [SDXL Text_G + Text_L](./SDXL_text_g-l.json)

此工作流让您尝试为 `text_g` 和 `text_l` 使用不同的提示词（有关更多详细信息，请参阅上一个工作流）。下面是使用相同的 text_l/g 与两个不同提示词的差异。

<img src="images/prompt_comparison.jpg" alt="clip skip" width="100%" />

## [SDXL 仅使用 Base 模型](./SDXL_base_only.json)

SDXL 也可以仅使用 base 模型。如果您的资源有限或一般实验，这可能很有用。

# 实验

在实验中，我们应用我们在类别中学到的知识，以尝试探索更高级的工作流。

## [比较采样器](./experiments/compare_samplers.json)

在此工作流中，我们检查四个采样器之间的差异。我们使用相同的检查点、步数和 CFG 比例来查看哪个采样器提供最佳结果。

<details>
<summary>图像比较</summary>
<img src="images/compare_samplers.png" alt="compare samplers" width="768" />
</details>

## [比较检查点](./experiments/compare_checkpoints.json)

在此工作流中，我们使用相同的提示词和采样器选项比较两个检查点：[Absolute Reality](https://civitai.com/models/81458/absolutereality) 和 [Realistic Vision](https://huggingface.co/SG161222/Realistic_Vision_V3.0_VAE)。

请注意，工作流中的所有模型都需要加载到内存中，因此比较检查点可能会消耗大量资源。

## [保存每个去噪步骤](./experiments/save_noise_steps.json)

此工作流将去噪过程的每一步保存到 `output` 目录中。要自动化该过程，请在主 ComfyUI 菜单中选择 `Extra options`，并将批次数设置为总步数（在此示例中为 20）。

记住每次生成新图像时都需要将 **primitive** `end_at_step` 设置回 1。