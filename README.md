# QAutoWeChat 🤖💬

基于 Qwen 语言模型的微信自动回复工具 | [English Documentation](#) （可选）

![License](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## 目录
- [项目功能](#项目功能)
- [快速开始](#快速开始)
  - [环境配置](#环境配置)
  - [使用步骤](#使用步骤)
- [项目特点](#项目特点)
- [已知问题](#已知问题)
- [未来计划](#未来计划)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

## 项目功能
- **智能监听**：自动识别微信窗口，精准定位联系人
- **无缝衔接**：通过本地 API 连接语言模型（默认集成 Qwen）
- **灵活扩展**：支持替换/微调本地大语言模型
- **解放双手**：全自动消息监听与回复流程

## 快速开始

### 环境配置
**强烈建议使用 Anaconda 为auto-WX.py和qwen-api-main.py创建两个独立环境**：

1. **Auto-WX 环境（微信自动化）**：
   ```bash
   conda create -n wx-auto python=3.8
   conda activate wx-auto
   pip install wxauto requests
   ```

2. **Qwen-API 环境（模型服务）**：
   ```bash
   conda create -n qwen-api python=3.8
   conda activate qwen-api
   pip install transformers flask
   ```

### 使用步骤
1. **启动模型服务**：
   ```bash
   conda activate qwen-api
   python qwen-api-main.py
   ```
   > 看到 ` * Running on http://127.0.0.1:5000` 表示服务已启动

2. **配置监听名单**：
   - 打开 `auto-wx.py`
   - 修改第12行：`listen_list = ['小号']` → 填入目标微信昵称（支持多个用户）

3. **启动微信自动化**：
   ```bash
   conda activate wx-auto
   python auto-wx.py
   ```

## 项目特点
✅ **精准定位**  
- 智能识别微信主界面/聊天窗口，自动搜索目标联系人

🚀 **一键部署**  
- 双环境隔离设计，避免依赖冲突
- 本地 API 服务，轻松切换不同语言模型

⚙️ **模块化架构**  
```text
├── auto-wx.py          # 微信自动化客户端
└── qwen-api-main.py    # 模型服务端（可替换模型）
```

## 已知问题
⚠️ **性能提示**  
- 中低端设备回复延迟：测试目标（联想拯救者Y9000P RTX4060）设备测试响应时间约 9 秒
- 首次加载模型需要较长时间（取决于硬盘速度）

🛠 **兼容性说明**  
- 当前版本需手动编辑代码配置，后续将提供图形界面
- 微信版本更新可能导致窗口识别失效（我们将持续跟进）

## 未来计划
- [ ] 添加命令行参数配置功能
- [ ] 开发可视化配置界面
- [ ] 支持多模型热切换
- [ ] 增加消息过滤规则

## 贡献指南
欢迎通过 Issue 或 PR 参与改进！包括但不限于：
- 优化窗口识别逻辑
- 添加新的语言模型支持
- 改进错误处理机制

## 许可证
[MIT License](LICENSE) © 2025 [Liuce CN]
