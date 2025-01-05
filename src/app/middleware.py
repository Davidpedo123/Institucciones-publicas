from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse

class RedirectToAPIMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Si la ruta no empieza con '/api', redirige a '/api'
        if not request.url.path.startswith("/api/instituciones"):
            return RedirectResponse(url=f"/api/instituciones")
        # Si la ruta ya tiene el prefijo '/api', continúa con el flujo normal
        response = await call_next(request)
        return response