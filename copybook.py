# xiaoshuo
import requests
import time
from bs4 import BeautifulSoup

# 获取章节列表
def getBookSetionList(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    html = req.text

    dv_html = BeautifulSoup(html, "html5lib")
    dv_content = dv_html.find("div", id="list")

    # 章节 index
    # i = 0
    # 章节 List
    book_setion_list = []
    for k in dv_content.find_all("a"):
        book_setion_title = k.string
        book_setion_href = k['href']
        new_book_setion_href = "http://www.xbiquge.la{}".format(book_setion_href)
        # 直接存入
        book_setion_list.append({book_setion_title: new_book_setion_href})

        # try:
        #     # 去除无用章节
        #     book_setion_title_index = str(book_setion_title).index("章", 0)
        #     # index切片 获取新的章节标题 从1截取 不包括1
        #     new_book_setion_title = book_setion_title[book_setion_title_index + 1:]
        #     i = i + 1
        #     # 去除章节标题含有的空格
        #     new_book_setion_titles = "第{}章".format(i) + new_book_setion_title  #.lstrip()
        #     # 拼接新的章节链接
        #     new_book_setion_href = "http://www.xbiquge.la{}".format(book_setion_href)
        #     print(new_book_setion_titles)
        #     # 存入List
        #     book_setion_list.append({new_book_setion_titles: new_book_setion_href})
        # except:
        #     # 捕捉异常 没有找到"章"字符索引
        #     print("*****************不是正文章节节点,不予记录****************")
        #     # print("原标题=", book_setion_title)
        #     # print("原链接=", book_setion_href)
    return book_setion_list


# href获取章节具体内容
def getBookSetionContents(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    html = req.text

    dv_html = BeautifulSoup(html, "html5lib")
    dv_content = dv_html.find("div", id="content")

    # try:
    #     if(dv_content == None):
    #         pass
    # except:
    #     print("出现错误")
    #     pass

    # 去除script标记 和 html标记
    # [script.extract() for script in dv_content.findAll('script')]
    # [style.extract() for style in dv_content.findAll('style')]

    book_setion_content = dv_content.text
    return book_setion_content


# 写入本地
def saveBookContents(filepath, content):
    with open(filepath, mode="w", encoding="UTF-8") as f:
        f.writelines(content)
        f.write('\n\n')


# mian
if __name__ == '__main__':
    book_list = getBookSetionList("http://www.xbiquge.la/0/218/")
    content_url = ""
    for list in book_list:
        filepath = "d:\\123\\"
        print(list.keys())
        for key in list.keys():
            filepath = filepath + key
            content_url = list[key]
        content = getBookSetionContents(content_url)
        saveBookContents(filepath, content)
        # 出现 'NoneType' object is not iterable
        time.sleep(3)
