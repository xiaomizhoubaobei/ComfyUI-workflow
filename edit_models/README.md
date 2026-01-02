# 图像编辑模型示例

编辑模型也称为 InstructPix2Pix 模型，是可以使用文本提示编辑图像的模型。

这是 stability SDXL 编辑模型的工作流，检查点可以从[这里](https://huggingface.co/stabilityai/cosxl)下载。要使用它，下载 cosxl_edit.safetensors 文件并将其放入 ComfyUI/models/checkpoints 文件夹。

![示例](sdxl_edit_model.png)

您可以下载上述图像，然后将其拖动或加载到 ComfyUI 上以获取嵌入在图像中的工作流。

上述示例中使用的输入图像可以在[这里](../unclip/mountains.png)找到。
