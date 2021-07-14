from django.http import Http404


class Utility:

    @classmethod
    def get_obj_by_pk(cls, model, obj_id):
        try:
            return model.objects.get(pk=obj_id)
        except model.DoesNotExist:
            raise Http404