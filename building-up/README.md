# 基础构建

一系列用于教授 ComfyUI 基础知识的工作流。

## 开始

* <a href="basic-workflow-v03.json">基础工作流 .json 文件</a>  
<img src="./pix/basic-workflow-v03.png" align="middle">

一旦 ComfyUI 安装并运行，添加工作流就像将图像或 ComfyUI 创建的工作流拖放到浏览器窗口的空白区域一样简单。

要跟随本教程，请下载[该工作流](https://raw.githubusercontent.com/wyrde/wyrde-comfyui-workflows/main/basics/building-up/basic-workflow-v03.json)并保存。然后使用 ComfyUI 中的 `[  Load  ]` 按钮加载它。

这个基础工作流根据正面和负面提示词生成图像。
* 处理从"检查点"开始，由左侧的**加载检查点**节点加载。
* 来自检查点的信息通过节点路径和模型路径发送到两个 CLIP 框。
* 附加到**KSampler** 正面输入的 CLIP 文本编码节点在正面提示词中。
* 附加到**KSampler** 负面输入的 CLIP 文本编码节点在负面提示词中。
* **空潜空间图像**是"起始图像"，是一块空白噪声。就像画家的画布。
* 模型是 Stable Diffusion 通过**KSampler**将噪声解析为图像所使用的所有原始信息。
* 我不知道**VAE**是什么，但它们很重要。
  * 所有模型都包含一个 VAE，但并非所有模型都有好的 VAE。
  * 可以通过 VAE 加载器将外部 VAE 添加到工作流中（见下文）。
* **KSampler**节点有许多选项。我不会在这里详细介绍所有选项，但目前最重要的是：
  * 种子是用于随机性的数字。在其他条件相同的情况下，具有相同种子的工作流将生成相同的图像。
  * 如果种子没有改变且其他任何东西都没有改变，ComfyUI 甚至不会处理工作流。结果与上次相同。如果其他任何东西都没有改变但种子改变了，则会生成新图像。它们可能彼此之间差异很大。
  * 这使得很容易判断是否没有任何变化。
  * 种子下方的行是如何生成新种子的。
    * 固定：不生成。种子保持不变。用于检查其他参数并生成相同的基本图像。
    * 递增/递减：种子变化 +/- 1。
    * 随机：数字不断变化，蝙蝠侠！
  * 通过单击箭头滚动选项或直接单击值以查看列表来更改值。

在生成图像之前，需要一个模型。继续选择 `v1-5-pruned-emaonly.safetensors`
* 什么，没有它？好吧，从[这里获取](https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main)。
* 不要单击文件名，它会引导到网页。单击右侧下载文件。<img src="./pix/dlv15.png" width="80%" align="middle">
* 将文件放在 `ComfyUI\models\checkpoints\` 中

单击窗口侧面框中的"队列提示"以生成图像。如果使用上述工作流的相同设置，它看起来非常像  
<img src="./pix/ComfyUI_00335_.png" width="20%" aligh="middle">
* 如果不是，那么，嗯，哎呀？
* 如果屏幕上有错误，那么可能没有选择模型
  * 或者连线断开了
* 如果控制台窗口有错误，那么其他地方有问题。

	
## 添加 VAE 加载器

* <a href="basic-workflow-vae-v03.json">工作流 + vae.json 文件</a>  
<img src="./pix/basic-workflow-vae-v03.png" align="middle">

添加节点主要有三种方式
  * 连线拖动
    * 左键单击并从节点的输出点拖动。会出现一条连线。
    * 将连线拖到一个好位置并松开。
    * 将出现一个包含相同类型节点的选择框。
  * 双击
    * 在空白处双击左键，将出现一个列表。
    * 滚动列表或开始输入以过滤它。
    * 选择所需的节点
  * 右键菜单
    * 在画布上的空白处右键单击
    * 出现上下文菜单
    * 左键单击添加节点以获取节点子菜单
    * 左键单击子菜单以获取所需节点的节点列表或更多菜单

对于 VAE 加载器
* 右键单击。添加节点 → 加载器 → 加载 VAE
* 双击左键，输入 VAEL 并选择它
* 可以从 VAE 解码节点的输入中拉出一条连线并放下以显示菜单中的 VAE 加载器，但这会很乱。让我们把混乱的工作流留给像 comfy 和 mike 这样的疯狂女巫。
* 继续放置一个 VAE

从 [stabilityai](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/tree/main) 下载 VAE 并将其放入 `ComfyUI\models\vae`。获取 pruned.safetensors 文件。
  * 不要单击文件名（这会导致一个令人困惑的页面，直到眼睛最终发现"下载"链接），单击右侧。<img src="./pix/downloadvae.png" width="75%" align="middle">。
  * 将文件放在 `ComfyUI\models\vae\` 中
  * 下载后，按 F5 刷新窗口，以便 Comfy 知道文件在那里。
  * 有一个 VAE，很容易通过单击箭头或列表在 VAE 加载器中选择它。

在这种特定情况下，创建一个链接了 VAE 的新版本并没有太大的区别。要了解 VAE 会产生什么差异，请查看[此比较](https://github.com/wyrde/wyrde-comfyui-workflows/tree/main/compare/model-vae)。那些有糟糕 VAE 的图像是褪色和暗淡的。好的 VAE 是鲜艳的。

注意
* Automatic1111 将 VAE 文件名与模型匹配并将它们放在模型文件夹中的方法对 ComfyUI 不重要。要么直接加载 VAE，要么使用模型内置的 VAE。
* [这里有一些关于 VAE 的好信息](https://rentry.org/sdvae)

## 添加 LoRA


* <a href="basic-workflow-vae-lora.json">工作流 + vae + lora.json 文件</a>  
<img src="./pix/basic-workflow-vae-lora.png" align="middle">

LoRA（及其变体）是很酷的迷你模型，用于改变更大的模型。把它们想象成特洛伊木马，但每个人都对结果感到满意。通常。

[这里有一个 LoRA](https://civitai.com/models/44960?modelVersionId=49584) 可以测试。将其放入 `ComfyUI\models\lora\` 文件夹。
* 与其他文件一样，按 F5 刷新文件列表
* 暂时忽略 LoRA 页面中的文本，首先看到的是针对 3.0 版本的，而我们使用的是 1 版本。

添加 LoRA 比 VAE 加载器稍微复杂一些，因为它们位于模型和 KSampler 之间。
* 与 automatic1111 不同，LoRA 不放在提示词中。

为 LoRA 加载器节点腾出一点空间。
* 在 CLIP 文本节点和加载检查点之间，按住控制键并用左鼠标按钮拖动。它将绘制一个框。释放左鼠标按钮时，框内的所有内容都将被选中。
* 现在按住 shift 并左键单击选定的节点之一。拖动鼠标时，所有节点都将作为一组拖动。
* 通过向右拖动节点而不是向左来腾出空间更好
* 刷新窗口会缩放到起始节点所在的几乎不可见的蓝色框。
* 一直向左平移变得很烦人

现在在空白处放一个 LoRA 加载器。
* 将加载检查点模型和 CLIP 输出连接到加载 LoRA。
  * 加载 LoRA 的模型输出转到模型重路由（到 KSampler 模型输入）
    * 这将自动将其从加载检查点分离。
  * 加载 LoRA 的 CLIP 输出通过连线连接到两个 CLIP 节点的输入。
    * 这将自动将其从加载检查点分离。
* 为 lora_name 字段选择 mPixel_v10pixelArt.safetensors。
* 将 strength_model 和 strength_clip 更改为 0.8

单击队列提示时，图像现在应该是一个像素艺术瓶子。  
<img src="./pix/ComfyUI_00344_.png" width="20%" align="middle">

## 高分辨率修复

所以，关于稳定扩散的一个重要事情是模型在小图像上训练。512x512 像素是大多数基于 SD1.5 的模型的标准尺寸（少数为 768）。SD2.x 模型可以是 512px 或 768px，取决于选择的模型。

但这对普通用户意味着什么？大多数人想要更大的图像（例如 1920x1080）。问题是，仅仅将潜空间图像大小更改为 1920x1080 往往会非常、非常错误。这是因为稳定扩散并不真正理解"大小"或"构图"。当它看到巨大的画布大小时，它会尝试用提示词填充它的每一部分。
* 具有先前提示词和配置以及 1920x1080 大小潜空间的图像：  
<img src="./pix/ComfyUI_00351_.png" width="10%" align="middle">

但不要害怕，有一些技术可以将图像大小从 512px 增加到更宏伟的大小。
* 潜空间放大：这获取潜空间图像并使其变大。结果还可以，但较大的图像缺少许多可能的细节。
* 像素空间放大：往往比潜空间放大看起来更好，但仍然缺少细节。
* 使用模型的像素空间放大：有专门为更好的放大结果设计的特殊模型。有些甚至可以推断细节。
* 高分辨率修复：通常缩写为 HR-Fix 或进一步缩写为 HRF，这种方法是上述许多方法的组合。它使用许多步骤，需要更长时间，但结果是高细节图像。还有一个额外的好处是稳定扩散甚至可以"修复"图像的损坏部分！有时。

这个潜空间与像素空间是什么？
* 潜空间是稳定扩散工作的混乱和随机区域。这些并不是人类眼睛看到的真正图像，而是计算机处理的数学魔法表示。
* 像素空间是实际图像，以像素渲染。人类眼睛和图形艺术程序喜欢处理的东西。
* VAE 解码和编码用于将潜空间图像转换为像素并返回。
* 某些过程只能在潜空间中完成（如 K 采样），而其他只能在像素空间中完成（颜色校正、模型放大）

HR 修复有一些注意事项。
* 尽可能多地使用小步骤。
* 坚持使用 64px 的倍数。这对于不同宽高比的图像可能具有挑战性。有一些自定义节点对此有帮助。
* 如果宽高比使得 64px 的倍数具有挑战性，请在像素空间中进行图像放大
  * 由于涉及的数学运算，即使那样，最好也使用 8 像素的倍数。
* 最好（也更快）通过许多低分辨率潜空间样本，然后进行大的像素放大。这为像素放大提供了大量细节。

但首先，让我们做一个基本的 HR-Fix。
* 在工作流的右侧，将 VAE 解码和保存图像节点向右移动（尝试也抓住底部的 VAE 重路由）。
  * 大约是它们当前占据的距离，也许多一点。
* 在 KSampler 旁边放一个放大潜空间节点
* 将 KSampler 上的 LATENT 输出连接到放大潜空间节点上的样本输入。
* 在放大潜空间和 VAE 解码之间放一个 KSampler 节点。
* 将放大潜空间节点上的 LATENT 输出连接到新 KSampler 节点上的潜空间图像输入。
* 将 KSampler 上的 LATEN 输出连接到 VAE 解码节点上的样本输入。
  * 这也将擦除从旧 KSampler 到 VAE 解码的连线
* 在放大潜空间节点上，将宽度和高度增加 64 像素。通过单击数字右侧的箭头很容易做到。

但是等等！我们还没完成。新的 KSampler 仍然有许多空输入。这是因为采样器需要知道如何处理潜空间图像。

看到挂在正面提示词角落的模型重路由了吗？
* 左键单击以激活它。
* Ctrl-C 克隆它。
* 将鼠标向右移动一点（在旧 KSampler 上方也可以）  
<img src="./pix/cloning reroutes 1.png" align=middle>

* ctrl-V 粘贴克隆的重路由  
<img src="./pix/cloning reroutes 2.png" align=middle>

* 现在连接它们
<img src="./pix/cloning reroutes 3.png" align=middle>

* 然后向右拖动它，使其靠近新的 KSampler  
<img src="./pix/cloning reroutes 4.png" align=middle>

* 并将其连接到新 KSampler 上的模型输入
<img src="./pix/cloning reroutes 5.png" align=middle>

* 重路由仍然在剪贴板中，所以在初始模式重路由下面再做一个 ctrl-v。  
<img src="./pix/cloning reroutes 6.png" align=middle>

* 这次，将正面提示词的条件输出连接到新的重路由。名称会改变，但颜色不会。  
<img src="./pix/cloning reroutes 7.png" align=middle>

* 右键单击重路由节点，左键单击颜色，然后选择黄色
<img src="./pix/cloning reroutes 8.png" align=middle>

* 重复最后几步，为负面节点制作第二个重路由并将颜色更改为黑色。
<img src="./pix/cloning reroutes 9.png" align=middle>

* 现在整理一下它们。
* 提示：拖动时 shift-左鼠标"将节点对齐到网格"。使它们更容易均匀放置。  
<img src="./pix/cloning reroutes 10.png" align=middle>

* Shift-左键单击两个新的条件节点以选择它们。  
<img src="./pix/cloning reroutes 11.png" align=middle>  

* Ctrl-C 将它们克隆到剪贴板
* Ctrl V 稍微向右以将它们粘贴到工作流上。  
<img src="./pix/cloning reroutes 12.png" align=middle>

* 从先前的条件节点运行连线到新节点。  
<img src="./pix/cloning reroutes 13.png" align=middle>

* 并向右拖动它们。它们应该仍然被选中，所以 shift+左鼠标将移动它们两者。  
<img src="./pix/cloning reroutes 14.png" align=middle>

* 然后将它们连接到正面和负面的输入。  
<img src="./pix/cloning reroutes 15.png" align=middle>  

* 放大和 KSampler 应该准备好了。如果您更改了空潜空间图像节点以测试更大的尺寸，请将其改回 512px。
* 单击队列提示
* 惊叹于稍微更大和更详细的像素瓶子！  
<img src="./pix/ComfyUI_00354_.png" width="20%" align=middle>  

但是等等！这个瓶子不是和以前有点不同吗？确实如此！原因如下：
* 在新的 KSampler 上，去噪设置为 1.000
* 这告诉 KSampler 将潜空间图像输入视为新画布，并像新图像一样推断结果。
* 将去噪降低以更紧密地匹配原始潜空间，同时仍然添加细节。
* 0.500 通常是第一个"HR 修复"的好数字
* 再次单击队列提示。
* ComfyUI 应该从第二个 KSampler 开始，而不是运行整个工作流。这是因为工作流的前面部分没有变化。  
<img src="./pix/ComfyUI_00355_.png" width="20%" align=middle>

* 如果第一个 KSampler 再次运行，这意味着
  * 种子改变了
  * 自上次以来 comfy 已重新启动
  * 我不知道我在说什么。

所以，嗯。呃...

为什么要所有的重路由和颜色编码？我们不能直接从模型和条件输出连接到新的 KSampler 吗？
* 当然可以！虽然现在很容易看出发生了什么...
* 想象一个有 100 个节点的工作流
* 现在想象一个月后回到工作流或者...
* 查看另一个人的工作流。
* 运行重路由、颜色编码和保持整洁会有很大帮助！
* 此外，使用稳定扩散是为了制作漂亮的图片。让我们也制作漂亮的工作流！

## 扩展修复

### 更多潜空间修复

添加更多节点并增加 HR-Fix 很容易。
* 将输出节点向右拖动，以便有更多空间。  
<img src="./pix/expand hrf 1.png" width="80%" align="middle">

* 选择末尾的重路由、潜空间和 KSampler 节点。  
<img src="./pix/expand hrf 2.png" width="80%" align="middle">

* Ctrl-C 克隆  
* 将鼠标移到上方并 ctrl-V 粘贴
* 一点 shift-拖动魔术来对齐事物  
<img src="./pix/expand hrf 3.png" width="80%" align="middle">

* 拖动连线以链接  
<img src="./pix/expand hrf 4.png" width="80%" align="middle">

* 并增加放大潜空间宽度和高度值  
<img src="./pix/expand hrf 5.png" width="80%" align="middle">

* 并稍微降低去噪。对于这个，.450 很好。
* HRF 中的每个 KSampler 都会降低噪声
* 虽然对于潜空间，大约 .2 是最低的。通常。

[这里是当前的工作流](basic-wf-vae-lora-latemt-upscale-x2.json)

更多的潜空间 HRF 将逐渐增加输出图像，同时添加细节。但让我们在这里停止并添加一些像素空间 HRF。前进，高贵的战马！  
<img src="./pix/m1B90jt.jpg" width="20%" align="middle">

### 像素空间 HR 修复

首先，我们需要从潜空间转换为像素空间。

* 选择 VAE 解码及其下方的 VAE 重路由，并将它们克隆到最后一个 KSampler 旁边。  
<img src="./pix/pixel space hrf 1.png" width="80%" align="middle">

* 再次将输出节点向右拖动  
<img src="./pix/pixel space hrf 2.png" width="80%" align="middle">

* 现在添加一个放大图像节点  
<img src="./pix/pixel space hrf 3.png" width="80%" align="middle">  
<img src="./pix/pixel space hrf 4.png" width="80%" align="middle">  
<img src="./pix/pixel space hrf 5.png" width="80%" align="middle">

* 在放大节点之后，我们需要一个 VAE 编码节点。  
<img src="./pix/pixel space hrf 8.png" width="80%" align="middle">  
<img src="./pix/pixel space hrf 9.png" width="80%" align="middle">

* 选择重路由节点和 KSampler 并将它们克隆到新编码节点之后的空间  
<img src="./pix/pixel space hrf 10.png" width="80%" align="middle">

* 连接所有连线  
<img src="./pix/pixel space hrf 11.png" width="80%" align="middle">  
<img src="./pix/pixel space hrf 12.png" width="80%" align="middle">  
<img src="./pix/pixel space hrf 13.png" width="80%" align="middle">

* 在此过程中，与最左侧的第一个 VAE 重路由的连接可能会丢失。不要担心！按住空格键的同时移动鼠标向左平移。
  * 空格 + 鼠标 = 平移。
  * 释放空格以移回鼠标
  * 空格 + 鼠标再次平移
* 开始从最左侧的 VAE 重路由拖动连线
  * 空格和鼠标以继续
* 并将其附加到较新的 VAE 重路由。
* 工作流现在应该看起来像这样：  
<img src="./pix/pixel space hrf 15.png" width="80%" align="middle">

* 将放大图像高度和宽度调整为 704
* 与潜空间 HR 修复不同，在像素放大后，去噪不需要降低那么多。在这种情况下，将其保留在 .5 是可以的。
  * 通常来说，在像素空间放大后采样不需要降低到 0.400 以下。通常。总会有例外。这是稳定扩散的常态。
* 输出：  
<img src="./pix/ComfyUI_00357_.png" width="25%" align="middle">


## 放大

使用高分辨率修复改进图像是一回事，但简单地使其更大呢？这就是放大的用武之地。如前所述，由于缺乏细节，不建议从 512px 跳跃到 1080p 及更高。每个 HR 修复也给了稳定扩散纠正错误的机会。（虽然并不总是如此。稳定扩散是一个固执的野兽。）

一旦图像有一些细节，进一步放大它的最佳方法之一是使用放大模型。这里有很多[放大模型](https://upscale.wiki/wiki/Model_Database)，但我们将使用 PSNRx2 保持简单。跟随 [https://huggingface.co/wyrde/upscales/tree/main/apache2](https://huggingface.co/wyrde/upscales/tree/main/apache2) 并单击 LFS 按钮下载。  
<img src="./pix/dl psnr 2.png" width="80%" align="middle">

将文件保存在 `ComfyUI\models\upscale_models\` 中

现在让我们设置放大！
* 像往常一样，通过一点拖动腾出空间。
* VAE 解码可以保持不变，因为我们要使用它。这次只需要移动保存图像节点。  
<img src="./pix/upscale with model 1.png" width="80%" align="middle">

* 现在添加加载放大模型和使用模型放大图像节点。  
<img src="./pix/upscale with model 2.png" width="80%" align="middle">  
<img src="./pix/upscale with model 3.png" width="80%" align="middle">

* 连接输入和输出  
<img src="./pix/upscale with model 4.png" width="80%" align="middle">  
<img src="./pix/upscale with model 5.png" width="80%" align="middle">  
<img src="./pix/upscale with model 6.png" width="80%" align="middle">

* 现在，这将导致 1408x1408 的图像。但如果那太大了怎么办？
* 添加一个图像缩放节点，但将其大小设置得更低。1024x1024 今天就很好。  
<img src="./pix/upscale with model 7.png" width="80%" align="middle">  
<img src="./pix/upscale with model 8.png" width="80%" align="middle">

* 单击队列提示
* 由于工作流的前面部分没有改变，它通过缩放器运行缓存的图像。
<img src="./pix/ComfyUI_00358_.png" width="25%" align="middle">

## 嵌入/文本反转

也称为文本反转，嵌入与 comfy 工作流的常规添加有点不同。它们不是节点，而是直接添加到提示词中。这是由于嵌入的性质，它们是提供令牌特定含义的专用模型。

等等，令牌？

虽然提示词是人类可读的，但稳定扩散不会以人类方式阅读它们。它们被翻译成令牌，稳定扩散根据模型中的关联为它们分配含义（包括 LoRA，它们位于提示词之前）。

令牌使用关键字 `embedding:` 后跟嵌入的文件名放置在提示词中。例如，一个流行的负面嵌入是 EasyNegative.pt。

`    embedding:EasyNegative`

`embedding:` 和 `EasyNegative` 之间没有空格，它是一个"单词"。如果需要，可以省略文件名扩展名（在此例中为 `.pt`）。

嵌入可以根据需要放置在正面或负面提示词中。与 LoRA 非常相似，触发词不是严格必需的，但可以为提示词添加额外的"权重"。

<!-- note about embeds in folders
:
It requires the folder, and the slash has to be escaped. `embedding:_neg____//7dirtywords,`
At least, there's no errors.
-->

## 自定义节点

ComfyUI 的一个优点是很容易将自定义节点添加到工作流中。通常。并非所有自定义节点的安装难度都相同。

以下说明适用于独立的便携式 Windows 版本。

首先，有三种基本类型的节点。
* 基于 Python 的节点。这些进入 `ComfyUI\custom_nodes` 文件夹。
* 用户界面的扩展。这些进入 `ComfyUI\web\extensions` 文件夹。
* 混合节点，有文件进入每个文件夹。

有两种基本方法获取节点。
* 存档格式，通常在 civitai.com 上找到。
* 作为 github 或其他存储库站点上的存储库。

使用自定义节点的第一步是安装 git。即使只使用一次，它也会在以后节省很多麻烦。
* [https://github.com/git-guides/install-git](https://github.com/git-guides/install-git)

第二步是知道如何打开 shell 到 custom_nodes 文件夹。
* 最简单的方法是打开文件资源管理器，导航到 custom_nodes 文件夹，然后在地址栏中输入 CMD 并按回车键。  
<img src="https://i.imgur.com/IeWKNGw.png" width="50%" align="middle">  
<img src="https://i.imgur.com/akxAaLm.png" width="50%" align="middle">  
<img src="https://i.imgur.com/txOblf7.png" width="50%" align="middle">  

### 使用 ComfyUI 管理器

安装节点的最简单方法是使用 ComfyUI 管理器，由令人敬畏的 Lt Data 编写（其神秘起源迷失在时间的迷雾中）。它本身就是一个节点，但安装起来相当容易。
* 不是 ComfyUI 的官方部分
  * 管理器仍在开发中
  * 它不支持所有节点，但其安装过程对大多数节点都有效。
* 从这里获取：[https://github.com/ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
  * 即使下载了 zip 版本，它仍然需要 git 来安装其他自定义节点。
* 打开命令窗口到 custom_nodes（见上文）
* 将 `git clone https://github.com/ltdrdata/ComfyUI-Manager.git` 粘贴到命令窗口并按回车键。
* 它将下载文件  
<img src="./pix/git clone manager 01.png" width="50%" align="middle">  
* 启动 comfyui 并刷新窗口。管理器现在应该在主菜单中。  
<img src="./pix/git clone manager 02.png"  align="middle"> 

### 从 zip 安装

大多数存档只需将它们解压缩到正确的文件夹即可。如果需要更多，作者通常会提供说明。
* 如果 zip 只有以 `.py` 结尾的文件，将它们直接放在 `custom_nodes` 中
* 如果 zip 有一个文件夹/目录，将它们（以及其中的文件）放在 `custom_nodes` 中
  * 注意，如果文件夹不包含名为 `__init__.py` 的文件，则在 comfy 启动时会在控制台中显示错误。虽然很烦人，但可以忽略错误。

### 从 git 安装

过程与安装节点管理器相同。
* 从存储库上的绿色代码框复制 URL  
<img src="./pix/git clone manager 03.png" width="30%" align="middle">

* 打开命令窗口或 powershell 到 custom_nodes 目录
* 输入 `git clone ` 并粘贴 URL，然后按回车键。
* 如果有额外步骤（如安装要求），请遵循存储库页面或自述文件上的说明。

### Conda 虚拟环境

也称为 venv。使用 conda 管理 Python 虚拟环境超出了本文档的范围。但如果您使用 Windows 便携版并"手动"安装自定义节点，有一件重要的事情需要知道。
* 当说明说要使用 python 时，您必须告诉它使用独立版本中的 python 版本。
* 要从 custom_nodes 文件夹运行"setup.py"，需要类似这样的行：

```
    ..\..\..\python_embeded\python.exe .\setup.py
```

* 这是为了运行正确的 python，并将所需的包安装到 comfyui 可以看到它们的地方。
* 如果使用管理器，这不是问题，因为管理器已经在使用正确的 python。

## CLIP 跳过
（仍在编写此内容）

## 权重提示词
（也在编写此内容）

## 选项和考虑事项
（也在编写此内容）

## 自定义图像保存
（某一天...）
<!-- 
custom file paths, the yaml file and start argument for save files
 -->
<!-- <img src="./pix/" width="10%" align="middle"> -->

## 资源

<!-- 人们可能想要复制结果的东西 -->

模型
* https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main

VAE
* https://huggingface.co/stabilityai/sd-vae-ft-mse-original/tree/main

LoRA
* https://civitai.com/models/44960?modelVersionId=49584

嵌入
* EasyNegative https://civitai.com/models/7808/easynegative
* bad-hands-5 https://huggingface.co/yesyeahvh/bad-hands-5/tree/main

放大器
* 2x PSNR at https://huggingface.co/wyrde/upscales/tree/main/apache2