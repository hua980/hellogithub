
# 简单使用
from bs4 import BeautifulSoup
file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser") # 缩进格式
print('格式化html结构,把内容全部打印出来:')
print(bs.prettify())
print(' \n获取title标签的名称以及里面的内容:')
print(bs.title)
print('\n获取title的name:')
print(bs.title.name)
print('\n获取title标签的所有内容:')
print(bs.title.string)
print('\n获取head标签的名称以及里面的内容:')
print(bs.head)
print('\n获取第一个div标签中的所有内容')
print(bs.div)
print('\n获取第一个div标签的id的值')
print(bs.div["id"])
print('\n获取a标签的名称以及里面的内容:')
print(bs.a)
print('\n获取所有的a标签')
print(bs.find_all("a")) # 获取所有的a标签
print('\n # 获取id="u1":')
print(bs.find(id="u1")) # 获取id="u1"
print('\n获取所有的a标签，并遍历打印a标签中的href的值')
for item in bs.find_all("a"):
    print(item.get("href")) # 获取所有的a标签，并遍历打印a标签中的href的值
print('\n获取所有的a标签，并遍历打印a标签中的内容')
for item in bs.find_all("a"):
    print(item.get_text())



print('\n四、BeautifulSoup4四大对象种类\n')
'''  
四、BeautifulSoup4四大对象种类
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
        Tag
        NavigableString
        BeautifulSoup
        Comment
'''


'''
4.1、Tag
    Tag通俗点讲就是HTML中的一个个标签，例如：
'''
from bs4 import BeautifulSoup
file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
# 获取title标签的所有内容
print(bs.title)
# 获取head标签的所有内容
print(bs.head)
# 获取第一个a标签的所有内容
print(bs.a)
# 类型
print(type(bs.a))


# 对于 Tag，它有两个重要的属性，是 name 和 attrs：

from bs4 import BeautifulSoup
file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
# [document] #bs 对象本身比较特殊，它的 name 即为 [document]
print('\n',bs.name)
# head #对于其他内部标签，输出的值便为标签本身的名称
print(bs.head.name)
# 在这里，我们把 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
print(bs.a.attrs)
#还可以利用get方法，传入属性的名称，二者是等价的
print(bs.a['class']) # 等价 bs.a.get('class')
# 可以对这些属性和内容等等进行修改
bs.a['class'] = "newClass"
print(bs.a)
# 还可以对这个属性进行删除
del bs.a['class']
print(bs.a)


'''
4.2、NavigableString
既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文字怎么办呢？很简单，用 .string 即可，例如：
'''
from bs4 import BeautifulSoup

file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html, "html.parser")

print('\n',bs.title.string)
print(type(bs.title.string))

'''
4.4、Comment

Comment 对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号。
'''

from bs4 import BeautifulSoup
file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
print('\n',bs.a)
# 此时不能出现空格和换行符，a标签如下：
# <a class="mnav" href="http://news.baidu.com" name="tj_trnews"><!--新闻--></a>
print(bs.a.string)   # 新闻
print(type(bs.a.string))   # <class 'bs4.element.Comment'>

'''
五、遍历文档树
5.1、.contents：获取Tag的所有子节点，返回一个list
'''

# tag的.content 属性可以将tag的子节点以列表的方式输出
print('\n',bs.head.contents)
# 用列表索引来获取它的某一个元素
print(bs.head.contents[1])


# 5.2、.children：获取Tag的所有子节点，返回一个生成器

for child in  bs.body.children:
    print('\n',child)
'''
5.3、.descendants：获取Tag的所有子孙节点

5.4、.strings：如果Tag包含多个字符串，即在子孙节点中有内容，可以用此获取，而后进行遍历

5.5、.stripped_strings：与strings用法一致，只不过可以去除掉那些多余的空白内容

5.6、.parent：获取Tag的父节点

5.7、.parents：递归得到父辈元素的所有节点，返回一个生成器

5.8、.previous_sibling：获取当前Tag的上一个节点，属性通常是字符串或空白，真实结果是当前标签与上一个标签之间的顿号和换行符

5.9、.next_sibling：获取当前Tag的下一个节点，属性通常是字符串或空白，真是结果是当前标签与下一个标签之间的顿号与换行符

5.10、.previous_siblings：获取当前Tag的上面所有的兄弟节点，返回一个生成器

5.11、.next_siblings：获取当前Tag的下面所有的兄弟节点，返回一个生成器

5.12、.previous_element：获取解析过程中上一个被解析的对象(字符串或tag)，可能与previous_sibling相同，但通常是不一样的

5.13、.next_element：获取解析过程中下一个被解析的对象(字符串或tag)，可能与next_sibling相同，但通常是不一样的

5.14、.previous_elements：返回一个生成器，可以向前访问文档的解析内容

5.15、.next_elements：返回一个生成器，可以向后访问文档的解析内容

5.16、.has_attr：判断Tag是否包含属性
'''

