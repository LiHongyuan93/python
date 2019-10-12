#对文件的操作

#将小说的主要任务记录在文件中
file1 = open('name.txt','w')
file1.write('诸葛亮')
file1.close()               #写入完成记得要关闭

#读取文件
file2 = open('name.txt')
print(file2.read())

#追加写入信息
file3 = open('name.txt','a')
file3.write('刘备')
file3.close()
print(file3.read())

#逐行读入
file4 = open('name.txt', encoding='UTF-8')
print(file4.readline())

file5 = open('name.txt', encoding='UTF-8')
for line in file5.readlines():
    print(line)
    print('===')

#指针 seek
file6 = open('name.txt', encoding='UTF-8')
print(file6.tell())     #0 指针，告诉用于文件在什么位置。
file6.read(2)
print(file6.tell())     #6
file6.seek(0)        #seek可以配置两个参数，0表示把指针指向0
print(file6.tell())     #0

file6.seek(5,0)         #第一个参数代表偏移位置，第二个参数0表示从文件开头偏移，1表示从当前位置偏移，2表示从文件结尾
print('当前文件指针的位置 %s' %file6.tell())










