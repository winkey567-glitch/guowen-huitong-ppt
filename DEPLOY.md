# 🚀 部署指南 - 把PPT发布到网上

## 为什么要部署？

传统PPT的痛点：
- ❌ 文件太大（几百MB）
- ❌ 字体丢失
- ❌ 视频打不开
- ❌ 需要安装软件

网页PPT的优势：
- ✅ 发一个链接就行
- ✅ 手机/电脑/平板都能看
- ✅ 动画丝滑流畅
- ✅ 看起来极其专业

---

## 方法1: GitHub Pages（免费 + 简单）

### 步骤1: 创建GitHub账号
访问 github.com 注册（如果已有账号跳过）

### 步骤2: 创建仓库
1. 点击右上角 "+" → "New repository"
2. 仓库名: `my-ppt` （可以改成任何名字）
3. 选择 "Public"
4. 点击 "Create repository"

### 步骤3: 上传文件
1. 点击 "uploading an existing file"
2. 拖拽您的 HTML 文件和 components 文件夹
3. 点击 "Commit changes"

### 步骤4: 开启Pages
1. 点击 "Settings"
2. 左侧菜单找到 "Pages"
3. Source 选择 "main" 分支
4. 点击 "Save"

### 步骤5: 获取链接
等待1-2分钟，刷新页面会看到：
```
Your site is live at https://your-username.github.io/my-ppt/
```

**完成！** 现在可以把这个链接发给任何人了。

---

## 方法2: Vercel（推荐 - 更快更专业）

### 步骤1: 访问Vercel
打开 vercel.com，用GitHub账号登录

### 步骤2: 导入项目
1. 点击 "Add New..." → "Project"
2. 选择 "Import Git Repository"
3. 选择您刚才创建的GitHub仓库
4. 点击 "Import"

### 步骤3: 配置（可选）
- Project Name: 改成您想要的名字
- Framework Preset: 选择 "Other"
- 其他保持默认

### 步骤4: 部署
点击 "Deploy"，等待30秒

### 步骤5: 获取链接
部署完成后会看到：
```
https://your-project.vercel.app
```

**优势：**
- ⚡ 全球CDN加速（打开速度快）
- 🔄 自动部署（GitHub更新后自动同步）
- 📊 访问统计
- 🎯 自定义域名

---

## 方法3: Netlify（备选方案）

### 拖拽式部署（最简单）
1. 访问 netlify.com
2. 注册/登录
3. 直接把文件夹拖到页面上
4. 获得链接: `https://random-name.netlify.app`

### 自定义域名
1. 点击 "Domain settings"
2. 点击 "Add custom domain"
3. 输入您的域名（如果有的话）

---

## 🎯 实战演示

### 场景: 给领导汇报

**传统方式：**
```
您: "领导，我把PPT发您邮箱了"
领导: "文件太大，发不过来"
您: "那我用U盘拷给您"
领导: "我电脑没装Office"
您: "..."
```

**网页PPT方式：**
```
您: "领导，这是汇报链接"
    https://your-project.vercel.app
领导: （手机点开）"嗯，做得不错，发我看看"
您: （直接转发链接）
领导: （任何设备都能完美打开）
```

---

## 📱 分享技巧

### 生成二维码
1. 访问 qr-code-generator.com
2. 输入您的PPT链接
3. 下载二维码
4. 放在PPT最后一页："扫码查看完整版"

### 短链接
使用 bit.ly 或 tinyurl.com 把长链接缩短：
```
原链接: https://your-username.github.io/my-ppt/index.html
短链接: https://bit.ly/my-ppt
```

---

## 🔒 隐私设置

### 如果不想公开
**GitHub Pages**: 仓库设为Private（需要GitHub Pro）
**Vercel**: 添加密码保护
```javascript
// 在HTML顶部添加
const password = prompt("请输入密码:");
if (password !== "your-password") {
    document.body.innerHTML = "密码错误";
}
```

---

## 📊 查看访问数据

### Vercel Analytics
1. 项目设置 → Analytics
2. 查看访问量、地区分布等

### Google Analytics（进阶）
在 `<head>` 中添加：
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-ID');
</script>
```

---

## 🛠️ 常见问题

### Q: 更新内容后怎么办？
**GitHub Pages**: 直接在GitHub上编辑文件或重新上传
**Vercel**: 推送到GitHub，自动部署

### Q: 链接太丑怎么办？
购买域名（如 aliyun.com），在Vercel/Netlify绑定

### Q: 视频文件太大？
上传到YouTube/Bilibili，用iframe嵌入：
```html
<iframe src="https://www.youtube.com/embed/VIDEO_ID"></iframe>
```

### Q: 想要访问统计？
使用 umami.is（开源免费）或 Google Analytics

---

## 🎁 额外福利

### 自动化部署脚本
创建 `.github/workflows/deploy.yml`：
```yaml
name: Deploy
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

每次推送代码自动部署！

---

**现在您的PPT不仅好看，还能随时随地分享！** 🎉
