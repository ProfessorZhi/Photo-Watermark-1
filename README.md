# Photo Watermark Tool 📷

一个简单而强大的命令行工具，用于为照片批量添加基于 EXIF 拍摄日期的水印。

## 功能特性 ✨

- 📅 自动从照片 EXIF 信息中提取拍摄日期（年-月-日格式）
- 🎨 支持自定义水印字体大小、颜色和位置
- 📁 批量处理目录下的所有图片文件
- 💾 自动在原目录下创建 `_watermark` 子目录保存处理后的图片
- 🖼️ 支持多种图片格式：JPG, PNG, BMP, TIFF
- 🎯 支持 7 种水印位置：左上、上中、右上、居中、左下、下中、右下
- 🌈 支持颜色名称和 RGB 值自定义

## 快速开始（助教运行指南）🎓

### 第一步：克隆项目

```bash
git clone https://github.com/ProfessorZhi/Photo-Watermark-1.git
cd Photo-Watermark-1
```

### 第二步：安装依赖

**Windows 系统：**
```bash
pip install -r requirements.txt
```

**Mac/Linux 系统：**
```bash
pip3 install -r requirements.txt
```

或直接安装 Pillow：
```bash
pip install Pillow
# Mac/Linux 使用: pip3 install Pillow
```

### 第三步：运行程序

#### 查看帮助信息
```bash
python main.py --help
```

#### 基本运行示例

**Windows 示例：**
```bash
# 处理指定目录的照片（使用默认设置：白色字体、右下角、字体大小50）
python main.py "C:\Users\YourName\Pictures\MyPhotos"

# 处理当前目录下的 test_images 文件夹
python main.py .\test_images
```

**Mac/Linux 示例：**
```bash
# 处理指定目录的照片
python3 main.py /home/user/photos

# 处理当前目录
python3 main.py ./photos
```

#### 自定义水印样式
```bash
# 设置字体大小和颜色
python main.py ./photos --font-size 60 --color red

# 设置水印位置（左上角）和边距
python main.py ./photos --position top-left --margin 30

# 使用 RGB 颜色值（橙色）
python main.py ./photos --color "255,165,0"

# 组合多个选项
python main.py ./photos --font-size 70 --color blue --position bottom-center --margin 40
```

### 第四步：查看结果

程序运行后，会在原目录下创建一个新的子目录：
```
原目录/
  ├── photo1.jpg
  ├── photo2.jpg
  └── 原目录_watermark/    ← 新创建的目录
      ├── photo1.jpg        ← 带水印的图片
      └── photo2.jpg
```

### 测试运行输出示例

```
============================================================
📷 Photo Watermark Tool
============================================================
输入目录: C:\Users\Admin\Pictures\Screenshots
字体大小: 50
字体颜色: white
水印位置: bottom-right
边距: 20px
============================================================

📁 输出目录: C:\Users\Admin\Pictures\Screenshots\Screenshots_watermark
📷 找到 15 张图片

处理: IMG_001.jpg
  ✓ 已处理: IMG_001.jpg

处理: IMG_002.jpg
  ⚠ IMG_002.jpg 没有 EXIF 信息
  ⚠ 使用文件修改日期: 2025-11-12
  ✓ 已处理: IMG_002.jpg

...

✓ 完成! 成功处理 15/15 张图片
📁 输出目录: C:\Users\Admin\Pictures\Screenshots\Screenshots_watermark
```

## 安装依赖 📦

```bash
pip install -r requirements.txt
```

或直接安装：

```bash
pip install Pillow
```

## 使用方法 🚀

### 基本用法

```bash
python main.py /path/to/photos
```

### 自定义选项

```bash
# 设置字体大小和颜色
python main.py /path/to/photos --font-size 60 --color red

# 设置水印位置和边距
python main.py /path/to/photos --position top-left --margin 30

# 使用 RGB 颜色值
python main.py /path/to/photos --color "255,200,0"

# 组合使用多个选项
python main.py /path/to/photos --font-size 70 --color blue --position bottom-center --margin 40
```

## 命令行参数 ⚙️

