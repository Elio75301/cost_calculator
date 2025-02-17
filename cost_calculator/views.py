from django.shortcuts import render
from .forms import OliveOilCalculationForm
from .models import OliveOilCalculation

def calculate_cost(request):
    if request.method == 'POST':
        form = OliveOilCalculationForm(request.POST)
        if form.is_valid():
            calculation = form.save()
            return render(request, 'cost_calculator/result.html', {
                'calculation': calculation
            })
    else:
        form = OliveOilCalculationForm()
    
    return render(request, 'cost_calculator/calculate.html', {
        'form': form
    })
