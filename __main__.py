#!/usr/bin/env python
# coding:utf-8

import sys
import os

BANNER = '''\
===============================================================
 GoAgent服务端部署程序, 开始上传 gae 应用文件夹
 Linux/Mac 用户, 请使用 python uploader.zip 来上传应用
===============================================================

请输入您的appid, 多个appid请用|号隔开
注意：appid 请勿包含 android/ios 字样，否则可能被某些网站识别成移动设备。
'''

FOOTER = '''\
上传成功，请不要忘记编辑proxy.ini把你的appid填进去，谢谢。按回车键退出程序。
'''

def main():
    import mimetypes
    mimetypes._winreg = None
    import appcfg
    dirname = os.path.dirname(os.path.abspath(__file__))
    if dirname.endswith('.zip'):
    	dirname = os.path.dirname(dirname)
    os.chdir(dirname)
    appcfg.main()

if __name__ == '__main__':
   try:
        print BANNER.decode('utf-8').encode(sys.getfilesystemencoding(), 'replace')
        main()
        print
        print FOOTER.decode('utf-8').encode(sys.getfilesystemencoding(), 'replace')
        raw_input()
   except KeyboardInterrupt:
        pass