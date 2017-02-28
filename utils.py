"""utilities"""
# coding: utf-8

import requests

def youdao(word):
    url = r'http://fanyi.youdao.com/openapi.do?keyfrom=sorrible&key=1660616686&type=data&doctype=json&version=1.1&q='
    builded_url = url+word
    result = requests.get(builded_url).json()
    if result['errorCode'] == 0:
        if 'basic' in result.keys():
            trans = u'%s:\n%s\n%s\n网络释义：\n%s'%(result['query'],''.join(result['translation']),' '.join(result['basic']['explains']),'\n'.join(result['web'][0]['value']))
            return trans
        else:
            trans = u'%s:\n基本翻译:%s\n'%(result['query'],''.join(result['translation']))
    elif result['errorCode'] == 20:
        return u'对不起，要翻译的文本过长'
    elif result['errorCode'] == 30:
        return u'对不起，无法进行有效的翻译'
    elif result['errorCode'] == 40:
        return u'对不起，不支持的语言类型'
    else:
        return u'对不起，您输入的单词%s无法翻译,请检查拼写'% word
        
        
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree
import model
import urllib

class WeixinInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="infixz" 
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
        
    def POST(self):
        #获得post来的数据,xml为解析完毕的内容
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        #提取用户消息属性
        toUser = xml.find("ToUserName").text
        fromUser = xml.find("FromUserName").text
        msgtype = xml.find("MsgType").text
        
        #信息类型是event
        if msgtype == "event":#"event"是用户关注公众号产生的动作
            eventContent = xml.find("Event").text
            if eventContent == "subscribe":
                replayText = u'''感谢你关注本公众平台。\n如果有什么疑问，请添加朋友：infixz\n目前实用功能：1.通过有道api进行中英文互译。\n输入menu查看操作指令'''
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
            if eventContent == "unsubscribe":
                replayText = u'''你确定？
                再加回来我当做没看见，否则我会真人当面请教你为什么的。
                hehe,see you！'''
                return self.render.reply_text(oAEpauGNei5KIfeG0qJL5JsW4c_k,toUser,int(time.time()),replayText)
        
        #信息类型是text
        if msgtype == "text":
            content = xml.find("Content").text
            if content.startswith(u'约约约'):
                name=content[4:]#消除空格
                bbstime = time.strftime('%Y-%m-%d %H:%M',time.localtime())
                model.addbbs(fromUser,bbstime,content[3:].encode('utf-8'))
                return self.render.reply_text(fromUser,toUser,int(time.time()),u'see you then！'+name)
            if content == "xixi":
                   #添加一个调用网页的函数
                basic_data = {'Content':'test'}
                urldata = urllib.urlencode(basic_data)
                requrl = "http://2.postmsg.sinaapp.com/transmit"
                #req = urllib2.Request(url=requrl,data=urldata)
                urllib.urlopen(requrl)
                return self.render.reply_text(fromUser,toUser,int(time.time()),u'see you then！')
            if content == "menu":
                replayText = u'''1.输入中文或者英文句子或单词返回对应的英中翻译(有道API）\n2.（未完成）\n3（未完成）\n'''
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
            if content == "admin":
                bbsurl = r'http://chengsapp.sinaapp.com/bbs'
                return self.render.reply_text(fromUser,toUser,int(time.time()),bbsurl)
            if content == u'约吗':
                replayText= u'''约！约！约！\n\n本周六晚6点（11月29日)图门烧烤，就等你来！你的微信号是%s。\n\n回复\n\n约约约+空格+你的名字or昵称\n\n参与我们的”约吗“上线庆祝活动！！！'''% fromUser
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
            if type(content).__name__ == 'unicode':
                content = content.encode('utf-8')
            t_word = youdao(content)
            return self.render.reply_text(fromUser,toUser,int(time.time()),t_word+u'\n\n**************************\n回复 menu 查看更多信息\n**************************')
        
        #信息类型是voice
        if msgtype == "voice":
            voiceRec = xml.find("Recognition").text
            if voiceRec == u'约吗':
                replayText= u'''约！约！约！\n\n本周六晚6点（11月29日)图门烧烤，就等你来！\nTEL：13262790790\n回复:\n约约约+空格+你的名字\n\n参与我们的”约吗“上线庆祝活动！！！'''
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
            return self.render.reply_text(fromUser,toUser,int(time.time()),u'嗯哼？\n你是何方妖孽，竟然会《千里传音》？\n这可是家门不外传之秘笈。呵呵，不过在如今那也是作古的雕虫小技了。\n\n且看我《同声传译》大法！\n=>"'+voiceRec+'"')

#通过youdao API 实现翻译功能
def youdao(word):
    qword = urllib2.quote(word)
    baseurl = r'http://fanyi.youdao.com/openapi.do?keyfrom=sorrible&key=1660616686&type=data&doctype=<doctype>&version=1.1&q='
    builded_url = baseurl+qword
    resp = urllib2.urlopen(builded_url)
    result = json.loads(resp.read())
    if result['errorCode'] == 0:        
        if 'basic' in result.keys():
            trans = u'%s:\n%s\n%s\n网络释义：\n%s'%(result['query'],''.join(result['translation']),' '.join(result['basic']['explains']),'\n'.join(result['web'][0]['value']))
            return trans
        else:
            trans = u'%s:\n基本翻译:%s\n'%(result['query'],''.join(result['translation']))
    elif result['errorCode'] == 20:
        return u'对不起，要翻译的文本过长'
    elif result['errorCode'] == 30:
        return u'对不起，无法进行有效的翻译'
    elif result['errorCode'] == 40:
        return u'对不起，不支持的语言类型'
    else:
        return u'对不起，您输入的单词%s无法翻译,请检查拼写'% word