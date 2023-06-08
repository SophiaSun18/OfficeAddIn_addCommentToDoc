# Modified from quickstart.py provided by Google Workspace.

from __future__ import print_function

import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']
DOC_ID = '1aI_pYu92MmxplE5zTtjGGlO8vmPxyf6V660936twX-Y'

def get_credentials():
    """ Set up the credentials and create the token if necessary. """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def read_paragraph_element(element):
    """ Read through a paragraph of a document and extract the text. """
    return element.get('textRun').get('content')

def read_structural_elements(elements):
    """ Read through a list of structural elements of a document and extract the text. """
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)
    return text

def main():
    """ Using Google API to add comments to a certain Google Doc. """
    try:

        """ First part: using Docs API to extract all the q words and count the length. """
        doc_service = build('docs', 'v1', credentials=get_credentials())

        # Call the Docs v1 API and get the text part of the document
        results = doc_service.documents().get(documentId = DOC_ID).execute()
        doc = read_structural_elements(results.get('body').get('content'))
        
        # Output the Google docs document into a JSON file
        # with open("example.json", "w") as outfile:
        #     outfile.write(json.dumps(results, indent=4))

        # Print all the q words and the length of the words
        q = {}
        for i in doc.split():
            if i[0] == 'q':
                q[i] = len(i)
        # print(q)

        """ Second part: using Drive API to create new comments in the document. """
        drive_service = build('drive', 'v3', credentials=get_credentials())
        
        # Call the Drive v3 API and create a new comment in the document
        comment = {"content": "a new comment", "anchor": {'r': 256, 'a': [{'txt': {'o': 15, 'l': 8}}]}}
        drive_service.comments().create(fileId=DOC_ID, body=comment, fields='*').execute()

        # Call the Drive v3 API and get the list of comment of the document
        request = drive_service.comments().list(fileId=DOC_ID, includeDeleted=True, fields='*').execute()

        # Output the comment list into a JSON file
        # with open("comments.json", "w") as outfile:
        #     outfile.write(json.dumps(request, indent=4))

        revision = drive_service.revisions().list(fileId=DOC_ID, fields='*').execute()
        # Output the revision history into a JSON file
        with open("revision.json", "w") as outfile:
            outfile.write(json.dumps(revision, indent=4))

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()