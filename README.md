# Human Benchmark Reaction Time Bot

A simple Python Selenium bot for the Human Benchmark reaction time test from https://humanbenchmark.com/tests/reactiontime. The bot waits for the presence of the green element ".view-go". Once it is detected, the bot clicks the button. Please note that this was made for Firefox; if using Chrome please change webdriver.Firefox() to webdriver.Chrome() on line 6.
