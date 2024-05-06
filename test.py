import os

class Chapter(object):
    
    def __init__(self, title, path, encoding='utf8'):
        """
        Chapter类对象包含两个属性:
        title: 章节标题，如：第01章 风雪惊变
        content: 章节内容
        """
        self.title = title
        self._path, self._encoding = path, encoding
        with open(self._path, 'rt', encoding=self._encoding) as fin:
            self.content = fin.read()
    
    # 使用print函数等方式输出时显示章节标题
    def __repr__(self):
        return self.title
               
class Novel(object):
    
    def __init__(self, title, path, encoding='utf8'):
        """
        Novel类对象包含三个属性：
        title：小说标题，如：射雕英雄传
        chapters：小说正文章节
        misc：小说后记、附录等其他章节
        """
        self.title = title
        self._path, self._encoding = path, encoding
        self.chapters, self.misc = self.load_chapters()
        
            
    def load_chapters(self):
        """
        请补全这个函数，实现读取Path目录下小说的章节
        对每一章请构造一个Chapter对象，将小说正文章节加入chapters列表中；将小说后记、附录等内容加入到misc列表中返回。
        请注意:1)需要根据各章节文件名判断是否是正文章节；2）需要对小说正文章节进行排序。
        """
        chapters, misc = [], []
        filenames = os.listdir(self._path)
        for filename in filenames:
            path = os.path.join(self._path, filename)
            ext = os.path.splitext(path)[1]
            if ext == '.txt':
                if self.is_normal_chapter(path):
                    chapters.append(self.read_chapter(path))
                else:
                    misc.append(self.read_chapter(path))
            chapters.sort(key=lambda x: x.title)
            misc.sort(key=lambda x: x.title)
       
        return chapters, misc
    
    def is_normal_chapter(self, path): 
        # 代码补完部分开始
        chap_title = os.path.splitext(os.path.basename(path))[0]
        if chap_title[0] =='第':
            return True
        else:
            return False

        # 代码补完部分结束

    def read_chapter(self, path):
        # 代码补完部分开始
        title = os.path.splitext(os.path.basename(path))[0]
        return Chapter(title, path)


        # 代码补完部分结束
    
    # 你可以自由添加辅助函数
    # 代码补完部分开始

    # 代码补完部分结束
    
    #添加以下代码将使得我们可以遍历小说，每次返回正文中的一个章节
    def __iter__(self):
        return iter(self.chapters)
    
    #返回小说正文的章节数量
    def __len__(self):
        return len(self.chapters)
    
    #使用[]方式索引小说章节
    def __getitem__(self, key):
        return self.chapters[key]
    
    # 使用print函数等方式输出时显示小说标题
    def __repr__(self):
        return self.title
                        
# novel = Novel('射雕英雄传', 'D:\JupyterSpace\AI&python\大作业2\射雕英雄传', encoding='utf8')

import jieba

class TokenizedChapter(Chapter):
    
    def __init__(self, title, path, encoding='utf8'):
        """
        ToknizedChapter类对象包含三个属性:
        title: 章节标题，如：第01章 风雪惊变
        content: 章节内容
        tokenized_content: 分词后的内容
        """
        super().__init__(title, path, encoding=encoding) #调用父类构造函数，初始化title和content属性
        self.tokenized_content = list(jieba.tokenize(self.content))
        
    def word_count(self):
        """
        以字典或Counter的形式，返回该章节词频统计的结果，注意这里我们只统计长度大于1的词
        """
        # 代码补完部分开始
        cut_contents = jieba.lcut(self.content)
        mls_list = ['，', '。', '\\n', '、', '：', '？', '‘', '’', '“', '”']
        from collections import defaultdict
        word_count = defaultdict(int)
        for item in cut_contents:
            if (len(item) == 1) or (item in mls_list):
                continue
            else:
                word_count[item] = word_count.get(item, 0) + 1        

        return word_count

        # 代码补完部分结束
        
    def most_frequent_words(self, k=5):
        """
        实现函数，返回该章节中出现频率最高的5个词
        """
        # 代码补完部分开始
        output = {}
        items = list(TokenizedChapter.word_count(self).items())
        items.sort(key=lambda x: x[1], reverse=True)
        for i in range(k):
            word, count = items[i]
            output[word] = count

        return output.items()
        # 代码补完部分结束
    
    # 遍历TokenizedChapter类对象会依次输出分词后的结果
    def __iter__(self):
        return iter(self.tokenized_content)
    
    # 使用[]能访问第key个词
    def __getitem__(self, key):
        return self.tokenized_content[key]
        
