# 视频示例

## 图像转视频

在撰写本文时，有两个图像转视频的检查点。这里是[用于生成 14 帧视频的模型](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid/blob/main/svd.safetensors)和[用于生成 25 帧视频的模型](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/main/svd_xt.safetensors)的官方检查点。将它们放入 ComfyUI/models/checkpoints 文件夹中。


使用图像转视频模型最基本的方法是给它一个初始图像，就像下面这个使用 14 帧模型的工作流一样。
您可以下载这个 webp 动画图像并加载它，或者将其拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 上以获取工作流。

![示例](image_to_video.webp)
[Json 格式的工作流](workflow_image_to_video.json)

如果您想要确切的输入图像，可以在 [unCLIP 示例页面](../unclip) 上找到它

您也可以像在这个工作流中那样使用它们，该工作流使用 SDXL 生成初始图像，然后将其传递给 25 帧模型：

![示例](txt_to_image_to_video.webp)
[Json 格式的工作流](workflow_txt_to_img_to_video.json)

#### 参数说明：

video_frames：要生成的视频帧数。

motion_bucket_id：数值越高，视频中的运动越多。

fps：fps 越高，视频越流畅。

augmentation level：添加到初始图像的噪声量，数值越高，视频看起来越不像初始图像。增加它以获得更多运动。

VideoLinearCFGGuidance：这个节点稍微改进了这些视频模型的采样，它的作用是在不同帧之间线性缩放 cfg。在上面的示例中，第一帧的 cfg 为 1.0（节点中的 min_cfg），中间帧为 1.75，最后一帧为 2.5。（采样器中设置的 cfg）。这样，距离初始帧越远的帧会获得逐渐更高的 cfg。
