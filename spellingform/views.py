"""
Views
"""

from django.views.generic import FormView
from .forms import SpellingForm
from .utils import convert_number_to_text

class FormView(FormView):
    form_class = SpellingForm
    template_name = 'spelling_form.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        form = SpellingForm(request.POST)
        if not form.is_valid():
            return self.render_to_response({})

        number = form.data['number'].lstrip('0')
        context = {
            'number': number,
            'spelled_number': convert_number_to_text(number)
        }
        return self.render_to_response(context)
