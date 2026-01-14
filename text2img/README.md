<!-- TOC -->

- [文本到图像](#文本到图像)
    - [词权重](#词权重)
    - [Embedding/文本反转](#embedding文本反转)
    - [条件连接](#条件连接)
    - [条件平均](#条件平均)
    - [区域条件](#区域条件)
    - [时间步进](#时间步进)
    - [GLIGEN 框](#gligen-框)
- [实验](#实验)
    - [比较合并方法](#比较合并方法)
    - [空白令牌技巧](#空白令牌技巧)
    - [负面中的恐怖元素](#负面中的恐怖元素)
    - [区域条件 vs GLIGEN 框](#区域条件-vs-gligen-框)

<!-- /TOC -->

# 文本到图像

文本提示词是 Stable Diffusion 图像生成的基础，但有许多方法可以通过与文本交互来获得更好的结果。

这些工作流探索了我们使用文本进行图像条件的多种方式。

与往常一样，标题直接链接到工作流。

:warning: **重要：** 并不总是容易预见哪种条件方法对给定任务更好。通常结果会模糊在一起，预测模型会做什么是不可能的。唯一的方法是实验，幸运的是 ComfyUI 非常擅长比较工作流，查看 [实验](#experiments) 部分以获取一些示例。

## [词权重](./word_weighting.json)

这非常简单且广泛使用，但无论如何值得一提。

您可以通过将单词或一系列单词放在括号中来赋予它们更高（或更低）的权重：`closeup a photo of a (freckled) woman smiling`。

在这个示例中，我们给 "freckled" 稍微更高的权重。我们可以通过添加更多权重来增加效果，例如：`(freckled:1.3)`。通常 `1.1` 到 `1.4` 之间的值就足够了，但可能因模型而异。

您还可以通过将数字设置为低于 1 来降低权重。因此 `(freckled:0.7)` 将会非常轻微地 *freckled*。

:bulb: **提示：** `(freckled:1.1)` 等同于 `(freckled)`

<img src="./images/word_weight.png" alt="word weighting" width="256" height="256" />

## [Embedding/文本反转](./embeddings.json)

Embeddings 是非常简单的条件，因为它们非常容易训练，有时非常有效而受到欢迎。

对于这个示例工作流，您需要 [UnrealisticDream](https://civitai.com/models/72437?modelVersionId=77173) 和 [BadDream](https://civitai.com/models/72437?modelVersionId=77169) embeddings。下载文件并将它们放在 `ComfyUI/models/embeddings` 目录中。

要激活 embedding，请使用语法：`embedding:FileName`。要使用 UnrealisticDream，请使用 `embedding:UnrealisticDream`。不需要包含文件扩展名。

Embeddings 的作用类似于标准单词，因此它们在提示词中的位置很重要（即：它们在提示词中出现的越早，它们的重要性就越高），您还可以增加它们的权重。

在下图中，您可以看到相同提示词有无 embeddings 的差异。我们使用了：`(embedding:UnrealisticDream:1.2), embedding:BadDream`。

<img src="./images/embedding.jpg" alt="embeddings" width="512" height="256" />

:point_right: **注意：** 值得注意的是，embeddings 不是能解决所有问题的神奇东西。有时 embedding 会产生比解决的问题更多的问题。明智地使用它们并进行实验。

## [条件连接](./conditioning_concat.json)

使用提示词的一种非常强大的方法是通过 **conditioning concat** 节点。

模型通常不擅长理解多个概念和情境化不同元素的特征。例如，指定不同颜色的对象可能非常困难。

考虑提示词：`a blue ball a red bucket on the beach`。

<img src="./images/blue_ball_red_bucket.jpg" width="256" alt="fail" >

在这种情况下，成功率非常低，大约 25 张图像中只有 1 张实际显示红色桶和蓝色球。

我们可以通过使用 *concat* 来增加我们的机会，如下所示：

<img src="./images/conditioning_concat.png" width="100%" alt="conditioning concat" >

在这种情况下，我们的成功率约为 1/3。

<img src="./images/concat_success.jpg" width="256" alt="concat success" >

## [条件平均](./conditioning_average.json)

有时您想要将两个概念合并在一起，比如...一个斑马-变色龙：

<img src="./images/conditioning_average.png" width="256" height="256" alt="a zebra chameleon" >

您可以通过简单的提示词获得幸运，但更好的选择是使用 **conditioning average** 节点。

## [区域条件](./conditioning_area.json)

有时您需要在图像内部空间定位对象。不使用 ControlNet 的最简单方法是使用 **area conditioning** 节点。语法非常简单：

<img src="images/area_conditioning.png" alt="area conditioning" width="100%"/>

1. 使用提示词描述您的场景

2. 使用第二个提示词描述您想要定位的事物

3. 将第二个提示词连接到 **conditioning area** 节点并设置区域大小和位置。在这个示例中，我们有一个 768x512 的潜空间，我们希望 "godzilla" 在最右边。我们设置了一个 512x512 的区域条件并将其推到 X 轴上的 256px。

4. 使用 **Conditioning combine** 节点连接场景提示词和空间条件。

剩下的就是将条件组合发送到 KSampler 正面提示词，等待魔法发生。

当然，您可以使用此技术定位多个对象，而不仅仅是一个，如本示例所示。

:point_right: **注意：** 提供的工作流做了一些稍微不同的事情。它首先设置两个区域（一个在左边，一个在右边），然后对整个图像应用第二遍以使所有内容统一。这是使其在 SDXL 上工作的最佳方法。

## [时间步进](./timestepping.json)

`ConditioningSetTimestepRange` 是 ComfyUI 中的一个新节点，也是我们拥有的最强大的文本条件工具之一。

该节点允许您为每个提示词设置开始/停止时间位置。假设我们有 20 步，您可以告诉采样器在 5 步内开始"绘制"一只猫（这可能是最重要的），然后忘记猫并在剩余的 15 步中开始生成一只狗。

这是混合提示词的一种非常有效的方法，可能是提供更高级别微调的方法。每个提示词不需要在前一个结束的地方开始，但它们也可以相互融合，以便在几步内两个概念将合并。

在这个工作流中，我们尝试生成一个有雀斑的非裔美国人/日本女性。为此，我们在去噪阶段以不同的时间混合了 3 个概念（雀斑、日本人、非裔美国人）。结果非常令人印象深刻。

<img src="images/timestepping.png" alt="timestepping" width="256" height="256" />

:point_right: **注意：** 您可以有多个时间步节点，每个节点可以在不同的时间开始/停止，但重要的是没有任何时间框架未被条件化。即：如果您有两个提示词，第一个在 0.5 结束，第二个应该在 0 到 0.5 之间的任何位置开始，但不能在 0.6，否则您将有一些没有条件的步骤。

## [GLIGEN 框](./gligen_box.json)

GLIGEN 是*引导*文本到图像模型。Comfy 目前只支持框条件，它类似于我们之前描述的 [区域条件](#area-conditioning)。要使其工作，您需要 [下载 GLIGEN 模型](https://huggingface.co/comfyanonymous/GLIGEN_pruned_safetensors/tree/main) 并将它们放在 `ComfyUI/models/gligen` 目录中。

<img src="images/gligen_box.png" width="100%" alt="gligen box" />

第一步是提示您的场景，然后为您想要条件的场景的每个元素创建一个 `GLIGENTextBoxApply` 并将它们连接到 `GLIGENLoader` 节点。

在我们的示例中，我们使用提示词：`high quality illustration of red riding hood hugging the wolf in the forest` 作为一般指导。然后我们设置两个 GLIGEN 框，一个用于 `red riding hood` 文本，另一个用于 `wolf`，并将它们空间定位。多个框可以直接相互连接，最后连接到采样器，如上图所示。

结果通常比标准区域条件更好，但 GLIGEN 模型未能引起太多兴趣。

:point_right: **注意：** 在这个工作流中，我们使用 [dreamshaper](https://civitai.com/models/4384/dreamshaper) 检查点，但您当然可以选择任何您想要的模型。

# 实验

## [比较合并方法](./experiments/compare_conditioning_merge.json)

此工作流比较了合并两个著名演员以生成具有两者面部特征的新人的方法。

我们使用：
- 标准提示词，只需在主提示词中添加两个演员
- 条件平均
- 条件连接
- 时间步进

:warning: **重要：** 每种方法的结果在很大程度上取决于提示词的复杂性和使用的检查点。当提示词简单（如本示例）时，通常很容易让模型做您想做的事情。当提示词扩展或模型未针对特定概念进行训练时，事情会变得复杂。

此工作流仅作为示例呈现，您应该扩展和实验。此外，每种类型的条件可能需要不同的提示词语法，而为了简单起见，我们对所有条件使用相同的语法。

## [空白令牌技巧](./experiments/blank_token.json)

任何东西都可能影响图像生成。有时您可能会尝试在提示词中添加奇怪的不相关单词，只是为了看看模型如何反应。问题是任何有意义的单词都可能过多地引导构图，如果您想给图像一点推动力而不改变任何实质内容怎么办？

好吧，尝试在提示词中添加一个空白空间，如下所示：`a photo of a cat wearing a spacesuit inside a spaceship, high resolution, detailed, 4k, ,`

注意末尾的 `, ,`。

此工作流比较了有无空白令牌的两个提示词。

## [负面中的恐怖元素](./experiments/horrors_negative.json)

这是一个好奇的，实际上非常有效的技术，可以用一个简单的单词*美化*您的构图。我们注意到，在负面提示词中添加任何与 *恐怖* 相关的单词会使图像通常更令人愉悦，而不会过多地改变原始概念。

在此工作流中，我们比较以下单词的结果：`horror`、`zombie`、`Frankenstein`。更通用的 "horror" 是一个安全的选择，因为它不会影响太多，但尝试各种单词并检查结果。

:point_right: **注意：** 根据主题，从构图中移除恐怖元素往往会使图像"太完美"而不太现实。所以要负责任地使用。

## [区域条件 vs GLIGEN 框](./experiments/area_vs_gligen.json)

此工作流比较区域条件和 GLIGEN，这是我们在本节中探索的两种空间条件技术。

它们都是不错的选择，但 GLIGEN 通常更忠实于您要求的构图。

此示例使用 [dreamshaper](https://civitai.com/models/4384/dreamshaper) 检查点。