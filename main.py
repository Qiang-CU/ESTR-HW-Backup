import os
import re
import shutil

# 定义文件夹路径
folder_path = './hw3'
# 移动文件并重新命名
backup_folder = './hw3_backup'

# 存储学生信息的字典
student_info = {'sid': [], 'grade': [], 'flag': []}

# 存储学生成绩的列表
grades = []

# 遍历文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 仅处理txt文件
        if file.endswith('.txt'):
            file_path = os.path.join(root, file)
            
            # 读取txt文件内容
            with open(file_path, 'r') as txt_file:
                txt_content = txt_file.read()
                
                # 使用正则表达式提取学生ID和成绩信息
                student_id_match = re.search(r'Name:.*\((\d+)\)', txt_content)
                grade_match_override = re.search(r'Override Grade: (\d+(\.\d+)?)', txt_content)
                grade_match_current = re.search(r'Current Grade: (\d+(\.\d+)?)', txt_content)
                
                if student_id_match:
                    student_id = student_id_match.group(1)
                    
                    if grade_match_override:
                        grade = round(float(grade_match_override.group(1)))
                    elif grade_match_current:
                        grade = round(float(grade_match_current.group(1)))
                    else:
                        grade = 0  # 如果没有成绩信息，默认为0.0
                    
                    # 将学生ID和成绩添加到相应的列表中
                    student_info['sid'].append(student_id)
                    student_info['grade'].append(grade)
                    grades.append(grade)

# 对成绩列表进行排序
sorted_grades = sorted(grades, reverse=True)
mid = len(sorted_grades) // 2
top5, mid5, bot5 = sorted_grades[:5], sorted_grades[mid-2:mid+2], sorted_grades[-5:]

# 根据排序后的成绩填入对应的flag
for grade in student_info['grade']:
    if grade in top5:
        student_info['flag'].append('top5')
    elif grade in mid5:
        student_info['flag'].append('mid5')
    elif grade in bot5:
        student_info['flag'].append('bot5')
    else:
        student_info['flag'].append('')

# 打印学生信息和对应的flag
for i in range(len(student_info['sid'])):
    print(f"Student ID: {student_info['sid'][i]}, Grade: {student_info['grade'][i]}, Flag: {student_info['flag'][i]}")



# 检查备份文件夹是否存在，如果不存在则创建
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# 遍历文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # 找到不以txt结尾且文件名中不包含declaration的文件
        if not file.endswith('.txt') and 'declaration' not in file:
            file_path = os.path.join(root, file)
            
            # 从文件名中提取学生ID和成绩信息
            # 从文件名中提取学生ID和成绩信息
            student_id_match = re.search(r'(\d+)_attempt_', file)
            
            if student_id_match:
                student_id = student_id_match.group(1)
                
                # 找到对应学生的信息
                index = student_info['sid'].index(student_id)
                grade = student_info['grade'][index]
                flag = student_info['flag'][index]
            
                # 构建新的文件名
                new_filename = f"SID{student_id}_Grade{grade}_{flag}{os.path.splitext(file)[1]}"
                
                # 复制文件到备份文件夹并重命名
                destination = os.path.join(backup_folder, new_filename)
                shutil.copyfile(file_path, destination)
