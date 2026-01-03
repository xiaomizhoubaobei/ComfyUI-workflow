# 多采样像素空间锐化
我觉得这是一个很好的名字。不确定。

<img src="multi-sample-pixel-space-sharpening.png" width="90%">

从文本提示词获取图像并
* 采样它
* 使用模型放大
* 重新采样
* 重复
* 最后，使用 4x 放大模型再次增加大小
* 以总共 x8 的大小保存它

基本上是一系列高分辨率修复然后是模型放大

移动连线在模型 VAE 和 VAE 加载器之间切换。

## 示例

## 变体

* [使用潜空间放大](../multi-sample-sharpening/)
* [使用标准图像放大节点](./multi-sample-pixel-space-sharpening-b.json)
* [一个图像尺寸较小的快速版本](./multi-sample-pixel-space-sharpening-c.json) 用于"检查一下"之类的事情。
* [调整了图像大小，添加了 img2img 节点，清理了一些线条和节点](./multi-sample-pixel-space-sharpening-d.json)<br>
<img src="multi-sample-pixel-space-sharpening-d.png" width="90%" align="middle">

* [保存文件名前缀节点](./multi-sample-pixel-space-sharpening-e.json)
* [使用平铺 K 采样器和平铺 VAE](./multi-sample-pixel-space-sharpening-tiled.json)
  * 需要 blenderneko 的[平铺 K 采样器](https://github.com/BlenderNeko/ComfyUI_TiledKSampler)
  * 还包括最新版本的自定义文件夹/前缀替换

## 资源

WAS 节点
* https://github.com/WASasquatch/was-node-suite-comfyui

平铺 K 采样器
* https://github.com/BlenderNeko/ComfyUI_TiledKSampler

模型
* https://civitai.com/models/8281/perfect-world

放大
* Lollypop https://drive.google.com/u/1/uc?id=10h8YXKKOQ61ANnwLjjHqXJdn4SbBuUku&export=download
* PSNR https://drive.google.com/drive/folders/1ldwajXL50uC7PCS63B4Wato6Dnk-svNL

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative

## 致谢
来自 davemane42 的原始工作流
<img src="../multi-sample-sharpening/davemane2 ComfyUI_01275_.png" width="20%" align="middle">
* 基于 reddit 帖子 https://www.reddit.com/r/StableDiffusion/comments/124xv9v/paradise_and_stone/



<p align="right"><a href="..">[返回]</a><a href="../../../.."> [首页]</a></p>