import os
import git
import listgits
import webbrowser
from win10toast import ToastNotifier

# parentDir = "C:\\Users\\GDA-Admin\\Documents\\GTech\\repo_gtech\\"
logFile = "C:\\Users\\GDA-Admin\\Documents\\GTech\\eclipse-project\\git\\git_repo.log"
# parentDir = "C:\\Users\\GDA-Admin\\Documents\\GTech\\eclipse-project\\git\\"
parentDir = "C:\\Users\\GDA-Admin\\Documents\\GTech\\python\\"
repoDir = "None"
repoPath = os.path.join(parentDir, repoDir)

toaster = ToastNotifier()


def updateRepo():
    os.system('listgits --g fetch > "'+logFile+'" ')
    os.system('listgits --g pull > "'+logFile+'" ')


os.chdir(parentDir)

if os.path.isdir('./None'):
    updateRepo()
else:
    # andriyan token
    os.system("gitlabber -t ksx3gmhsqyFJyrcvDUVG -u https://git.blubox.id/")
#     os.system("gitlabber -t UMmbhWv8xgubjtkCyLK7 -u https://git.blubox.id/") # bot token

toaster.show_toast("Update Repository Finish",
                   duration=10,
                   threaded=True)

webbrowser.open("git_repo.log")
