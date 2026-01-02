# Omnigen 2

[Omnigen 2](https://github.com/VectorSpaceLab/OmniGen2) 是一个可以用文本提示编辑图像的模型。

## 需要下载的文件

您首先需要：

[omnigen2_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/blob/main/split_files/diffusion_models/omnigen2_fp16.safetensors) 放入：ComfyUI/models/diffusion_models/

[qwen_2.5_vl_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/blob/main/split_files/text_encoders/qwen_2.5_vl_fp16.safetensors) 放入：ComfyUI/models/text_encoders/

[ae.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/blob/main/split_files/vae/ae.safetensors)，这是您可能已经拥有的 flux VAE，放入：ComfyUI/models/vae/

## 工作流

这是一个使用图像作为角色参考的基本工作流。对于多个图像输入，将 ReferenceLatent 节点链接在一起。

![示例](omnigen2_example.png)

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载此图像以获取完整的工作流。

您可以在[这里](../images/fennec_girl_sing.png)找到输入图像

