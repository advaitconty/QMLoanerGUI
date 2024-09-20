def mongo_host_connection(username, password, default=False):
    if default == True:
        return ("mongodb+srv://user:CATerOmPe@qmloaner.ficx2qe.mongodb.net/?retryWrites=true&w=majority&appName=QMLoaner")
    else:
        return (f"mongodb+srv://{username}:{password}@qmloaner.ficx2qe.mongodb.net/?retryWrites=true&w=majority&appName=QMLoaner")


GEMINI_API_KEY = "AIzaSyAemiIaYORQw1j8pAAEoH9Z8fIXRTaMevE"
ATTENDANCE_EMAILS = ["elias_wong_yi_hang@students.edu.sg",
                     "chen_li_yan@moe.edu.sg",
                     "faith_ang_si_ying@moe.edu.sg",
                     "toh_mei_fang_belinda@moe.edu.sg",
                     "ryan_lim_jun_long@students.edu.sg",
                     "faaiz_ashraf@students.edu.sg"]
TEST_EMAILS = ["advait@contractor.net",
               "ryanlim2009@gmail.com"]
NAMES = ['Laconi Giuliano', 'Elliot Ho Yihui', 'Hazim Matin Bin Helmy',
         'Wong Jun Xi Lucius', 'Ethan Ryo Young', 'Sim Jun Kai Noah',
         'Greg Tan Hee Theang', 'Lee Cit Hoi, Kiran', 'Axel Soong Hong Wei',
         'Alexander Saviour', 'Elijah Nathan Joseph', 'Goh Toh Yo',
         'Haziq Matin Bin Helmy', 'Isaiah Tamayo Abella',
         'Caleb Yang Jingyang',  # End of S1s
         'Tan Shao Xi', 'Anay Shandilya', 'Lee Jing Song Ryan',
         'Vancoppenolle Julien Joo Duk', 'Evan Elijah Koh Yong Zhe', 'Sugai Yuki',
         'Thaddeus Lee Guan Zong', 'Dhivyan S/O Siva Kumar',  # End of S2s
         'Ayaan Ahmad Khan', 'Dylan Wee Yong Hao', 'Ethan Chng Jun Kai',
         'Luke Lim', 'Wong An Yu', 'Elias Wong Yihang',
         'Kaeson Liang Z Kai', 'Ryan Lim Jun Long (Lin Junlong)',
         'Faaiz Ashraf', 'Samson Wong Bing Cheng']  # End of S3s
QM_CODE = "Soote Flap"
EMAIL_ID = "spsge.loans@hotmail.com"
EMAIL_PASSWORD = "BAtARgLaxwOrNEQ"
