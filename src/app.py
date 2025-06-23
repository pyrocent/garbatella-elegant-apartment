from pyairbnb import get_calendar
from datetime import timedelta
from secrets import token_hex
from config import lang
from flask import (
    Flask,
    jsonify,
    request,
    redirect,
    send_file,
    make_response,
    render_template
)

app = Flask(__name__, template_folder = "app/templates/min", static_folder = "app/static")
app.config.update(
    SECRET_KEY = token_hex(16),
    SESSION_COOKIE_NAME = "lang",
    SESSION_COOKIE_SECURE = True,
    SESSION_COOKIE_HTTPONLY = True,
    SESSION_COOKIE_SAMESITE = "strict",
    SESSION_COOKIE_DOMAIN = ".garbatella-elegant-apartment.com"
)

@app.get("/")
def index():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("index.min.html", lang = lang[user_lang]["index"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/more/<tab>")
def more(tab):
    if tab == "home" or tab == "neighborhood":
        user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
        response = make_response(render_template("more.min.html", lang = lang[user_lang]["more"], tab = tab))
        response.set_cookie("lang", user_lang, timedelta(weeks = 52))
        return response
    else:
        return redirect("/")

@app.get("/book-holiday-home")
def book_holiday_home():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("book-holiday-home.min.html", lang = lang[user_lang]["book-holiday-home"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/thanks")
def thanks():
    user_lang = request.cookies.get("lang", request.accept_languages.best_match(lang.keys(), default = "EN"))
    response = make_response(render_template("thanks.min.html", lang = lang[user_lang]["thanks"]))
    response.set_cookie("lang", user_lang, timedelta(weeks = 52))
    return response

@app.get("/tourist-tax-payment")
def tourist_tax_payment(): return redirect("https://buy.stripe.com/fZe2akcUl7gOdRC002")

@app.get("/policy")
def policy(): return redirect("https://audaxly.com/privacy-policy?code=ln3hbi9fqw5k6r")

@app.post("/disable_days")
def disable_days():
    return jsonify([
        day["calendarDate"]
        for year in get_calendar(room_id = "1103438586972971737")
            for day in year["days"]
                if day["bookable"] == False
    ])

@app.post("/")
@app.post("/more/home")
@app.post("/more/neighborhood")
@app.post("/book-holiday-home")
@app.post("/tourist-tax-payment")
def change_language():
    response = make_response(redirect(request.referrer))
    response.set_cookie("lang", request.form.get("lang"))
    return response

@app.get("/robots.txt")
@app.get("/sitemap.xml")
def serve_file(): return send_file(f"app/{request.path}")

@app.errorhandler(404)
@app.errorhandler(405)
def error(_): return redirect("/")