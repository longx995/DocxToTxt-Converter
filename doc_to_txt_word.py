#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用Microsoft Word批量将doc/docx文件转换为txt文件
需要安装pywin32库: pip install pywin32
"""

import os
import sys
from pathlib import Path
import win32com.client
import time


def convert_doc_to_txt_with_word(doc_path, txt_path=None):
    """
    使用Microsoft Word将doc/docx文件转换为txt文件
    
    参数:
        doc_path: doc/docx文件的绝对路径
        txt_path: 输出txt文件的绝对路径，如果为None则自动生成
    返回:
        True表示成功，False表示失败
    """
    # 确保路径是绝对路径
    doc_path = os.path.abspath(doc_path)
    
    if txt_path is None:
        txt_path = str(Path(doc_path).with_suffix('.txt'))
    else:
        txt_path = os.path.abspath(txt_path)
    
    # 检查源文件是否存在
    if not os.path.exists(doc_path):
        print(f"✗ 文件不存在: {Path(doc_path).name}")
        return False
    
    word = None
    doc = None
    
    try:
        # 创建Word应用程序对象
        # 这里不重新创建，而是使用已有的或创建新的
        word = win32com.client.Dispatch("Word.Application")
        
        # 设置Word为不可见（后台运行）
        word.Visible = False
        word.DisplayAlerts = 0  # 不显示任何警告
        
        # 打开文档
        doc = word.Documents.Open(doc_path, ReadOnly=True)
        
        # 保存为纯文本格式
        # wdFormatText = 2 表示纯文本格式
        # wdFormatUnicodeText = 7 表示Unicode文本格式（推荐，支持中文）
        doc.SaveAs2(txt_path, FileFormat=7, Encoding=65001)  # 65001 = UTF-8
        
        # 关闭文档
        doc.Close(SaveChanges=False)
        
        print(f"✓ 成功转换: {Path(doc_path).name} -> {Path(txt_path).name}")
        return True
        
    except Exception as e:
        print(f"✗ 转换失败 {Path(doc_path).name}: {str(e)}")
        
        # 尝试关闭可能打开的文档
        try:
            if doc:
                doc.Close(SaveChanges=False)
        except:
            pass
        
        return False
        
    finally:
        # 注意：不要在这里退出Word，因为我们要批量处理
        # 会在批量处理结束后统一退出
        pass


def batch_convert_docs_to_txt(source_dir, output_dir=None):
    """
    批量转换指定目录下的所有doc/docx文件为txt文件
    
    参数:
        source_dir: 包含doc/docx文件的源目录
        output_dir: 输出目录，如果为None则输出到源目录
    """
    source_path = Path(source_dir)
    
    if not source_path.exists():
        print(f"错误: 源目录不存在: {source_dir}")
        return
    
    # 如果指定了输出目录，确保它存在
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = source_path
    
    # 查找所有doc和docx文件
    doc_files = list(source_path.glob('*.doc')) + list(source_path.glob('*.docx'))
    
    # 过滤掉临时文件（以~$开头的文件）
    doc_files = [f for f in doc_files if not f.name.startswith('~$')]
    
    if not doc_files:
        print(f"在 {source_dir} 目录下没有找到doc/docx文件")
        return
    
    print(f"=" * 70)
    print(f"批量DOC/DOCX转TXT工具 - 使用Microsoft Word")
    print(f"=" * 70)
    print(f"源目录: {source_dir}")
    print(f"输出目录: {output_dir if output_dir else '与源文件相同'}")
    print(f"找到 {len(doc_files)} 个文件")
    print(f"-" * 70)
    
    # 创建Word应用程序对象（只创建一次）
    word = None
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        print(f"已启动Microsoft Word...")
        print(f"-" * 70)
    except Exception as e:
        print(f"错误: 无法启动Microsoft Word: {str(e)}")
        print(f"请确保已安装Microsoft Office")
        return
    
    # 统计
    success_count = 0
    fail_count = 0
    
    try:
        # 批量转换
        for i, doc_file in enumerate(doc_files, 1):
            # 生成输出文件路径
            txt_file = output_path / f"{doc_file.stem}.txt"
            
            print(f"[{i}/{len(doc_files)}] 正在转换: {doc_file.name}...")
            
            doc = None
            try:
                # 打开文档
                doc = word.Documents.Open(str(doc_file.absolute()), ReadOnly=True)
                
                # 保存为纯文本格式
                doc.SaveAs2(str(txt_file.absolute()), FileFormat=7, Encoding=65001)
                
                # 关闭文档
                doc.Close(SaveChanges=False)
                
                print(f"    ✓ 成功: {txt_file.name}")
                success_count += 1
                
            except Exception as e:
                print(f"    ✗ 失败: {str(e)}")
                fail_count += 1
                
                # 尝试关闭可能打开的文档
                try:
                    if doc:
                        doc.Close(SaveChanges=False)
                except:
                    pass
            
            # 每处理10个文件显示一次进度
            if i % 10 == 0:
                print(f"-" * 70)
                print(f"进度: {i}/{len(doc_files)} | 成功: {success_count} | 失败: {fail_count}")
                print(f"-" * 70)
    
    finally:
        # 退出Word应用程序
        try:
            if word:
                word.Quit()
                print(f"\n已关闭Microsoft Word")
        except:
            pass
    
    # 输出统计信息
    print(f"=" * 70)
    print(f"转换完成!")
    print(f"总计: {len(doc_files)} 个文件")
    print(f"成功: {success_count} 个")
    print(f"失败: {fail_count} 个")
    print(f"=" * 70)


if __name__ == "__main__":
    # 设置源目录（包含doc/docx文件的目录）
    source_directory = r"D:\jiangji"
    
    # 设置输出目录（如果想输出到同一目录，设为None；如果想输出到其他目录，指定路径）
    output_directory = None  # 默认输出到源目录
    # output_directory = r"D:\jiangji\txt_output"  # 如果想输出到单独的文件夹，取消注释这行
    
    # 执行批量转换
    batch_convert_docs_to_txt(source_directory, output_directory)
