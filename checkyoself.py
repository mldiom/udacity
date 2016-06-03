import urllib

def read_text():
    lyrics = open ("/Users/user/Documents/panda.txt")
    content_of_file = lyrics.read()
    #print (content_of_file)
    #print(enumerate( "shit", start=1))
    lyrics.close()
    check_profanity(content_of_file)

def check_profanity(txt_to_txt):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+txt_to_txt)
    output = connection.read()
    print(output)
    connection.close()


read_text() 
