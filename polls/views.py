"""# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubmissionForm

def index(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            # Extract the validated data from the form
            presenter = form.cleaned_data['presenter']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            authors = form.cleaned_data['authors']
            institute = form.cleaned_data['institute']
            resume = form.cleaned_data['resume']
            key_words = form.cleaned_data['key_words']
            modality = form.cleaned_data['modality']
            group = form.cleaned_data['group']

            # You can either process the form data (store in database, etc.)
            response_data = (
                f"Presenter: {presenter}<br>"
                f"Email: {email}<br>"
                f"Title: {title}<br>"
                f"Authors: {authors}<br>"
                f"Institution: {institute}<br>"
                f"Resume: {resume}<br>"
                f"Keywords: {key_words}<br>"
                f"Modality: {modality}<br>"
                f"Group: {group}<br>"
            )
            return HttpResponse(response_data)
        else:
            # If the form is not valid, we re-render the form with errors
            return render(request, 'polls/index.html', {'form': form})

    else:
        form = SubmissionForm()  # Instantiate a new form instance for GET request
        return render(request, 'polls/index.html', {'form': form})
"""

# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SubmissionForm
from .utils import generate_pdf
from django.forms import modelformset_factory
from .models import Author
from .forms import AuthorForm

def form_view(request):
    AuthorFormSet = modelformset_factory(Author, form=AuthorForm, extra=1)
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST)
        form = SubmissionForm(request.POST)
        if form.is_valid():
            principal_authors = formset.cleaned_data.get('is_principal', [])
            if sum(1 for author in principal_authors if author) > 1:
                # Display an error if more than one principal author is selected
                formset.errors.append('Only one principal author can be selected.')
            else:
                formset.save()
                # return redirect('success_url')  # Replace with actual success page URL
            # Get the form data as a dictionary
            form_data = {
                'presenter': form.cleaned_data['presenter'],
                'email': form.cleaned_data['email'],
                'title': form.cleaned_data['title'],
                'authors': form.cleaned_data['authors'],
                'institute': form.cleaned_data['institute'],
                'resume': form.cleaned_data['resume'],
                'key_words': form.cleaned_data['key_words'],
                'modality': form.cleaned_data['modality'],
                'group': form.cleaned_data['group'],
            }

            # Generate the PDF using form data
            pdf = generate_pdf(form_data)

            # Create an HTTP response to send the PDF file to the user
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="form_submission.pdf"'

            return response
    else:
        form = SubmissionForm()
        formset = AuthorFormSet(queryset=Author.objects.none())

    return render(request, 'polls/index.html', {'form': form})