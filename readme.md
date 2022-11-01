## clear_tool

## 安装

```
git clone https://github.com/xanszZZ/clear_tool
```

## 使用

本工具是由python编写的windows、linux系统痕迹清理工具。

支持清理windows web日志清理，包括IIS、apache、nginx中间件的日志文件清理

支持清理linux web日志清理

在使用本工具前需找到对应系统web日志目录

```
一些中间件默认web日志目录：

IIS：
%SystemDrive%\inetpub\logs\LogFiles
注：不同的 Win版本iis日志路径不一样，这里列出几个
C:\Windows\System32\LogFiles # win_s_2003
C:\inetpub\logs\LogFiles # win_s_2008r2
%SystemDrive%\inetpub\logs\LogFiles # win_s_2012r2

apache：
apache默认日志在安装目录下的logs目录中

nginx：
nginx默认日志在安装目录下的logs目录中。
```

参数

```
 -s 选择w或l ，对应windows和linux系统

-u 选择想要清理的关键ip

-p 在IIS中间件中，对应目标日志文件的名字不同，选择对应的名字，在linux中选择要删除的日志文件
```

将工具放入对应目录下

```
python clear_tool.py -s w -u 127.0.0.1 

目标主机没有python环境可直接使用打包好的exe文件
clear_tool.exe -s w -u 127.0.0.1 
```

注：python环境需使用大于python3.5

## 免责声明🧐

本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建测试环境。

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。