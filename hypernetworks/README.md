# 超网络示例

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载这些图像以获取完整的工作流。

超网络是应用于主 MODEL 的补丁，因此要使用它们，请将它们放入 models/hypernetworks 目录并使用 Hypernetwork Loader 节点，如下所示：

![示例](hypernetwork_example.png)

您可以通过按顺序链接多个 Hypernetwork Loader 节点来应用多个超网络。
