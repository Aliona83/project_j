from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler403(request, exception):
    """Rendering the 403 page."""
    if isinstance(exception, PermissionDenied):
        return render(request, 'errors/403.html', status=403)
    else:
        # Handle unexpected errors with a generic 500 error page
        return render(request, 'errors/500.html', status=500)
