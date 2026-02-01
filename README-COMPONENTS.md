# 🚀 网页PPT组件库使用指南

## 📦 已创建的5大核心组件

### 1. **Hero Slide (全屏封面)** 
📁 `components/hero-slide.html`
- **用途**: PPT开场，镇场子专用
- **特点**: 大标题 + 动态粒子背景 + 渐变装饰
- **修改点**: 标题、副标题、底部标语

### 2. **Bento Grid (多卡片布局)**
📁 `components/bento-grid.html`
- **用途**: 讲产品功能、要点、团队介绍（万能布局）
- **特点**: 苹果风格圆角卡片，支持3列/跨列
- **修改点**: 图标emoji、卡片标题、描述内容

### 3. **Timeline (时间轴)**
📁 `components/timeline.html`
- **用途**: 公司发展历程、项目计划、过去与未来
- **特点**: 左右交错布局 + 金色连接线
- **修改点**: 年份、阶段标题、描述

### 4. **Dashboard (数据仪表盘)**
📁 `components/dashboard.html`
- **用途**: 汇报业绩、讲增长率、展示关键数据
- **特点**: 数字滚动动画 + 环形图 + 柱状图
- **修改点**: 数字、百分比、图表数据

### 5. **Mockup (样机演示)**
📁 `components/mockup.html`
- **用途**: 展示数字化产品、App或网站
- **特点**: iPhone + MacBook样机 + 浮动动画
- **修改点**: 截图路径或嵌入视频

---

## 🎯 快速开始（10分钟做一套PPT）

### 步骤1: 复制模板
```bash
复制 template.html 为 your-project.html
```

### 步骤2: 选择组件
从 `components/` 文件夹中选择需要的组件，复制到模板的 `<div class="slides">` 中

### 步骤3: 修改内容
只需要改这些地方：
- 📝 标题文字
- 🎨 图标emoji
- 📊 数据数字
- 🖼️ 图片路径

### 步骤4: 预览
用浏览器打开 HTML 文件，按空格键翻页

---

## 💡 使用示例

### 示例1: 创建一个商业计划书PPT

```html
<div class="slides">
    <!-- 第1页: 封面 -->
    <!-- 复制 hero-slide.html 的内容 -->
    
    <!-- 第2页: 市场分析 -->
    <!-- 复制 dashboard.html 的内容 -->
    
    <!-- 第3页: 产品功能 -->
    <!-- 复制 bento-grid.html 的内容 -->
    
    <!-- 第4页: 发展规划 -->
    <!-- 复制 timeline.html 的内容 -->
    
    <!-- 第5页: 产品演示 -->
    <!-- 复制 mockup.html 的内容 -->
</div>
```

### 示例2: 对Windsurf说的话

```
"请帮我创建一个PPT，包含：
1. 封面页（使用hero-slide组件）
2. 3个数据展示页（使用dashboard组件）
3. 团队介绍页（使用bento-grid组件，3列布局）
4. 发展路线图（使用timeline组件，4个时间节点）

主题色改为蓝色系，标题改为'XX项目商业计划书'"
```

---

## 🎨 自定义配色

在 `<style>` 标签中修改：

```css
/* 主背景渐变 */
.reveal {
    background: radial-gradient(
        circle at top right, 
        #1a237e 0%,    /* 改这里 - 深蓝 */
        #0f172a 50%,   /* 改这里 - 午夜蓝 */
        #000000 100%   /* 改这里 - 纯黑 */
    );
}

/* 金色渐变（强调色） */
.gold-gradient {
    background: linear-gradient(135deg, 
        #FFD700 0%,    /* 改这里 - 金色 */
        #FFA500 100%   /* 改这里 - 橙金 */
    );
}
```

---

## 🚀 部署上线（发链接给别人）

### 方法1: GitHub Pages（免费）
1. 创建GitHub仓库
2. 上传HTML文件
3. 设置 → Pages → 选择分支
4. 获得链接: `https://your-username.github.io/your-repo`

### 方法2: Vercel（推荐，更快）
1. 访问 vercel.com
2. 导入GitHub仓库
3. 自动部署
4. 获得链接: `https://your-project.vercel.app`

---

## 📱 快捷键

- **空格键**: 下一页
- **Shift + 空格**: 上一页
- **Esc**: 概览模式（查看所有页面）
- **F**: 全屏模式
- **S**: 演讲者备注模式

---

## 🔥 进阶技巧

### 1. 添加演讲者备注
```html
<section>
    <h2>标题</h2>
    <aside class="notes">
        这里写备注，只有演讲者能看到
    </aside>
</section>
```

### 2. 嵌入视频
```html
<video autoplay loop muted>
    <source src="demo.mp4" type="video/mp4">
</video>
```

### 3. 添加动画
```html
<div class="fragment">这段文字会延迟出现</div>
<div class="fragment fade-in">淡入效果</div>
<div class="fragment fade-up">上浮效果</div>
```

---

## 📞 需要帮助？

### 对Windsurf/Claude说：
- "帮我把这个组件的颜色改成红色系"
- "添加一个新的卡片，内容是..."
- "把这个数据图表改成柱状图"
- "优化移动端显示"

### 常见问题：
**Q: 字体太小？**
A: 修改 `text-5xl` 为 `text-6xl` 或 `text-7xl`

**Q: 卡片间距太窄？**
A: 修改 `gap-8` 为 `gap-12` 或 `gap-16`

**Q: 想要不同的动画？**
A: 搜索 "Reveal.js transitions" 查看更多效果

---

## 🎁 额外资源

- **图标**: 使用emoji或访问 icons8.com
- **配色**: coolors.co 生成配色方案
- **字体**: Google Fonts (已集成 Noto Sans SC)
- **图片**: unsplash.com 免费高质量图片

---

**祝您做PPT愉快！10分钟搞定一套大片级演示文稿！** 🎉
