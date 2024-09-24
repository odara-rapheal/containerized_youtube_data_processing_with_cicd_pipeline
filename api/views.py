from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import fetch_video_details, fetch_video_comments

# Create your views here.

class VideoDataView(APIView):
    def get(self, request):
        video_id = request.query_params.get('video_id')
        if not video_id:
            return Response({"error": "video_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        video_details = fetch_video_details(video_id)
        if not video_details:
            return Response({"error": "Invalid video_id or video not found"}, status=status.HTTP_404_NOT_FOUND)

        comments = fetch_video_comments(video_id)
        return Response({
            "video_details": video_details,
            "comments": comments
        })



