#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量将doc/docx文件转换为txt文件的脚本
支持旧的.doc格式（Word 97-2003）和新的.docx格式
"""

import os
import subprocess
from pathlib import Path


def convert_doc_to_txt_with_antiword(doc_path, txt_path=None):
    """
    使用antiword将doc文件转换为txt（仅限Linux/Mac）
    
    参数:
        doc_path: doc文件的路径
        txt_path: 输出txt文件的路径
    """
    if txt_path is None:
        txt_path = str(Path(doc_path).with_suffix('.txt'))
    
    try:
        result = subprocess.run(['antiword', doc_path], 
                                capture_output=True, 
                                text=True, 
                                encoding='utf-8')
        
        if result.returncode == 0:
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(result.stdout)
            return True
        else:
            return False
    except:
        return False


def convert_doc_to_txt_with_textract(doc_path, txt_path=None):
    """
    使用textract将doc文件转换为txt
    
    参数:
        doc_path: doc文件的路径
        txt_path: 输出txt文件的路径
    """
    try:
        import textract
        
        if txt_path is None:
            txt_path = str(Path(doc_path).with_suffix('.txt'))
        
        # 使用textract提取文本
        text = textract.process(doc_path)
        
        # 写入txt文件
        with open(txt_path, 'wb') as f:
            f.write(text)
        
        return True
        
    except Exception as e:
        return False


def convert_doc_with_libreoffice(doc_path, output_dir):
    """
    使用LibreOffice将doc文件转换为txt
    
    参数:
        doc_path: doc文件的路径
        output_dir: 输出目录
    """
    try:
        # 查找LibreOffice可执行文件
        possible_paths = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
            "soffice",  # Linux/Mac
            "/Applications/LibreOffice.app/Contents/MacOS/soffice"  # Mac
        ]
        
        soffice_path = None
        for path in possible_paths:
            if os.path.exists(path) or path == "soffice":
                soffice_path = path
                break
        
        if soffice_path is None:
            return False
        
        # 使用LibreOffice转换
        cmd = [
            soffice_path,
            '--headless',
            '--convert-to', 'txt:Text',
            '--outdir', output_dir,
            doc_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, timeout=30)
        return result.returncode == 0
        
    except Exception as e:
        return False


def simple_read_doc_file(doc_path):
    """
    尝试直接从doc文件中读取文本（简单粗暴的方法，可能有乱码）
    """
    try:
        with open(doc_path, 'rb') as f:
            content = f.read()
        
        # 尝试解码，忽略错误
        text = content.decode('utf-8', errors='ignore')
        
        # 简单清理：移除大部分非打印字符
        import re
        text = re.sub(r'[^\x20-\x7E\u4e00-\u9fff\n\r\t]', '', text)
        
        # 移除过多的空行
        lines = [line.strip() for line in text.split('\n')]
        lines = [line for line in lines if line]
        text = '\n'.join(lines)
        
        return text if text else None
        
    except:
        return None


def convert_doc_to_txt(doc_path, txt_path=None):
    """
    将doc/docx文件转换为txt文件
    尝试多种方法
    
    参数:
        doc_path: doc文件的路径
        txt_path: 输出txt文件的路径
    """
    if txt_path is None:
        txt_path = str(Path(doc_path).with_suffix('.txt'))
    
    filename = Path(doc_path).name
    output_dir = str(Path(doc_path).parent)
    
    # 方法1: 尝试使用LibreOffice
    print(f"正在转换: {filename}...")
    if convert_doc_with_libreoffice(doc_path, output_dir):
        print(f"✓ 成功转换: {filename} -> {Path(txt_path).name}")
        return True
    
    # 方法2: 尝试使用textract
    if convert_doc_to_txt_with_textract(doc_path, txt_path):
        print(f"✓ 成功转换: {filename} -> {Path(txt_path).name} (使用textract)")
        return True
    
    # 方法3: 尝试简单读取（最后的办法，可能有乱码）
    text = simple_read_doc_file(doc_path)
    if text:
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"⚠ 使用简单方法转换: {filename} -> {Path(txt_path).name} (可能有部分乱码)")
        return True
    
    print(f"✗ 转换失败: {filename}")
    return False


def batch_convert_docs_to_txt(source_dir):
    """
    批量转换指定目录下的所有doc/docx文件为txt文件
    
    参数:
        source_dir: 包含doc文件的源目录
    """
    source_path = Path(source_dir)
    
    if not source_path.exists():
        print(f"错误: 源目录不存在: {source_dir}")
        return
    
    # 查找所有doc和docx文件
    doc_files = list(source_path.glob('*.doc')) + list(source_path.glob('*.docx'))
    
    # 过滤掉临时文件
    doc_files = [f for f in doc_files if not f.name.startswith('~$')]
    
    if not doc_files:
        print(f"在 {source_dir} 目录下没有找到doc/docx文件")
        return
    
    print(f"=" * 60)
    print(f"批量DOC/DOCX转TXT工具")
    print(f"=" * 60)
    print(f"源目录: {source_dir}")
    print(f"找到 {len(doc_files)} 个文件")
    print(f"-" * 60)
    
    # 统计
    success_count = 0
    fail_count = 0
    
    # 批量转换
    for doc_file in doc_files:
        txt_file = doc_file.with_suffix('.txt')
        
        if convert_doc_to_txt(str(doc_file), str(txt_file)):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"-" * 60)
    print(f"转换完成! 成功: {success_count}, 失败: {fail_count}")
    print(f"=" * 60)


if __name__ == "__main__":
    # 设置源目录
    source_directory = r"D:\jiangji"
    
    # 执行批量转换
    batch_convert_docs_to_txt(source_directory)
