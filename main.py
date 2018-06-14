import cloud
import music


def main(opt, search, file_name=None, background="white", font="简约字体.ttf", masker=None, 
stopword=[], masker_val=0.5,w=1000,h=1000,maxsize=None,
fontstep=2, simple=True, usr='local'):
    stopword.append("首歌")
    if opt==0:
        try:
            cloud.draw_wordcloud('data/'+usr+'/comment.txt', background=background,
             font="简约字体.ttf", masker='data/'+usr+'img.jpg', stopword=stopword, 
             masker_val=masker_val, w=w, h=h, maxsize=maxsize,fontstep=fontstep,
             simple=simple, usr=usr)
        except:
            print('draw_cloud wrong')
            return -1
        return 0
    
    elif opt==1:
        flag = music.singer_craw(search,usr)
        if flag != 0:
            return -1
        # try:
        cloud.draw_wordcloud(file_name='data/'+usr+'/comment.txt', background=background, 
        font="简约字体.ttf", masker='data/'+usr+'/img.jpg', 
        stopword=[], masker_val=masker_val,w=1000,h=1000,maxsize=None,
        fontstep=2, simple=True, usr=usr)
        # except:
            # return -1
        return 0

    elif opt==2:
        print("Do nothing")
        return 0


if __name__ == '__main__':
    main(1, '杨千嬅')