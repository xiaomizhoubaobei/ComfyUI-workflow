# wyrde 的非常复杂的多潜空间修复和摆弄

广泛使用了 [WAS 节点](https://github.com/WASasquatch/was-node-suite-comfyui)
* 安装 WAS 套件以避免一堆红色框的混乱。

<img src="workflow smaller.png" align="middle">

## 这个工作流的目标是三重的
* 生成一系列图像，SD 重复采样。
  * 它们倾向于缓慢改进，但有时会有剧烈变化
* 使用具有高度随机性的提示词
  * 人物、头发、耳朵和服装。可以以这些为例随机化更多元素。
* 使完整的提示词可以与结果图像共享
  * 在 ComfyUI 中，{花括号 | 用 | 管道分隔 | 的单词 | 用于}生成随机结果。由于 ComfyUI 的功能方式，图像的工作流将仅包含为图像评估的提示词中的项目。其他随机元素将被丢弃。


## 工作流
* 从几个随机列表生成文本提示词
* 各部分连接在一起
* 提示词被采样
* 再次采样
* 再次采样——10 次
* 切换宽高比
* 再次执行所有操作。
* 总共输出是 20 张图像

末尾的大框有备用节点，便于复制粘贴

包括一些 LoRA。还有一些地方，移动连线会改变生成。

## 示例结果
* 肖像行

<img src="img/multi latent chain_00084_.png" width="10%"><img src="img/multi latent chain_00086_.png" width="10%"><img src="img/multi latent chain_00087_.png" width="10%"><img src="img/multi latent chain_00088_.png" width="10%"><img src="img/multi latent chain_00089_.png" width="10%"><img src="img/multi latent chain_00090_.png" width="10%"><img src="img/multi latent chain_00091_.png" width="10%"><img src="img/multi latent chain_00092_.png"  width="10%"><img src="img/multi latent chain_00093_.png" width="10%"><img src="img/multi latent chain_00094_.png" width="10%">

* 风景行

<img src="img/multi latent chain_00085_.png" width="18%"><img src="img/multi latent chain_00095_.png" width="18%"><img src="img/multi latent chain_00096_.png" width="18%"><img src="img/multi latent chain_00097_.png" width="18%"><img src="img/multi latent chain_00098_.png" width="18%">
<img src="img/multi latent chain_00099_.png" width="18%"><img src="img/multi latent chain_00100_.png" width="18%"><img src="img/multi latent chain_00101_.png"  width="18%"><img src="img/multi latent chain_00102_.png" width="18%"><img src="img/multi latent chain_00103_.png" width="18%">

<!-- <img src="" width="10%"> -->

## 资源

模型
* https://civitai.com/models/4384/dreamshaper

LoRA
* https://civitai.com/models/8858/maplestory2game-chibi-style-hn
* https://civitai.com/models/21670/astrobabes
* https://civitai.com/models/25803/battle-angels

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main