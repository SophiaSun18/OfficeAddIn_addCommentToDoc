# addCommentToDoc: GoogleAPI

## References:
* Manage comments: https://developers.google.com/drive/api/guides/manage-comments#anchor
* Scopes: https://developers.google.com/identity/protocols/oauth2/scopes#docs
* Docs API: https://developers.google.com/docs/api/reference/rest
* Drive API: https://developers.google.com/drive/api/reference/rest/v3
* Region classifiers: https://developers.google.com/drive/api/guides/ref-region-classifiers
* Example - Output document as JSON file: https://developers.google.com/docs/api/samples/output-json#python
* Example - Extract text from document: https://developers.google.com/docs/api/samples/extract-text#python

## Features: 
* Using Docs API to extract all the q words and count the length.
* Using Drive API to create new unanchored comments in the document.

## Issue: 
* Unable to add an anchored comment. When a region classifier is added into the program as described in the documentation, the output doesn't really change and is still an unanchored comment over the entire document.