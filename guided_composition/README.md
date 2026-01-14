<!-- TOC -->

- [引导构图](#引导构图)
    - [姿态](#姿态)
    - [Canny 边缘](#canny-边缘)
    - [深度](#深度)
- [实验](#实验)
    - [多个 ControlNet](#多个-controlnet)

<!-- /TOC -->

# 引导构图

这里开始变得有趣了。文本提示词或图像到图像只能带您走到这一步，杰作的秘密在于 ControlNet 和类似的引导构图。

对于本节中的大多数工作流，您需要 [ComfyUI 的 ControlNet 辅助预处理器扩展](https://github.com/Fannovel16/comfyui_controlnet_aux)。在继续之前，请确保已安装它。

与往常一样，标题直接链接到工作流。

## [姿态](./pose.json)

所有 control net 的工作流基本相同，不同的是您用于处理的模型，可能还有预处理器。

在这个第一个示例中，我们使用 openpose 将 *火柴人* 转换为实际角色。

<img src="./images/pose.png" width="100%" alt="open pose" />

您会注意到每个 Controlnet 或 T2Adapter 都可以与多个预处理器一起使用。对于姿态，`DWPreprocessor` 非常有效，通常比 `OpenPose 预处理器` 产生更好的结果。

## [Canny 边缘](./canny.json)

在资源使用方面，**canny** 是一种极其有效且经济的方法。预处理器将图像转换为原始图像的简化"涂鸦"，可用作新构图的参考。

![canny](./images/canny.jpg)

## [深度](./depth.json)

深度 controlnet 是一个非常有效的 controlnet，它允许您在 3D 空间中定义形状和体积。深度图的一个很好的预处理器是 **Zoe**。

:point_right: **注意：** 只要您有正确的参考图像，就不一定要使用预处理器。如果您使用 Blender，有一个[非常有趣的工具](https://toyxyz.gumroad.com/l/ciojz)。[PoseMy.Art](https://posemy.art/) 让您可以使用易于使用的界面创建角色。[Cascadeur](https://cascadeur.com/) 是另一个用于角色摆姿势的专业解决方案。

:bulb: **提示：** 为了获得更好的结果，请记住您始终可以链接多个 controlnet。查看下面的 [实验](#experiments)。

:bulb: **提示：** 记得调整 `Apply ControlNet` 节点的强度。降低强度通常是一个好主意，以便给模型一些回旋余地。

:warning: **重要：** controlnet 必须与您使用的检查点版本匹配。对于 SDXL，您需要专门为其训练的 controlnet，v1.5 和 2.1 也是如此。

# 实验

## [多个 ControlNet](./experiments/multiple_controlnets.json)

当然可以链接多个 controlnet。在这个示例中，我们使用 **openpose** 来摆角色姿势，使用 **shuffle** 来增加构图的趣味性。