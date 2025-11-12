#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Photo Watermark Tool
为照片添加基于 EXIF 拍摄日期的水印
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from PIL.ExifTags import TAGS


class WatermarkConfig:
    """水印配置类"""
    
    POSITIONS = {
        'top-left': 'top_left',
        'top-center': 'top_center',
        'top-right': 'top_right',
        'center': 'center',
        'bottom-left': 'bottom_left',
        'bottom-center': 'bottom_center',
        'bottom-right': 'bottom_right',
    }
    
    def __init__(self, font_size=50, color='white', position='bottom-right', margin=20):
        self.font_size = font_size
        self.color = color
        self.position = position
        self.margin = margin


def get_exif_date(image_path):
    """
    从图片的 EXIF 信息中提取拍摄日期
    
    Args:
        image_path: 图片文件路径
        
    Returns:
        格式化的日期字符串 (YYYY-MM-DD) 或 None
    """
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if exif_data is None:
            print(f"  ⚠ {image_path.name} 没有 EXIF 信息")
            return None
        
        # 查找 DateTimeOriginal (拍摄时间) 标签
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if tag_name in ['DateTimeOriginal', 'DateTime', 'DateTimeDigitized']:
                # EXIF 日期格式通常是: "2024:11:12 14:30:45"
                date_str = value.split()[0]  # 只取日期部分
                date_str = date_str.replace(':', '-')  # 转换格式
                return date_str
        
        print(f"  ⚠ {image_path.name} 的 EXIF 中没有找到拍摄日期")
        return None
        
    except Exception as e:
        print(f"  ✗ 读取 {image_path.name} 的 EXIF 失败: {e}")
        return None


