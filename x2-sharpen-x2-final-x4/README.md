# wyrde 高分辨率修复模型放大 x2 x2（x4 最终）

包括 WAS 节点。https://github.com/WASasquatch/was-node-suite-comfyui

从文本提示词（或图像）获取图像并
* 采样它
* 使用放大模型将大小加倍
* 通过采样器对图像进行高分辨率修复
* 使用 4x 放大模型再次增加大小
* 以总共 x4 的大小保存它

包括几个 LoRA。还有一些地方，移动连线会改变生成。

## 资源

模型
* https://civitai.com/models/8281/perfect-world

LoRA
* https://civitai.com/models/17892/cat-lingerie
* https://civitai.com/models/16687/butterfly-wings

放大
* PSNR https://drive.google.com/drive/folders/1ldwajXL50uC7PCS63B4Wato6Dnk-svNL
* Lollypop https://drive.google.com/u/1/uc?id=10h8YXKKOQ61ANnwLjjHqXJdn4SbBuUku&export=download

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main


<p align="right"><a href="..">[返回]</a><a href="../../../.."> [首页]</a></p>