# wyrde 的模板分享
_模板_是用于更快构建工作流的节点集合，而不是完整的工作流。目前还没有（尚未）直接在用户之间共享模板的方法，但导入它们相当容易。

## 如何添加模板
* 下载这些 json 文件之一。
  * 单击上面列表中的文件。
  * 单击右上角的 RAW 按钮。
  * CTRL-S 保存结果。
* 在 ComfyUI 中，单击清除按钮以清空工作区。
  * 单击加载按钮
  * 选择之前的 json 文件
* 在工作流中，高亮显示节点
  * 右键单击空工作流并选择"将选定内容另存为模板"
  * 给它一个名称
* 它现在应该在模板列表中了！

<!-- <img src="some image" align="middle"> -->

## 模板

* 用于[设置自定义保存文件](https://raw.githubusercontent.com/wyrde/wyrde-comfyui-workflows/main/templates/tem.savefile.prefix.1.json)的节点（使用 WAS 节点）。<img src="tem.savefile.prefix.1.png" width="30%" align="middle">
* 上面的节点，但带有[匹配的保存图像节点](https://raw.githubusercontent.com/wyrde/wyrde-comfyui-workflows/main/templates/tem.savefile.prefix.2.json) <img src="tem.savefile.prefix.2.png" width="30%" align="middle">
* [重路由节点](https://raw.githubusercontent.com/wyrde/wyrde-comfyui-workflows/main/templates/tem.reroute.nodes.1.json)对，颜色排序 <img src="tem.reroute.nodes.1.png" width="30%" align="middle">

<!--
* 图像
 <img src="" width="10%" align="middle"> -->

## 资源

<!-- 人们可能想要复制结果的东西 -->

自定义节点
* [WAS 套件](https://github.com/WASasquatch/was-node-suite-comfyui)