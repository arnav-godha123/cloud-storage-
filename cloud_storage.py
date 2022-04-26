import dropbox
class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.BFJcBtGkeX3t5MsXlXVdIIuNIa8frQTGPYiMIu8GdRDNBfhRS0aPgJRAVFBfs9-7ByK-6LyJPHxbC3glmW8CHQOPEqs4iY4IGSi8M7qpLtkOH2o5ccPKcbLCcTceANd3jZ-MAghWN9v6"
    transferdata=Transferdata(access_token)
    file_from="C:/Users/INDIA/Desktop/cloud_storage-master/project.txt"
    file_to="/game2/test3.txt"
    transferdata.upload_file(file_from,file_to)
    print("file has been moved")

main()
