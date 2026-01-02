# Lora 示例

这些示例演示了如何使用 Loras。所有 LoRA 类型：Lycoris、loha、lokr、locon 等...都以这种方式使用。

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载这些图像以获取完整的工作流。

Loras 是应用于主 MODEL 和 CLIP 模型之上的补丁，因此要使用它们，请将它们放入 models/loras 目录并使用 LoraLoader 节点，如下所示：

![示例](lora.png)

您可以通过链接多个 LoraLoader 节点来应用多个 Loras，如下所示：

![示例](lora_multiple.png)
