from django.shortcuts import render

def home(request):
    return render(request,'home.html')



def about(request):
    return render(request,'about.html')

def result(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
    max_word = 0
    

    
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    for word in word_list:
         if max_word < word_dictionary[word]:
              max_word = word_dictionary[word]

            
             

    return render(request,'result.html',{'fulltext' :  full_text,'total':len(word_list),'dictionary':sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True),'max':max_word})

# Create your views here.
