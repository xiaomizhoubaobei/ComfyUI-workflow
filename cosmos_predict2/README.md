# Nvidia Cosmos Predict2

这是来自 Nvidia 的一系列文本转图像和图像转视频模型。

## 需要下载的文件

您首先需要：

#### 文本编码器和 VAE：

[oldt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/cosmos_1.0_text_encoder_and_VAE_ComfyUI/tree/main/text_encoders) 放入：ComfyUI/models/text_encoders/

[wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/vae/wan_2.1_vae.safetensors) 放入：ComfyUI/models/vae/


注意：oldt5_xxl 与 flux 和其他模型中使用的 t5xxl 不同。
oldt5_xxl 是 t5xxl 1.0，而 flux 和其他模型中使用的是 t5xxl 1.1


您可以在这里找到所有扩散模型（放入 ComfyUI/models/diffusion_models/）：[重新打包的 safetensors 文件](https://huggingface.co/Comfy-Org/Cosmos_Predict2_repackaged/tree/main) 或 [官方 Nvidia 模型文件](https://huggingface.co/collections/nvidia/cosmos-predict2-68028efc052239369a0f2959)


## 工作流

### 文本转图像

此工作流使用 2B 文本转图像 cosmos predict2 模型。工作流中使用的文件是 [cosmos_predict2_2B_t2i.safetensors](https://huggingface.co/Comfy-Org/Cosmos_Predict2_repackaged/blob/main/cosmos_predict2_2B_t2i.safetensors)，此文件放入：ComfyUI/models/diffusion_models/

![示例](cosmos_predict2_2b_t2i_example.png)

您可以在 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 中加载此图像以获取完整的工作流。

我认为 2B 模型是最有趣的，但您可以在这里找到更大的 14B 模型：[cosmos_predict2_14B_t2i.safetensors](https://huggingface.co/Comfy-Org/Cosmos_Predict2_repackaged/blob/main/cosmos_predict2_14B_t2i.safetensors) 并在上面的工作流中使用它。


### 图像转视频

这些模型对视频的分辨率/长度非常挑剔。此工作流适用于 480p 模型，对于 720p 模型，您必须将分辨率设置为 720p，否则结果可能会很差。

此工作流使用 2B 图像转视频 cosmos predict2 模型。工作流中使用的文件是 [cosmos_predict2_2B_video2world_480p_16fps.safetensors](https://huggingface.co/Comfy-Org/Cosmos_Predict2_repackaged/blob/main/cosmos_predict2_2B_video2world_480p_16fps.safetensors)，此文件放入：ComfyUI/models/diffusion_models/

![示例](cosmos_predict2_2b_i2v_example.webp)

[Json 格式的工作流](cosmos_predict2_2b_i2v_example.json)


