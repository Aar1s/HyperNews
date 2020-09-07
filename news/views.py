from django.shortcuts import render, HttpResponse, Http404, redirect
from django.views import View
import itertools, json, random
from  datetime import datetime


class IntroView(View):
    def get(self, request):
        return HttpResponse('Coming soon')

def open_json():
    with open('C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\task\\news.json', 'r') as json_file:
        dict_from_json = json.load(json_file)
    groups = []
    uniquekeys = []
    sorted_data = sorted(dict_from_json, key=lambda i: i['created'][:10], reverse=True)
    for k, g in itertools.groupby(sorted_data, lambda i: i['created'][:10]):
        groups.append(list(g))
        uniquekeys.append(k)
    return dict_from_json, groups


def generate_link():
    link_set = set()
    dict_from_json = open_json()[0]
    for article in dict_from_json:
        link_set.add(article['link'])
    link = random.randint(1, 1000)
    if link in link_set:
        return generate_link()
    else:
        return link

print(generate_link())
class MainView(View):
    def get(self, request, *args, **kwargs):
        groups = open_json()[1]
        context = {'groups': groups}
        return render(request,'main/Main.html', context)


class NewsView(View):
    def get(self, request, page, *args, **kwargs):
        groups = open_json()[1]
        for group in groups:
            for article in group:
                if int(page) == article['link']:
                    context = {
                        'Created': article['created'],
                        'Title': article['title'],
                        'Text': article['text'],
                    }
                    return render(request, 'news/news.html', context=context)
        raise Http404


class CreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'news/create.html')


    def post(self, request, *args, **kwargs):
        created = str(datetime.now())
        created = created[:19]
        link = generate_link()
        new_data = {'created': created, 'text': request.POST.get('text'), 'title':request.POST.get('title'),  'link': link}
        dict_from_json = open_json()[0]
        dict_from_json.append(new_data)
        with open('C:\\Users\\User\\PycharmProjects\\HyperNews Portal\\task\\news.json', 'w') as json_out_file:
            json.dump(dict_from_json, json_out_file)

        return redirect('/news')
