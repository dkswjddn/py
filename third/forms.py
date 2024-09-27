from django.forms import ModelForm
from third.models import Restaurant
from django.utils.translation import gettext_lazy as _

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']
        labels = {
            'name' :_('이름'),
            'address' :_('주소')
        }
        help_text = {
            'name' : _('이름을 입력해주세요'),
            'address' :_('주소를 입력해주세요')
         }
        errorr_massages = {
            'name' : {
                'max_length' :_('이름이 너무 깁니다 30자 이내로 입력해주세요')
            }
        }
        