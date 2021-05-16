import requests
import json

easy = requests.get(
    "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
data1 = easy.json()['results']

medium = requests.get(
    "https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean")
data2 = medium.json()['results']

hard = requests.get(
    "https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean")
data3 = hard.json()['results']

type = 0


def getQuestion(x):
    if x == "1":
        return data1[0]['question']
    if x == "2":
        return data2[0]['question']
    if x == "3":
        return data3[0]['question']


def getAnswer(x):
    if x == "1":
        return data1[0]['correct_answer']
    if x == "2":
        return data2[0]['correct_answer']
    if x == "3":
        return data3[0]['correct_answer']


def playingQuestion():
    x = input("Enter N if you DO NOT want to play:: ")
    if x == "N" or x == "n":
        end()


def questionType():
    qtype = input(
        "What type of diffifulty do you want? Enter:\n1 :: Easy\n2 :: Medium\n3 :: Hard\nEnter :: ")
    return qtype


def intro():
    print("Welcome to this simple Trivia Game!")
    print("---------------------------------------------------")
    playingQuestion()
    type = questionType()
    print("---------------------------------------------------")
    print("Lets start playing!!\nYour Question is:")
    print(getQuestion(type))
    answer(type)
    end()


def answer(x):
    print("---------------------------------------------------")
    ans = input("Is this True or False? :: ")
    correct = str(getAnswer(x))
    print("---------------------------------------------------")
    if ans == correct:
        print("Wow! You are very smart! You got the Question right")
    else:
        print("Oh no! Thats not the correct answer! The correct answer was " +
              correct)


def end():
    print("---------------------------------------------------")
    print("Thank you for playing this game with us! I hope to see you again!")
    exit()


intro()
