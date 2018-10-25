import swapper

from django.db import models

from biodata.models.faculty.abstract_classes import BaseModel

class AbstractFacSpace(BaseModel):
    """
    This Model is the faculty space associated with the faculty member.
    """
    
    space = models.IntegerField()  
    # space alloted in GB, if row is not found,
    # then default space will be 5GB

    def __str__(self):
        return str(self.user.username) + "-" + str(self.space) + "GB"
        

class FacSpace(AbstractFacSpace):
    """
    This class implements FacSpace
    """

    class Meta:
        """
        Meta class for FacSpace
        """

        swappable = swapper.swappable_setting('faculty_profile', 'FacSpace')


        



    

  




        

  
        





    


    


        




 

        

        


        



