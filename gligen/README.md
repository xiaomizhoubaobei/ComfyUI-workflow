# GLIGEN 示例

这是一个[下载支持的 GLIGEN 模型文件修剪版本的链接](https://huggingface.co/comfyanonymous/GLIGEN_pruned_safetensors/tree/main)

将 GLIGEN 模型文件放入 ComfyUI/models/gligen 目录。

### 文本框 GLIGEN

文本框 GLIGEN 模型让您可以指定图像中多个对象的位置和大小。要正确使用它，您应该正常编写提示，然后使用 GLIGEN Textbox Apply 节点来指定您希望提示中的某些对象/概念在图像中的位置。

![示例](gligen_textbox_example.png)

这是一个如何使用它的示例。您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载此图像以获取工作流。

