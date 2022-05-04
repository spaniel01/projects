# -*- coding: utf-8 -*-
import random
import datetime 
import pickle

#Initalise pickle file ONCE for successful load prior to running code
vocab = {}
vocabFails = {}
with open('savedDics.txt', 'wb') as file:
    pickle.dump([vocab, vocabFails], file)

#mainMenu func for 1 and 2
def vocabTest(vocab):
    print("\nPlease enter the correct English word.\nIf you are correct, the word will not be tested again. If not, you will be asked time and again, until you have correctly translated all the words! Good luck!\nIf you want to stop practicing, write Exit.")
    vocabPrac = vocab.copy()
    vocabTestFails = {}
    answer = ""
    while len(vocabPrac) > 0 and answer != "Exit":
        word = random.choice(list(vocabPrac.keys()))
        answer = input(word+":  ")
        if answer == "Exit":
            print("If you wish to practice the words you struggled with, choose option 2 from the main menu!")
            break
        else:
            if answer == vocabPrac[word]:
                print("Correct! Well done!")
                del vocabPrac[word]
                if len(vocabPrac) == 0:
                    print("Good job, you got them all!")
            else:
                print("Close, but not close enough! The right answer is: " +vocabPrac[word])
                vocabTestFails.update({word : vocabPrac[word]})
    return vocabTestFails
     
#mainMenu func for 3
def vocabTestGraded(vocab):
    corAns = 0
    wrAns = 0
    print("\nThis is a test! Please enter the correct English word.\nGood luck!\nIf you want to termiante the test early, write Exit.")
    vocabPrac = vocab.copy()
    vocabTestFails = {}
    answer = ""
    while len(vocabPrac) > 0 and answer != "Exit":
        word = random.choice(list(vocabPrac.keys()))
        answer = input(word+":  ")
        if answer == "Exit":
            # print("If you wish to practice the words you struggled with, choose option 2 from the main menu!")
            break
        else:
            if answer == vocabPrac[word]:
                corAns += 1
                del vocabPrac[word]
                print("Correct!")
                if len(vocabPrac) == 0:
                    print("You have finished the test! Well done!")   
            else:
                wrAns += 1
                print("The correct answer was: "+vocabPrac[word])
                vocabTestFails.update({word : vocabPrac[word]})
                del vocabPrac[word]  
    print("Your results:\nYou were shown "+str(corAns + wrAns)+" words.\nYou got "+str(corAns)+" right and "+str(wrAns)+" wrong (average of "+str((corAns/(corAns + wrAns))*100)+" percent correct. If you wish to practice the words you struggled with, choose option 2 from the main menu!\n")
    return vocabTestFails

#mainMenu func for 4
def editVocab(vocab):
    editVocabOpts = 0
    while editVocabOpts != 4:
        text = "\nDo you wish to:\n(1) View vocab\n(2) Add vocab\n(3) Delete vocab \n(4) Exit"
        print(text)
        editVocabOpts = input("Please input the corresponding number: ")
        editVocabOpts = userInputValid(editVocabOpts, text, 1, 2, 3, 4)
        if editVocabOpts == 1:
            counter = 1
            print("\nThis is your current vocab list:")
            for key, value in vocab.items():
                print(str(counter)+" "+key+" - "+value)
                counter += 1
        elif editVocabOpts == 2:
            print("You can now input new words. Input Exit when you are finished!")
            newWord=""
            while newWord != "Exit":
                newWord = input("Please input the new word in German: ")
                if newWord == "Exit":
                    break
                newWordTrans = input("Please input the new word in English: ")
                if newWordTrans == "Exit":
                    break
                vocab.update({newWord : newWordTrans})
        elif editVocabOpts == 3:
            print("You can now delete words. Input Exit when you are finished! These are the current words included in your dictionary.")  
            print(list(vocab.keys()))
            wordToDel = ""
            while wordToDel != "Exit":
                wordToDel = input("Please input the German word to delete it. ")
                if wordToDel in vocab.keys():
                    print("The words "+ wordToDel+ "- " + vocab.pop(wordToDel)+" have been deleted!")
                else:
                    print("That word is not contained in the dictionary!")
        elif editVocabOpts == 4:
            return vocab

#User input validation
def userInputValid(menuOpt, message, *args):
    mainMenuEval = True
    while mainMenuEval:
        try: 
            menuOpt = int(menuOpt)
        except ValueError:
            print("\nNot a number!\n" + message)
            menuOpt = input("Please enter the corresponding number: ")
            continue
        if menuOpt in args:
            mainMenuEval = False
            continue
        else:
            print("\nNot an option!\n" + message)
            menuOpt = input("Please enter the corresponding number: ")
            continue
    return menuOpt

#Main prog
def vocabTrainer():
    leave = "no"
    #Load previously saved data, welcome message
    with open('savedDics.txt', 'rb') as file:
        vocab, vocabFails = pickle.load(file)
    today = datetime.date.today() 
    print("Welcome!\nToday is " + today.strftime("%B %d, %Y")+".")
    while leave != "yes":
        text = "\nWhat do you wish to do? \n(1) Practice all\n(2) Practice last fails\n(3) Do a test \n(4) Edit vocab \n(5) Exit program"
        print(text)
        menuOpt = input("Please enter the corresponding number: ")
        menuOpt = userInputValid(menuOpt, text, 1, 2, 3, 4, 5)
        if menuOpt == 1:
            vocabFails = vocabTest(vocab)
        elif menuOpt == 2:
            if len(vocabFails) == 0:
                print("You have not made any fails recently. Please practice or do a test to identify your weaknesses!")
            else:
                vocabFails = vocabTest(vocabFails)
        elif menuOpt == 3:
            vocabFails = vocabTestGraded(vocab)
        elif menuOpt == 4:
            vocab = editVocab(vocab)
        elif menuOpt == 5:
            print("\nAre you sure you wish to leave?")
            leave = input("Type yes or no! ")
            if leave == "yes":
                print("Thanks for visiting! See ya!")
                with open('savedDics.txt', 'wb') as file:
                    pickle.dump([vocab, vocabFails], file)
vocabTrainer()

