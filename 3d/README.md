# 3D 示例

## Stable Zero123

Stable Zero123 是一个扩散模型，给定一个带有对象和简单背景的图像，可以生成该对象从不同角度的图像。

[检查点可以在这里下载](https://huggingface.co/stabilityai/stable-zero123/blob/main/stable_zero123.ckpt) 将其放入 ComfyUI/models/checkpoints 文件夹。

您可以下载此图像并将其加载或拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 上以获取工作流。

![示例](stable_zero123_example.png)

输入图像可以在[这里](../hypernetworks/hypernetwork_example_output.png)找到，它是 [hypernetworks](../hypernetworks) 示例的输出图像。

仰角和方位角以度为单位，控制对象的旋转。
