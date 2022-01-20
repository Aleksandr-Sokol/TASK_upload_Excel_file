from django.http import FileResponse
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serialize import ExcelFileSerializer
from .models import ExcelFile


class SingleDownloadExcelFile(GenericAPIView):
    """
    Get request return one excel file from database
    """
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', 0)
        obj = ExcelFile.objects.get(id=pk)
        filename = obj.initial_file.path
        response = FileResponse(open(filename, 'rb'))
        return response


class SingleExcelFile(RetrieveUpdateDestroyAPIView):
    """
    Information for one excel file in base
    """
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer
    permission_classes = [IsAuthenticated]


class ImportFileView(ListCreateAPIView):
    """
    GET: Information for all excel file in base
    POST: save file to database. File as 'initial_file'
    """
    parser_classes = (MultiPartParser, FormParser)
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        file_serializer = ExcelFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
