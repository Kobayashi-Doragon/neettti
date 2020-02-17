# 各メソッドを用意する用
import sql
import random

class player():
# コンストラクタ
    def __init__(self):
        self.player_id=0
        self.mother_fatigue=0
        self.money=1000
        self.neet_fulness=0
        self.neet_motivation=0
        self.time="仕事前"
        sql.connect(self)


# 入力を元にログインしてゲーム画面に
    def login(self,id,password):
        # DBと入力を照合(true or false)
        text="select exists(select * from users where player_id = '"+id+"');"
        result = sql.query(self, text)

        # ユーザIDが重複するとき
        if (result[0]):
            text="select * from users where player_id="+id
            result = sql.query(self, text)
            if result[1]==password:
                self.player_id = id
                self.mother_fatigue=result[2]
                self.money=result[3]
                self.time=result[4]
                self.neet_fulness=result[5]
                self.neet_motivation=result[6]
                return True
            else:
                return False
        # ユーザIDが重複しないとき
        else:
            return False

# アカウントの作成
    def create(self,id,password):
        text="select exists(select * from users where player_id = "+id+");"
        result=sql.query(self,text)

        # ユーザIDが重複するとき
        if (result[0]):
            return False
        # ユーザIDが重複しないとき
        else:
            text="insert into users values("+id+",'"+password+"',0,1000,'仕事前',0,0);"
            sql.add(self,text)
            self.player_id=id
            return True

# セーブ、ログアウトしてログイン画面に
    def logout(self):
        # saveメソッド呼び出し
        return True

# ステータスをDBに格納
    def save(self):
        # selfのステータスをDBに格納
        text="update users set mother_fatigue="+str(self.mother_fatigue)+",money="+str(self.money)+",time='"+self.time+"',neet_fulness="+str(self.neet_fulness)+",neet_motivation="+str(self.neet_motivation)+" where player_id="+str(self.player_id)+";"
        sql.add(self,text)
        return True

# 話しかけたとき
    def talk(self,talk_id):
        # selfのステータスを更新
        # DBのtalkテーブルからニートの返事を選択
        text = "select * from talk where talk_id = '" + talk_id + "'"
        result = sql.query(self, text)
        self.neet_motivation += result[3]
        return result[2][random.randint(0,1)]

# 食事を与えたとき
# 選択されたアイテムとDBを照合しステータスを更新
    def feed(self,food_id):
        # お金が足りるか確認用
        check="select food_price from food1 where food_id = '" + food_id + "'"
        price=sql.query(self,check)[0]

        if self.money-price<0:
            return "お金が足りません"
        else:
            text="select * from food1 where food_id = '" + food_id + "'"
            result=sql.query(self,text)
            self.money-=price
            self.neet_fulness+=result[3]
            self.neet_motivation+=result[4]
            return result[1]+"をあげた"

# 物を買ってあげたとき
# 選択されたアイテムとDBを照合しステータスを更新
    def buy(self,buy_id):
        # お金が足りるか確認用
        check = "select buy_price from buy where buy_id = '" + buy_id + "'"
        price = sql.query(self, check)[0]

        if self.money - price < 0:
            return "お金が足りません"
        else:
            text = "select * from buy where buy_id = '" + buy_id + "'"
            result = sql.query(self, text)
            self.money -= price
            self.neet_motivation += result[3]
            return result[1] + "をあげた"

# 仕事に行ったとき
    def work(self):
        if self.time == "仕事前":
            # ステータス(時間、疲労度、お金)を更新
            self.time="寝る前"
            self.mother_fatigue+=100
            self.money+=2000
            self.neet_fulness-=20
            self.neet_motivation+=self.neet_fulness/10
            return "仕事に行った"
        return "仕事に行く前に寝よう"

# 寝たとき
    def sleep(self):
        if self.time == "寝る前":
            # ステータス(時間、疲労度)を更新
            self.time = "仕事前"
            self.mother_fatigue -= 100
            return "寝た"
        return "先に仕事を終わらせよう"

# ニートの機嫌を確認
    def check_neet(self):
        if self.neet_motivation >= 100:
            return True
        else:
            return False