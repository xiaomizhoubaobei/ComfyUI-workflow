# 区域组合示例

这些示例演示了 ConditioningSetArea 节点。您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载这些图像以获取完整的工作流。

### 使用 Anything-V3 进行区域组合 + 使用 AbyssOrangeMix2_hard 进行第二遍

此图像包含 4 个不同的区域：夜晚、傍晚、白天、早晨

![示例](night_evening_day_morning.png)

这是工作流在 ComfyUI 中的样子：

![示例](workflow_night_evening_day_morning.png)

此图像包含与前一个相同的区域，但顺序相反。

![示例](morning_day_evening_night.png)

通过添加另一个区域提示在图像底部中心添加一个主体。

![示例](night_evening_day_morning_subject.png)


## 使用区域组合提高图像一致性

Stable diffusion 在生成接近 512x512 分辨率的方形图像时创建最一致的图像。但是如果我们想要生成 16:9 纵横比的图像呢？
让我们生成一个带有坐着主体的 16:9 图像。如果正常生成，成功率会很低，肢体不自然地延伸到整个图像以及其他一致性问题。

通过使用区域组合为主体提供方形区域，一致性会更高，并且由于它与图像的其余部分同时生成，因此整体图像的一致性将非常出色。

此工作流使用 Anything-V3，它是一个 2 遍工作流，在第一遍中使用区域组合处理图像左侧的主体。第二遍的原因只是为了提高分辨率，如果您对 1280x704 的图像满意，可以跳过第二遍。

![示例](square_area_for_subject.png)

通过在图像右侧的区域提示添加一个红发主体。

第一遍输出（1280x704）：

![示例](square_area_for_2_subjects_first_pass.png)

第二遍输出（1920x1088）：

![示例](square_area_for_2_subjects.png)

此第二遍输出图像说明了 Stable Diffusion 的行为之一。第二遍没有区域提示。您会注意到主体 1 的头发是金色的带有粉红色高光，而主体 2 的头发是粉红色的而不是红发，这与第一遍输出中的情况不同。这是因为 Stable Diffusion 试图使整体图像与自身一致，其中一个副作用是将头发颜色合并在一起。

