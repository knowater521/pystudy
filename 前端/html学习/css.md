## css选择器 与 常用属性

###  1.通用选择器 
`
*｛｝`

### 2.标签选择器：
`div｛｝
p{}
span{}`

### 3. 类选择器
`<div id=“big” class="test"> </div>
`

选择 .test{}

### 4.id选择器
`id只能一一对应：  #big｛｝
`
### 5.复合选择器
`   div.test
 div#id
`
### 6.群组选择器(并列选择器)
`div,span, .test{}`

### 7.后代选择 器
`
#big div span {}
`

### 8.直接后代选择器
div>p{}

### 9.兄弟 选择器
div + p{}
div ~ p{}
### 10.属性选择器
div[name] {}

# 伪类和伪元素
例如：hover（伪类：获得焦点时，改变属性）
伪元素：选择首行、首字母
等。
#### 否定伪类。
div:not{}


# 选择器的优先级

# 标签元素划分
块元素 ：div，p，ui，li等
可单独设置宽高大小，换行
行内元素：a，
不换行，不可设置大小
行内块元素：不换行，可设置大小
标签元素转换：
css中的 display 属性修改：block，inline。


# 盒子模型
（width，height，top，button，left，right，）
content:内容，盒子内装的东西，一般为文本或图片
padding:内边距，内容与盒子边框间的距离
border: 边框，盒子本身
margin: 外边距，盒子与外界之间的距离

# 常见属性：
## 内容：
height,max-height,max-width,min-height,min-width,width，background-color
## 内边距：
padding:1px 2px 3px 4px;(上右下左), padding-top,padding-right,padding-left,padding-buttom, 
## 边框：
border:5pxsolid red;(依次设置)border-width，border-style,border-color，也可以单独设置某个边框如：border-top,border-right,
## 边框圆角：
border-radius:50%，直接设置为圆形了.
也可单独设置某个角：border-top-left-radius:
## 外边框：
margin:1px,2px,3px,4px,上右下左。

## 浮动
 float:left,top,right,button

## 标签居中：水平，垂直
text-align：center 文字居中（行内标签）。
margin:0 auto；左右居中（块标签）

## 常用属性
visibility:visible,hidden. 元素是否可见。位置始终占据。
display：none，这个隐藏位置不占据。
cursor：pointer，光标显示的样式
color:设置文字颜色
font，（font-family,size,weight,style）设置文字样式。
text-decoration:none    去除下划线
text-indent:首行缩进
list-style:列表属性  ul常用
overflow：控制内容溢出的情况
line-height：设置行高