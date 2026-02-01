# ⚡ 10分钟快速上手指南

## 📂 文件结构

```
g:/PPT/
├── components/              # 5大核心组件库
│   ├── hero-slide.html     # 封面页
│   ├── bento-grid.html     # 多卡片布局
│   ├── timeline.html       # 时间轴
│   ├── dashboard.html      # 数据仪表盘
│   └── mockup.html         # 样机演示
├── template.html           # 通用模板（复制这个开始）
├── README-COMPONENTS.md    # 组件使用说明
├── DEPLOY.md              # 部署上线指南
└── content_structure.md   # 内容大纲提炼
```

---

## 🚀 3步做一套PPT

### 第1步: 复制模板 (10秒)
```bash
复制 template.html → your-project.html
```

### 第2步: 插入组件 (5分钟)
打开 `components/` 文件夹，选择需要的组件，复制粘贴到模板中

**示例：做一个商业计划书**
```
封面 → 复制 hero-slide.html
数据展示 → 复制 dashboard.html  
产品功能 → 复制 bento-grid.html
发展规划 → 复制 timeline.html
```

### 第3步: 改文字 (5分钟)
只需要修改：
- 标题文字
- 数字数据
- 图标emoji
- 描述内容

**完成！** 用浏览器打开，按空格键翻页查看效果。

---

## 💡 对Windsurf/Claude说什么？

### 创建新PPT
```
"用template.html创建一个新PPT，包含：
1. 封面页（标题：XX项目）
2. 数据页（显示3个关键指标）
3. 功能介绍页（3列卡片布局）
4. 时间轴（4个发展阶段）

主题色改为蓝色系"
```

### 修改现有组件
```
"把dashboard组件中的数字改成：
- 第一个改为 25.8万亿
- 第二个改为 85%
- 添加一个新的数据卡片显示用户数"
```

### 调整样式
```
"把所有卡片的圆角改大一点，间距增加到20px"
```

---

## 🎨 快速配色

### 改主题色（在template.html的`<style>`中）

**蓝色系：**
```css
background: radial-gradient(circle, #1e3a8a 0%, #0f172a 50%, #000 100%);
.gold-gradient { background: linear-gradient(135deg, #60a5fa, #3b82f6); }
```

**绿色系：**
```css
background: radial-gradient(circle, #065f46 0%, #0f172a 50%, #000 100%);
.gold-gradient { background: linear-gradient(135deg, #34d399, #10b981); }
```

**紫色系：**
```css
background: radial-gradient(circle, #6b21a8 0%, #0f172a 50%, #000 100%);
.gold-gradient { background: linear-gradient(135deg, #a78bfa, #8b5cf6); }
```

---

## 📱 发布分享

### 最快方式：Netlify拖拽
1. 访问 netlify.com
2. 拖拽HTML文件
3. 获得链接分享

### 专业方式：Vercel
1. 上传到GitHub
2. Vercel导入
3. 自动部署 + CDN加速

详见 `DEPLOY.md`

---

## 🔥 实战案例

### 案例1: 国文汇通商业计划书（已完成）
- 16页完整PPT
- 包含数据可视化、时间轴、卡片布局
- 文件：`web-ppt/index-complete.html`

### 案例2: 10分钟做一个产品发布会PPT
```
1. 复制 template.html
2. 插入 hero-slide（产品名称）
3. 插入 bento-grid（3大功能）
4. 插入 mockup（产品演示）
5. 插入 dashboard（核心数据）
6. 完成！
```

---

## 💪 进阶技巧

### 1. 添加视频背景
```html
<video autoplay loop muted class="absolute inset-0 w-full h-full object-cover opacity-30">
    <source src="background.mp4" type="video/mp4">
</video>
```

### 2. 添加音效
```html
<audio autoplay loop>
    <source src="bgm.mp3" type="audio/mpeg">
</audio>
```

### 3. 嵌入外部内容
```html
<!-- YouTube视频 -->
<iframe src="https://www.youtube.com/embed/VIDEO_ID"></iframe>

<!-- 在线图表 -->
<iframe src="https://charts.example.com/chart1"></iframe>
```

---

## 🎯 下次做PPT的流程

1. **打开** `template.html`
2. **对Windsurf说**: "创建一个XX主题的PPT，包含..."
3. **等待** AI生成代码
4. **预览** 浏览器打开查看
5. **微调** 改改文字和颜色
6. **部署** 拖到Netlify
7. **分享** 发链接

**总耗时：10-15分钟** ⚡

---

## 📞 遇到问题？

### 常见问题速查

**Q: 组件样式乱了？**
A: 确保复制了完整的`<style>`标签

**Q: 动画不生效？**
A: 检查是否引入了Reveal.js的CDN

**Q: 手机显示不正常？**
A: 添加 `md:` 前缀做响应式，如 `md:grid-cols-3`

**Q: 想要不同的字体？**
A: 在Google Fonts选择，替换`@import`链接

---

## 🎁 额外资源

- **图标库**: emojipedia.org
- **配色工具**: coolors.co
- **免费图片**: unsplash.com
- **渐变生成**: cssgradient.io

---

**恭喜！您已经掌握了"降维打击"的武器！** 🎉

**以后做PPT就是填空题，不再是折磨！**
