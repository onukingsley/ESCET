import json
from requests import request


mobile = '+234 808 579 6361'
email = 'escet@gmail.com'
school = 'ESCET'

page_details = {
    'mobile': mobile ,
    'email': email,
    'school': school,
     'logo': '../static/images/download.jpg',
}
menu = {
    '.' : ['home2','home'],
    'about': ['address-book','Contact'],
    'courses': ['library_books','Our Courses',['Math','Science and Engineering','Arts and Humanities','Economics and Finance','Business Administration','Computer Science']],
    'campus': ['building', 'Our Campus', ['Academic','News', 'Our Interns','Our Leadership','Careers','Human Resources']],
    'contact':['phone_android', 'Contact'],

}

# header = {
#     '.' :  ,
#     '.':  ,
#     '.': ,
#     '.': ,
#     '.': ,
# }

header = [['ENUGU STATE COLLEDGE OF EDUCATION TECHNICAL: AN INSTITUTION FOR LEARNING AND HARDWORK.', '/static/images/xcourse_5.jpg.pagespeed.ic.rI86ZBarTv_2.jpg'],['ADMISSION ADMISSION ADMISSION !!! : </BR> ON GOING 2021/2020 ADMISSION, CLICK ON THE LINK TO ENROLL ', 'IMAGE'],['25TH ANIVESRY OF THE SCHOOL OF VOCATIONAL EDUCATION: </BR> THE SCHOOL OF VOCATIONAL EDUCATION CELEBRATES HER 25 YEARS ANIVESARY.','/static/images/xcourse_6.jpg.pagespeed.ic.dzMG9vk6VZ.jpg'],['STUDENTS YOUTH FORUM:</BR> ALL STUDENTS ARE INVITED TO PARTICIPATE IN THE UPCOMING YOUTH FORUM..','/static/images/xhero_1.jpg.pagespeed.ic.-yaFVozZ39.jpg'],['SECOND SEMESTER EXAMINATION: </BR> SUTDY HARD PAYS, ALL STUDENTS ARE EXPECTED TO STUDY HARD FOR THE FORTH COMING EXAMINATION','/static/images/xcourse_4.jpg.pagespeed.ic.tqNvuJbiJI.jpg']]
token ='  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 '<'pexelx.com'