def calculate_text_position(image_size, text_bbox, position, margin):
    """
    计算文本在图片上的位置坐标
    
    Args:
        image_size: 图片尺寸 (width, height)
        text_bbox: 文本边界框 (left, top, right, bottom)
        position: 位置名称
        margin: 边距
        
    Returns:
        (x, y) 坐标元组
    """
    img_width, img_height = image_size
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    position_map = {
        'top_left': (margin, margin),
        'top_center': ((img_width - text_width) // 2, margin),
        'top_right': (img_width - text_width - margin, margin),
        'center': ((img_width - text_width) // 2, (img_height - text_height) // 2),
        'bottom_left': (margin, img_height - text_height - margin),
        'bottom_center': ((img_width - text_width) // 2, img_height - text_height - margin),
        'bottom_right': (img_width - text_width - margin, img_height - text_height - margin),
    }
    
    return position_map.get(position, position_map['bottom_right'])


def add_watermark(image_path, output_path, date_text, config):
    """
    为图片添加水印
    
    Args:
        image_path: 原始图片路径
        output_path: 输出图片路径
        date_text: 水印文本
        config: 水印配置对象
    """
    try:
        # 打开图片
        image = Image.open(image_path)
        
        # 转换为 RGB 模式（如果需要）
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # 创建绘图对象
        draw = ImageDraw.Draw(image)
        
        # 尝试加载字体
        try:
            # 尝试使用系统字体
            font = ImageFont.truetype("arial.ttf", config.font_size)
        except:
            try:
                # Windows 系统字体
                font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", config.font_size)
            except:
                # 使用默认字体
                font = ImageFont.load_default()
                print(f"  ⚠ 无法加载指定字体，使用默认字体")
        
        # 获取文本边界框
        text_bbox = draw.textbbox((0, 0), date_text, font=font)
        
        # 计算文本位置
        position = calculate_text_position(
            image.size, 
            text_bbox, 
            WatermarkConfig.POSITIONS.get(config.position, 'bottom_right'),
            config.margin
        )
        
        # 添加阴影效果（可选）
        shadow_offset = 2
        draw.text(
            (position[0] + shadow_offset, position[1] + shadow_offset),
            date_text,
            font=font,
            fill='black'
        )
        
        # 绘制主文本
        draw.text(position, date_text, font=font, fill=config.color)
        
        # 保存图片
        image.save(output_path, quality=95)
        print(f"  ✓ 已处理: {output_path.name}")
        
    except Exception as e:
        print(f"  ✗ 处理 {image_path.name} 失败: {e}")


def process_directory(input_dir, config):
    """
    处理目录下的所有图片文件
    
    Args:
        input_dir: 输入目录路径
        config: 水印配置对象
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"✗ 错误: 目录不存在 - {input_dir}")
        return
    
    if not input_path.is_dir():
        print(f"✗ 错误: 不是一个目录 - {input_dir}")
        return
    
    # 创建输出目录
    output_dir = input_path / f"{input_path.name}_watermark"
    output_dir.mkdir(exist_ok=True)
    print(f"📁 输出目录: {output_dir}")
    
    # 支持的图片格式
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif'}
    
    # 查找所有图片文件
    image_files = [
        f for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in image_extensions
    ]
    
    if not image_files:
        print(f"✗ 在目录 {input_dir} 中没有找到图片文件")
        return
    
    print(f"📷 找到 {len(image_files)} 张图片\n")
    
    # 处理每张图片
    success_count = 0
    for image_file in image_files:
        print(f"处理: {image_file.name}")
        
        # 获取 EXIF 日期
        date_text = get_exif_date(image_file)
        
        if date_text is None:
            # 如果没有 EXIF 信息，使用文件修改日期
            mod_time = datetime.fromtimestamp(image_file.stat().st_mtime)
            date_text = mod_time.strftime('%Y-%m-%d')
            print(f"  ⚠ 使用文件修改日期: {date_text}")
        
        # 输出文件路径
        output_file = output_dir / image_file.name
        
        # 添加水印
        add_watermark(image_file, output_file, date_text, config)
        success_count += 1
        print()
    
    print(f"✓ 完成! 成功处理 {success_count}/{len(image_files)} 张图片")
    print(f"📁 输出目录: {output_dir}")


def parse_color(color_str):
    """解析颜色字符串（支持颜色名称和 RGB 值）"""
    color_str = color_str.lower()
    
    # 预定义颜色
    color_map = {
        'white': 'white',
        'black': 'black',
        'red': 'red',
        'green': 'green',
        'blue': 'blue',
        'yellow': 'yellow',
        'cyan': 'cyan',
        'magenta': 'magenta',
    }
    
    if color_str in color_map:
        return color_map[color_str]
    
    # 尝试解析 RGB 格式 (如 "255,255,255")
    if ',' in color_str:
        try:
            rgb = tuple(map(int, color_str.split(',')))
            if len(rgb) == 3 and all(0 <= c <= 255 for c in rgb):
                return rgb
        except:
            pass
    
    return 'white'  # 默认颜色


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='为照片添加基于 EXIF 拍摄日期的水印',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python main.py /path/to/photos
  python main.py /path/to/photos --font-size 60 --color red
  python main.py /path/to/photos --position top-left --margin 30
  python main.py /path/to/photos --color "255,200,0"
        """
    )
    
    parser.add_argument(
        'directory',
        help='包含照片的目录路径'
    )
    
    parser.add_argument(
        '--font-size',
        type=int,
        default=50,
        help='字体大小 (默认: 50)'
    )
    
    parser.add_argument(
        '--color',
        type=str,
        default='white',
        help='字体颜色，支持颜色名称 (white/black/red/green/blue等) 或 RGB 值 (如 "255,255,255") (默认: white)'
    )
    
    parser.add_argument(
        '--position',
        type=str,
        choices=['top-left', 'top-center', 'top-right', 'center', 
                 'bottom-left', 'bottom-center', 'bottom-right'],
        default='bottom-right',
        help='水印位置 (默认: bottom-right)'
    )
    
    parser.add_argument(
        '--margin',
        type=int,
        default=20,
        help='水印边距 (像素) (默认: 20)'
    )
    
    args = parser.parse_args()
    
    # 解析颜色
    color = parse_color(args.color)
    
    # 创建配置对象
    config = WatermarkConfig(
        font_size=args.font_size,
        color=color,
        position=args.position,
        margin=args.margin
    )
    
    # 打印配置信息
    print("=" * 60)
    print("📷 Photo Watermark Tool")
    print("=" * 60)
    print(f"输入目录: {args.directory}")
    print(f"字体大小: {config.font_size}")
    print(f"字体颜色: {config.color}")
    print(f"水印位置: {args.position}")
    print(f"边距: {config.margin}px")
    print("=" * 60)
    print()
    
    # 处理图片
    process_directory(args.directory, config)


if __name__ == '__main__':
    main()
