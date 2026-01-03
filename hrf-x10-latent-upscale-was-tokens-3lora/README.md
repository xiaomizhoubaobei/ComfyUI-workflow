# wyrde 的非常复杂的多潜空间高分辨率修复和缩放

广泛使用了 [WAS 节点](https://github.com/WASasquatch/was-node-suite-comfyui)
* 安装 WAS 套件以避免一堆红色框的混乱。

<img src="wyrde-hrf-x10-latent-upscale-was-random-3lora-v1.0.png" align="middle">

## 原理

基于一个[非常复杂的多潜空间修复和摆弄](../random-prompt-hrf-20img-output/)工作流。

WAS 好心地编写了一个巧妙的节点，允许通过 ascii/文本节点设置令牌。这大大简化了以前工作流中的随机提示词生成。

所以，当然，我**不得不**让它更复杂。

这个工作流
* 生成一系列图像，SD 重复采样。
  * 它们倾向于缓慢改进，但有时会有剧烈变化
  * 图像然后被高分辨率修复和放大
* 使用具有高度随机性的提示词
  * 人物、头发、耳朵和服装。可以以这些为例随机化更多元素。
  * 值从列表中选取，然后分配给令牌。令牌然后可以在其他区域中评估。
* 像以前一样，我希望所有提示词数据都与图像共享。
  * 在 ComfyUI 中，{花括号 | 用 | 管道分隔 | 的单词 | 用于}生成随机结果。由于 ComfyUI 的功能方式，图像的工作流将仅包含为图像评估的提示词中的项目。其他随机元素将被丢弃。


## 工作流
* 从几个随机列表生成文本提示词
* 各部分分配给令牌。
* 提示词被采样并评估令牌
* 再次采样
* 再次采样——总共 10 次。
* 然后对结果样本进行高分辨率修复和放大。

整个过程在我的 1060gtx 上大约需要 30 分钟

包括一些 LoRA。还有一些地方，移动连线会改变生成。

## 版本
* v1.0 - 很乱，你懂的
* v1.1 - 添加了 img2img 节点，清理了线条，更好的分组

## 示例结果

最终，我累了。

<!-- <img src="" width="10%"> -->

## 特别说明
由于后端评估文本框的方式，它在解析提示词时不知道令牌的内容已更改。有两种方法可以解决这个问题：
* 在提示词中放入 `{ | | }`。它每次都会评估空格并运行提示词，从而也评估令牌。
* 创建一个新的多行节点→随机行节点→文本连接（随机结果和提示词）→文本解析令牌→文本到条件
  * 这更复杂，但在图像工作流中保留了文本提示。
<img src="text concatenate image.png" align="middle">

## 资源

我需要更改这些以匹配。明天会做。

模型
* https://civitai.com/models/4384/dreamshaper

LoRA
* https://civitai.com/models/8858/maplestory2game-chibi-style-hn
* https://civitai.com/models/21670/astrobabes
* https://civitai.com/models/25803/battle-angels

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main


<p align="right"><a href="..">[返回]</a><a href="../../../.."> [首页]</a></p>