# Domain Parser Steps
### These are the steps to clean up the domains and return only resolvable domains using [HostResolver](https://github.com/subfission/HostResolver)


#### Step 1 
get your list of domains ready. 
this script will parse out ANY of the following domains:

* \*.google.com/*
* *.google.com
* *.google.com/
* .google.com/
* .google.com
* .google.com/
* google.com/*
* google.com/

and will return the following (removing any duplicates):
* google.com

and so on ... you get the idea!

now to run the script do the following:

```python
python3 domain-cleanup-v2.py domains.txt
```
**Note!** Version 2 will match the full domain url:  

* google.com/my/cool/site

### vs.   

* google.com

If you want to match the second option, use domain-cleanup.py and NOT the version 2: domain-cleanup-v2.py

this should now create a script_output.txt with the domains it cleaned up!

#### Step 2 

download and setup the following GitHub repo to then be able to use the script generated from Step 1

Repo: https://github.com/subfission/HostResolver

#### Step 3 

once installed, run the following command:

```python
python3 resolv.py script_outtput.txt >> new-domains.txt
```

* script_output.txt = is the file generated from step 1
* new-domains.txt = is where the output of the HostResolver program will go.

#### Step 4 

now, take the new-domains.txt file and run it with the resolver-cleanup.py program

```python
python3 resolver-cleanup.py new-domains.txt
```

you are now set and ready to use the new file generated from step 4 and will only include the list of domains that were resolved and will also delete any duplicates. 

#### Step 5 

finally, take the new list generated from Step 4 and run the following program "re-format-domains.py" to appened the following wildcards/chars: 

* \*.google/*
* *.google
* google.com/*
* google.com


```python
python3 re-format-domains.py new-domains.txt
```

you should now see the following file "re-format-output.txt" created with the re-formating of the domains 



