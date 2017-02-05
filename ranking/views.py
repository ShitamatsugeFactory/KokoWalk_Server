from django.http import HttpResponse
import json
from .models import Ranking
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ranking(request):

    if request.method == 'GET':
        return HttpResponse("not allowed get", content_type='application/json')

    elif request.method == 'POST':
        part = request.POST.get('part')
        name = request.POST.get('name')
        score = request.POST.get('score')

        ranking = Ranking(part=part, name=name, score=score)
        rankings = Ranking.objects.filter(part=part)

        rankings = sorted(rankings, key=lambda x: int(x.score))
        rev_rankings = sorted(rankings, key=lambda x: -1*int(x.score))
        #ranking.save()
	
        rank = 1
        list = []
        user_rank = -1
        first = True
        for rank_item in rev_rankings:
            if first == True:
                if int(score) == int(rank_item.score) or int(score) > int(rank_item.score):
                    list.append({'rank':rank, 'name':name, 'score':score})
                    user_rank = rank
                    rank = rank + 1
                    ranking.save()
                    first = False

            list.append({'rank':rank, 'name':rank_item.name, 'score':rank_item.score})
            if rank > 10:
                rank_item.delete()
            rank = rank + 1

        result = {'user_rank':user_rank, 'ranking':list}

        return HttpResponse(str(result), content_type='application/json')