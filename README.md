# denigmacli

## What is it?

A commandline interface for [denigma](https://denigma.app/),
a website that explains code using machine learning.

For convenience, you might want to add this to your [shell configuration](https://linuxize.com/post/how-to-create-bash-aliases/)(Linux/Mac) or [Command Prompt PATH](https://windowsloop.com/how-to-add-to-windows-path/)(on Windows)

## How to use it?

Example:

`python3 denigmacli.py code_to_explain.java`

## Requirements

`pip install -r requirements.txt`

## Rate limiting

As this program scrapes the demo page, there is a limit
to how many times they let you submit code. So if you use it too many times in a short timeframe it might not work.
I've managed to bypass that by routing it through Tor, using [torify](https://linuxaria.com/howto/how-to-anonymize-the-programs-from-your-terminal-with-torify).
Simply prepend the command with `torify`, like so:

`torify python3 denigmacli.py code_to_explain.java`

It's not quite reliable though, it does work but there's a possibility the response is that there is a Cloudflare Version 2 Captcha. The [Cloudflare bypassing module](https://github.com/VeNoMouS/cloudscraper) can't handle those.