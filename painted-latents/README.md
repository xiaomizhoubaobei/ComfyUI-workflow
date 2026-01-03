# 潜空间绘画的乐趣

<img src="painted-latent-v12.png" align="middle">
<a href="painted-latent-v12.json">painted-latent-v12</a>

## 绘制的潜空间

与其使用"常规"潜空间，不如使用被绘制或以其他方式操作的潜空间可以创建引人注目的构图。

这个工作流
* 根据提示词创建潜空间
* 掩码潜空间的一部分
* 使用主提示词根据潜空间生成图像
* 通过几个步骤对图像进行高分辨率修复

## 示例结果

* wyrde  
<img src="img/wyrde-painted-latent-v12_00004_.png" width="15%" align="middle"><img src="img/wyrde-painted-latent-v12_00007_.png" width="15%" align="middle"><img src="img/wyrde-painted-latent-v12_00010_.png" width="15%" align="middle"><img src="img/wyrde-painted-latent-v12_00014_.png" width="15%" align="middle"><img src="img/wyrde-painted-latent-v12_00015_.png" width="15%" align="middle"><img src="img/wyrde-painted-latent-v12_00016_.png" width="15%" align="middle"><img src="img/wyrde-painted-latent-v12_00017_.png" width="15%" align="middle"><img src="img/wyrde-painted-latent-v12_00018_.png" width="15%" align="middle">
 
* tjhayasaka  
<img src="img/tjhayasaka fairy_endlessreality_00033_.png" width="15%" align="middle"><img src="img/tjhayasaka coral-peacock_endlessreality_00001_.png" width="15%" align="middle">

* M1r077  
<img src="img/M1r077 coral-peacock_endlessreality_00046_.png" width="15%" align="middle"><img src="img/M1r077 coral-peacock_endlessreality_00040_.png" width="15%" align="middle"><img src="img/M1r077 coral-peacock_endlessreality_00032_.png" width="15%" align="middle"><img src="img/M1r077 coral-peacock_endlessreality_00084_.png" width="15%" align="middle"><img src="img/M1r077 coral-peacock_endlessreality_00041_.png" width="15%" align="middle"><img src="img/M1r077 coral-peacock_endlessreality_00004_.png" width="15%" align="middle">

## 实验

* 将潜空间的种子设置为随机，以便每次运行都有新的潜空间
* 更改潜空间大小
* 更改掩码大小
* 不同的模型和 VAE
* 添加 LoRA 和嵌入/文本反转

## 资源

<!-- 人们可能想要复制结果的东西 -->

模型
* https://civitai.com/models/7371

放大
* https://drive.google.com/drive/folders/1ldwajXL50uC7PCS63B4Wato6Dnk-svNL
* https://drive.google.com/u/1/uc?id=10h8YXKKOQ61ANnwLjjHqXJdn4SbBuUku&export=download

VAE：  
* https://huggingface.co/stabilityai/sd-vae-ft-mse-original/tree/main

嵌入  
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main