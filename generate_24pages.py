# -*- coding: utf-8 -*-
"""
生成24页完整投资人版本PPT
"""

# 读取PPT内容
with open('ppt_content.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 背景图列表
backgrounds = [
    'output/pawel-czerwinski-stcl1Pj2WzY-unsplash.jpg',
    'output/andrew-kliatskyi-JdX0OeTj5S0-unsplash.jpg',
    'output/majed-swan-tzhqSmy58d8-unsplash.jpg',
    'output/pawel-czerwinski-WtNk-Ab9JEY-unsplash.jpg'
]

# 解析slides
slides = []
current_slide = None
for line in content.split('\n'):
    if line.startswith('## Slide '):
        if current_slide:
            slides.append(current_slide)
        current_slide = {'title': '', 'content': []}
    elif current_slide is not None:
        if line.strip():
            if not current_slide['title']:
                current_slide['title'] = line.strip()
            else:
                current_slide['content'].append(line.strip())
if current_slide:
    slides.append(current_slide)

print(f"Found {len(slides)} slides")

# 生成HTML
html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>国文汇通商业计划书 - 完整版</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;700;900&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <script src="particles.js-master/particles.js-master/particles.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; scrollbar-width: none; }
        *::-webkit-scrollbar { display: none; }
        
        body {
            font-family: 'Inter', sans-serif;
            overflow-y: scroll;
            scroll-snap-type: y mandatory;
            background: #0A0A0A;
            color: #F9F9F7;
        }
        
        .page {
            min-height: 100vh;
            scroll-snap-align: start;
            position: relative;
            padding: 10vh 8vw;
            overflow: hidden;
        }
        
        /* 封面特殊布局 */
        .page-1 {
            display: grid;
            grid-template-columns: 60% 40%;
            padding: 0;
        }
        
        .content-left {
            padding: 10vh 8vw;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
            z-index: 2;
        }
        
        .whitespace-right {
            background: linear-gradient(135deg, rgba(10, 10, 10, 0.3) 0%, rgba(17, 17, 17, 0.4) 50%, rgba(26, 26, 26, 0.5) 100%);
            position: relative;
        }
        
        .divider {
            position: absolute;
            left: 0;
            top: 20%;
            bottom: 20%;
            width: 1px;
            background: linear-gradient(180deg, transparent 0%, rgba(255, 215, 0, 0.3) 20%, rgba(255, 215, 0, 0.6) 50%, rgba(255, 215, 0, 0.3) 80%, transparent 100%);
        }
        
        /* 文字样式 */
        .subtitle {
            font-size: 0.9rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: rgba(255, 215, 0, 0.7);
            margin-bottom: 4rem;
        }
        
        .title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(4rem, 10vw, 9rem);
            font-weight: 900;
            line-height: 1.1;
            background: linear-gradient(135deg, #FFD700, #D4AF37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 3rem;
        }
        
        .description {
            font-size: 1.1rem;
            line-height: 1.8;
            color: rgba(255, 255, 255, 0.7);
            max-width: 600px;
            margin-bottom: 4rem;
        }
        
        .button {
            display: inline-block;
            padding: 0.8rem 2.5rem;
            background: transparent;
            border: 1px solid #FFD700;
            color: #FFD700;
            font-size: 0.85rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            text-decoration: none;
            transition: all 0.4s ease;
            width: fit-content;
        }
        
        .button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.4);
        }
        
        /* 3D 青铜爵杯 */
        .cup-3d-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 350px;
            height: 450px;
            perspective: 1000px;
            z-index: 5;
        }
        
        .cup-3d {
            position: relative;
            width: 100%;
            height: 100%;
            transform-style: preserve-3d;
            animation: rotate3d 20s linear infinite;
        }
        
        .cup-3d img {
            position: absolute;
            width: 100%;
            height: 100%;
            object-fit: contain;
            filter: drop-shadow(0 0 40px rgba(255, 215, 0, 0.6));
        }
        
        @keyframes rotate3d {
            0% { transform: rotateY(0deg) rotateX(5deg); }
            100% { transform: rotateY(360deg) rotateX(5deg); }
        }
        
        .cup-glow {
            position: absolute;
            width: 400px;
            height: 400px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255, 215, 0, 0.15) 0%, rgba(255, 215, 0, 0.05) 50%, transparent 100%);
            animation: pulse-glow 4s ease-in-out infinite;
        }
        
        @keyframes pulse-glow {
            0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.6; }
            50% { transform: translate(-50%, -50%) scale(1.1); opacity: 1; }
        }
        
        .light-beam {
            position: absolute;
            top: -10%;
            right: -5%;
            width: 350px;
            height: 700px;
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.2) 0%, rgba(255, 215, 0, 0.08) 50%, transparent 100%);
            transform: rotate(-15deg);
            filter: blur(40px);
            animation: shimmer 5s ease-in-out infinite;
            pointer-events: none;
        }
        
        @keyframes shimmer {
            0%, 100% { opacity: 0.4; }
            50% { opacity: 0.7; }
        }
        
        /* 内容样式 */
        .section-number {
            font-family: 'Playfair Display', serif;
            font-size: 8rem;
            font-weight: 300;
            color: rgba(249, 249, 247, 0.08);
            margin-bottom: 2rem;
        }
        
        .content-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 3rem;
        }
        
        .section-label {
            text-align: center;
            font-size: 0.85rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: rgba(255, 215, 0, 0.6);
            margin-bottom: 4vh;
        }
        
        .divider-thin {
            width: 100%;
            height: 1px;
            background: rgba(249, 249, 247, 0.2);
            margin: 2rem 0;
        }
        
        .data-card {
            background: rgba(249, 249, 247, 0.03);
            border: 1px solid rgba(249, 249, 247, 0.1);
            padding: 2rem;
            margin-bottom: 1.5rem;
            transition: all 0.4s ease;
        }
        
        .data-card:hover {
            background: rgba(249, 249, 247, 0.05);
            transform: translateX(10px);
        }
        
        .card-label {
            font-size: 0.75rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: rgba(249, 249, 247, 0.5);
            margin-bottom: 1rem;
        }
        
        .card-value {
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            font-weight: 300;
            background: linear-gradient(135deg, #FFD700, #D4AF37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1rem;
        }
        
        .card-text {
            color: rgba(249, 249, 247, 0.7);
            line-height: 1.7;
            font-size: 0.95rem;
        }
        
        .data-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            margin-bottom: 3rem;
        }
        
        .number-box {
            padding: 3rem 2rem;
            border: 1px solid rgba(255, 215, 0, 0.2);
            background: rgba(255, 255, 255, 0.03);
        }
        
        .big-number {
            font-family: 'Playfair Display', serif;
            font-size: clamp(3rem, 6vw, 5rem);
            font-weight: 300;
            background: linear-gradient(135deg, #FFD700, #D4AF37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1.5rem;
        }
        
        .unit {
            font-size: 1.5rem;
            color: rgba(255, 255, 255, 0.8);
            margin-left: 0.5rem;
        }
        
        .number-desc {
            font-size: 0.9rem;
            line-height: 1.8;
            color: rgba(255, 255, 255, 0.6);
        }
        
        /* 装饰元素 */
        .grid-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: linear-gradient(rgba(255, 215, 0, 0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 215, 0, 0.05) 1px, transparent 1px);
            background-size: 100px 100px;
            pointer-events: none;
            z-index: 0;
        }
        
        .geometric-bg {
            position: absolute;
            top: 10%;
            right: 5%;
            width: 400px;
            height: 400px;
            border: 1px solid rgba(255, 215, 0, 0.1);
            border-radius: 50%;
            animation: pulse 8s ease-in-out infinite;
            z-index: 0;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.3; }
            50% { transform: scale(1.05); opacity: 0.6; }
        }
        
        /* Particles.js */
        #particles-js {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: 1;
            pointer-events: none;
        }
        
        /* 全屏按钮 */
        .fullscreen-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.9), rgba(212, 175, 55, 0.9));
            border: none;
            border-radius: 8px;
            color: white;
            font-size: 24px;
            cursor: pointer;
            z-index: 999;
            transition: all 0.3s ease;
        }
        
        .fullscreen-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.5);
        }
        
        /* 页码指示器 */
        .page-indicator {
            position: fixed;
            right: 30px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 998;
            max-height: 80vh;
            overflow-y: auto;
        }
        
        .dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: rgba(255, 215, 0, 0.4);
            margin: 8px 0;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .dot.active {
            background: linear-gradient(135deg, #FFD700, #D4AF37);
            transform: scale(1.5);
        }
        
        /* Timeline 样式 */
        .timeline-item {
            position: relative;
            padding-left: 3rem;
            margin-bottom: 2.5rem;
            border-left: 2px solid rgba(255, 215, 0, 0.3);
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -6px;
            top: 0;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #FFD700;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
        }
        
        /* 列表样式 */
        .feature-list {
            list-style: none;
            padding: 0;
        }
        
        .feature-list li {
            padding: 1rem 0;
            border-bottom: 1px solid rgba(255, 215, 0, 0.1);
            color: rgba(255, 255, 255, 0.7);
        }
        
        .feature-list li::before {
            content: '✓';
            color: #FFD700;
            font-weight: bold;
            margin-right: 1rem;
        }
        
        /* 三列布局 */
        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
        }
        
        /* 中心内容 */
        .center-content {
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }
    </style>
