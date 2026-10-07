from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe

        fields = [
            'title',
            'description',
            'category',
            'cooking_time',
            'calories',
            'protein',
            'fat',
            'carbs',
            'ingredients',
            'instructions',
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Например: Паста с курицей'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Краткое описание рецепта',
                    'rows': 3
                }
            ),

            'cooking_time': forms.NumberInput(
                attrs={
                    'placeholder': 'Время в минутах',
                    'min': 1
                }
            ),

            'calories': forms.NumberInput(
                attrs={
                    'placeholder': 'Калорийность',
                    'min': 0
                }
            ),

            'protein': forms.NumberInput(
                attrs={
                    'placeholder': 'Белки, г',
                    'min': 0,
                    'step': 0.1
                }
            ),

            'fat': forms.NumberInput(
                attrs={
                    'placeholder': 'Жиры, г',
                    'min': 0,
                    'step': 0.1
                }
            ),

            'carbs': forms.NumberInput(
                attrs={
                    'placeholder': 'Углеводы, г',
                    'min': 0,
                    'step': 0.1
                }
            ),

            'ingredients': forms.Textarea(
                attrs={
                    'placeholder': 'Укажите ингредиенты каждый с новой строки',
                    'rows': 7
                }
            ),

            'instructions': forms.Textarea(
                attrs={
                    'placeholder': 'Опишите процесс приготовления по шагам',
                    'rows': 7
                }
            ),

            'category': forms.Select(
                attrs={}
            ),
        }