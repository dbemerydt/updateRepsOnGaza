# updateRepsOnGaza
Pulls the latest stories about the ongoing US-funded genocide in Gaza and sends them to the reps and senator for Boulder County, Colorado.

You'll need to write a Python dictionary to a pickle file called `info.pickle` with the following fields:
```
firstname
lastname
address
city
zipcode
phone
email
subject
```

For Senator Hickenlooper and Rep Neguse, you'll have to manually click "submit", as they have infrastructure preventing automated submissions. Hickenlooper's form often hangs upon clicking "submit". I don't know why, and am not speculating.

Also please edit `messageBody.txt` to say your name instead of mine, and maybe change the language in it if you want?

To run, type `python pull-send.py` and keep an eye on the terminal for user prompts.

These are that package versions I'm working with. Your versions don't need to be the same exactly, but these are the ones that definitely work.
```
beautifulsoup4==4.12.3
numpy==1.24.3
pandas==2.0.3
requests==2.31.0
selenium==4.16.0
webdriver_manager==4.0.1
```