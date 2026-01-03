# 使用令牌生成随机值

使用了 [WAS 节点](https://github.com/WASasquatch/was-node-suite-comfyui) 和 omar 的 [QoL 节点](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92)
* WAS 节点对于此示例是必需的
* omar 的"文本 _O"节点可以删除，它们是注释和说明。
* omar 的按因子潜空间放大节点可以用任何潜空间放大替换。

<img src="./token random values example.png" align="middle" width="90%">

创建令牌，然后从列表框中为其分配随机值。
<img src="./token nodes 1.png" align="middle" width="50%">

令牌名称放置在文本框中。列表框的内容发送到条件。
<img src="./token nodes 3.png" align="middle" width="50%">

为什么要这样做而不是使用{花括号}？
* 在 ComfyUI 中，{花括号 | 用 | 管道分隔 | 的单词 | 用于}生成随机结果。由于 ComfyUI 的功能方式，图像的工作流将仅包含为图像评估的提示词中的项目。随机列表的其余部分将被丢弃。

为什么要文本连接？
* 由于后端评估文本框的方式，它在解析提示词时不知道令牌的内容已更改。有两种方法可以解决这个问题：
  * 在提示词中放入 `{ | | }`。它每次都会评估空格并运行提示词，从而也评估令牌。
  * 创建一个新的多行节点→随机行节点→文本连接（随机结果和提示词）→文本解析令牌→文本到条件
    * 这更复杂，但在图像工作流中保留了文本提示。

<!-- <img src="some image" align="middle"> -->


## 示例结果

* <img src="example-prefix_00008_.png" width="25%" align="middle"><img src="example-prefix_00009_.png" width="25%" align="middle">
* <img src="example-prefix_00010_.png" width="25%" align="middle"><img src="example-prefix_00011_.png" width="25%" align="middle">
* <img src="example-prefix_00012_.png" width="25%" align="middle"><img src="example-prefix_00013_.png" width="25%" align="middle">
* <img src="example-prefix_00014_.png" width="25%" align="middle"><img src="example-prefix_00015_.png" width="25%" align="middle">

<!-- <img src="" width="10%" align="middle"> -->

## 资源

<!-- 人们可能想要复制结果的东西 -->

模型
* https://huggingface.co/Vsukiyaki/SukiyakiMix-v1.0

LoRA
* https://civitai.com/models/21458/anime-kisses
* https://civitai.com/models/21670/astrobabes
* https://civitai.com/models/25803/battle-angels

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main

自定义节点
* [WAS 套件](https://github.com/WASasquatch/was-node-suite-comfyui)
* [omar QoL](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92)

<!-- 可能会忘记仔细检查这一点 -->
<p align="right"><a href="..">[返回]</a><a href="../../../.."> [首页]</a></p>