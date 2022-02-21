import tkinter as tk
import requests

def news():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=d7e7f7bd03ef45fc96260228dcba6e3d"
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n"

    label.config(text = my_news)


canvas = tk.Tk()
canvas.geometry("1200x600")
canvas.title("News App")

label = tk.Label(canvas, font = 24, text = "NEWS - INDIA")
label.pack(pady = 30)
label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)
button = tk.Button(canvas, font = 24, text = "Reload", command = news)
button.pack(pady = 50)

news()
canvas.mainloop()