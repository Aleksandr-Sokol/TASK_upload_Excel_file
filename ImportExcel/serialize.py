from rest_framework import serializers
from .models import ExcelFile


class ExcelFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = ('id', 'initial_file', 'file_name', 'date_upload', 'date_processed', 'status', 'results')

    def validate_initial_file(self, value):
        """
        validate: file extensions is *.xlsx or *.xls
        """
        allowable_extensions = ('xlsx', 'xls', 'csv')
        try:
            file_name = value.name
            ext = file_name.split('.')[-1]
            if ext not in allowable_extensions:
                raise serializers.ValidationError(f"File extensions must be *.xlsx or *.xls, this extensions is {ext}")
        except Exception as e:
            raise serializers.ValidationError(e)
        return value
