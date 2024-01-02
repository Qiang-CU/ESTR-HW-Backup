import yaml
import os
import re
import shutil

# 读取YAML文件并处理学生成绩
file_path = './midterm/submission_metadata.yml'  # 期中考试文件路径
backup_folder = './midterm_backup'
student_info = {'sid': [], 'grade': [], 'filename': []}  # 存储学生信息的字典

with open(file_path, 'r') as file:
    data = yaml.safe_load(file)

grade = []
for filename, info in data.items():
    sid = info[':submitters'][0][':sid']
    score = info[':score']
    student_info['sid'].append(sid)  # 将成绩存储到学生信息字典中
    student_info['filename'].append(filename)
    student_info['grade'].append(round(score))

# 获得成绩排名
sorted_student_info = sorted(zip(student_info['sid'], student_info['grade'], student_info['filename']),
                             key=lambda x: x[1], reverse=True)

# 给学生添加 flag 标签
top5 = sorted_student_info[:5]
mid5 = sorted_student_info[len(sorted_student_info)//2 - 2:len(sorted_student_info)//2 + 3]
bot5 = sorted_student_info[-5:]
student_info['flag'] = []

for sid, grade, filename in zip(student_info['sid'], student_info['grade'], student_info['filename']):
    if (sid, grade, filename) in top5:
        student_info['flag'].append('top5')
    elif (sid, grade, filename) in mid5:
        student_info['flag'].append('mid5')
    elif (sid, grade, filename) in bot5:
        student_info['flag'].append('bot5')
    else:
        student_info['flag'].append('')

# 打印排序后的学生信息
for sid, grade, filename, flag in zip(student_info['sid'], student_info['grade'], student_info['filename'], student_info['flag']):
    print(f"SID: {sid}, Grade: {grade}, Filename: {filename}, Flag: {flag}")


# 打印带有标记的学生信息或进行其他操作
        # 检查备份文件夹是否存在，如果不存在则创建
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

for sid, grade, filename, flag in zip(student_info['sid'], student_info['grade'], student_info['filename'], student_info['flag']):

    if flag != '':
        path = os.path.join(backup_folder, filename)
        new_filename = f"SID{sid}_Grade{grade}_{flag}{os.path.splitext(filename)[1]}"

        destination = os.path.join(backup_folder, new_filename)
        shutil.copyfile(file_path, destination)












# 遍历文件夹中的所有文件
for root, dirs, files in os.walk(file_path):
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
                new_filename = f"{student_id}_{grade}_{flag}{os.path.splitext(file)[1]}"
                
                # 复制文件到备份文件夹并重命名
                destination = os.path.join(backup_folder, new_filename)
                shutil.copyfile(file_path, destination)