class TokenizedNovel(Novel):
    
    def __init__(self, title, path, encoding='utf8'):
        super().__init__(title, path, encoding=encoding)
        
    # 请补完以下代码，通过重载Novel类相应的方法
    # 使得TokenizedNovel类对象的chapters和misc属性下保存的列表内的元素为TokenizedChapter类对象
    # 代码补完部分开始
        self.title = title
        self._path, self._encoding = path, encoding
        self.chapters, self.misc = self.load_tokenizedchapters()

    def load_tokenizedchapters(self):
        chapters, misc = [], []
        filenames = os.listdir(self._path)
        for filename in filenames:
            path = path = os.path.join(self._path, filename)
            ext = os.path.splitext(path)[1]
            if ext == '.txt':
                if self.is_normal_chapter(path):
                    chapters.append(self.count_chapter(path))
                else:
                    misc.append(self.count_chapter(path))
            chapters.sort(key=lambda x: x.title)
            misc.sort(key=lambda x: x.title)
       
        return chapters, misc
    
    def is_normal_chapter(self, path):
        return super().is_normal_chapter(path)
    
    def count_chapter(self, path):
        title = os.path.splitext(os.path.basename(path))[0]
        return TokenizedChapter(title, path)



    # 代码补完部分结束
    
# novel = TokenizedNovel('射雕英雄传', 'D:\JupyterSpace\AI&python\大作业2\射雕英雄传', encoding='utf8')
# print('小说{}共包含{}章：'.format(novel.title, len(novel)))
# for chap in novel:
#     print(chap.title) # 输出章节标题
#     print('==========')
#     for word, count in chap.most_frequent_words(3):
#         print(word, count)
#     print('==========')    

from collections import defaultdict

class TokenizedChapterWithCharacter(TokenizedChapter):
    
    def __init__(self, title, path, novel_characters, encoding='utf8'):
        """
        ToknizedChapter类对象包含四个属性:
        title: 章节标题，如：第01章 风雪惊变
        content: 章节内容
        tokenized_content: 分词后的内容
        characters: 本章出现的人物的列表
        character_positions: 一个dict，key为人物名称，value为一个list保存本章人物出现的位置（是第几个词）
        """
        super().__init__(title, path, encoding='utf-8') #调用父类构造函数
        # 补完代码，正确的根据novel_characters中的人物信息，初始化characters和character_positions属性
        # 代码补完部分开始
        self._title = title
        self._path = path
        self.charaters = []
        self.character_positions = defaultdict(int)

        with open(self._path, 'rt', encoding=self._encoding) as fin:
            self.content = fin.read()


        for word in self.tokenized_content:
            if word in novel_characters:
                self.charaters.append(word)
                self.character_positions[word] = self.cut_contents.index(word)

        # 代码补完部分结束
    
    def get_character_count(self, character_name):
        # 请补完以下函数，返回人物在章节中出现的次数
        # 代码补完部分开始
        chapcount = self.word_count()
        return chapcount.get(character_name, 0)

        # 代码补完部分结束
    
    def find_character(self, character_name, k=0):
        # 请补完以下函数，返回人物在该章节第k次出现的上下文，并且在人物名称周围加上*，例如：*郭靖*
        # 代码补完部分开始
        if character_name not in self.charaters:
            return None 
        
        if k > len(self.content):
            return "Error: there aren't enough characters!"
        
        index = self.content.find(character_name)
        if index == -1:
            return "Not found"
        
        context_length = 20
        start_index = max(0, index - context_length)
        end_index = index + len(character_name) + context_length
        context = self.content[start_index: end_index]
        context = context.replace(character_name, f"*{character_name}*")

        return context
        # 代码补完部分结束
 
        
