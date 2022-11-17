from django import forms

product_quantity_choise = [(i, str(i)) for i in range(1, 21)]


class AddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=product_quantity_choise, coerce=int)  # слайдер для выбора кол во
    update = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=False)
