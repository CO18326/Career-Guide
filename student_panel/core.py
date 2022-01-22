# filename : core.py 
# ********************************************************************
# ************** contain function related to work analysis. **********
# ******************************************************************** 
from course_system.models import CourseData, SkillHotWords 
from course_system.views import get_json_object 
from course_system.core import CourseJSONdataExtractor, CourseSkillMap, CourseUnitData 
from typing import List 
from django.contrib.auth.models import User 

