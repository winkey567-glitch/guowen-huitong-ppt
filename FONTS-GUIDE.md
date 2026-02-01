# 🎨 网页PPT字体使用指南

## 📚 已集成的字体

### 1. **Playfair Display** - 奢华衬线体
- **用途**：标题、大数字、强调文字
- **风格**：高对比度、优雅、编辑风格
- **权重**：300 (Light), 700 (Bold), 900 (Black)
- **适合**：封面标题、章节标题

```css
font-family: 'Playfair Display', serif;
```

### 2. **Inter** - 现代无衬线体
- **用途**：正文、描述、小标签
- **风格**：清晰、易读、科技感
- **权重**：300, 400, 500, 600
- **适合**：正文内容、按钮文字

```css
font-family: 'Inter', sans-serif;
```

### 3. **Cormorant Garamond** - 优雅衬线体（新增）
- **用途**：副标题、引用文字
- **风格**：古典、文学、精致
- **权重**：300, 400, 600, 700
- **适合**：诗意表达、文化类内容

```css
font-family: 'Cormorant Garamond', serif;
```

### 4. **Montserrat** - 几何无衬线体（新增）
- **用途**：数据标签、图表文字
- **风格**：几何、现代、清晰
- **权重**：300, 400, 600, 700
- **适合**：数据可视化、信息图表

```css
font-family: 'Montserrat', sans-serif;
```

### 5. **Crimson Pro** - 编辑风格衬线体（新增）
- **用途**：长文本、段落内容
- **风格**：报纸、杂志、专业
- **适合**：详细说明、正文段落

```css
font-family: 'Crimson Pro', serif;
```

---

## 🎯 字体搭配建议

### 黑金商务风格（当前使用）
```
标题：Playfair Display (900)
副标题：Inter (300, uppercase)
正文：Inter (400)
数字：Playfair Display (300)
```

### 文化艺术风格
```
标题：Cormorant Garamond (700)
副标题：Montserrat (300)
正文：Crimson Pro (400)
```

### 科技现代风格
```
标题：Montserrat (700)
副标题：Inter (600)
正文：Inter (400)
数字：Montserrat (300)
```

---

## 🌐 更多免费字体资源

### Google Fonts（推荐）
- 网址：https://fonts.google.com
- 特点：免费、CDN加速、无需下载
- 使用方法：
  1. 选择字体
  2. 复制`<link>`标签
  3. 粘贴到HTML的`<head>`中

### 热门字体推荐

#### 衬线体（Serif）
- **Merriweather** - 适合长文本阅读
- **Lora** - 优雅、现代
- **EB Garamond** - 古典、学术
- **Libre Baskerville** - 报纸风格

#### 无衬线体（Sans-serif）
- **Roboto** - Google默认字体
- **Open Sans** - 通用、友好
- **Raleway** - 细长、优雅
- **Poppins** - 圆润、现代

#### 等宽字体（Monospace）
- **Fira Code** - 编程、代码展示
- **JetBrains Mono** - 清晰、专业

---

## 💡 字体使用技巧

### 1. 字体对比
- **大小对比**：标题 5rem vs 正文 1rem
- **粗细对比**：标题 900 vs 正文 300
- **字体对比**：衬线标题 + 无衬线正文

### 2. 字间距调整
```css
letter-spacing: 0.1em;  /* 标签、小标题 */
letter-spacing: -0.02em; /* 大标题 */
```

### 3. 行高设置
```css
line-height: 1.1;  /* 大标题 */
line-height: 1.6;  /* 正文 */
line-height: 1.8;  /* 长文本 */
```

### 4. 响应式字体
```css
font-size: clamp(2rem, 5vw, 5rem);
/* 最小2rem，理想5vw，最大5rem */
```

---

## 🚀 快速替换字体

在 `gallery-simple.html` 中修改：

```css
/* 替换标题字体 */
.title {
    font-family: 'Cormorant Garamond', serif; /* 改这里 */
}

/* 替换正文字体 */
.description {
    font-family: 'Montserrat', sans-serif; /* 改这里 */
}
```

---

## 📦 中文字体方案

### 在线CDN（推荐）
```html
<!-- 思源黑体 -->
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;700&display=swap" rel="stylesheet">

<!-- 思源宋体 -->
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@300;400;700&display=swap" rel="stylesheet">
```

### 本地字体（备用）
```css
font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
```

---

## ⚡ 性能优化

### 1. 只加载需要的字重
```
❌ family=Inter:wght@100;200;300;400;500;600;700;800;900
✅ family=Inter:wght@300;400;600
```

### 2. 使用 display=swap
```
?family=Inter&display=swap
```
防止字体加载时的闪烁

### 3. 预加载关键字体
```html
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
```

---

## 🎨 字体效果增强

### 渐变文字
```css
background: linear-gradient(135deg, #FFD700, #D4AF37);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

### 文字阴影
```css
text-shadow: 0 2px 10px rgba(255, 215, 0, 0.3);
```

### 描边文字
```css
-webkit-text-stroke: 1px #FFD700;
```

---

**提示**：所有字体都已自动集成到您的 `gallery-simple.html` 中，直接使用即可！
