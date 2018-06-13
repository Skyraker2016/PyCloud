import cloud
import music


def main(opt, search, file_name=None, background="white", font="ttf/简约字体.ttf", masker=None, 
stopword=[], masker_val=0.5,w=1000,h=1000,maxsize=None,
fontstep=2, simple=True, usr='local'):
    stopword.append("首歌")
    if opt==0:
        cloud.draw_wordcloud(file_name, background, font, masker, 
                            stopword, masker_val,maxsize,fontstep, simple, usr)
        return
    
    elif opt==1:
        music.singer_craw(search,usr)
        cloud.draw_wordcloud(file_name='data/'+usr+'/comment.txt', background=background, 
        font="简约字体.ttf", masker='data/'+usr+'/img.jpg', 
        stopword=[], masker_val=0.5,w=1000,h=1000,maxsize=None,
        fontstep=2, simple=True, usr=usr)
        return

    elif opt==2:
        print("Do nothing")
        return 


if __name__ == '__main__':
    main(1, '杨千嬅')