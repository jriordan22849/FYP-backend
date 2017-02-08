from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import NameForm
import posts.models
from posts.models import Question
from posts.models import Answers



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'sitepages/name.html',{'form':form} )

def surveyProcess(request):
    return HttpResponse("success")


def create_survey(request):
    return render(request, 'sitepages/create_survey.html')

def view_survey(request):
    return HttpResponse("Woofghdfgla")



def add_questions(request):
    i = 1
    j = 1

    answers = []
    if request.method == "POST":
        if request.POST["surveyName"]:
            questionCounter = request.POST.get('numquestion', False)
            questionNumber = request.POST.get('questionNumber', False)
            ansNumber = request.POST.get('ans',False)
            #print("\n\n\nNumber of answers " + str(ansNumber))

            # save the survey title and information regarding the survey to the database.
            survey = posts.models.Post()
            survey.title = request.POST["surveyName"]
            survey.dateSurvCreated = timezone.datetime.now()
            survey.numOfQuestions = questionCounter
            survey.numOfTimesCompleted = 0


            print("\n\n\nSurvey Title: " + survey.title)
            survey.save()

            # Save the question label to the database.
            while i <= int(questionCounter): 
                #print("\n\n\nNumber of questions in the survey " + questionCounter);
                numAns = 0
                question = posts.models.Question()  
                question.questionLabel = request.POST.get("Question" + str(i),False)
                question.surveybelongto = survey.title
                question.questionNumber = i
                question.numberOfAnswers = request.POST.get("ans" + str(i),"0")
                print("Question " + str(i) + " Title: " + question.questionLabel);
                print("Number of answers for question " + str(i) + " is: " + question.numberOfAnswers)

                while j <= int(question.numberOfAnswers):
                    ans = posts.models.Answers()
                    ans.answerID = str(j)
                    ans.questionNumber = i
                    ans.surveyTitle = survey.title 
                    ans.questionLabel = question.questionLabel
                    ans.questionType = request.POST.get("questionType" + str(i), "No Choice")
                    #print("Python questionType" + str(i))
                    print("Question " + str(i) + " type: " + ans.questionType)

                    if ans.questionType == "multiple":
                        print("Question " + str(i) + " type: " + ans.questionType)
                        ans.answerLabel = request.POST.get("question"+str(i)+"Answer"+str(j),"False")
                        print("Answer Option " + str(j) + " : " + ans.answerLabel)
                        numAns = j

                    if ans.questionType == "images":
                        print("optionSelected"+str(i) + "Option"+str(j))
                        ans.urlForImage = request.POST.get("question"+str(i)+"Image"+str(j), "No URL")
                        ans.answerLabel = request.POST.get("question"+str(i)+"Image"+str(j), "No URL")
                        print("Url " +ans.urlForImage)

                    ans.save()
                    j += 1

                #question.numberOfAnswers = numAns + 1
                #print("Print questionNumber " + str(i))
                question.save()
                j = 1
                i += 1
            


            return render(request, 'sitepages/addQuestions.html', {'survey': survey})
        else:
            return render(request, 'sitepages/create_survey.html')
    else:
        return render(request, 'sitepages/create_survey.html')