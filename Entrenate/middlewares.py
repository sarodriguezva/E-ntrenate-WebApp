# @method_decorator(protect)
class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("hola desde la middleware ###########################")
        response = self.get_response(request)

        # print(request.path)
        # if request.path == "/api/v1/usuarios/" or request.path == "/api/v1/auth/register/":
        #     print("crete user")

        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(view_args, "view_args") # ()
        # print(view_kwargs, "view_kwargs") # {'userId': '61e4d2ed356dc212eef17ac2'}
        print(view_func.__name__, "nombre de la función")
        ProtectedViews = []
        # print(view_func.__name__ not in notProtectedViews)
        if view_func.__name__ in ProtectedViews:
            print("La función sin protect")
            return view_func(request)
        return None

class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        # print(request.path)
        # if request.path == "/api/v1/usuarios/" or request.path == "/api/v1/auth/register/":
        #     print("crete user")

        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        adminRoutes = ['usuariosAPI', "cursosAPI"]
        profRoutes = ["cursosAPI, getMyCreatedCourses"]
        studentRoutes = ["joinCourse", "getMyCourses"]

        if view_func.__name__ in adminRoutes:
            return view_func(request, ['administrador'])
        elif  view_func.__name__ in profRoutes:
            return view_func(request, ['administrador', 'profesor'])
        elif view_func.__name__ in studentRoutes:
            return view_func(request, ['estudiante'])
        return None
