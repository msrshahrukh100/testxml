# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Data
from django.core import serializers
# Create your views here.

def create_chunks(queryset, chunk_size=100) :
	'''
		Doc string
		this function divides our queryset into smaller chunk size for handling larger datasets
		here yield helps in returning a generator 
	'''
	for i in range(0, queryset.count(), chunk_size) :
		yield queryset[i : i + chunk_size]

final_string = ""

def recur_form_xml(item) :
	global final_string
	final_string += "<Node name='"+item.name+"' id='"+str(item.id)+ "'>\n"

	children = queryset.filter(managerid = item.id)
	if children.exists() :
		for c in children :
			recur_form_xml(c)

	final_string += "</Node>\n"



def home(request) :

	global queryset
	global final_string
	final_string = ""
	queryset = Data.objects.all()
	# here we'll choose a desired chunk size 
	# chunks = create_chunks(queryset, 2)
	# top_managers = []
	# created_nodes = []
	# for chunk in chunks :

	# 	for item in chunk :
	# 		if item.managerid == None :
	# 			top_managers.append(item)

	# 		if item not in created_nodes :
	# 			n = Nodes(item)
	# 			created_nodes.append(n)
	# 		c = chunk.filter(id = item.managerid)
	# 		for i in c :
	# 			if i not in created_nodes :
	top_managers = queryset.filter(managerid = None)
	for i in top_managers :
		recur_form_xml(i)
			
	return render(request, "index.html", {'data' : final_string})
