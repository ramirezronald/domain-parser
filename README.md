# Domain Parser Steps
### These are the steps to clean up the domains and return only resolvable domains using [HostResolver](https://github.com/subfission/HostResolver)


#### Step 1 
get your list of domains ready. 
this script will parse out ANY of the following domains:

* *.google.com/*
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
python3 domain-cleanup.py domains.txt
```

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

finally, take the new-domains.txt file and run it with the resolver-cleanup.py program

```python
python3 resolver-cleanup.py new-domains.txt
```

you are now set and ready to use the new file generated from step 4 and will only include the list of domains that were resolved and will also delete any duplicates. 



