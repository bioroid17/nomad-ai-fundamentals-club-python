# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r", encoding="utf-8") as f:
        return json.load(f)


# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

ITEMS_PER_PAGE = 20


@app.get("/")
def home():
    page = request.args.get("page", 1, type=int)
    jobs = load_jobs()
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    paginated_jobs = jobs[start:end]
    return render_template(
        "home.html",
        total_jobs=len(jobs),
        jobs=paginated_jobs,
        page=page,
        total_pages=(len(jobs) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE,
    )


@app.get("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = load_jobs()
    filtered_jobs = [job for job in jobs if keyword.lower() in job["title"].lower()]
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    paginated_jobs = filtered_jobs[start:end]
    return render_template(
        "search.html",
        total_jobs=len(filtered_jobs),
        jobs=paginated_jobs,
        keyword=keyword,
        page=page,
        total_pages=(len(filtered_jobs) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE,
    )


# /YOUR CODE


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT
