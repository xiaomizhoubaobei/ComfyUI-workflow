# ControlNet 和 T2I-Adapter 示例

请注意，在这些示例中，原始图像直接传递给 ControlNet/T2I 适配器。

每个 ControlNet/T2I 适配器都需要传递给它的图像采用特定格式，如深度图、canny 图等，具体取决于特定模型，如果您想要良好的结果。

ControlNetApply 节点不会为您将常规图像转换为深度图、canny 图等。您必须单独执行此操作或使用节点来预处理您的图像，您可以在这里找到：[这里](https://github.com/Fannovel16/comfy_controlnet_preprocessors)

您可以在这里找到最新的 controlnet 模型文件：[原始版本](https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main) 或 [更小的 fp16 safetensors 版本](https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/tree/main)

对于 SDXL，stability.ai 发布了 Control Loras，您可以在[这里（rank 256）](https://huggingface.co/stabilityai/control-lora/tree/main/control-LoRAs-rank256)或[这里（rank 128）](https://huggingface.co/stabilityai/control-lora/tree/main/control-LoRAs-rank128)找到它们。它们的使用方式与常规 ControlNet 模型文件完全相同（放入同一目录）。

ControlNet 模型文件放入 ComfyUI/models/controlnet 目录。

### 涂鸦 ControlNet

这是一个如何使用 controlnets 的简单示例，此示例使用涂鸦 controlnet 和 AnythingV3 模型。您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载此图像以获取完整的工作流。


![示例](controlnet_example.png)

这是我用于此工作流的输入图像：

<img src="input_scribble_example.png" width="256" />

### T2I-Adapter 与 ControlNets

T2I-Adapters 比 ControlNets 高效得多，所以我强烈推荐它们。ControlNets 会显著降低生成速度，而 T2I-Adapters 对生成速度几乎没有负面影响。

在 ControlNets 中，ControlNet 模型每次迭代运行一次。对于 T2I-Adapter，模型总共运行一次。

T2I-Adapters 在 ComfyUI 中的使用方式与 ControlNets 相同：使用 ControlNetLoader 节点。

这是此示例中将使用的输入图像[来源](https://commons.wikimedia.org/wiki/File:Stereogram_Tut_Shark_Depthmap.png)：

<img src="shark_depthmap.png" width="512" />

这是使用深度 T2I-Adapter 的方法：

![示例](depth_t2i_adapter.png)

这是使用深度 Controlnet 的方法。请注意，此示例使用 DiffControlNetLoader 节点，因为使用的 controlnet 是 diff control net。Diff controlnets 需要正确加载模型的权重。DiffControlNetLoader 节点也可用于加载常规 controlnet 模型。加载常规 controlnet 模型时，它的行为与 ControlNetLoader 节点相同。

![示例](depth_controlnet.png)

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载这些图像以获取完整的工作流。

### 姿势 ControlNet

这是此示例中将使用的输入图像：

![示例](pose_worship.png)


这是一个使用第一遍 AnythingV3 配合 controlnet，第二遍不使用 controlnet 配合 AOM3A3（abyss orange mix 3）并使用其 VAE 的示例。

![示例](2_pass_pose_worship.png)

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载此图像以获取完整的工作流。


### 混合 ControlNets

可以像这样应用多个 ControlNets 和 T2I-Adapters 以获得有趣的结果：

![示例](mixing_controlnets.png)

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载此图像以获取完整的工作流。

输入图像：

<img src="pose_present.png" width="256" /><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><img src="house_scribble.png" width="256" />

