from django.shortcuts import render, redirect
from django.views.generic import ListView
from color_liker.models import Color
from django.http import HttpResponse
import json
# Create your views here.

MIN_SEARCH_CHARS = 2

class ColorList(ListView):
	model = Color
	context_object_name = "colors"

	# method between request and response, middleman
	def dispatch(self, request, *args, **kwargs):
		self.request = request # So get_context_data can access it.
		return super(ColorList,self).dispatch(request,*args,**kwargs)

	def get_queryset(self):
		'''Returns the all colors, for display in the main table. The search result 
		query set, if any, is passed as context.'''
		return super(ColorList,self).get_queryset()

	def get_context_data(self, **kwargs):
		#The current context
		context = super(ColorList,self).get_context_data(**kwargs)

		
		#For display under the search form
		context["MIN_SEARCH_CHARS"] = MIN_SEARCH_CHARS

		return context

# def submit_color_search_from_ajax(request):
# 	# model = Color
# 	colors=[]
# 	global MIN_SEARCH_CHARS

# 	search_text =""

# 	if request.method=="GET":
# 		search_text = request.GET.get("color_search_text", "").strip().lower()
# 		if(len(search_text)< MIN_SEARCH_CHARS):
# 			search_text = ""

# 	color_results =[]

# 	if search_text != "":
# 		color_results = Color.objects.filter(name__contains = search_text)
	
# 	context ={
# 	"search_text":search_text,
# 	"color_search_results": color_results,
# 	"MIN_SEARCH_CHARS": MIN_SEARCH_CHARS,
# 	};

# 	return render(request,"color_liker/color_search_results_html_snippet.txt", context=context)

def toggle_color_like(request, color_id):
	color= None
	try:
		#There's only one object with thid id, but this returns a list
		# of length one. Get the first (index=0)
		color = Color.objects.filter(id=color_id)[0]
	except Color.DoesNotExist as e:
		raise ValueError("Unknown color.id"+ str(color_id)+ '.Original error:'+str(e))
	 #print("pre-toggle:  color_id=" + str(color_id) + ", color.is_favorited=" + str(color.is_favorited) + "")

	color.is_favorited = not color.is_favorited
	color.save() # Commit the change to the database

	#print("post-toggle: color_id=" + str(color_id) + ", color.is_favorited=" + str(color.is_favorited) + "")
	return render(request, "color_liker/color_like_link_html_snippet.txt", {"color":color})

def get_color_ajax(request):
	if request.is_ajax():
		search_text = request.GET.get('term',"")
		colors = Color.objects.filter(name__contains=search_text)
		color_search_results=[]

		for color in colors:
			color_json={}
			color_json['id']=color.id
			color_json['label']=color.name
			color_json['value']= color.name
			color_search_results.append(color_json)
		data = json.dumps(color_search_results)
	else:
		data='fail'
	mimetype = 'application/json'

	return HttpResponse(data, mimetype)