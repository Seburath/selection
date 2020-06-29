# selection_1
Selection process of June 29, 2020 [12:00 GMT]

Raise the containers:

docker-compose up -d

Install python requirementes:

docker-compose exec cyberhead pip3 install -r requirements.txt

Serve the backtesting:

docker-compose exec cyberhead python3 serve.py

This should serve a webpage on: http://localhost:5000

Objective:
- Send only one pull request that fix this repository

Rules:
- The repository will be kept empty until the selection begins.
- We start at 12:00 GMT.
- We finish at 14:00 GMT.
- Do not answer messages during these two hours, to avoid chaos.

Caution!
- Do not send your pull request before the end time, so we avoid suspicions that someone will copy you.
- Do not send your pull request after the end time, so we avoid suspicions that you copied.

Clarifications:
- Branch 0 has a past selection process, you can see it as a reference, but this is test will be diferent.
- Fully fixing this repository should take way more than 2 hours, don't stress out about and do what you can! :)
- You should not focus on changing "Dockerfile" or "docker-compose.yml" but feel free to to send anything that you find important.

Any question you can ask me at:

t.me/seburath
