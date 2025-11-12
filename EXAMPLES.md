# 使用示例 📖

## 快速开始

### 1. 准备测试图片

假设你有一个包含照片的目录：
```
E:\Photos\2024-Trip\
    ├── IMG_001.jpg
    ├── IMG_002.jpg
    └── IMG_003.jpg
```

### 2. 基本使用（使用默认设置）

```bash
python main.py "E:\Photos\2024-Trip"
```

**输出结果：**
```
E:\Photos\2024-Trip\
    ├── IMG_001.jpg
    ├── IMG_002.jpg
    ├── IMG_003.jpg
    └── 2024-Trip_watermark\      # 新创建的目录
        ├── IMG_001.jpg           # 带水印的图片
        ├── IMG_002.jpg
        └── IMG_003.jpg
```

## 进阶使用示例

### 示例 1：大字体白色水印在右下角

```bash
python main.py "E:\Photos\2024-Trip" --font-size 70 --color white --position bottom-right
```

适合：深色背景的照片

### 示例 2：红色水印在左上角

```bash
python main.py "E:\Photos\2024-Trip" --font-size 50 --color red --position top-left --margin 30
```

适合：浅色背景的照片，需要醒目标记

### 示例 3：黄色水印居中

```bash
python main.py "E:\Photos\2024-Trip" --font-size 80 --color yellow --position center
```

适合：需要明显日期标记的场景

### 示例 4：使用自定义 RGB 颜色

```bash
# 橙色水印 (RGB: 255, 165, 0)
python main.py "E:\Photos\2024-Trip" --color "255,165,0" --position bottom-center

# 淡蓝色水印 (RGB: 135, 206, 235)
python main.py "E:\Photos\2024-Trip" --color "135,206,235" --font-size 60
```

### 示例 5：小字体水印在角落

```bash
python main.py "E:\Photos\2024-Trip" --font-size 30 --color white --position bottom-right --margin 10
```

适合：不想让水印太显眼的场景

## 常见场景配置

### 旅行照片（户外风景）
```bash
python main.py ./photos --font-size 60 --color white --position bottom-right --margin 25
```

### 活动照片（室内）
```bash
python main.py ./photos --font-size 55 --color yellow --position bottom-left --margin 30
```

### 证件照片（需要明显日期）
```bash
python main.py ./photos --font-size 45 --color red --position top-right --margin 15
```

### 艺术摄影（低调水印）
```bash
python main.py ./photos --font-size 35 --color white --position bottom-right --margin 15
```

## 颜色参考表

| 颜色名称 | 效果 | 适用场景 |
|---------|------|----------|
| `white` | 白色 | 深色背景照片 |
| `black` | 黑色 | 浅色背景照片 |
| `red` | 红色 | 需要醒目标记 |
| `yellow` | 黄色 | 中等亮度背景 |
| `blue` | 蓝色 | 温暖色调照片 |
| `green` | 绿色 | 城市/建筑照片 |
| `cyan` | 青色 | 日落/黄昏照片 |
| `magenta` | 品红 | 自然风景照片 |

## 位置参考图

```
┌─────────────────────────────────┐
│ top-left    top-center  top-right│
│                                   │
│                                   │
│           center                  │
│                                   │
│                                   │
│bottom-left bottom-center bottom-right│
└─────────────────────────────────┘
```

## 批量处理技巧

### 处理多个目录

创建一个批处理脚本 `process_all.bat` (Windows):
```batch
@echo off
python main.py "E:\Photos\2024-01-January" --font-size 50 --color white
python main.py "E:\Photos\2024-02-February" --font-size 50 --color white
python main.py "E:\Photos\2024-03-March" --font-size 50 --color white
echo All done!
pause
```

或者 PowerShell 脚本 `process_all.ps1`:
```powershell
$folders = @(
    "E:\Photos\2024-01-January",
    "E:\Photos\2024-02-February",
    "E:\Photos\2024-03-March"
)

foreach ($folder in $folders) {
    Write-Host "Processing: $folder"
    python main.py $folder --font-size 50 --color white --position bottom-right
}

Write-Host "All done!"
```

### Linux/Mac 批处理

创建 `process_all.sh`:
```bash
#!/bin/bash

folders=(
    "/home/user/Photos/2024-01-January"
    "/home/user/Photos/2024-02-February"
    "/home/user/Photos/2024-03-March"
)

for folder in "${folders[@]}"; do
    echo "Processing: $folder"
    python3 main.py "$folder" --font-size 50 --color white --position bottom-right
done

echo "All done!"
```

## 注意事项

1. **路径包含空格**：使用引号括起来
   ```bash
   python main.py "E:\My Photos\Summer 2024"
   ```

2. **原图保护**：原始照片不会被修改，新图片保存在 `_watermark` 子目录

3. **EXIF 信息**：如果照片没有 EXIF 信息，程序会自动使用文件修改日期

4. **支持格式**：JPG, JPEG, PNG, BMP, TIFF, TIF

5. **字体问题**：如果系统找不到字体文件，会使用默认字体（可能较小）

## 故障排除

### 问题：找不到 Python
```bash
# Windows: 使用完整路径
C:\Python39\python.exe main.py ./photos

# 或者使用 py 启动器
py main.py ./photos
```

### 问题：Pillow 未安装
```bash
pip install Pillow
# 或
pip install -r requirements.txt
```

### 问题：字体太小
默认字体可能很小，建议指定较大的字体大小：
```bash
python main.py ./photos --font-size 80
```

### 问题：水印看不清
- 尝试更改颜色（白色换黑色，或反之）
- 增加字体大小
- 调整位置避开照片主体

## 获取帮助

查看所有可用选项：
```bash
python main.py --help
```
