# OBS Scripts
**Some OBS Studio scripts useful to me (Lua &amp; Python).**
You have all the OBS scripts in the /scripts folder of the repository. You may have some additional instructions to these scripts.

Installation to put these scripts in OBS: Tools / Scripts > Select the script you want to import with the + button.

> [!WARNING]
> This repository and all the scripts inside are designed and only work with OBS Studio v27!! (or below v27 at your own risks.)
>
> Please read carefully this README to understand why I keep v27.

### Lua scripts :
You don't have anything to do to make them work.

### Python scripts :
- Download Python 3.6.8, the only Python fully supported by the latest OBS Studio 27 (v27.2.4). *(updated 2025-09-01)*
  - https://github.com/obsproject/obs-studio/releases/tag/27.2.4
  - https://www.python.org/downloads/release/python-368/
  - https://pypi.org/project/requests/2.27.1/ (needed for few scripts that requires requests, 2.27.1 is the last Python 3.6.x compatible)
- At the installation, if you don't want some problems and if you don't know anything about Python, please click on **Customize** and then check **"Install for all users"**, **"Add Python to environment variables"** and **"Precompile standard library"** on the Python Setup.
- Once installed, you should find your Python Path for the OBS Python Settings into `C:\Program Files\Python36` or `C:\Users\YOUR_USERNAME\AppData\Local\Programs\Python\Python36`

![image](https://user-images.githubusercontent.com/49253492/181560527-8a00e625-d07b-4370-bb35-4b789040da82.png)

**Warning :** You may need some external librairies to let OBS Python scripts work properly. Please read the .md file (which is a README file) in each folder where the script is.

<br/>

---

<br/>

## Why are you still using OBS v27 ?
Well I need [StreamFX](https://github.com/Vhonowslend/StreamFX-Public) for my personnal layouts, pretty popular few years ago... and now it has been stopped by its maintainer i'm stuck here! :P

## Make requests to Twitch API
In some scripts of that repository, you may need a Client ID and a OAuth parameter. (make sure you have [requests](https://pypi.org/project/requests/2.27.1/) installed)

### How to get them ?

Well the easiest way to get these parameters are the following instructions :
- Go to this link : https://dev.twitch.tv/console/apps (accept all the Twitch stuff to let you be a real developer 😎)
- Click on **Register Your Application**
![image](https://user-images.githubusercontent.com/49253492/181560828-0f693d78-ffcc-490d-a9a6-e52ef4e677d6.png)
- Then create your application, just type `http://localhost:3000` in the URL OAuth redirection text field.
![image](https://user-images.githubusercontent.com/49253492/181560916-b1c89865-10fe-408f-a3e4-f739db82757f.png)
- Once created, go to Edit and copy the Client ID code (we don't need the Client Secret code)
- Then you'll have to create a link to get the OAuth token.
![image](https://user-images.githubusercontent.com/49253492/181565602-eeb6f214-d810-4fc3-906e-e5eeb18947af.png)
`https://id.twitch.tv/oauth2/authorize?response_type=token&client_id= YOUR CLIENT ID &redirect_uri=http://localhost:3000`
- And just get the OAuth token here
![image](https://user-images.githubusercontent.com/49253492/181567452-906d1aa0-a58a-4461-9739-f134e684ab16.png)
`http://localhost:3000/#access_token= YOUR OAUTH TOKEN TO GET &scope=&token_type=bearer`

**Note :** If you need more permissions with your token to access to some private data on the Twitch API, you can add Scopes where you create the link.

Example with "Read Extensions" permission : `https://id.twitch.tv/oauth2/authorize?response_type=token&client_id= YOUR CLIENT ID &redirect_uri=http://localhost:3000&scope=analytics:read:extensions`

**Documentation :** https://dev.twitch.tv/docs/authentication/scopes

**Finished !** Just copy and paste the Client ID and the OAuth token into the following text fields of your favorite script !
![image](https://user-images.githubusercontent.com/49253492/181570386-597cfaa2-65b4-4834-8ad3-3d1a5956a02d.png)


If you want to go further or you already have your token generator here's the Twitch documentation : https://dev.twitch.tv/docs/api/get-started
