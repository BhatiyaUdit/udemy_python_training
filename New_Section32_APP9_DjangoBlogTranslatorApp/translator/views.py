from django.shortcuts import render


# Create your views here.

def translator_view(request):
    output_text = {}
    if request.method == 'POST':
        input_text = request.POST['my_textarea']
        print("Input Text ==", input_text)
        output = input_text.upper()
        output_text = {'output_text': output, 'original_text': input_text}
    return render(request, "translator.html", output_text)
