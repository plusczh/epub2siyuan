import os
from epub2note_onePage import Epub2note

def getFileNames(file_dir, tail_list=['.png','.jpg','.JPG','.PNG']): 
        L=[] 
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] in tail_list:
                    L.append(os.path.join(root, file))
        return L

book_path = '/Users/rod/Library/Mobile Documents/iCloud~QReader~MarginStudy/Documents'
note = Epub2note(notebook_name='Book')
if book_path[-4:] == 'epub':
    note.gen_note(epub_path=book_path)
else:
    epub_files = getFileNames(book_path, tail_list=['.epub'])
    for path in epub_files:
        try:
            note.gen_note(epub_path=path)
        except KeyError:
            continue