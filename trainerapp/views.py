from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'trainerapp'


# Create your views here.

def trainerhomepagecall(request):
    return render(request,'trainerapp/trainerhomepage.html')

def course(request):
    return render(request,'trainerapp/courses.html')

def it(request):
    return render(request,'trainerapp/ittools.html')
def it2(request):
    return render(request,'trainerapp/ittools2.html')

from django.shortcuts import render

# Define the correct answers to the assignment questions
CORRECT_ANSWERS = {
    'q1': 'a',
    'q2': 'b',
    'q3': 'b',
    'q4': 'c',
    'q5': 'a',
    'q6': 'd',
    'q7': 'b',
    'q8': 'b',
    'q9': 'a',
    'q10': 'b',
}


# Function to evaluate the answers and calculate progress
def evaluate_answers(user_answers):
    correct_count = 0
    for key, correct_answer in CORRECT_ANSWERS.items():
        if user_answers.get(key) == correct_answer:
            correct_count += 1

    wrong_count = len(CORRECT_ANSWERS) - correct_count
    return correct_count, wrong_count


# View to render the assignment form and calculate progress
def assignment_view(request):
    if request.method == "POST":
        # Get user-submitted answers
        user_answers = {
            'q1': request.POST.get('q1'),
            'q2': request.POST.get('q2'),
            'q3': request.POST.get('q3'),
            'q4': request.POST.get('q4'),
            'q5': request.POST.get('q5'),
            'q6': request.POST.get('q6'),
            'q7': request.POST.get('q7'),
            'q8': request.POST.get('q8'),
            'q9': request.POST.get('q9'),
            'q10': request.POST.get('q10'),
        }

        # Evaluate the answers
        correct_count, wrong_count = evaluate_answers(user_answers)
        total_questions = len(CORRECT_ANSWERS)

        # Calculate percentages
        correct_percentage = (correct_count / total_questions) * 100
        wrong_percentage = (wrong_count / total_questions) * 100

        # Send the percentages to the template
        context = {
            'correct_percentage': correct_percentage,
            'wrong_percentage': wrong_percentage,
            'correct_count': correct_count,
            'wrong_count': wrong_count,
        }
        return render(request, 'trainerapp/progress.html', context)

    # If GET request, show the assignment form
    return render(request, 'trainerapp/assignment.html')


