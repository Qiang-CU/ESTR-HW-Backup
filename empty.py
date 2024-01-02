from PyPDF2 import PdfWriter
import os
from faker import Faker
import random
import ruamel.yaml
import yaml

# # 定义要处理的文件夹路径
# folder_path = 'midterm'

# # 获取文件夹中的所有文件
# pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]

# # 逐个生成空白 PDF 文件
# for file in pdf_files:
#     output_path = os.path.join(folder_path, file)
#     pdf_writer = PdfWriter()

#     # 创建空白页面并保存为新的 PDF
#     with open(output_path, 'wb') as output_pdf:
#         pdf_writer.write(output_pdf)


fake = Faker()
file_path = './midterm/submission_metadata.yml'  # 期中考试文件路径
student_info = {'sid': [], 'grade': [], 'filename': []}  # 存储学生信息的字典

with open(file_path, 'r') as file:
    data = yaml.safe_load(file)

output = {}
for filename, info in data.items():
    item_info = ruamel.yaml.comments.CommentedMap({
        ":submitters": [
            {
                ":name": fake.name(),
                ":sid": fake.random_int(min=1150000000, max=1159999999),
                ":email": fake.email()
            }
        ],
        ":created_at": "2023-11-06 07:13:47.644186000 Z",
        ":score": round(random.uniform(60.0, 100.0), 1),
        ":original_filename": "AAAA2050-2050MidExam-AnsScan.pdf"
    })
    output[filename] = item_info

yaml = ruamel.yaml.YAML()
yaml.default_flow_style = False
# 将生成的信息写入 YAML 文件
with open('your_file.yml', 'w') as file:
    yaml.dump(output, file)
