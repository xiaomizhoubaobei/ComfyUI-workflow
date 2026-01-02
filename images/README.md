# Chroma

这是一个从 [flux](../flux/) 修改而来的模型，在架构上进行了一些更改。

要使用它，您需要一个 t5xxl 文本编码器模型文件，可以在 [这个仓库](https://huggingface.co/comfyanonymous/flux_text_encoders/tree/main) 中找到，推荐使用 fp16 版本，如果内存不够，推荐使用 fp8_scaled 版本。将其放入 ComfyUI/models/text_encoders/ 文件夹中。

然后您可以从 [官方 huggingface 页面](https://huggingface.co/lodestones/Chroma1-HD) 下载最新的 chroma 检查点文件，放入 ComfyUI/models/diffusion_models/ 文件夹中。

在 ComfyUI 中加载或拖动此图像以获取示例工作流：

![示例](chroma_example.png)