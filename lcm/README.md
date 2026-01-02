# LCM 示例

LCM 模型是旨在用非常少的步骤进行采样的特殊模型。

### LCM Lora

LCM loras 是可以用来将常规模型转换为 LCM 模型的 loras。

LCM SDXL lora 可以从[这里](https://huggingface.co/latent-consistency/lcm-lora-sdxl/blob/main/pytorch_lora_weights.safetensors)下载

下载它，将其重命名为：lcm_lora_sdxl.safetensors 并将其放入您的 ComfyUI/models/loras 目录。

然后您可以在 ComfyUI 中加载此图像以获取工作流，该工作流展示了如何将 LCM SDXL lora 与 SDXL 基础模型一起使用：

![示例](lcm_basic_example.png)

重要的部分是使用低 cfg，使用"lcm"采样器和"sgm_uniform"或"simple"调度器。将 lcm 设置为采样选项的 ModelSamplingDiscrete 节点会稍微改善结果，因此也推荐使用，但并不总是必要的。

其他 LCM loras 可以在其各自的模型上以完全相同的方式使用。
