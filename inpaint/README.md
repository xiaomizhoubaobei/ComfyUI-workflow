# 修复示例

![示例](inpaint_example.png)

在此示例中，我们将使用此图像。下载它并将其放置在您的 input 文件夹中。

![示例](yosemite_inpaint_example.png)

此图像已使用 gimp 将其一部分擦除为 alpha，alpha 通道是我们将用作修复掩码的内容。如果使用 GIMP，请确保保存透明像素的值以获得最佳结果。

ComfyUI 还有一个掩码编辑器，可以通过在 LoadImage 节点中右键单击图像并"在 MaskEditor 中打开"来访问。


以下图像可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载以获取完整的工作流。

使用 v2 修复模型修复猫：

![示例](inpain_model_cat.png)

使用 v2 修复模型修复女人：

![示例](inpain_model_woman.png)

它也适用于非修复模型。这是一个使用 anythingV3 模型的示例：

![示例](inpaint_anythingv3_woman.png)

### 外扩

您也可以使用类似的工作流进行外扩。外扩与修复是同一回事。有一个"为外扩填充图像"节点，可以在创建适当掩码的同时自动为外扩填充图像。在此示例中，此图像将被外扩：

![示例](yosemite_outpaint_example.png)


使用 v2 修复模型和"为外扩填充图像"节点（在 ComfyUI 中加载它以查看工作流）：

![示例](inpain_model_outpainting.png)

