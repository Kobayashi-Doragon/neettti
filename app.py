# ルートによってメソッドを呼び出す

from flask import Flask,render_template,request
import methods

app = Flask(__name__)
player=methods.player()

# 初めのログイン画面表示
@app.route("/")
def login_screen():
    return render_template("login.html",message="")

# ログインボタンでログインしゲーム画面へ
@app.route("/login",methods=["POST"])
def login():
    # 入力データを引数にloginメソッド呼ぶ
    id=request.form["id"]
    password=request.form["password"]
    # DBと同じならゲーム画面へ、違うならもう一度入力してもらう
    if(player.login(id,password)):
        return render_template("game.html",money=player.money,fatigue=player.mother_fatigue,time="仕事前")
    else:
        return render_template("login.html",message="ユーザIDもしくはパスワードが間違っています")

# 入力を元にアカウント追加
@app.route("/create",methods=["POST"])
def create_account():
    id = request.form["id"]
    password = request.form["password"]

    if(player.create(id,password)):
        return render_template("game.html",money=player.money,fatigue=player.mother_fatigue,time="仕事前")
    else:
        return render_template("login.html",message="ユーザIDが既に使用されています")


# セーブボタン用


# セーブしてログイン画面に戻る
@app.route("/logout")
def logout():
    # セーブ
    return render_template("login.html")

# ご飯と同じく選択肢で
@app.route("/talk")
def talk():
    # トーク
    answer=player.talk()
    return render_template("game.html",message="話しかけた",neet_answer=answer,money=player.money,fatigue=player.mother_fatigue,time="仕事前")

@app.route("/feed")
def feed():
    # feed
    food_id = request.args.get("food_id")
    result=player.feed(food_id)
    return render_template("game.html",message=result,neet_answer="",money=player.money,fatigue=player.mother_fatigue,time="仕事前")

@app.route("/buy")
def buy():
    # buy
    buy_id = request.args.get("buy_id")
    return render_template("game.html",message=buy_id+"を与えた",neet_answer="",money=player.money,fatigue=player.mother_fatigue,time="仕事前")

@app.route("/work")
def work():
    # work
    return render_template("game.html",message="仕事に行った",money=player.money,fatigue=player.mother_fatigue,time="仕事前")

@app.route("/sleep")
def sleep():
    # sleep
    return render_template("game.html",message="寝た",money=player.money,fatigue=player.mother_fatigue,time="仕事前")



if __name__ == '__main__':
    app.run()