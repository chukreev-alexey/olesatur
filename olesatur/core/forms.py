# -*- coding: utf-8 -*-
from django import forms

class FormMixin(forms.BaseForm):
    error_css_class = 'error'
    required_css_class = 'required'

    def as_eul(self):
        return self._html_output(
            normal_row = u'<li%(html_class_attr)s><div class="form_label">%(label)s <span>*</span></div><div class="form_info"><div class="form_error">%(errors)s</div><div class="form_field">%(field)s</div><div class="form_help_text">%(help_text)s</div></div></li>',
            error_row = u'<li>%s</li>',
            row_ender = '</li>',
            help_text_html = u' %s',
            errors_on_separate_row = False)