# addCommentToDoc: WordAPI

This project implements a Microsoft Word add-in that uses FastAPI to communicate with a server (hosted at https://dev6.kenarnold.org), analyze the Word document and provide (**for now, fake**) AI-generated comments that will be inserted into the document to assists writers in reflection and revision.

## How to Sideload an Office Add-in?
* You can find official tutorials here: https://learn.microsoft.com/en-us/office/dev/add-ins/testing/test-debug-office-add-ins?view=word-js-preview#sideload-an-office-add-in-for-testing

## References:
* Add-in Template: https://github.com/OfficeDev/Office-Add-in-samples/tree/main/Samples/hello-world/word-hello-world
* Microsoft Word API: https://learn.microsoft.com/en-us/javascript/api/word?view=word-js-preview
* Tutorial about Manifest.xml: https://learn.microsoft.com/en-us/javascript/api/manifest?view=word-js-preview
* FastAPI: https://fastapi.tiangolo.com/
