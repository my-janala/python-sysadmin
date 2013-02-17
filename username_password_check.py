# source: http://www.ibm.com/developerworks/aix/library/au-python/
# Managing security is a critical part of the job for any system administrator. 
# Python makes this job easier, as the last example illustrates.
# uses the pwd module to access the password database. It checks userids and passwords for security policy compliance (in this case, that userids are at least six characters long and passwords are at least eight characters long).
# There are two caveats:
# This program works only if you have full rights to /etc/passwd.
# If you use shadow passwords, this script won't work (however, Python 2.5 does have a spwd module that does the job).


import pwd

#initialize counters
erroruser = []
errorpass = []

#get password database
passwd_db = pwd.getpwall()

try:
    #check each user and password for validity
    for entry in passwd_db:
        username = entry[0]
        password = entry [1]
        if len(username) < 6:
            erroruser.append(username)
        if len(password) < 8:
            errorpass.append(username)

    #print results to screen
    print "The following users have an invalid userid (less than six characters):"
    for item in erroruser:
        print item
    print "\nThe following users have invalid password(less than eight characters):"
    for item in errorpass:
        print item
except:
    print "There was a problem running the script."
