
# Create your views here.
from django.views.generic import View
from django.shortcuts import get_object_or_404, render, redirect
from.models import Feed #현재폴더에 models 라는 파일에서 
#Feed 라는 이름의 class를 가져오세요.

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
class TagStudy(View):
    template_name = 'tag_study.html'

    def get(self, request):
        return render(request, self.template_name)
    
class Newcontent(View):
    templete_name = "upload_form.html"
    
    def get(self, request):
        return render(request, self.templete_name)
    def post(self, request):
        param = request.POST.get('content','')
        param2 = request.FILES.get('up_photo', False)
        
        print(f"param{param}")
        feed = Feed(content = param, photo = param2)
        feed.save()
        return redirect('edu:tag_study')
    