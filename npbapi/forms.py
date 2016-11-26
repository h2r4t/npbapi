# -*- coding: utf-8 -*-
from django import forms
from npbapi.models import Mail

EMPTY_CHOICES = (
    ('', '--'),
)

YEAR_CHOICES = (
    ('2016','2016年'),
)

MONTH_CHOICES = (
    ('03','3月'),
    ('04','4月'),
    ('05','5月'),
    ('06','6月'),
    ('07','7月'),
    ('08','8月'),
    ('09','9月'),
    ('10','10月'),
)

DAY_CHOICES = (
    ('01','1日'),
    ('02','2日'),
    ('03','3日'),
    ('04','4日'),
    ('05','5日'),
    ('06','6日'),
    ('07','7日'),
    ('08','8日'),
    ('09','9日'),
    ('10','10日'),
    ('11','11日'),
    ('12','12日'),
    ('13','13日'),
    ('14','14日'),
    ('15','15日'),
    ('16','16日'),
    ('17','17日'),
    ('18','18日'),
    ('19','19日'),
    ('20','20日'),
    ('21','21日'),
    ('22','22日'),
    ('23','23日'),
    ('24','24日'),
    ('25','25日'),
    ('26','26日'),
    ('27','27日'),
    ('28','28日'),
    ('29','29日'),
    ('30','30日'),
    ('31','31日'),
)

class DateForm(forms.Form):
    year = forms.ChoiceField(
        widget=forms.Select(attrs={'onChange':'dateCheck()'}),
        choices=YEAR_CHOICES,
        required=True,
    )
    month = forms.ChoiceField(
        widget=forms.Select(attrs={'onChange':'dateCheck()'}),
        choices=EMPTY_CHOICES + MONTH_CHOICES,
        required=True,
    )
    day = forms.ChoiceField(
        widget=forms.Select,
        choices=EMPTY_CHOICES + DAY_CHOICES,
        required=True,
    )

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'rows':5, 'class': 'form-control'}),
        }
