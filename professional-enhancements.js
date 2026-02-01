// 专业化增强脚本 - 防翻车必备

// 全屏功能
function toggleFullscreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
            console.log(`Error attempting to enable fullscreen: ${err.message}`);
        });
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}

// 创建全屏按钮
function createFullscreenButton() {
    const btn = document.createElement('button');
    btn.className = 'fullscreen-btn';
    btn.title = '全屏模式 (F11)';
    btn.innerHTML = `
        <svg viewBox="0 0 24 24">
            <path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>
        </svg>
    `;
    btn.onclick = toggleFullscreen;
    document.body.appendChild(btn);
}

// 键盘快捷键
document.addEventListener('keydown', (e) => {
    // F11 全屏
    if (e.key === 'F11') {
        e.preventDefault();
        toggleFullscreen();
    }
    
    // Esc 退出全屏
    if (e.key === 'Escape' && document.fullscreenElement) {
        document.exitFullscreen();
    }
});

// 页面加载完成后初始化
window.addEventListener('DOMContentLoaded', () => {
    // 创建加载动画
    const loadingOverlay = document.createElement('div');
    loadingOverlay.className = 'loading-overlay';
    loadingOverlay.innerHTML = '<div class="loading-spinner"></div>';
    document.body.appendChild(loadingOverlay);
    
    // 创建全屏按钮
    createFullscreenButton();
    
    // 页面完全加载后隐藏加载动画
    window.addEventListener('load', () => {
        setTimeout(() => {
            loadingOverlay.classList.add('hidden');
            setTimeout(() => loadingOverlay.remove(), 600);
        }, 500);
    });
});

// 滚轮翻页功能（配合Reveal.js）
let isScrolling = false;
document.addEventListener('wheel', (e) => {
    if (isScrolling) return;
    
    isScrolling = true;
    setTimeout(() => isScrolling = false, 800);
    
    if (e.deltaY > 0) {
        Reveal.next();
    } else if (e.deltaY < 0) {
        Reveal.prev();
    }
}, { passive: true });

// 移动端触摸滑动
let touchStartY = 0;
document.addEventListener('touchstart', (e) => {
    touchStartY = e.touches[0].clientY;
}, { passive: true });

document.addEventListener('touchend', (e) => {
    const touchEndY = e.changedTouches[0].clientY;
    const diff = touchStartY - touchEndY;
    
    if (Math.abs(diff) > 50) {
        if (diff > 0) {
            Reveal.next();
        } else {
            Reveal.prev();
        }
    }
}, { passive: true });

// 打印前优化
window.addEventListener('beforeprint', () => {
    // 展开所有幻灯片以便打印
    Reveal.configure({ embedded: true });
});

window.addEventListener('afterprint', () => {
    // 恢复正常模式
    Reveal.configure({ embedded: false });
});

// 性能监控（可选）
if (window.performance && window.performance.timing) {
    window.addEventListener('load', () => {
        const loadTime = window.performance.timing.loadEventEnd - window.performance.timing.navigationStart;
        console.log(`页面加载时间: ${loadTime}ms`);
    });
}
