# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r", encoding="utf-8") as f:
        return json.load(f)


# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:
@app.get("/")
def home():
    jobs = load_jobs()
    print(len(jobs))
    return render_template("home.html", jobs=jobs)


@app.get("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = load_jobs()
    filtered_jobs = [job for job in jobs if keyword.lower() in job["title"].lower()]
    return render_template("search.html", jobs=filtered_jobs, keyword=keyword)


# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT
