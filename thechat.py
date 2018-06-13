#coding=utf8
import itchat
import main
import os

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def text_reply(msg):
    if (msg['Content'].startswith('07624')):
        l = msg['Content'].split()
        if len(l)==2:
            print(msg['FromUserName']+': Begin to create '+str(l[1]))
            itchat.send('Begin to create '+str(l[1])+', please wait ...',toUserName=msg['FromUserName'])
            
            if not os.path.exists('data/'+ msg['FromUserName']):
                os.makedirs('data/'+ msg['FromUserName'])

            try:
                main.main(1, l[1], usr=msg['FromUserName'])
            except:
                print('Generate Error')
                itchat.send('sorry, something wrong on generating the wordcloud of '+str(l[1])+'. Byebye~',toUserName=msg['FromUserName'])

            itchat.send('@img@data/'+msg['FromUserName']+'/img.jpg' ,toUserName=msg['FromUserName'])
            itchat.send('@fil@data/'+msg['FromUserName']+'/comment.txt',toUserName=msg['FromUserName'])
            itchat.send('@img@data/'+msg['FromUserName']+'/result.jpg',toUserName=msg['FromUserName'])
            itchat.send('Finish '+str(l[1]),toUserName=msg['FromUserName'])



# itchat.send('Hello world!',toUserName='filehelper')
# itchat.send('@img@example/img.jpg' ,toUserName='filehelper')
# itchat.send('@fil@example/comment.txt',toUserName='filehelper')
# itchat.send('@img@example/comment.txt',toUserName='filehelper')



itchat.auto_login(hotReload=True)

itchat.run()