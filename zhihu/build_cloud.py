import jieba, re
with open('answers.txt', 'r', encoding='utf-8') as f:
    seg_list = jieba.cut(f.read())  # 默认是精确模式

f = open("result.txt", "w", encoding='utf-8')  
f.write(re.sub(r'的|是|都|和|吗|做|上|对|呢|与|新|中|用|有|写|在',""," ".join(seg_list)))
f.close()