</head>
<body>
'''

# 生成页面
for i, slide in enumerate(slides, 1):
    bg_idx = (i - 1) % len(backgrounds)
    bg = backgrounds[bg_idx]
    
    if i == 1:
        # 封面页
        html += f'''
    <!-- 页面{i}：封面 -->
    <div class="page page-1 bg-1" id="page{i}" style="background: radial-gradient(ellipse at 30% 50%, rgba(20, 20, 20, 0.75) 0%, rgba(10, 10, 10, 0.85) 40%, rgba(10, 10, 10, 0.90) 100%), url('{bg}'); background-size: cover; background-position: center;">
        <div id="particles-js"></div>
        <div class="content-left">
            <div class="subtitle">Business Proposal · 2026</div>
            <h1 class="title">国文汇通</h1>
            <p class="description">
                数字文创资产合规发行与交易一站式平台<br>
                响应国家文化数字化战略，构建权威、透明的文化资产生态体系
            </p>
            <a href="#page2" class="button">探索详情</a>
        </div>
        <div class="whitespace-right">
            <div class="divider"></div>
            <div class="light-beam"></div>
            <div class="cup-glow"></div>
            <div class="cup-3d-container">
                <div class="cup-3d">
                    <img src="output/cup.png" alt="青铜爵杯">
                </div>
            </div>
        </div>
    </div>
