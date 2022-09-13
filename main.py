import functions_framework
from utils import start_instance, stop_instance

@functions_framework.http
def main(request):
    project_id = 'mightyhive-data-science-poc'
    zone = 'us-west1-b'
    instance_name = 'ma-ds-segmentation-story1' 

    if request.args['command'] == 'start':

        start_instance(project_id, zone, instance_name)
        return f"VM {instance_name} in project {project_id} (zone: {zone}) has been started"
    else:
        stop_instance(project_id, zone, instance_name)
        return f"VM {instance_name} in project {project_id} (zone: {zone}) has been stopped"

    