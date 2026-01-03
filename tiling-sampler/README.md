# 平铺采样示例

使用了 blenderneko 的[平铺 K 采样器节点](https://github.com/BlenderNeko/ComfyUI_TiledKSampler)

<!--
<img src="some image" align="middle">
-->

## 目的

这个工作流使用平铺采样在高分辨率修复中对大图像进行采样。平铺 K 采样器类似于高级 K 采样器节点，因此与"标准"K 采样器有一些重要区别。
* 去噪通过相对于总步数的开始和停止步数来处理。
* 使用 30 步，从第 15 步开始到第 30 步结束（15 步）相当于 0.500 去噪。
* 平铺宽度和高度应该是 GPU 可以合理处理的最大尺寸。
  * 将这些值设置得太低可能会导致额外的伪影和噪声

## 版本

## 示例结果

* 图像  
<img src="img/sampler-1A_00005_.png" width="20%" align="middle"><img src="img/sampler-1B_00005_.png" width="20%" align="middle">  
<img src="img/sampler-2A_00005_.png" width="20%" align="middle"><img src="img/sampler-2B_00005_.png" width="20%" align="middle"><img src="img/sampler-2C_00005_.png" width="20%" align="middle">  
<img src="img/sampler-3A_00005_.png" width="20%" align="middle"><img src="img/sampler-3B_00005_.png" width="20%" align="middle">

当平铺大小太小时：  
<img src="img/sampler-3A_00005b_.png" width="20%" align="middle">


<!-- <img src="img/" width="10%" align="middle"> -->

## 资源

<!-- 人们可能想要复制结果的东西 -->

模型
* https://civitai.com/models/21916/

自定义节点
* [blenderneko 的平铺 K 采样器节点](https://github.com/BlenderNeko/ComfyUI_TiledKSampler)