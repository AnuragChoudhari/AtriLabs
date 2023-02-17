from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    """
    This function is called everytime "Publish" button is hit in the editor.
    The argument "at" is a dictionary that has initial values set from visual editor.
    Changing values in this dictionary will modify the intial state of the app.
    """
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
  if at.upload1.onChange:
        # sanity check if user has successfully uploaded a file
        if at.upload1.io.files != None:
            files = at.upload1.io.files
            # here is the difference, we are looping over all files
            for i, uploadFile in enumerate(files):
                # get the python's BinaryIO file from starlette.UploadFile
                binaryFile = uploadFile.file
                # read the bytes in file
                data = binaryFile.read()
                # optional - convert bytes into utf-8 format
                data_utf8 = data.decode()
                # process data as you process bytes in python ...
                # process data_utf8 as you process strings in python ...
