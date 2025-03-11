from django import forms
from django.core.validators import RegexValidator
from .models import Author

class SubmissionForm(forms.Form):
    # Regex validator to allow only letters and spaces for the presenter field
    presenter_validator = RegexValidator(
        regex=r'^[A-Z][a-z]*([ -][A-Z][a-z]*)*$',  # Only letters (uppercase and lowercase) and spaces
        message='Presenter name can only contain letters and spaces.'
    )

    # Regex validator for email address
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',  # Standard email format
        message='Enter a valid email address.'
    )

    # Regex validator for title (only letters, numbers, and spaces)
    title_validator = RegexValidator(
        regex=r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$',  # Only letters, numbers, and spaces
        message='Title can only contain letters, numbers, and spaces.'
    )

    # Regex validator for authors (only letters, numbers, and commas for separating names)
    authors_validator = RegexValidator(
        regex=r'^[A-Za-z0-9\s,]+$',  # Letters, numbers, and commas for separating authors
        message='Authors can only contain letters, numbers, and commas.'
    )

    # Regex validator for institute (only letters, numbers, and spaces)
    institute_validator = RegexValidator(
        regex=r'^[A-Za-z0-9\s]+$',  # Letters, numbers, and spaces
        message='Institute name can only contain letters, numbers, and spaces.'
    )

    # Regex validator for resume (this is optional, but you could restrict the length or format)
    resume_validator = RegexValidator(
        regex=r'^[A-Za-z0-9\s,.\-]+$',  # Letters, numbers, spaces, commas, periods, and dashes
        message='Resume can only contain letters, numbers, spaces, commas, periods, and dashes.'
    )

    # Regex validator for keywords (only letters, numbers, and commas for separating keywords)
    keywords_validator = RegexValidator(
        regex=r'^[A-Z][a-zA-Z\s]*(?:, [A-Z][a-zA-Z\s]*){4}$',  # Letters, numbers, and commas for separating keywords
        message='Keywords can only contain letters, numbers, and commas.'
    )

    # Presenter field with validation
    presenter = forms.CharField(
        max_length=100,
        required=True,
        validators=[presenter_validator],
    )

    # Email field with validation
    email = forms.EmailField(
        required=True,
        validators=[email_validator],
    )

    # Title field with validation
    title = forms.CharField(
        max_length=255,
        required=True,
        validators=[title_validator],
    )

    # Authors field with validation
    authors = forms.CharField(
        max_length=255,
        required=True,
        validators=[authors_validator],
    )

    # Institute field with validation
    institute = forms.CharField(
        max_length=255,
        required=True,
        validators=[institute_validator],
    )

    # Resume field with validation
    resume = forms.CharField(
        widget=forms.Textarea,
        max_length=250,
        required=True,
        validators=[resume_validator],
    )

    # Keywords field with validation
    key_words = forms.CharField(
        max_length=255,
        required=True,
        validators=[keywords_validator],
    )

    # Modality field (choices are pre-defined, so regex isn't necessary here)
    modality = forms.ChoiceField(
        choices=[('oral', 'Oral'), ('poster', 'Poster')],
        required=True,
    )

    # Group field with validation
    group = forms.ChoiceField(
        choices=[('corrosion', 'Corrosión'), ('attrition', 'Desgaste'), ('thin-films', 'Películas delgadas'), ('surface', 'Ingeniería de Superficies')],
        required=True,
    )

class AuthorForm(forms.ModelForm):
    class Meta:
        authors_validator = RegexValidator(
        regex=r'^[A-Za-z0-9\s,]+$',  # Letters, numbers, and commas for separating authors
        message='Authors can only contain letters, numbers, and commas.'
        )
        
        model = Author
        fields = ['name', 'is_principal']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter author\'s name', 'required': 'true'}),
            'is_principal': forms.CheckboxInput(),
        }
        
        