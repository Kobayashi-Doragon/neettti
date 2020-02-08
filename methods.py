# 各メソッドを用意する用
import sql

class player():
# コンストラクタ
    def __init__(self):
        self.player_id=0
        self.mother_fatigue=0
        self.money=1000
        self.time=True
        self.neet_fulness=0
        self.neet_motivation=0
        sql.connect(self)


# 入力を元にログインしてゲーム画面に
    def login(self,id,password):
        # DBと入力を照合(true or false)
        return True

# アカウントの作成
    def create(self,id,password):
        # 入力に基づいてDBに追加
        # IDがかぶってる場合メッセージ表示
        return True

# セーブ、ログアウトしてログイン画面に
    def logout(self):
        # saveメソッド呼び出し
        return True

# ステータスをDBに格納
    def save(self):
        # selfのステータスをDBに格納
        return True

# 話しかけたとき
    def talk(self):
        # selfのステータスを更新
        # DBのtalkテーブルからニートの返事を選択
        # 返事を画面に表示
        answer="(ニートの返事)"
        return answer

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
    def buy(self):
        # 選択されたアイテムとDBを照合しステータスを更新
        return True

# 仕事に行ったとき
    def work(self):
        # ステータス(時間、疲労度、お金)を更新
        # 画面を更新
        return True

# 寝たとき
    def sleep(self):
        # ステータス(時間、疲労度)を更新
        # 画面を更新
        return True