class TokenizedNovelWithCharacter(TokenizedNovel):
    def __init__(self, title, path, character_file_path, encoding='utf8'):
        """
        TokenizedNovelWithCharacter类对象包含四个属性：
        title：小说标题，如：射雕英雄传
        chapters：小说正文章节
        misc：小说后记、附录等其他章节
        characters：一个list，保存小说中出现的所有人物名称
        """
        # 补完代码，打开保存人物名称的文件，初始化characters属性
        # 代码补完部分开始
        self._title = title
        self._path, self._encoding = path, encoding
        self.characters = []

        with open(character_file_path, "rt", encoding=encoding) as file:
            name_content =  file.read()
            name_dict = name_content.split("\n")
        
        self.characters = name_dict

        # 代码补完部分结束
        
        # 初始化jieba分词，并将人物名称作为自定义词加入词典
        jieba.initialize()
        for c in self.characters:
            jieba.add_word(c, freq=1024)
            
        super().__init__(title, path, encoding=encoding)
            
        # 请补完以下代码，通过重载TokenizedNovel类相应的方法
        # 使得TokenizedNovelWithCharacter类对象的chapters和misc属性下
        # 保存的列表内的元素为TokenizedChapterWithCharacter类对象
        # 代码补完部分开始
        self.chapters, self.misc = self.load_tokenizedchapterswithcharacter()


    def load_tokenizedchapterswithcharacter(self):
        
        chapters, misc = [], []
        filenames = os.listdir(self._path)
        for filename in filenames:
            path = os.path.join(self._path, filename)
            ext = os.path.splitext(path)[1]
            if ext == '.txt':
                if self.is_normal_chapter(path):
                    chapters.append(self.read_chapter(path))
                else:
                    misc.append(self.read_chapter(path))
            chapters.sort(key=lambda x: x.title)
            misc.sort(key=lambda x: x.title)
       
        return chapters, misc

    def read_chapter_t(self, path):
        title = os.path.splitext(os.path.basename(path))[0]
        return TokenizedChapterWithCharacter(title, path, self.characters)
    
        # 代码补完部分结束
    
    def character_count_in_chapter(self, character_name, chapter_index):
        # 请补完以下函数，返回人物在指定章节中出现的次数
        # 代码补完部分开始
        chapter = self.chapters[chapter_index]
        return chapter.get_character_count(character_name)
    
        # 代码补完部分结束
        
    def character_count(self, character_name):
        # 请补完以下函数，返回人物在整部小说中出现的次数
        # 代码补完部分开始
        total_count = 0
        for chapter in self.chapters:
            total_count += chapter.get_character_count(character_name)

        return total_count

        # 代码补完部分结束
    
    def find_character_in_chapter(self, character_name, chapter_index, k=0):
        # 请补完以下函数，返回人物在某个章节第k次出现的上下文
        # 代码补完部分开始
        # index = self.content.find(character_name)
        # if index == -1:
        #     return "Not found"
        
        # context_length = 20
        # start_index = max(0, index - context_length)
        # end_index = index + len(character_name) + context_length
        # context = self.content[start_index: end_index]
        # occurrences = []


        # for index, chapter in enumerate(self.chapters):
        #     pos = 0
        #     while True:
        #         pos = chapter.find(character_name, pos)
        #     if pos != -1:
        #         occurrences.append((pos, index))
        #         pos += len(character_name)  # 移动到下一个可能的位置
        #     else:
        #         break  # 如果找不到，退出循环

        # if k < len(occurrences):
        #     position, chapter_index = occurrences[k]
        #     chapter_text = self.chapters[chapter_index]
        #     start = max(0, position - context_length)
        #     end = min(len(chapter_text), position + context_length)
        #     context = chapter_text[start:end]
        #     return context, chapter_index
        # else:
        #     return None, None
        chapter = self.chapters[chapter_index]
        return chapter.find_character(character_name, k)

        # 代码补完部分结束
        
    def find_character(self, character_name, k=0):
        # 请补完以下函数，返回人物在整部小说中第k次出现的上下文,和所在章节
        # 代码补完部分开始
        occurrences = 0
        for index, chapter in enumerate(self.chapters):
            occurrences += chapter.count(character_name)
        if k < occurrences:
            # 找到第k次出现的章节
            position = -1
            for _ in range(k + 1):
                position = chapter.index(character_name, position + 1)
            # 获取上下文
            context_size = 20  # 可以根据需要调整
            start = max(0, position - context_size)
            end = min(len(chapter), position + context_size)
            context = chapter[start:end]
            return context, index
        k -= chapter.count(character_name)
        return None, None

        # 代码补完部分结束
        

        
novel = TokenizedNovelWithCharacter('射雕英雄传', 'D:\JupyterSpace\AI&python\大作业2\射雕英雄传', 'D:\JupyterSpace\AI&python\大作业2\射雕英雄传人物.txt', encoding='utf8')
# 输出人物在小说中出现的次数，并从高到低排序
character_counts = sorted(
    [(c, novel.character_count(c)) for c in novel.characters],
    key=lambda x: x[1],
    reverse=True
)
for c, count in character_counts:
    print('{:4} : {}'.format(c, count))

