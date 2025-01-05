from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse

class RedirectToAPIMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        
        if not request.url.path.startswith("/api/instituciones"):
            return RedirectResponse(url=f"/api/instituciones")
        
        response = await call_next(request)
        return response
