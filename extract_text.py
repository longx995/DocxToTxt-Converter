#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用纯文本提取方式批量转换特殊格式的doc/docx文件
适用于非标准格式的文档文件
"""

import os
import re
from pathlib import Path


def extract_chinese_text(file_path):
    """从文件中提取中文文本"""
    try:
        # 以二进制方式读取文件
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # 尝试多种编码方式解码
        text = None
        for encoding in ['gbk', 'gb18030', 'gb2312', 'utf-8', 'big5']:
            try:
                text = content.decode(encoding, errors='ignore')
                if text:
                    break
            except:
                continue
        
        if not text:
            return None
        
        # 提取可打印字符（包括中文、英文、数字、标点符号）
        pattern = r'[\u4e00-\u9fff\u3000-\u303fa-zA-Z0-9\s，。！？、；：""''（）《》【】…—·\-\.\,\!\?\;\:\'\"\(\)\[\]\n\r\t]+'
        matches = re.findall(pattern, text)
        
        if not matches:
            return None
        
        # 合并所有匹配的文本
        extracted_text = ' '.join(matches)
        
        # 清理：移除过多的空格
        # 保持原有的换行符，只清理多余的空格
        extracted_text = re.sub(r' +', ' ', extracted_text)  # 多个空格替换为单个
        extracted_text = re.sub(r' +\n', '\n', extracted_text)  # 行尾空格
        extracted_text = re.sub(r'\n +', '\n', extracted_text)  # 行首空格
        
        # 移除空行但保持段落结构
        lines = [line.strip() for line in extracted_text.split('\n')]
        lines = [line for line in lines if line and len(line) > 1]
        
        result = '\n'.join(lines)
        return result if result else None
        
    except Exception as e:
        return None


def convert_to_txt(source_file, output_file=None):
    """转换文件为txt"""
    if output_file is None:
        output_file = str(Path(source_file).with_suffix('.txt'))
    
    # 提取文本
    text = extract_chinese_text(source_file)
    
    if text and len(text) > 10:
        # 写入文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        return True
    else:
        return False


def batch_convert(source_dir):
    """批量转换"""
    source_path = Path(source_dir)
    
    if not source_path.exists():
        print(f"错误: 目录不存在: {source_dir}")
        return
    
    # 查找所有文件
    files = list(source_path.glob('*.doc')) + list(source_path.glob('*.docx'))
    files = [f for f in files if not f.name.startswith('~$')]
    
    if not files:
        print("没有找到文件")
        return
    
    print("=" * 70)
    print("批量提取文本工具")
    print("=" * 70)
    print(f"找到 {len(files)} 个文件")
    print("-" * 70)
    
    success_count = 0
    fail_count = 0
    
    for i, file in enumerate(files, 1):
        txt_file = file.with_suffix('.txt')
        
        print(f"[{i}/{len(files)}] {file.name}...", end=' ')
        
        try:
            if convert_to_txt(str(file), str(txt_file)):
                print("✓")
                success_count += 1
            else:
                print("✗ (内容为空)")
                fail_count += 1
        except Exception as e:
            print(f"✗ ({str(e)})")
            fail_count += 1
        
        # 每100个文件显示进度
        if i % 100 == 0:
            print("-" * 70)
            print(f"进度: {i}/{len(files)} | 成功: {success_count} | 失败: {fail_count}")
            print("-" * 70)
    
    print("=" * 70)
    print(f"转换完成! 成功: {success_count} | 失败: {fail_count}")
    print("=" * 70)


if __name__ == "__main__":
    import argparse
    
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description='批量将doc/docx文件转换为txt文本文件',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
使用示例:
  %(prog)s -d "D:\\jiangji"              转换指定目录下的所有doc/docx文件
  %(prog)s --directory "C:\\Documents"   使用完整参数名指定目录
  %(prog)s                               不带参数运行，将提示输入目录路径
        '''
    )
    
    parser.add_argument(
        '-d', '--directory',
        type=str,
        help='包含doc/docx文件的目录路径',
        metavar='DIR'
    )
    
    args = parser.parse_args()
    
    # 如果没有提供参数，交互式询问
    if args.directory:
        source_dir = args.directory
    else:
        print("=" * 70)
        print("批量DOC/DOCX转TXT工具")
        print("=" * 70)
        source_dir = input("请输入包含doc/docx文件的目录路径: ").strip()
        
        # 移除可能的引号
        if source_dir.startswith('"') and source_dir.endswith('"'):
            source_dir = source_dir[1:-1]
        elif source_dir.startswith("'") and source_dir.endswith("'"):
            source_dir = source_dir[1:-1]
    
    # 检查目录是否存在
    if not source_dir:
        print("错误: 未指定目录路径")
        input("\n按回车键退出...")
        exit(1)
    
    # 执行转换
    try:
        batch_convert(source_dir)
        print("\n转换完成！")
        input("\n按回车键退出...")
    except Exception as e:
        print(f"\n发生错误: {str(e)}")
        input("\n按回车键退出...")
        exit(1)
