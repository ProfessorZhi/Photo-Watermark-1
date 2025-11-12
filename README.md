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

## 注意事项 ⚠️

- 仅处理当前目录下的图片文件，不包括子目录
- 如果照片没有 EXIF 信息，将使用文件的修改日期
- 输出图片为高质量 JPEG 格式（质量参数 95）
- 水印带有黑色阴影，增强可读性

## 许可证 📄

MIT License

## 作者 👨‍💻

Vibe Coding Project
