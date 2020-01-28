# spyder_module
FireFlieStudio：一个懒人爬虫模块.  


(使用条件:
版本:python3
,模块: requests redis random lxml os )


(注:本模块需要安装redis,作者会尽快更新,摆脱redis的魔爪,若您没有安装redis则代理模式无法正常使用,其他各模块可正常使用)


一.导入模块

from module import *

(注:模块文件位置要置于PATH或项目文件旁.)

二.使用模块
内置函数:

1.spyder() 


spyder函数用于爬取网站源码,接收三个参数(分别是: url pro down)


①.url参数控制要爬取的网站.


②.pro参数控制代理的开启/关闭,默认关闭.


③.down由down函数控制,开启down时返还比特流,用于下载文件.



实例:


仅爬取模式:
spyder('http://down.firefliestudio.com/spyder_module/') 

代理模式:
spyder('http://down.firefliestudio.com/spyder_module/',pro='on')



2.down()


down函数用于下载文件,接收三个参数(分别是: url name mod).


①.url参数控制下载的文件.


②.name参数控制写出的文件名(不传入时默认使用原名).


③.mod函数控制下载的文件类型,目前仅支持 txt(文本) picv(图片).



实例:


下载txt文件:
down('http://down.firefliestudio.com/spyder_module/README.txt')

下载图片:
down('http://down.firefliestudio.com/spyder_module/FireFleStudio.png')

下载图片并重命名:
down('http://down.firefliestudio.com/spyder_module/FireFleStudio.png','FFS.png')



3.write()


write函数用于写入数据(写入txt文本),接收两个参数(分别是: name datas )


①.name参数控制输出的文件名字.


②.datas参数为数据,既写入内容.



实例:


写入数据:
write('newfile','Hello World')



4.mkdir()


mkdir函数由于创建文件夹,接收一个参数(name)


①.name参数控制文件夹的名字.

实例:


创建文件夹:
mkdir('newdir')



5.cd()


cd函数用于切换工作目录,接收一个参数(name)


①.name参数控制要切换的目录.(传入的参数不存在时跳过)



实例:


切换工作目录:
cd('/root')


骚操作:

url=spyder('http://down.firefliestudio.com/spyder_module/',pro='on').xpath("/html/body/pre/a[2]/@href")


mkdir('tmp')

cd('tmp')


down(url)


write('log','Done!')


感谢您的使用,如果发现该模块有任何BUG请给我们反馈,我们的邮箱:


firefliestudio@163.com


由FireFlies'Studio发布源码
