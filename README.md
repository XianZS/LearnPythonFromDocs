# 🐍 从官方文档学`Python`

（`LearnPythonFromDocs`）

> 不刷短视频教程，不背二手笔记 —— 直接啃 **`Python` 3.14 官方教程（中文翻译版）**，配合本地可运行的示例脚本，一边看文档一边敲代码。
>
> 本仓库是 B 站系列视频 **《从官方文档学 `Python`》** 的配套代码与规划文档。

## 目录

- [系列简介](#系列简介)
- [B 站系列（合集）](#b-站系列合集)
- [获取项目（git clone）](#获取项目git-clone)
- [环境说明](#环境说明)
- [项目结构](#项目结构)
- [如何运行示例](#如何运行示例)

## 🎬 系列简介

本系列以 **`Python` 3.14 官方教程**（《`The Python Tutorial`》）为主线，从第 1 章「课前甜点」讲到第 16 章「附录」，每一章对应一期（或几期）视频：

- 📖 以官方文档为准，术语、示例、顺序全部对齐文档原文；
- 💻 每节配套一个独立 `.py` 脚本，跟着敲、随手改、立刻跑；
- 🐍 全程使用 `conda` 环境 `lpfd`（Python 3.14），与文档版本保持一致。

## 📺 B 站系列（合集）

🔗 合集地址：<https://space.bilibili.com/3690991649294439/lists/8804339>

每期视频发布后，配套脚本会同步提交到本仓库。

## 📥 获取项目（`git clone`）

```bash
# SSH 方式
git clone git@github.com:XianZS/LearnPythonFromDocs.git

# 或 HTTPS 方式
git clone https://github.com/XianZS/LearnPythonFromDocs.git

cd LearnPythonFromDocs
```

## ⚙️ 环境说明

本机开发环境：

| 项目 | 值 |
| --- | --- |
| `conda` 环境 | `lpfd` |
| `Python` 版本 | 3.14.6（`/home/byqh/miniconda3/envs/lpfd/bin/python`） |
| 官方文档版本 | `Python` 3.14 中文翻译版 |
| 操作系统 | `Linux`（`WSL2`） |

激活与验证：

```bash
# 创建 conda 环境（首次使用）
conda create -n lpfd python=3.14

# 激活环境
conda activate lpfd

# 验证环境
python --version   # 期望输出 Python 3.14.x
```

## 📁 项目结构

```text
LearnPythonFromDocs/
├── README.md                        # 本文件：教程说明与使用指南
└── Tutorial/                        # 每集配套示例脚本，按官方文档章节组织
    ├── Chapter_1/                   # 1. 课前甜点
    ├── Chapter_2/                   # 2. 使用 Python 的解释器
    ├── Chapter_3/                   # 3. Python 速览
    ├── Chapter_4/                   # 4. 更多控制流工具
    ├── Chapter_5/                   # 5. 数据结构
    ├── Chapter_6/                   # 6. 模块
    ├── Chapter_7/                   # 7. 输入与输出
    ├── Chapter_8/                   # 8. 错误和异常
    ├── Chapter_9/                   # 9. 类
    ├── Chapter_10/                  # 10. 标准库概览
    ├── Chapter_11/                  # 11. 标准库概览 --- 第二部分
    ├── Chapter_12/                  # 12. 虚拟环境和包
    ├── Chapter_13/                  # 13. 接下来？
    ├── Chapter_14/                  # 14. 交互式编辑和编辑历史
    ├── Chapter_15/                  # 15. 浮点算术：问题和限制
    └── Chapter_16/                  # 16. 附录
```

脚本命名规则：`<章>_<节>_<主题>_use.py`，与官方文档的小节编号一一对应。

## ▶️ 如何运行示例

```bash
# 激活环境
conda activate lpfd

# 运行任意脚本
python Tutorial/Chapter_2/2_1_1.py hello world
python Tutorial/Chapter_4/4_1_if_use.py
python Tutorial/Chapter_4/4_3_range_use.py
```

需要交互输入的脚本（如 `4_1_if_use.py` 会 `input()`）直接在终端里输入即可。

## 📧 联系

联系：QQ3135989009
邮箱同上@qq
