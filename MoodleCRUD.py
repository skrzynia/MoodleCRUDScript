from requests import get, post


# Module variables to connect to moodle api:
## Insert token and URL for your site here.
## Mind that the endpoint can start with "/moodle" depending on your installation.
KEY = "8cc87cf406775101c2df87b07b3a170d"
URL = "https://034f8a1dcb5c.eu.ngrok.io"
ENDPOINT="/webservice/rest/server.php"

def rest_api_parameters(in_args, prefix='', out_dict=None):
    """Transform dictionary/array structure to a flat dictionary, with key names
    defining the structure.
    Example usage:
    >>> rest_api_parameters({'courses':[{'id':1,'name': 'course1'}]})
    {'courses[0][id]':1,
     'courses[0][name]':'course1'}
    """
    if out_dict==None:
        out_dict = {}
    if not type(in_args) in (list,dict):
        out_dict[prefix] = in_args
        return out_dict
    if prefix == '':
        prefix = prefix + '{0}'
    else:
        prefix = prefix + '[{0}]'
    if type(in_args)==list:
        for idx, item in enumerate(in_args):
            rest_api_parameters(item, prefix.format(idx), out_dict)
    elif type(in_args)==dict:
        for key, item in in_args.items():
            rest_api_parameters(item, prefix.format(key), out_dict)
    return out_dict

def call(fname, **kwargs):
    """Calls moodle API function with function name fname and keyword arguments.
    Example:
    >>> call_mdl_function('core_course_update_courses',
                           courses = [{'id': 1, 'fullname': 'My favorite course'}])
    """
    parameters = rest_api_parameters(kwargs)
    parameters.update({"wstoken": KEY, 'moodlewsrestformat': 'json', "wsfunction": fname})
    #print(parameters)
    response = post(URL+ENDPOINT, data=parameters).json()
    if type(response) == dict and response.get('exception'):
        raise SystemError("Error calling Moodle API\n", response)
    return response

################################################
# Rest-Api classes
################################################

class LocalGetSections(object):
    """Get settings of sections. Requires courseid. Optional you can specify sections via number or id."""
    def __init__(self, cid, secnums = [], secids = []):
        self.getsections = call('local_wsmanagesections_get_sections', courseid = cid, sectionnumbers = secnums, sectionids = secids)

class LocalCreateSections(object):
    """Adds sections. Requires: courseid, position, number of sections"""
    def __init__(self, cid, pos, num = 1):
        self.createsections = call('local_wsmanagesections_create_sections', courseid = cid, position = pos, number = num)

class LocalDeleteSections(object):
    """Delete sections. Requires courseid. Optional you can specify sections via number or id."""
    def __init__(self, cid, secnums = [], secids = []):
        self.deletesections = call('local_wsmanagesections_delete_sections', courseid = cid, sectionnumbers = secnums, sectionids = secids)

class LocalMoveSection(object):
    """Move section. Requires courseid, sectionnumber, (new) position."""
    def __init__(self, cid, secnum, newpos):
        self.movesection = call('local_wsmanagesections_move_section', courseid = cid, sectionnumber = secnum, position = newpos)

class LocalUpdateSections(object):
    """Updates sectionnames. Requires: courseid and an array with sectionnumbers and sectionnames"""
    def __init__(self, cid, sectionsdata):
        self.updatesections = call('local_wsmanagesections_update_sections', courseid = cid, sections = sectionsdata)
################################################
# Example
################################################

courseid = "8" # Exchange with valid id.
# Get all sections of the course.
sec = LocalGetSections(courseid)
# Get sections ids of the course with the given numbers.
# sec = LocalGetSections(courseid, [0, 1, 2, 3, 5, 6])
# # Get sections ids of the course with the given ids.
# sec = LocalGetSections(courseid, [], [7186, 7187, 7188, 7189])
# # Get sections ids of the course with the given numbers and given ids.
# sec = LocalGetSections(courseid, [0, 1, 2, 3, 5, 6], [7186, 7187, 7188, 7189])
# sec2 = LocalUpdateSections(courseid,[{'section': 1,'summary' :"Witam"}])
#
# print(sec.getsections[1]['summary'])