'''六、搜索文档树
6.1、find_all(name, attrs, recursive, text, **kwargs)

在上面的栗子中我们简单介绍了find_all的使用，接下来介绍一下find_all的更多用法-过滤器。这些过滤器贯穿整个搜索API，过滤器可以被用在tag的name中，节点的属性等。

（1）name参数：
    字符串过滤：会查找与字符串完全匹配的内容'''

a_list = bs.find_all("a")
print(a_list)

#
# 正则表达式过滤：如果传入的是正则表达式，那么BeautifulSoup4会通过search()来匹配内容

from bs4 import BeautifulSoup
import re
file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
t_list = bs.find_all(re.compile("a"))
for item in t_list:
   print('\n',item)



# 列表：如果传入一个列表，BeautifulSoup4将会与列表中的任一元素匹配到的节点返回
print('\n \t\t\t-----------分隔线-----------')
t_list = bs.find_all(["meta","link"])
for item in t_list:
    print(item)


# 方法：传入一个方法，根据方法来匹配

print('\n \t\t\t-----------分隔线-----------')
from bs4 import BeautifulSoup
file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
def name_is_exists(tag):
    return tag.has_attr("name")
t_list = bs.find_all(name_is_exists)
for item in t_list:
    print(item)

# （2）kwargs参数：
print('\n \t\t\t-----------分隔线-----------')
from bs4 import BeautifulSoup
import re
file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")
# 查询id=head的Tag
t_list = bs.find_all(id="head")
print(t_list)
# 查询href属性包含ss1.bdstatic.com的Tag
t_list = bs.find_all(href=re.compile("http://news.baidu.com"))
print(t_list)
# 查询所有包含class的Tag(注意：class在Python中属于关键字，所以加_以示区别)
t_list = bs.find_all(class_=True)
for item in t_list:
    print(item)


'''（3）attrs参数：
print('\n \t\t\t-----------分隔线-----------')
并不是所有的属性都可以使用上面这种方式进行搜索，比如HTML的data-*属性：'''

# t_list = bs.find_all(data-foo="value")
# 如果执行这段代码，将会报错。我们可以使用attrs参数，定义一个字典来搜索包含特殊属性的tag：

t_list = bs.find_all(attrs={"data-foo":"value"})
for item in t_list:
    print(item)



'''
（4）text参数：
print('\n \t\t\t-----------分隔线-----------')
通过text参数可以搜索文档中的字符串内容，与name参数的可选值一样，text参数接受 字符串，正则表达式，列表'''

from bs4 import BeautifulSoup
import re
file = open('./test.html', 'rb')
html = file.read()
bs = BeautifulSoup(html, "html.parser")
t_list = bs.find_all(attrs={"data-foo": "value"})
for item in t_list:
    print(item)
t_list = bs.find_all(text="hao123")
for item in t_list:
    print(item)
t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
for item in t_list:
    print(item)
t_list = bs.find_all(text=re.compile("\d"))
for item in t_list:
    print(item)


'''七、CSS选择器
BeautifulSoup支持发部分的CSS选择器，在Tag获取BeautifulSoup对象的.select()方法中传入字符串参数，即可使用CSS选择器的语法找到Tag:
7.1、通过标签名查找'''
print('\n \t\t\t-----------分隔线-----------')
print(bs.select('title'))
print(bs.select('a'))

# 7.2、通过类名查找
print('\n \t\t\t-----------分隔线-----------')
print(bs.select('.mnav'))

# 7.3、通过id查找
print('\n \t\t\t-----------分隔线-----------')
print(bs.select('#u1'))


# 7.4、组合查找
print('\n \t\t\t-----------分隔线-----------')
print(bs.select('div .bri'))

# 7.5、属性查找
print('\n \t\t\t-----------分隔线-----------')
print(bs.select('a[class="bri"]'))
print(bs.select('a[href="http://tieba.baidu.com"]'))

# 7.6、直接子标签查找
print('\n \t\t\t-----------分隔线-----------')
t_list = bs.select("head > title")
print(t_list)

# 7.7、兄弟节点标签查找
print('\n \t\t\t-----------分隔线-----------')
t_list = bs.select(".mnav ~ .bri")
print(t_list)

# 7.8、获取内容
print('\n \t\t\t-----------分隔线-----------')
t_list = bs.select("title")
print(bs.select('title')[0].get_text())