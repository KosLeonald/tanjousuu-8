import json 
import random
coding: shift_jis
#import time , datetime


from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json' , 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    mylist = [ "【誕生数１】\nこれまでの人生の中で、あなたはいくつも姿を変えて今日まで来ました。何もかも人任せで自分というものがなかった時期があったかも知れませんし、ただ我武者羅に頑張ることだけにエネルギーを注いだ時期もあったかも知れません。紆余曲折を経て今、新たな平穏が訪れつつあるようです。あなたが直感で感じることと心で願う事が一致し、気後れしたり虚勢を張ったりする必要もなく、力を抜いてごく自然体でいられる、つまり本来のあなた自身に戻れる時のようです。\n\n【誕生数２】\nあなたの心に強いストレスがかかっている様子が出ています。後でこんな風になったらよくないから、あれが心配だから、不安を消したいから・・・あらゆる不安や心配が心を占め、その予防のためにやるべき多くの事が身体を占め、あなたはもう一杯いっぱいですね。でも、不安や心配というのはそれがやって来てから対処をするので間に合います。先々の来るかどうか分からない事で悩むよりも、あなたの心の望むままに、「今」を生きてくださいね。\n\n【誕生数３】\nこれまであなたは難しい状況に屈することなく、あらゆる力を出して頑張ってきました。その成果が今にも現れようとしている時に、どうして自分を責めてしまっているのですか？自分の力不足や、他人への迷惑を思い、自己嫌悪に陥っているのでしょうか。そうであれば「３」の人らしい傾向ではありますが、誰もあなたに憤ってはいません。迷惑でもありません。さぁ頭を抱えて閉じた目を開けて、あなたがもたらした素晴らしい成果と称賛を受け取りましょう✨\n\n【誕生数４】\nあなたの心の声に耳を傾けてください。誰かの迷惑や噂や評価、顔色などを全く気にしなくてよい状況ならあなたはどんな答えを出すか、その声を聴いてみてください。本当はきっとあなたには分かっているのではないでしょうか。自分が何をしたいか、どう動きたいか。もしもそれが実行出来ていないとしたら、周りの環境のせいではなく、あなた自身への信頼不足なだけでしょう。今は、自分の心の声に素直になること、自分を信じてそれに飛び込んで行くことです。\n\n【誕生数５】\n今週は、あなたの情熱を注げることに対して行動することがカギとなるようです。その情熱は今はもう手放してしまっていること、あるいはその胸の内に抑え込んでいる事かも知れません。今もホットな状態で維持しているものの可能性もあります。あなたのエネルギーの中心にあって、マグマのように熱くうごめいているその情熱を今週は思い切り出していきましょう。迷いを捨ててワクワクする時です。情熱と共に光をまとって突き進みましょう。\n\n【誕生数６】\n痛みと苦しみに耐えていた時期が過ぎて、あなたの前に新たな展開、展望が広がってきました。これまで辛かった分を上回るほど、あなたは新たな展開に大きく期待が出来ますし、現在のところに留まらず、どこへでも飛んで行ける自由さも手に入れました。閉ざされ引き止められていた自分の根から起き上がり、これからはあまり深刻にならずに、もっともっと人生を楽しむ方向に舵を切りましょう。明るいきらめきの世界が広がっていることを信じてください。\n\n【誕生数７】\nあなたが結果を求めていることに関しては、もう少し時間が必要なようです。状況は悲観的ではありませんが、時間を必要としているのです。もともとこの道はゴールまでの道のりが果てしなく遠いものだったので、先々のことを考えたり先走ったりするのはあまり意味のないことでした。とは言え、結果は必ず出るよと告げられていますので、今は忍耐の時と割り切って、焦らず状況を楽しむくらいの感覚でいてください。芽が出たら花が咲く時が必ずやって来ます。\n\n【誕生数８】\n今の状態をあるがままに受け入れてください。抵抗せず、そのままを受け入れてください。どうしても認め難く変えたいと思うものは、一旦受け入れた後であなたの良いように変えてゆけばよいのです。状況はこれからとても良くなっていく可能性を秘めていますが、それはあなたの受容性の強化にかかっています。変化とはある程度の時間を要する事もありますから、タイミングが来るまでは意識的に「静かな受容」でいることに徹しましょう。\n\n【誕生数９】\nもしも今あなたが生き辛さや拘束感を感じて、息が詰まりそうな状態なら、それは自分で自分を縛っているからかも知れません。「９」のあなたは誠実で正直で、与えられたことは必ずやり遂げる意志の強さを持っています。けれどもあまりにも「こうあるべき」が強すぎてはいませんか？時には手抜きも息抜きも必要です。それは怠ける事ではなく、「建設的な柔軟さ」です。誰かの目や評価、ご機嫌など気にせず、あなたのやりやすい方法で生きてみてはいかがでしょうか♬\n\n\n占い＆タイ式リラクゼーション グラターイ\n俵 ひとみ","【誕生数１】\nあなたは今、リーダーとしての役割を意識的に全面的に受け入れる時です。あなたの集中力、専心、安定感、鍛錬を通して、あなたは裏方から登場し、能力と知恵の両方で人々に認められるようになります。そして他の人は自然とあなたのカリスマ的波動に引き付けられあなたを信頼できると感じ、あなたの指導力に従うでしょう。あなたは自分の明るい光を世の中に放ち、あなたが他の人々を高みに導いていく際、その情熱や自信について語らなくてよいのです。\nただし自分に無理を課したり、燃え尽きてしまうことには注意してください。\n「自信を持ってリードしていきなさい」\n\n【誕生数２】\nあなたを苦しめた全ての攻撃、裏切りによって、瞬間的に傷ついたあなたの魂が癒される時です。\n今このときは、自分自身を信頼することは難しいかも知れませんが、信頼をしなければなりません。起こってしまったことに対して、自分自身や他人を責めるのをやめ、全てを全面的に許しましょう。人間はみな、深刻で時には酷い誤りを犯すものです。あなたは侵害されたと感じても、それは自分の経験から学ぶべき教訓なのです。\nもしもあなたが否定の泥沼に留まるなら、それはあなたを不利な立場に陥れるだけです。あなたはこれらの不愉快な経験から学び、どのように再発防止ができるのかを考えてみましょう。\n「危機は去りました。あなたは安全です。今こそ癒され、そしてあなたの経験から学ぶ時です」\n\n【誕生数３】\nあなたが人生に望む物は何でも作り出すことができますが、それはあなたが必要な仕事を自ら進んでしようとする時のみにできることです。そこには、近道も迂回路も無料のランチもないということです。\n成功するための唯一の道は、鍛錬し、やり続けるということです。あなたの目的を果たすために必要なことは何でも、自ら進んで行ってください。もし、自分がしなければならないことが何か分からない時は、それが何であるかを学びましょう。ハートと頭をオープンにして、あなたの基準を高く掲げてください。\n「いかなる分野においても、習熟するということは、あなた自身の中から最善だと思うものを求めることに他なりません」\n\n"]
       
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
