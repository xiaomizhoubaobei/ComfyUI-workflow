# wyrde 多采样锐化与模型放大

<img src="wyrde multi sample sharpening w model upscale.png" width="90%">

从文本提示词获取图像并
* 采样它
* 潜空间放大
* 重新采样
* 重复
* 使用 4x 放大模型再次增加大小
* 以总共 x8 的大小保存它

基本上是一系列高分辨率修复然后是模型放大

移动连线在模型 VAE 和 VAE 加载器之间切换。

## 示例
第 1 代：512x512
<img src="ComfyUI_00012_.png" width="33%" align="middle">

第 2 代：640x640
<img src="ComfyUI_00013_.png" width="33%" align="middle">

第 3 代：768x768
<img src="ComfyUI_00014_.png" width="33%" align="middle">

第 4 代 1024x1024
<img src="latent upscale wf_00003_.png" width="33%" align="middle">

然后图像使用 lollypop x4 模型放大（未显示，因为 26mb 图像）

## 变体
更改调度器和采样器（更不用说模型）可以显着改变结果

* 将调度器更改为正常
* 步骤更改为 12
<img src="latent upscale wf_00009_.png" width="33%" align="middle">

* 切换到常规 VAE 解码
<img src="std vaedecode latent upscale wf_00011_.png" width="33%" align="middle">

* Dreamshaper 模型
<img src="dreamshaper latent upscale wf_00013_.png" width="33%" align="middle">

## 资源

WAS 节点
* https://github.com/WASasquatch/was-node-suite-comfyui

模型
* https://civitai.com/models/8281/perfect-world

放大
* Lollypop https://drive.google.com/u/1/uc?id=10h8YXKKOQ61ANnwLjjHqXJdn4SbBuUku&export=download

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main

## 致谢
来自 davemane42 的原始工作流
<img src="davemane2 ComfyUI_01275_.png" width="20%" align="middle">
* https://www.reddit.com/r/StableDiffusion/comments/124xv9v/paradise_and_stone/