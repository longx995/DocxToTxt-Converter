#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量将docx文件转换为txt文件的脚本
"""

import os
import zipfile
import re
from pathlib import Path
from docx import Document
from xml.etree import ElementTree as ET


def extract_text_from_xml(docx_path):
    """
    使用zipfile直接从docx的XML中提取文本（备用方案）
    """
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            # 读取document.xml文件
            xml_content = zip_ref.read('word/document.xml')
            tree = ET.XML(xml_content)
            
            # 提取所有文本节点
            namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            paragraphs = []
            for paragraph in tree.findall('.//w:p', namespace):
                texts = []
                for node in paragraph.findall('.//w:t', namespace):
                    if node.text:
                        texts.append(node.text)
                if texts:
                    paragraphs.append(''.join(texts))
            
            return '\n'.join(paragraphs)
    except Exception as e:
        raise Exception(f"XML提取失败: {str(e)}")


def convert_docx_to_txt(docx_path, txt_path=None):
    """
    将单个docx文件转换为txt文件
    
    参数:
        docx_path: docx文件的路径
        txt_path: 输出txt文件的路径，如果为None则自动生成
    """
    # 如果没有指定输出路径，则在同目录下创建同名的txt文件
    if txt_path is None:
        txt_path = str(Path(docx_path).with_suffix('.txt'))
    
    # 检查文件是否存在
    if not os.path.exists(docx_path):
        print(f"✗ 文件不存在: {Path(docx_path).name}")
        return False
    
    # 检查文件是否可读
    if not os.access(docx_path, os.R_OK):
        print(f"✗ 文件无法读取: {Path(docx_path).name}")
        return False
    
    try:
        # 方法1：尝试使用python-docx正常读取
        doc = Document(docx_path)
        
        # 提取所有段落的文本
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        
        content = '\n'.join(full_text)
        
        # 写入txt文件
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ 成功转换: {Path(docx_path).name} -> {Path(txt_path).name}")
        return True
        
    except Exception as e:
        # 方法2：如果python-docx失败，尝试使用XML直接提取
        try:
            print(f"  尝试使用备用方案提取: {Path(docx_path).name}")
            content = extract_text_from_xml(docx_path)
            
            # 写入txt文件
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ 使用备用方案成功转换: {Path(docx_path).name} -> {Path(txt_path).name}")
            return True
            
        except Exception as e2:
            print(f"✗ 转换失败 {Path(docx_path).name}: {str(e)} | 备用方案也失败: {str(e2)}")
            return False


def batch_convert_docx_to_txt(source_dir, output_dir=None):
    """
    批量转换指定目录下的所有docx文件为txt文件
    
    参数:
        source_dir: 包含docx文件的源目录
        output_dir: 输出目录，如果为None则输出到源目录
    """
    source_path = Path(source_dir)
    
    # 检查源目录是否存在
    if not source_path.exists():
        print(f"错误: 源目录不存在: {source_dir}")
        return
    
    # 如果指定了输出目录，确保它存在
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = source_path
    
    # 查找所有docx文件
    docx_files = list(source_path.glob('*.docx'))
    
    # 过滤掉临时文件（以~$开头的文件）
    docx_files = [f for f in docx_files if not f.name.startswith('~$')]
    
    if not docx_files:
        print(f"在 {source_dir} 目录下没有找到docx文件")
        return
    
    print(f"找到 {len(docx_files)} 个docx文件")
    print("-" * 50)
    
    # 统计转换结果
    success_count = 0
    fail_count = 0
    
    # 批量转换
    for docx_file in docx_files:
        # 生成输出文件路径
        txt_file = output_path / f"{docx_file.stem}.txt"
        
        # 转换文件
        if convert_docx_to_txt(str(docx_file), str(txt_file)):
            success_count += 1
        else:
            fail_count += 1
    
    # 输出统计信息
    print("-" * 50)
    print(f"转换完成! 成功: {success_count}, 失败: {fail_count}")


if __name__ == "__main__":
    # 设置源目录（包含docx文件的目录）
    source_directory = r"D:\jiangji"
    
    # 设置输出目录（如果想输出到同一目录，设为None；如果想输出到其他目录，指定路径）
    output_directory = None  # 默认输出到源目录
    # output_directory = r"D:\jiangji\txt_output"  # 如果想输出到单独的文件夹，取消注释这行
    
    print("=" * 50)
    print("批量DOCX转TXT工具")
    print("=" * 50)
    print(f"源目录: {source_directory}")
    print(f"输出目录: {output_directory if output_directory else '与源文件相同'}")
    print("=" * 50)
    
    # 执行批量转换
    batch_convert_docx_to_txt(source_directory, output_directory)
