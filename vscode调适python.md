# 第一步：在VS Code中添加Python 扩展：

       注意：不管你之前下载的是anaconda的python集成环境，还是从Python.org上下载的Python环境，这只是在后面IDE上进行配置时使用具体的环境，拥有上述的Python环境还不够；

       在VS Code中进行配置之前，必须还要有一个**Python Extension（Python 扩展），**这个在下图中提示中可以找到。找到以后，然后点“ 安装 ”按钮。（这里我安装过了，所以是“”禁用“”和“”卸载“”）。

![image](https://upload-images.jianshu.io/upload_images/13908612-396e4f3993415b2c?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 第二步：创建一个名为“ hello ”的工作目录

1、首先 win键+R ，输入cmd进入控制台，切换到你将要创建“hello”目录的路径下。

2、在控制台中输入：mkdir hello，然后回车；这个命令的意思是新建一个名为“hello ”的文件夹。

3、接着输入： cd hello ,然后回车；这个命令的意思是切换到 名为“ hello ”的工作目录下；

4、接着输入：code .  (code 后面是个英文的点号），这样就使用VS Code 的命令在“ hello ”文件夹下启动VS Code这个软件

这三条命令实现了：自动创建工作目录并在该目录下打开VS Code软件的目的，同时新创建的目录作为了此次程序的工作空间。

# 第三步：在工作目录下，为VS Code指定并配置Python环境（即生成settings.json 文件）

 1、在VS code中使用快捷键：**Ctrl + Shift +P**进入命令面板，输入**Preferences : Configure Language Specific Settings**,命令，点击红色框中的内容，来进行配置语言环境。

![image](https://upload-images.jianshu.io/upload_images/13908612-f831c394acd7aea7?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

       2、然后在紧接着出现的如下界面中，手动输入Python，单击红色框中的内容，即选定要配置的具体语言。

![image](https://upload-images.jianshu.io/upload_images/13908612-f6c358b25340679e?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        3、此时出现如下的“ 用户设置选项”，它主要跟一些个人习惯有关，涉及一些界面：主题、字体、字号等内容。在此暂时不做介绍，文末针对这一点会有入门介绍，这里不做详解。![image](https://upload-images.jianshu.io/upload_images/13908612-117ca0c16b05e71b?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        4、注意此时的“ 工作区设置”如下图所示，里边没有具体的内容。但在“左侧资源管理器”下边出现了“settings.json ”文件。到这一步只是告诉vs code软件要进行Python语言配置，因为python 有很多开发环境不同的人有不同的Python环境，比如：有人用anaconda这种Python的集成开发环境，有人用Python.org上的原始Python。下一步就是要找到你现在要用到具体的Python版本。

![image](https://upload-images.jianshu.io/upload_images/13908612-45bb25274b92331c?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        5、配置你**现在所使用的Python**环境，使用快捷键：**Ctrl + Shift +P**进入命令面板，输入**Python：Select Interpreter，**然后，单击红色框中的内容。这一步就是要选择你所使用的具体Python环境。

![image](https://upload-images.jianshu.io/upload_images/13908612-0588cc19b920399a?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        6、根据自己的使用情况，找到自己所使用的具体Python环境，例如本次使用的是anaconda ，对应的Python3.6版本，不是上边的anaconda，而是先边带有Python字样的那个。点击红色框内容，完成操作。

![image](https://upload-images.jianshu.io/upload_images/13908612-565cb30f0fbbaee3?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        7、单击上图的红色框中的内容之后，注意此时在“ 用户设置 ”中自动加载了你实际所使用的Python环境的具体路径；

![image](https://upload-images.jianshu.io/upload_images/13908612-6aad569d34cfc327?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        8、至此，指定具体的Python环境基本配置成功，即settings.json中填入了实际使用的Python环境的路径。

# 第四步：对Debug功能进行配置（即生成launch.json 文件）

        1、点击红色框中的内容，创建一个“ hello.py ”的文件。

![image](https://upload-images.jianshu.io/upload_images/13908612-d5bce2e000d61b80?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        2、在“ hello.py ”中输入一些内容，如下图所示，出现红框中提示内容（这种提醒的功能是各种IDE工具也就是vs code的智能联想功能），即settings.json配置成功。

![image](https://upload-images.jianshu.io/upload_images/13908612-9c09d601d2e3e5d0?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

           3、点击“ 调试 ”功能，即点击标记为“1”的绿框，然后点击标记为“ 2”的绿框中的齿轮；在出现的“选择环境”的字样中，**选择“Python”**不是“Python Experimental”。

![image](https://upload-images.jianshu.io/upload_images/13908612-f79f56fc25013a66?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        4、然后，在**“调试”**字样的**绿色按钮的旁边**有个下拉菜单，即点击红色框所示的下拉菜单。然后选中第一个“ Python Current File ”选项。

![image](https://upload-images.jianshu.io/upload_images/13908612-c2ef798cea11e8f9?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        5.点击标记“1”的资源管理器，在.vscode这个子文件夹下，出现了launch.json文件，表示调试功能，配置成功。

![image](https://upload-images.jianshu.io/upload_images/13908612-48d477bdef40bddd?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        6、测试“调试”功能：在第二行之前先打个断点，即第二行行号前有个小红点；点击标记“1”所示的绿色按钮或按F5，来启动调试功能；然后，按标记为“2”的按钮，出现第二行所示的黄色箭头，此时会在标记“3”的“ 调试控制台 ”出现预期的“hello world”结果。在标记“2”中涉及的Step Over、Step into 等功能的详细内容，请参考https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites

![image](https://upload-images.jianshu.io/upload_images/13908612-7037d201c705aef6?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 第五步：用户个性化设置：

#### （补齐第三步的3中提到的“用户选项设置”即如何根据自己爱好或习惯来设定显示的环境，如：主题、字号、等满足使用的习惯。）

        1、字号试样：点击 红色框中的settings.json文件，在打开的内容中点击“ editor.fontSize”旁边的“复制到设置”，

![image](https://upload-images.jianshu.io/upload_images/13908612-bbfaa555fdbca430?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

       字号的大小发生了变化，如下图所示，变小了！！！![image](https://upload-images.jianshu.io/upload_images/13908612-3b2ddb4d0bd6c5e8?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        2、主题试样：点击“工作台”功能下的“workbeach.colorTheme”,在下拉菜单中选中“Quiet Light”按钮

![image](https://upload-images.jianshu.io/upload_images/13908612-40d5d23d09be5d61?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

改变后的试样如下图所示：变成了白色背景。![image](https://upload-images.jianshu.io/upload_images/13908612-630e0fed596e9357?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

        3、对于这些个性化设置，可以按照自己习惯进行调节。这里以这两个简单的设置为例开个头，后续的各种习惯欢迎大家自己挖掘，从而为自己设计一个满足自己使用习惯的vs code 界面。
