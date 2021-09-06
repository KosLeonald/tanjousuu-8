import json
import random
#import time , datetime

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

option_1 = "【誕生数８】\n今の状態をあるがままに受け入れてください。抵抗せず、そのままを受け入れてください。どうしても認め難く変えたいと思うものは、一旦受け入れた後であなたの良いように変えてゆけばよいのです。状況はこれからとても良くなっていく可能性を秘めていますが、それはあなたの受容性の強化にかかっています。変化とはある程度の時間を要する事もありますから、タイミングが来るまでは意識的に「静かな受容」でいることに徹しましょう。"
option_2 = "【誕生数８】\nあなたの中で「再誕生」が始まっているようです。これまでの人生では、自ら動かずに人任せな時期や、反対に自分で何とかしようと息巻いて激しく突き進んだ時期もあったことでしょう。そのような時期を経て、これからは本来のあなたらしさ、自然のままのあなたを出していける無垢な時期に入ります。あなたが培ってきた強さやエネルギーが助けとなるでしょう♡"
option_3 = "【誕生数８】\nあなたは間違った選択か習慣的な行動のせいで、自分を自己批判し恥じ入る場面に遭遇するかも知れません。\nけれど、あなたは進化するためにここにいて、その道のりの中で多くの過ちも犯すでしょう。それはあなたの学習過程の一部であり、あなたの成長のために必要なことだという事を忘れないでください。\n結局のところ、とても深刻で重大であるがために、許しようがない過ちや失敗などないのです。周りの人たちも、たとえあなたがひどい過ちを犯しても、あなたを愛することを止めはしません。"
#option_4 = "確率分散 1"
#option_5 = "確率分散 2"
#option_6 = "確率分散 3"

def main():
    USER_ID = info['USER_ID']
    mylist = [ option_1,option_2,option_3]    
    messages1= TextSendMessage(random.choice(mylist))
    #messages = TextSendMessage(text=random.choice(mylist))
    #messages2= TextSendMessage(text = "今日も1日頑張りましょう♪")
    # today = datetime.datetime.fromtimestamp(time.time())
    #time  = today.strftime('%H')      
 
     #   if int(time) > 20 :
    line_bot_api.broadcast(messages1)
     #   else :
    #line_bot_api.broadcast(messages2)  
    
if __name__ == "__main__" :
    main()
