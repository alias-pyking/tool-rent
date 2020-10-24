from .models import Tool
from rest_framework.response import Response


def get_tool_or_none(pk):
    """
    params pk: pk of tool
    This is util method for getting tool object 
    or none if not found
    returns: Tool model object or None
    """
    try:
        tool = Tool.objects.get(id=str(pk))
    except:
        tool = None
    return tool


def tool_response(tool):
    return Response({
        'id':tool.id,
        'user':tool.user.username,
        'name': tool.name,
        'images':[img.image.url for img in tool.images.all()],
        'description':tool.description,
        'quantity': tool.quantity,
        'cost': tool.cost,
        'status':tool.status,
        'timestamp':tool.timestamp,
        'updated_on':tool.updated_on
    })
