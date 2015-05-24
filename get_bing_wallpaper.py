#! /usr/share/python
# -*- coding:utf-8 -*-

import sys, urllib2, socket, re, time, urllib, os

reload(sys)
sys.setdefaultencoding( "utf-8" )
socket.setdefaulttimeout(5)#设置网络连接超时时间

def get_page(url):
    """根据链接获取网页

    Args:
        url: 网页的url链接
        
        直接使用urllib2进行网页的下载，
        修改header防止访问被拒绝
    """
    #headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    content = ""
    try:
        content = urllib2.urlopen(req).read()
    except socket.error:
        errno, errstr = sys.exc_info()[:2]
        if errno == socket.timeout:
            print ("There was a timeout " + url)
        else:
            print ("There was some other socket error " + url)
    except:
        print ("There is OTHER ERROR " + url)
    #time.sleep(0.5)
    return content

def get_img_url(content):
    pattern = re.compile("g_img={url:'(.*?)'", re.S)
    urls = re.findall(pattern, content)
    return urls[0]

def download_img(url, target_dir):
    file_name = url.split("/")[-1]
    target = os.path.join(target_dir, file_name)
    urllib.urlretrieve(url, target)

if __name__ == "__main__":
    root="http://cn.bing.com/"
    content = get_page(root)
    img_url = get_img_url(content)
    download_img(img_url, "./wallpaper")