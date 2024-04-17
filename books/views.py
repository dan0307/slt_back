from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookProgressSerializer
from .models import Book, BookProgress
import json



@csrf_exempt  # Use csrf_exempt for simplicity in this example. Use CSRF protection in production.
def create_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_id = data.get('id')
        title = data.get('title')
        content = data.get('content')
        user_id = data.get('user_id')
        if book_id is None or title is None or content is None or user_id is None:
            return JsonResponse({'error': 'Missing required data'}, status=400)

        book = Book.objects.create( book_id = book_id, title=title, content=content, user_id = user_id)

        book_progress = BookProgress.objects.create(user_id=user_id, book=book, progress=1)

        return JsonResponse({'message': 'Book created successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


def check_book(request, book_id, user_id):
    try:
        book = Book.objects.get(book_id=book_id, user_id=user_id)
        return JsonResponse({'exists': True})
    except Book.DoesNotExist:
        return JsonResponse({'exists': False})
    
@api_view(['GET'])
def user_progress(request):
    user = request.user
    book_progress = BookProgress.objects.filter(user=user)
    serializer = BookProgressSerializer(book_progress, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_progress(request):
    book_id = request.query_params.get('book_id')
    book_progress = BookProgress.objects.filter(book_id=book_id)
    serializer = BookProgressSerializer(book_progress, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def get_progress(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('user_id')
        book_id = data.get('book_id')
        book = get_object_or_404(Book, book_id=book_id, user_id=user_id)

        if user_id is None or book is None:
            return JsonResponse({'error': 'User ID and Book ID are required'}, status=400)

        progress = BookProgress.objects.get(user_id=user_id, book=book).progress
        return JsonResponse({'progress': progress}, status=200)
    except BookProgress.DoesNotExist:
        return JsonResponse({'error': 'Progress not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
def user_started_books(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            
            if user_id is None:
                return JsonResponse({'error': 'User ID is required'}, status=400)

            # Query the BookProgress model for books the user has started (progress > 0)
            started_books = BookProgress.objects.filter(user_id=user_id, progress__gt=0).values_list('book_id', flat=True)

            # Return the list of book IDs as a JSON response
            return JsonResponse({'started_books': list(started_books)}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
@api_view(['POST'])
def update_progress(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('user_id')
        book_id = data.get('book_id')
        progress = data.get('progress')
        book = get_object_or_404(Book, book_id=book_id, user_id=user_id)
        # Check if a record already exists for this user and book
        book_progress, created = BookProgress.objects.get_or_create(user_id=user_id, book = book)

        # Update the progress field
        book_progress.progress = progress
        book_progress.save()

        # Return a success response
        return JsonResponse({'message': 'Progress updated successfully'}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User or book not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

