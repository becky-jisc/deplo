from django.forms import (CharField,
                          IntegerField,
                          DecimalField,
                          Textarea,
                          TextInput,
                          BooleanField,
                          HiddenInput,
                          Select,
                          DateField,
                          TimeField,
                          DateTimeField,
                          CheckboxInput,
                          RadioSelect,
                          URLField,
                          ModelChoiceField,
                          Form,
                          ModelForm,
                          modelformset_factory,
                          inlineformset_factory,
                          )

from .models import Job, TestRecord

from django.forms import BaseModelFormSet

class Job1FormSet(BaseModelFormSet):
    class Meta:
        model = Job
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super(Job1FormSet, self).__init__(*args, **kwargs)
        self.queryset = Job.objects.filter(done=False)

JobFormSet = modelformset_factory(Job, exclude=('id',), formset=Job1FormSet)


class TestRecordForm(ModelForm):
    class Meta:
        model = TestRecord
        exclude = ('id',)

TestRecordFormSet = inlineformset_factory(Job, TestRecord,
                                            form=TestRecordForm, extra=1)
TestFormset = modelformset_factory(TestRecord, exclude=('id',))

