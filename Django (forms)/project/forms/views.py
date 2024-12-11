from django.shortcuts import render
from .models import Question, Answer

def homepage(request):
    return render(request, "homepage.html")

def quiz_view(request):
    questions = Question.objects.all() 
    if request.method == 'POST':  
        correct_answers = 0  
        incorrect_answers = []  

        
        for question in questions:
            answer_id = request.POST.get(f'question_{question.id}')
            if answer_id:  
                answer = Answer.objects.get(id=answer_id)
                
                if answer.is_correct:
                    correct_answers += 1
                else:
                    correct_answer = question.answers.filter(is_correct=True).first()
                    incorrect_answers.append({
                        'question': question.text,
                        'user_answer': answer.text,
                        'correct_answer': correct_answer.text if correct_answer else 'No correct answer'
                    })

        return render(request, 'results.html', {
            'correct_answers': correct_answers,
            'total_questions': len(questions),
            'incorrect_answers': incorrect_answers
        })
    
    return render(request, 'forms.html', {'questions': questions})
