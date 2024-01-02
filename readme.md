
## 背景
main.py 用来处理日常作业的备份问题，将文件备份到指定的目录下，并重命名为sid+grade+flag的形式
其中flag为top5, mid5, bot5

- 日常作业下载到本地后，会有三个文件，declaration file, homework file, txt file
- 通过从txt file 中读取学号，和成绩(Overide Grade / Current Grade)信息

midterm.py 用来处理从Gradescopt上下载的期中作业的备份问题，将文件备份到指定的目录下，并重命名为sid+grade+flag的形式

- 从Gradescope上下载的文件，会有一个yml文件和一大堆的pdf file
- 通过从yml文件中读取学号，和成绩信息以及pdf file的名字

## 用法
- 将作业文件放到目录下
- 在main.py 或者 midterm.py 中修改文件路径，并指定备份文件路径
- 运行main.py 或者 midterm.py
  
### Remarks
- empty.py 用来生成一些mock data, 隐藏敏感数据