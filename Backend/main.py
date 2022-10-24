
from config import app
# routes of independent entities
from Routes.Independent.CourseRoutes import *
from Routes.Independent.SkillRoutes import *
from Routes.Independent.RoleRoutes import *

# routes of dependent entities
from Routes.Dependent.CourseSkillRelationRoutes import *
from Routes.Dependent.RoleSkillRelationRoutes import *
from Routes.Dependent.SkillRoleRelationRoutes import *

from HelperFunctions import *
from ErrorHandler import *
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware



@app.get("/")
async def hello():
    return "OK"


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)
