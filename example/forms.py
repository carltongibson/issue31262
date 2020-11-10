from django import forms

from .models import Book, Author, Publisher, Topic


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        author_choices = kwargs.pop("author_choices", None)
        publisher_choices = kwargs.pop("publisher_choices", None)
        topic_choices = kwargs.pop("topic_choices", None)
        super().__init__(*args, **kwargs)

        if author_choices:
            self.fields["author"].choices = author_choices

        if publisher_choices:
            self.fields["publisher"].choices = publisher_choices

        if topic_choices:
            self.fields["topic"].choices = topic_choices


class BookFormSet(forms.BaseModelFormSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.author_choices = [*forms.ModelChoiceField(Author.objects.all()).choices]
        self.publisher_choices = [*forms.ModelChoiceField(Publisher.objects.all()).choices]
        self.topic_choices = [*forms.ModelChoiceField(Topic.objects.all()).choices]

    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        kwargs['author_choices'] = self.author_choices
        kwargs['publisher_choices'] = self.publisher_choices
        kwargs['topic_choices'] = self.topic_choices
        return kwargs