'''
    elif i == 24:
        # 结束页
        html += f'''
    <!-- 页面{i}：感谢 -->
    <div class="page" id="page{i}" style="background: radial-gradient(ellipse at center, rgba(10, 10, 10, 0.94) 0%, rgba(10, 10, 10, 0.97) 100%), url('{bg}'); background-size: cover; background-position: center; display: flex; align-items: center; justify-content: center;">
        <div class="center-content">
            <div class="section-label" style="margin-bottom: 3rem;">Thank You</div>
            <h2 class="content-title" style="font-size: 4rem; text-align: center; margin-bottom: 3rem;">
                感谢聆听
            </h2>
            <div class="big-number" style="font-size: 5rem; margin-bottom: 2rem; text-align: center;">国文汇通</div>
            <p class="description" style="text-align: center; margin: 0 auto;">
                汇聚文化之光 · 通达数字未来
            </p>
        </div>
    </div>
'''
    else:
        # 普通内容页
        title = slide['title']
        content_lines = slide['content']
        
        html += f'''
    <!-- 页面{i}：{title} -->
    <div class="page" id="page{i}" style="background: linear-gradient(rgba(10, 10, 10, 0.96), rgba(10, 10, 10, 0.98)), url('{bg}'); background-size: cover; background-position: center;">
        <div class="grid-bg"></div>
        <div class="geometric-bg"></div>
        <div class="section-number">{i-1:02d}</div>
        <h2 class="content-title">{title}</h2>
        <div class="divider-thin"></div>
        <div class="card-text" style="margin-top: 2rem; line-height: 2;">
'''
        for line in content_lines[:15]:  # 限制每页内容行数
            if line:
                html += f'            {line}<br>\n'
        
        html += '''        </div>
    </div>
'''

# 添加页码指示器
html += '''
    <!-- 全屏按钮 -->
    <button class="fullscreen-btn" onclick="toggleFullscreen()">⛶</button>
    
    <!-- 页码指示器 -->
    <div class="page-indicator">
'''
for i in range(1, 25):
    active = ' active' if i == 1 else ''
    html += f'        <div class="dot{active}" onclick="scrollToPage({i})"></div>\n'

html += '''    </div>
    
    <script>
        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
            } else {
                document.exitFullscreen();
            }
        }
        
        function scrollToPage(num) {
            document.getElementById('page' + num).scrollIntoView({ behavior: 'smooth' });
        }
        
        // 更新页码指示器
        window.addEventListener('scroll', () => {
            const pages = document.querySelectorAll('.page');
            const dots = document.querySelectorAll('.dot');
            
            pages.forEach((page, index) => {
                const rect = page.getBoundingClientRect();
                if (rect.top >= -100 && rect.top < window.innerHeight / 2) {
                    dots.forEach(d => d.classList.remove('active'));
                    if (dots[index]) dots[index].classList.add('active');
                }
            });
        });
        
        // Particles.js 初始化
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 100, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": ["#FFD700", "#D4AF37", "#FF6B35", "#6B5FFF"] },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.4, "random": true, "anim": { "enable": true, "speed": 0.8, "opacity_min": 0.15 } },
                "size": { "value": 5, "random": true, "anim": { "enable": true, "speed": 3, "size_min": 2 } },
                "line_linked": { "enable": true, "distance": 180, "color": "#FFD700", "opacity": 0.25, "width": 1.5 },
                "move": { "enable": true, "speed": 1, "direction": "none", "random": true, "out_mode": "out" }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": { "onhover": { "enable": true, "mode": "grab" }, "resize": true },
                "modes": { "grab": { "distance": 200, "line_linked": { "opacity": 0.3 } } }
            },
            "retina_detect": true
        });
    </script>
</body>
</html>
'''

# 写入文件
with open('gallery-investor-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✓ 已生成 gallery-investor-v2.html，包含 {len(slides)} 页内容")
