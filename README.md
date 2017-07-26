# TemporaryDropboxUpload
Saves me some steps when I import my KeePass database into MiniKeePass on the IPhone.

## Here's what it does
Uploads a file to dropbox ->

Waits for 5 minutes (or however long you configure it to) ->

Deletes that same file from dropbox.

## Here's how to use it
Execute the python script "uploadfiletodropbox.py".

Import the database from dropbox before the file gets deleted.

## And here's how to configure it the first time
1. Log in to dropbox

2. In the same browser session where you logged in -> Get yourself an access token from this url: https://dropbox.github.io/dropbox-api-v2-explorer/#auth_token/from_oauth1

3. Copy the access token to the clipboard

4. Open pyconfig.txt and paste in the access token - replacing the text "{{ENTER_YOUR_DROPBOX_ACCESS_TOKEN_HERE}}"

5. Now finally enter your own values for these two configuration keys in pyconfig.txt

     - source_filepath (The path to the file you want to send to dropbox)

     - target_filepath (The path in dropbox. Begins with '/' as an alias for the root folder)
