# -*- coding: utf-8 -*-
"""
为 gallery-investor-v2.html 添加旁白功能
"""

import json

# 读取旁白数据
with open('speaker_notes.json', 'r', encoding='utf-8') as f:
    notes = json.load(f)

# 读取现有HTML
with open('gallery-investor-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 在 </style> 之前添加旁白相关样式
speaker_notes_css = '''
        /* ==================== 旁白功能样式 ==================== */
        
        /* 旁白触发按钮 */
        .notes-trigger {
            position: fixed;
            bottom: 30px;
            right: 90px;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.15), rgba(212, 175, 55, 0.15));
            border: 1px solid rgba(255, 215, 0, 0.4);
            border-radius: 8px;
            color: #FFD700;
            font-size: 20px;
            cursor: pointer;
            z-index: 999;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            backdrop-filter: blur(10px);
        }
        
        .notes-trigger:hover {
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.3), rgba(212, 175, 55, 0.3));
            transform: scale(1.1);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.4);
        }
        
        .notes-trigger.active {
            background: linear-gradient(135deg, rgba(255, 215, 0, 0.9), rgba(212, 175, 55, 0.9));
            color: #000;
        }
        
        /* 底部抽屉 */
        .notes-drawer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 35vh;
            background: linear-gradient(180deg, rgba(10, 10, 10, 0.98), rgba(15, 15, 15, 0.98));
            border-top: 2px solid rgba(255, 215, 0, 0.3);
            transform: translateY(100%);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 998;
            backdrop-filter: blur(20px);
            box-shadow: 0 -10px 50px rgba(0, 0, 0, 0.5);
        }
        
        .notes-drawer.open {
            transform: translateY(0);
        }
        
        .notes-drawer-handle {
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 4px;
            background: rgba(255, 215, 0, 0.4);
            border-radius: 2px;
            margin-top: 8px;
            cursor: pointer;
        }
        
        .notes-drawer-content {
            padding: 3rem 8vw 2rem;
            height: 100%;
            overflow-y: auto;
        }
        
        .notes-drawer-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
            color: #FFD700;
            margin-bottom: 0.5rem;
            letter-spacing: 0.05em;
        }
        
        .notes-drawer-page {
            font-size: 0.75rem;
            color: rgba(255, 215, 0, 0.6);
            text-transform: uppercase;
            letter-spacing: 0.2em;
            margin-bottom: 1.5rem;
        }
        
        .notes-drawer-text {
            font-size: 1.05rem;
            line-height: 2;
            color: rgba(255, 255, 255, 0.85);
            max-width: 900px;
        }
        
        /* 侧边栏模式 */
        .notes-sidebar {
            position: fixed;
            top: 0;
            right: 0;
            width: 400px;
            height: 100vh;
            background: linear-gradient(90deg, rgba(10, 10, 10, 0.95), rgba(15, 15, 15, 0.98));
            border-left: 2px solid rgba(255, 215, 0, 0.3);
            transform: translateX(100%);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 997;
            backdrop-filter: blur(20px);
            box-shadow: -10px 0 50px rgba(0, 0, 0, 0.5);
            overflow-y: auto;
        }
        
        .notes-sidebar.open {
            transform: translateX(0);
        }
        
        .notes-sidebar-content {
            padding: 4rem 2rem;
        }
        
        .notes-sidebar-close {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 30px;
            height: 30px;
            background: transparent;
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 4px;
            color: #FFD700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }
        
        .notes-sidebar-close:hover {
            background: rgba(255, 215, 0, 0.2);
            transform: rotate(90deg);
        }
        
        /* 模式切换按钮 */
        .notes-mode-toggle {
            position: fixed;
            bottom: 30px;
            right: 150px;
            padding: 0.6rem 1.2rem;
            background: rgba(255, 215, 0, 0.1);
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 6px;
            color: #FFD700;
            font-size: 0.75rem;
            letter-spacing: 0.1em;
            cursor: pointer;
            z-index: 999;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }
        
        .notes-mode-toggle:hover {
            background: rgba(255, 215, 0, 0.2);
            transform: translateY(-2px);
        }
        
        /* 快捷键提示 */
        .keyboard-hint {
            position: fixed;
            bottom: 95px;
            right: 90px;
            padding: 0.5rem 1rem;
            background: rgba(10, 10, 10, 0.9);
            border: 1px solid rgba(255, 215, 0, 0.2);
            border-radius: 4px;
            color: rgba(255, 215, 0, 0.7);
            font-size: 0.7rem;
            letter-spacing: 0.05em;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
            z-index: 1000;
            backdrop-filter: blur(10px);
        }
        
        .keyboard-hint.show {
            opacity: 1;
        }
        
        .keyboard-hint kbd {
            display: inline-block;
            padding: 0.2rem 0.5rem;
            background: rgba(255, 215, 0, 0.2);
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 3px;
            font-family: monospace;
            font-size: 0.8rem;
            margin: 0 0.2rem;
        }
        
        /* 演讲者模式提示 */
        .speaker-mode-hint {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 3rem 4rem;
            background: rgba(10, 10, 10, 0.95);
            border: 2px solid rgba(255, 215, 0, 0.4);
            border-radius: 12px;
            text-align: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
            z-index: 1001;
            backdrop-filter: blur(20px);
        }
        
        .speaker-mode-hint.show {
            opacity: 1;
            pointer-events: auto;
        }
        
        .speaker-mode-hint h3 {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            color: #FFD700;
            margin-bottom: 1rem;
        }
        
        .speaker-mode-hint p {
            color: rgba(255, 255, 255, 0.7);
            line-height: 1.8;
            margin-bottom: 2rem;
        }
        
        .speaker-mode-hint button {
            padding: 0.8rem 2rem;
            background: linear-gradient(135deg, #FFD700, #D4AF37);
            border: none;
            border-radius: 6px;
            color: #000;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .speaker-mode-hint button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(255, 215, 0, 0.4);
        }
        
        /* 响应式 */
        @media (max-width: 768px) {
            .notes-sidebar {
                width: 100%;
            }
            
            .notes-drawer {
                height: 50vh;
            }
            
            .notes-mode-toggle {
                display: none;
            }
        }
'''

html = html.replace('</style>', speaker_notes_css + '\n    </style>')

# 在 </body> 之前添加旁白HTML结构和JavaScript
speaker_notes_html = '''
    <!-- 旁白功能 -->
    <button class="notes-trigger" onclick="toggleNotes()" title="演讲者备注 (N)">
        <span id="notes-icon">📝</span>
    </button>
    
    <button class="notes-mode-toggle" onclick="toggleNotesMode()">
        <span id="mode-text">切换侧边栏</span>
    </button>
    
    <div class="keyboard-hint" id="keyboard-hint">
        按 <kbd>N</kbd> 切换旁白 · 按 <kbd>S</kbd> 演讲者模式
    </div>
    
    <!-- 底部抽屉 -->
    <div class="notes-drawer" id="notes-drawer">
        <div class="notes-drawer-handle" onclick="toggleNotes()"></div>
        <div class="notes-drawer-content">
            <div class="notes-drawer-page" id="drawer-page">Page 1 of 24</div>
            <div class="notes-drawer-title" id="drawer-title">封面 - 国文汇通</div>
            <div class="notes-drawer-text" id="drawer-text">
                各位投资人，大家好...
            </div>
        </div>
    </div>
    
    <!-- 侧边栏 -->
    <div class="notes-sidebar" id="notes-sidebar">
        <button class="notes-sidebar-close" onclick="toggleNotes()">✕</button>
        <div class="notes-sidebar-content">
            <div class="notes-drawer-page" id="sidebar-page">Page 1 of 24</div>
            <div class="notes-drawer-title" id="sidebar-title">封面 - 国文汇通</div>
            <div class="notes-drawer-text" id="sidebar-text">
                各位投资人，大家好...
            </div>
        </div>
    </div>
    
    <!-- 演讲者模式提示 -->
    <div class="speaker-mode-hint" id="speaker-mode-hint">
        <h3>演讲者模式</h3>
        <p>
            将在新窗口打开演讲者视图<br>
            包含当前页预览、旁白文档和计时器
        </p>
        <button onclick="openSpeakerMode()">打开演讲者模式</button>
        <button onclick="closeSpeakerHint()" style="background: transparent; border: 1px solid rgba(255,215,0,0.3); color: #FFD700; margin-left: 1rem;">取消</button>
    </div>
    
    <script>
        // 旁白数据
        const speakerNotes = ''' + json.dumps(notes, ensure_ascii=False) + ''';
        
        let notesMode = 'drawer'; // 'drawer' or 'sidebar'
        let notesOpen = false;
        let currentPage = 1;
        
        // 更新旁白内容
        function updateNotes(pageNum) {
            currentPage = pageNum;
            const note = speakerNotes[pageNum.toString()];
            
            if (note) {
                // 更新抽屉
                document.getElementById('drawer-page').textContent = `Page ${pageNum} of 24`;
                document.getElementById('drawer-title').textContent = note.title;
                document.getElementById('drawer-text').textContent = note.notes;
                
                // 更新侧边栏
                document.getElementById('sidebar-page').textContent = `Page ${pageNum} of 24`;
                document.getElementById('sidebar-title').textContent = note.title;
                document.getElementById('sidebar-text').textContent = note.notes;
            }
        }
        
        // 切换旁白显示
        function toggleNotes() {
            notesOpen = !notesOpen;
            const trigger = document.querySelector('.notes-trigger');
            
            if (notesMode === 'drawer') {
                const drawer = document.getElementById('notes-drawer');
                drawer.classList.toggle('open', notesOpen);
            } else {
                const sidebar = document.getElementById('notes-sidebar');
                sidebar.classList.toggle('open', notesOpen);
            }
            
            trigger.classList.toggle('active', notesOpen);
        }
        
        // 切换显示模式
        function toggleNotesMode() {
            const drawer = document.getElementById('notes-drawer');
            const sidebar = document.getElementById('notes-sidebar');
            const modeText = document.getElementById('mode-text');
            
            if (notesMode === 'drawer') {
                notesMode = 'sidebar';
                drawer.classList.remove('open');
                if (notesOpen) sidebar.classList.add('open');
                modeText.textContent = '切换抽屉';
            } else {
                notesMode = 'drawer';
                sidebar.classList.remove('open');
                if (notesOpen) drawer.classList.add('open');
                modeText.textContent = '切换侧边栏';
            }
        }
        
        // 打开演讲者模式
        function openSpeakerMode() {
            const speakerWindow = window.open('', 'SpeakerView', 'width=1200,height=800');
            speakerWindow.document.write(`
                <!DOCTYPE html>
                <html>
                <head>
                    <title>演讲者视图 - 国文汇通</title>
                    <style>
                        * { margin: 0; padding: 0; box-sizing: border-box; }
                        body {
                            font-family: 'Inter', sans-serif;
                            background: #0A0A0A;
                            color: #F9F9F7;
                            padding: 2rem;
                        }
                        .container {
                            display: grid;
                            grid-template-columns: 1fr 1fr;
                            gap: 2rem;
                            height: 100vh;
                        }
                        .preview {
                            border: 2px solid rgba(255, 215, 0, 0.3);
                            border-radius: 8px;
                            padding: 1rem;
                        }
                        .preview h2 {
                            color: #FFD700;
                            margin-bottom: 1rem;
                        }
                        .notes {
                            border: 2px solid rgba(255, 215, 0, 0.3);
                            border-radius: 8px;
                            padding: 2rem;
                            overflow-y: auto;
                        }
                        .notes h3 {
                            color: #FFD700;
                            margin-bottom: 1rem;
                        }
                        .notes p {
                            line-height: 2;
                            font-size: 1.1rem;
                        }
                        .timer {
                            position: fixed;
                            top: 2rem;
                            right: 2rem;
                            font-size: 3rem;
                            color: #FFD700;
                            font-family: monospace;
                        }
                        .page-info {
                            color: rgba(255, 215, 0, 0.7);
                            margin-bottom: 0.5rem;
                        }
                    </style>
                </head>
                <body>
                    <div class="timer" id="timer">00:00</div>
                    <div class="container">
                        <div class="preview">
                            <h2>当前页面</h2>
                            <div class="page-info" id="page-info">Page 1 of 24</div>
                            <iframe src="${window.location.href}" style="width: 100%; height: 80%; border: none; border-radius: 4px;"></iframe>
                        </div>
                        <div class="notes">
                            <h3 id="note-title">演讲者备注</h3>
                            <p id="note-text">准备开始演讲...</p>
                        </div>
                    </div>
                    <script>
                        const notes = ${JSON.stringify(notes)};
                        let seconds = 0;
                        
                        setInterval(() => {
                            seconds++;
                            const mins = Math.floor(seconds / 60);
                            const secs = seconds % 60;
                            document.getElementById('timer').textContent = 
                                String(mins).padStart(2, '0') + ':' + String(secs).padStart(2, '0');
                        }, 1000);
                        
                        // 监听主窗口的页面变化
                        window.addEventListener('message', (e) => {
                            if (e.data.type === 'pageChange') {
                                const pageNum = e.data.page;
                                const note = notes[pageNum.toString()];
                                if (note) {
                                    document.getElementById('page-info').textContent = \`Page \${pageNum} of 24\`;
                                    document.getElementById('note-title').textContent = note.title;
                                    document.getElementById('note-text').textContent = note.notes;
                                }
                            }
                        });
                    </script>
                </body>
                </html>
            `);
            closeSpeakerHint();
        }
        
        function closeSpeakerHint() {
            document.getElementById('speaker-mode-hint').classList.remove('show');
        }
        
        // 键盘快捷键
        document.addEventListener('keydown', (e) => {
            if (e.key === 'n' || e.key === 'N') {
                toggleNotes();
            } else if (e.key === 's' || e.key === 'S') {
                document.getElementById('speaker-mode-hint').classList.add('show');
            } else if (e.key === 'Escape') {
                if (notesOpen) toggleNotes();
                closeSpeakerHint();
            }
        });
        
        // 显示快捷键提示
        setTimeout(() => {
            document.getElementById('keyboard-hint').classList.add('show');
            setTimeout(() => {
                document.getElementById('keyboard-hint').classList.remove('show');
            }, 5000);
        }, 2000);
        
        // 监听页面滚动，更新旁白
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                const pages = document.querySelectorAll('.page');
                pages.forEach((page, index) => {
                    const rect = page.getBoundingClientRect();
                    if (rect.top >= -100 && rect.top < window.innerHeight / 2) {
                        updateNotes(index + 1);
                        
                        // 通知演讲者窗口
                        if (window.opener) {
                            window.opener.postMessage({ type: 'pageChange', page: index + 1 }, '*');
                        }
                    }
                });
            }, 100);
        });
        
        // 初始化
        updateNotes(1);
    </script>
'''

html = html.replace('</body>', speaker_notes_html + '\n</body>')

# 写入文件
with open('gallery-investor-v2.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ 已为 gallery-investor-v2.html 添加旁白功能")
print("\n功能说明：")
print("1. 点击右下角 📝 按钮：展开/收起旁白")
print("2. 按键盘 N 键：快速切换旁白显示")
print("3. 按键盘 S 键：打开演讲者模式（新窗口）")
print("4. 点击'切换侧边栏'按钮：在抽屉和侧边栏模式间切换")
print("5. 旁白会自动跟随页面滚动更新")
