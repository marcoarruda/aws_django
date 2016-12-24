from django.http import HttpResponse
from django.template import loader
from .models import Subscription
from django.utils import timezone


def index(request):
    template = loader.get_template('event/index.html')
    context = {'subscription_list': Subscription.objects.order_by('-subscription_datetime')[:5]}
    return HttpResponse(template.render(context, request))

def subscribe(request):
    template = loader.get_template('event/subscribe.html')
    name = request.POST['name'].encode('ascii', 'ignore')
    email = request.POST['email'].encode('ascii', 'ignore')
    subscription = Subscription(
        subscription_name=name,
        subscription_email=email,
        subscription_datetime=timezone.now())
    subscription.save()
    context = {'subscription': subscription,
        'message': "Congrat.., now you are subscribed!"}
    return HttpResponse(template.render(context, request))

