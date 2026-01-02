# Mochi 视频模型

[Mochi](https://huggingface.co/genmo/mochi-1-preview) 是一个最先进的视频模型。

您可以在[这里](https://huggingface.co/Comfy-Org/mochi_preview_repackaged/tree/main/split_files)找到以下工作流的所有模型文件

```
diffusion_models/mochi_preview_bf16.safetensors 放入：ComfyUI/models/diffusion_models/
text_encoders/t5xxl_fp16.safetensors 放入：ComfyUI/models/text_encoders/
vae/mochi_vae.safetensors 放入：ComfyUI/models/vae/
```

如果您有内存问题，可以选择 fp8 文件而不是 bf16/fp16 文件。

![示例](mochi_text_to_video_example.webp)

您可以下载这个 webp 动画图像并加载它，或者将其拖到 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 上以获取工作流。


还有一个一体化的 fp8 检查点[在这里](https://huggingface.co/Comfy-Org/mochi_preview_repackaged/blob/main/all_in_one/mochi_preview_fp8_scaled.safetensors)，它包含上述工作流中文件的 fp8 版本，打包在一个检查点中。

请注意，使用 fp8 文件将比使用 16 位文件提供更低的质量，但可能会更快，特别是如果您有支持 fp8 操作的 GPU。

以下是使用它的工作流：

![示例](mochi_simple_checkpoint.webp)

