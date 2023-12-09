class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtener el token de autorización
        authorization_header = request.headers.get('Authorization')
        user = None

        if authorization_header and authorization_header.startswith('Bearer '):
            token = authorization_header.split('Bearer ')[1]
            user = authenticate(request, token=token)
            if user:
                request.user = user

        # Verificar si el usuario está suspendido
        if user and user.is_suspended and user.suspended_until > timezone.now():
            raise SomeKindOfAuthorizationException("El usuario está suspendido.")

        return self.get_response(request)
