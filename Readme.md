<h1>TicketNotifier</h1>
Simple MacOS Notifier made by python
![Image of notification](ss.png)

<h3>Requirements</h3>
Python3

<h3>How to install</h3>
Update: api_key, domain, password in the FDcredentianls.py file
<br />
<br />
<br />Change notification style for "Script Editor"
<br />
<br />From this
<img src="Editor1.png")
<br />To this
<img src="Editor2.png")
<br />
<br />
<br />open crontab:
<br />crontab -e
<br /><code>*/10 * * * * python3 /{path_to_script}/TicketNotifier.py > /tmp/stdout.log 2>/tmp/stderr.log</code>