| 参数 | 说明 | 默认值 | 可选值 |
|------|------|--------|--------|
| `directory` | 照片所在目录路径 | *必填* | - |
| `--font-size` | 字体大小 | 50 | 任意正整数 |
| `--color` | 字体颜色 | white | white, black, red, green, blue, yellow, cyan, magenta 或 RGB (如 "255,255,255") |
| `--position` | 水印位置 | bottom-right | top-left, top-center, top-right, center, bottom-left, bottom-center, bottom-right |
| `--margin` | 水印边距（像素） | 20 | 任意正整数 |

## 工作流程 🔄

1. **扫描目录**：程序扫描指定目录下的所有图片文件
2. **读取 EXIF**：从每张照片的 EXIF 信息中提取拍摄日期
3. **备用方案**：如果照片没有 EXIF 信息，使用文件的修改日期
4. **添加水印**：根据配置在照片上绘制日期水印（带阴影效果）
5. **保存文件**：将处理后的照片保存到 `原目录名_watermark` 子目录

## 输出示例 📸

```
============================================================
📷 Photo Watermark Tool
============================================================
输入目录: E:\Photos\2024-Trip
字体大小: 50
字体颜色: white
水印位置: bottom-right
边距: 20px
============================================================

📁 输出目录: E:\Photos\2024-Trip\2024-Trip_watermark
📷 找到 15 张图片

处理: IMG_001.jpg
  ✓ 已处理: IMG_001.jpg

处理: IMG_002.jpg
  ✓ 已处理: IMG_002.jpg

...

✓ 完成! 成功处理 15/15 张图片
📁 输出目录: E:\Photos\2024-Trip\2024-Trip_watermark
```

## 技术栈 🛠️

- **Python 3.8+**：主要编程语言
- **Pillow (PIL)**：图像处理库，用于读取 EXIF、绘制水印
- **argparse**：命令行参数解析
- **pathlib**：现代化的文件路径处理

## 常见问题 FAQ ❓

### Q1: 如何确认 Python 已安装？
```bash
python --version
# 或
python3 --version
```
应该显示类似 `Python 3.9.13` 的版本信息。

### Q2: 如果没有安装 Python 怎么办？
- **Windows**: 访问 [python.org](https://www.python.org/downloads/) 下载安装
- **Mac**: 使用 `brew install python3`
- **Linux**: 使用 `sudo apt install python3` (Ubuntu/Debian)

### Q3: 程序提示找不到模块？
```bash
# 确保已安装 Pillow
pip install Pillow
```

### Q4: 如何处理包含空格的路径？
使用引号括起来：
```bash
python main.py "C:\My Photos\Summer 2024"
```

### Q5: 水印看不清怎么办？
尝试以下选项：
- 更改颜色：`--color black` 或 `--color white`
- 增加字体大小：`--font-size 80`
- 调整位置：`--position top-left`

### Q6: 可以处理哪些图片格式？
支持：JPG, JPEG, PNG, BMP, TIFF, TIF

### Q7: 原图会被修改吗？
不会！原图完全保留，带水印的图片保存在新的 `_watermark` 子目录中。

### Q8: 截图文件没有 EXIF 怎么办？
程序会自动使用文件的修改日期作为水印内容。

## 注意事项 ⚠️

- 仅处理当前目录下的图片文件，不包括子目录
- 如果照片没有 EXIF 信息，将使用文件的修改日期
- 输出图片为高质量 JPEG 格式（质量参数 95）
- 水印带有黑色阴影，增强可读性
- 原始照片不会被修改，可以放心使用

## Git 提交记录 📝

本项目包含至少 2 次提交和 1 个标签：
- ✅ 第 1 次 commit: 初始化项目，实现核心功能
- ✅ 第 2 次 commit: 添加使用示例和文档
- ✅ 标签: version1.0

查看提交历史：
```bash
git log --oneline --decorate
```

## 许可证 📄

MIT License

## 作者 👨‍💻

Vibe Coding Project

## 联系方式 📧

- GitHub: [ProfessorZhi/Photo-Watermark-1](https://github.com/ProfessorZhi/Photo-Watermark-1)
- 问题反馈: 请在 GitHub Issues 中提交
