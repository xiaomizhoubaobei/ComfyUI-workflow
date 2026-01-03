# wyrde 的 4 提示词比较

使用了 [WAS](https://github.com/WASasquatch/was-node-suite-comfyui) 和 [omar](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92) 节点。
* 安装套件以避免一堆红色框的混乱。

<img src="compare-prompt-diff-x4-v0.4.png" align="middle">

## 比较事物

稳定扩散可能很奇怪。有时用漂亮的图片来检查这种奇怪之处会有所帮助。这个工作流使用相同的设置运行 4 个不同的提示词，并输出图像结果。

利用了文本框、连接和命令行输出。

## 提示词中的标点符号

### 启用 xformers
 | 提示词 A | 提示词 B | 提示词 C | 提示词 D
 |:----:|:----:|:----:|:----:|
 |`Is, This, Different, Than` | `Is; This; Different; Than` | `Is: This: Different: Than` | `Is. This. Different. Than` |
 | <img src="./img/compare-prompt-diff-x4_00009_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00010_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00011_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00012_.png"   align="middle">

### 禁用 xformers
 | 提示词 A | 提示词 B | 提示词 C | 提示词 D
 |:----:|:----:|:----:|:----:|
 |`Is, This, Different, Than` | `Is; This; Different; Than` | `Is: This: Different: Than` | `Is. This. Different. Than` |
 | <img src="./img/compare-prompt-diff-x4_00013_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00014_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00015_.png"   align="middle"> | <img src="./img/compare-prompt-diff-x4_00016_.png"   align="middle">

<details>
  <summary>$\color{pink}{禁用\ xformers}$</summary>
要禁用 xformers：
* Windows 便携式独立版
  * 在文件 `run_nvidia_gpu.bat` 中的 `.\python_embeded\python.exe -s ComfyUI\main.py` 之后添加 ` --disable-xformers`
  * 所以它看起来像
  * `.\python_embeded\python.exe -s ComfyUI\main.py --disable-xformers`
* github 克隆版
  * 在启动命令中添加 ` --disable-xformers`。
  * `python .\main.py --disable-xformers`
</details>

----

## 文本反转（嵌入）

ComfyUI 中是否需要文本反转的"触发词"？

### 风格公主

[风格公主](https://civitai.com/models/3485/princess-style)

 | 提示词 A | 提示词 B | 提示词 C | 提示词 D
 |:----:|:----:|:----:|:----:|
 | `girl in a sunset style-princess` | `girl in a sunset embedding:style-princess style-princess` | `girl in a sunset embedding:style-princess` | `girl in a sunset`
 |<img src="img/compare-prompt-diff-x4_00017_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00018_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00019_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00020_.png"  align="middle">|

### GNTZ

[风格 GNTZ](https://civitai.com/models/22544/gntz)

 | 提示词 A | 提示词 B | 提示词 C | 提示词 D
 |:----:|:----:|:----:|:----:|
 | `girl in a sunset gntz` | `girl in a sunset embedding:gntz gntz` | `girl in a sunset embedding:gntz`  | `girl in a sunset` |
 |<img src="img/compare-prompt-diff-x4_00024_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00025_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00026_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00027_.png"  align="middle">|

结论：不需要，但它们确实增加了重要性。

----

## LoRA 和关键词

 | 提示词 A | 提示词 B | 提示词 C | 提示词 D
 |:----:|:----:|:----:|:----:|
 |`girl in a sunset `|`girl in a sunset `|`girl in a sunset holding_sign`|`girl in a sunset`|
 | 无 LoRA | LoRA 1,1 | LoRA 1,1 | LoRA 0,0 |
 |<img src="img/compare-prompt-diff-x4_00043_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00044_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00045_.png"  align="middle">|<img src="img/compare-prompt-diff-x4_00046_.png"  align="middle">|

* 使用 [动漫女孩举牌](https://civitai.com/models/42621/) 测试
  * 这是一个很好的测试 LoRA，因为当它工作时很明显
* [比较 LoRA 工作流](compare-prompt-diff-x4-v0.8-lora.json)

<!-- <img src=""  align="middle"> -->

----


## 资源

<!-- 人们可能想要复制结果的东西 -->

模型
* animatrix https://civitai.com/models/21916/animatrix

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main

自定义节点
* [WAS 套件](https://github.com/WASasquatch/was-node-suite-comfyui)
* [omar QoL 套件](https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92)

<!-- 可能会忘记仔细检查这一点 -->
<p align="right"><a href="..">[返回]</a><a href="../../../.."> [首页]</a></p>