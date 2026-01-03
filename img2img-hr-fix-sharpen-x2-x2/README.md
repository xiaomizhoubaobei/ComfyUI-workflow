# wyrde img2img-hr-fix-sharpen-x2-x2

使用 WAS 节点。https://github.com/WASasquatch/was-node-suite-comfyui

获取图像并
* 将其调整为 512x768
* 使用双三次缩放将其放大 x2
* 对其进行高分辨率修复采样
* 使用模型放大 x4（现在是原始大小的 x8），然后再次缩小以获得 2048x3072 的最终结果

值可以轻松更改。

模型
* https://civitai.com/models/8281/perfect-world

放大
* Lollypop https://drive.google.com/u/1/uc?id=10h8YXKKOQ61ANnwLjjHqXJdn4SbBuUku&export=download

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main


<p align="right"><a href="..">[返回]</a><a href="../../../.."> [首页]</a></p>