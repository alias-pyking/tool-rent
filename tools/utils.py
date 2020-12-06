from .models import Tool
from rest_framework.response import Response
from functools import wraps
from rest_framework.exceptions import NotFound


def get_tool_or_none(pk):
    """
    params pk: pk of tool
    This is util method for getting tool object 
    or none if not found
    returns: Tool model object or None
    """
    try:
        tool = Tool.objects.select_related('user').get(id=str(pk))
    except Tool.DoesNotExist:
        tool = None
    return tool


def tool_response(tool):
    return Response({
        'id': tool.id,
        'user': tool.user.username,
        'name': tool.name,
        'images': [img.image.url for img in tool.images.all()],
        'description': tool.description,
        'quantity': tool.quantity,
        'cost': tool.cost,
        'status': tool.status,
        'timestamp': tool.timestamp,
        'updated_on': tool.updated_on
    })


def ensure_tool(func):
    """
    Decorator for populating self.kwargs of any view with a tool
    if "tool_id" param is present in path, if tool not found,
    then raise NotFound Error
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        tool_id = self.kwargs['tool_id']
        tool = get_tool_or_none(tool_id)
        if tool is None:
            raise NotFound('Tool Not found')
        self.kwargs['tool'] = tool
        return func(self, *args, **kwargs)

    return wrapper
