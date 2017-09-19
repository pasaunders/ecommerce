from django.shortcuts import render, redirect


def rendering(request):
    return render(request, 'order_form/index.html')


def order(request):
    product_id = {
        '1': 19.99,
        '2': 9.99,
        '3': 4.99,
        '4': 49.99,
    }
    if 'spent' not in request.session:
        request.session['spent'] = 0
        request.session['orders'] = 0
        request.session['recent_purchase'] = None
    if request.method == "POST":
        request.session['orders'] += int(request.POST['number'])
        spending = int(request.POST['number']) * product_id[request.POST['product_id']]
        request.session['spent'] += spending
        request.session['recent_purchase'] = spending
        return redirect('/amadon/checkout')
    return redirect('/amadon')


def checkout(request):
    context = {
        'spent': request.session['spent'],
        'orders': request.session['orders'],
        'recent_purchase': request.session['recent_purchase'],
    }
    return render(request, 'order_form/checkout.html', context)