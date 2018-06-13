import cloud
import music


def main(opt, search, file_name, background="white", font="ttf/简约字体.ttf", masker=None, 
stopword=[], masker_val=0.5,w=1000,h=1000,maxsize=None,
fontstep=2, simple=True):
    stopword.append("首歌")
    if opt==0:
        cloud.draw_wordcloud(file_name, background, font, masker, 
                            stopword, masker_val,maxsize,fontstep, simple)
        return
    
    elif opt==1:
        music.singer_craw(search)
        cloud.draw_wordcloud('data/comment.txt', 'data/img.jpg', font, masker, 
                            stopword, masker_val,maxsize,fontstep, simple)
        return

    elif opt==2:
        print("Do nothing")
        return 
